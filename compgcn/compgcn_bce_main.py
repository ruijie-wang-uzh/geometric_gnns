import torch
import wandb
from itertools import product
import torchviz
import torch_scatter
import torch_geometric
from datetime import datetime
from compgcn_models import CompgcnLP
from torch.utils.data import DataLoader
from compgcn_utils import read_data, IndexSet, pre_train_triples


class CompgcnMain:
    def __init__(self, num_subgraphs: int, dropout: float, cluster_size: int, lr: float, weight_decay: float):
        self.data_path = "../data/FB15K237/"
        self.model_path = "../pretrained/FB15K237/compgcn_lp.pt"

        self.from_pre = False  # True: continue training
        self.num_epochs = 100  # number of training epochs

        self.valid_freq = 1  # do validation every x training epochs
        self.lr = lr  # learning rate
        self.dropout = dropout  # dropout rate
        self.weight_decay = weight_decay

        self.aggr = "add"  # aggregation scheme to use in CompGCN
        self.embed_dim = 100  # entity embedding dimension
        self.norm = 2  # norm

        self.num_bases = 50  # number of bases for relation embeddings in CompGCN

        self.num_subgraphs = num_subgraphs  # partition the training graph into x subgraphs; please set it according to your GPU memory (if applicable)
        self.cluster_size = cluster_size  # number of subgraphs in each cluster

        self.batch_size = 128  # training batch size
        self.vt_batch_size = 128  # validation/test batch size (num of triples)

        self.highest_mrr = 0.  # highest validation mrr during training

        if torch.cuda.is_available():
            self.device1 = torch.device("cuda:3")
            self.device2 = torch.device("cuda:4")
            self.eval_device = torch.device("cuda:5")
        else:
            self.device = torch.device("cpu")
            self.eval_device = torch.device("cpu")

        self.eval_sampling = False  # True: sample candidate entities in validation and test
        self.eval_sample_size = 10000  # sample x candidate entities in validation and test

        self.count = None  # {"entity": num_entities, "relation": num_relations, "train": num_train_triples, "valid": num_valid_triples, "test": num_test_triples};
        self.triples = None  # {"train": LongTensor(num_train_triples, 3), "valid": LongTensor(num_valid_triples, 3), "test": LongTensor(num_test_triples, 3)};
        self.pos_tails = {}  # {(head_entity_id, relation_id): {positive_tail_entity_ids: None}}

        self.graph = None  # the pytorch geometric graph consisting of training triples

        self.cluster_data = None  # generated subgraphs
        self.cluster_loader = None  # subgraph batch loader

    def print_config(self):
        print("-----")
        print("### Running - `{}`".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print("#### Configurations")
        print("- load data from `{}`".format(self.data_path))
        if self.from_pre:
            print("- continue training based on: `{}`".format(self.model_path))
        else:
            print("- new training")
        print("- embedding dimension: `{}`".format(self.embed_dim))
        print("- learning rate: `{}`".format(self.lr))
        print("- weight decay: `{}`".format(self.weight_decay))
        print("- dropout rate: `{}`".format(self.dropout))
        print("- number of bases: `{}`".format(self.num_bases))
        print("- compgcn aggregation scheme: `{}`".format(self.aggr))
        print("- number of subgraphs: `{}`".format(self.num_subgraphs))
        print("- training cluster size: `{}`".format(self.cluster_size))
        print("- number of epochs: `{}`".format(self.num_epochs))
        print("- validation frequency: `{}`".format(self.valid_freq))
        print("- training triple batch size: `{}`".format(self.batch_size))
        print("- norm: `{}`".format(self.norm))
        print("- validation/test triple batch size: `{}`".format(self.vt_batch_size))
        print("- highest mrr: `{}`".format(self.highest_mrr))
        print("- device1: `{}`".format(self.device1))
        print("- device2: `{}`".format(self.device2))
        print("- eval device: `{}`".format(self.eval_device))
        if self.eval_sampling:
            print("- evaluation sampling size: `{}`".format(self.eval_sample_size))
        else:
            print("- use all entities as candidates in evaluation")

    def data_pre(self):
        print("#### Preparing Data")
        self.count, self.triples, self.graph, self.pos_tails = read_data(self.data_path)
        print("- number of entities: `{}`".format(self.count["entity"]))
        print("- number of original relations: `{}`".format((self.count["relation"] - 1) // 2))
        print("- number of original training triples: `{}`".format(self.count["train"]))
        print("- number of validation triples: `{}`".format(self.count["valid"]))
        print("- number of testing triples: `{}`".format(self.count["test"]))

        # partition the training graph and instantiate the subgraph loader
        self.cluster_data = torch_geometric.data.ClusterData(data=self.graph, num_parts=self.num_subgraphs)
        self.cluster_loader = torch_geometric.data.ClusterLoader(cluster_data=self.cluster_data, batch_size=self.cluster_size, shuffle=True)

    def train(self):
        print("#### Model Training and Validation")

        # instantiate the model
        compgcn_lp = CompgcnLP(num_entities=self.count["entity"], num_relations=(self.count["relation"] - 1) // 2, dimension=self.embed_dim, num_bases=self.num_bases, aggr=self.aggr, norm=self.norm, dropout=self.dropout)
        if self.from_pre:
            compgcn_lp.load_state_dict(torch.load(self.model_path))
        compgcn_lp.to(self.device1)

        # use Adam as the optimizer
        optimizer = torch.optim.Adam(params=compgcn_lp.parameters(), lr=self.lr, weight_decay=self.weight_decay)
        # use binary cross entropy loss as the loss function
        criterion = torch.nn.BCELoss()

        compgcn_lp.train()
        plot = True

        wandb.watch(compgcn_lp, criterion, log="all", log_freq=10)

        for epoch in range(self.num_epochs):
            print("* epoch {}".format(epoch))
            epoch_loss = 0.
            cluster_size = []
            for step, cluster in enumerate(self.cluster_loader):
                cluster_size.append(cluster.edge_index.size(1))

                heads, relations, targets = pre_train_triples(head_ids=cluster.edge_index[0, :],
                                                              rel_ids=cluster.edge_attr.squeeze(1),
                                                              tail_ids=cluster.edge_index[1, :],
                                                              num_cluster_entities=cluster.x.size(0),
                                                              self_rel_id=self.count["relation"]-1)
                # heads, relations, size: (num_pos_triples_in_current_cluster)
                # targets, size: (num_pos_triples_in_current_cluster, num_entities_in_current_cluster)

                index_set = IndexSet(num_indices=heads.size(0))
                index_loader = DataLoader(dataset=index_set, batch_size=self.batch_size, shuffle=True)

                for batch in index_loader:
                    optimizer.zero_grad()

                    # update entity and relation embeddings in the current cluster
                    x, r = compgcn_lp.encode(ent_ids=cluster.x.squeeze(1).to(self.device1),
                                             edge_index=cluster.edge_index.to(self.device1),
                                             edge_type=cluster.edge_attr.squeeze(1).to(self.device1),
                                             y=cluster.y.squeeze(1).to(self.device1),
                                             second_device=self.device2)  # x: (num_entities_in_current_cluster, dimension); r: (num_relations, dimension)

                    # training batch
                    batch_heads = torch.index_select(input=heads, index=batch, dim=0)  # size: (batch_size)
                    batch_relations = torch.index_select(input=relations, index=batch, dim=0)  # size: (batch_size)
                    batch_targets = torch.index_select(input=targets, index=batch, dim=0)  # size: (batch_size, num_entities_in_current_cluster)

                    # compute loss
                    loss = compgcn_lp.train_decode(x=x, r=r, batch_heads=batch_heads.to(self.device2), batch_relations=batch_relations.to(self.device2))  # size: (batch_size, num_entities_in_current_cluster)
                    batch_loss = criterion(input=loss, target=batch_targets.to(self.device2))

                    if plot:
                        dot = torchviz.make_dot(batch_loss, params=dict(compgcn_lp.named_parameters()))
                        dot.format = 'png'
                        dot.render('./compgcn_lp_graph')
                        plot = False

                    batch_loss.backward()
                    optimizer.step()
                    epoch_loss += batch_loss.item()

            print("\t * number of triples in each cluster, min: {}, mean: {}, max: {}".format(min(cluster_size), 0 if len(cluster_size) == 0 else sum(cluster_size) / len(cluster_size), max(cluster_size)))
            print("\t * loss `{}`, time `{}`  ".format(epoch_loss, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

            if epoch % self.valid_freq == 0:
                self.evaluate(mode="valid", epoch=epoch, model=compgcn_lp)

            wandb.log({"epoch loss": epoch_loss}, step=epoch)

    def test(self):
        print("#### testing")
        test_model = CompgcnLP(num_entities=self.count["entity"], num_relations=(self.count["relation"] - 1) // 2, dimension=self.embed_dim, num_bases=self.num_bases, aggr=self.aggr, norm=self.norm, dropout=self.dropout)
        test_model.load_state_dict(torch.load(self.model_path))
        self.evaluate(mode="test", epoch=self.num_epochs, model=test_model)
        print("-----")
        print("  ")

    def evaluate(self, mode: str, epoch: int, model: CompgcnLP):
        model.eval()
        with torch.no_grad():
            model.cpu()
            x, r = model.encode(ent_ids=self.graph.x.squeeze(1), edge_index=self.graph.edge_index, edge_type=self.graph.edge_attr.squeeze(1), y=self.graph.y.squeeze(1), second_device=torch.device("cpu"))
            x = x.to(self.eval_device)
            r = r.to(self.eval_device)
            model.to(self.eval_device)
            all_head_ranks = None
            all_head_equals = None
            all_head_ranks2 = None
            all_tail_ranks = None
            all_tail_equals = None
            all_tail_ranks2 = None
            index_set = IndexSet(num_indices=self.count[mode])
            index_loader = DataLoader(dataset=index_set, batch_size=self.vt_batch_size, shuffle=False)
            for batch in index_loader:
                triples = torch.index_select(input=self.triples[mode], index=batch, dim=0).to(self.eval_device)  # size: (batch_size, 3)

                if self.eval_sampling:
                    sampled_entities = torch.LongTensor(list(
                        torch.utils.data.RandomSampler(data_source=IndexSet(num_indices=self.count["entity"]),
                                                       replacement=True,
                                                       num_samples=self.eval_sample_size)))  # sampled entities for evaluation, size: (eval_sample_size)
                    candidate_entities = sampled_entities.repeat(triples.size(0), 1).to(self.eval_device)  # size: (batch_size, eval_sample_size)
                else:
                    candidate_entities = torch.arange(self.count["entity"]).repeat(triples.size(0), 1).to(self.eval_device)  # size: (batch_size, num_entities)
                    self.eval_sample_size = self.count["entity"]

                # head prediction
                heads = triples[:, 0].view(-1, 1).to(self.eval_device)  # size: (batch_size, 1)
                test_heads = torch.cat((heads, candidate_entities), dim=1).unsqueeze(2)  # size: (batch_size, 1 + eval_sample_size, 1)

                no_heads = triples[:, 1:3].unsqueeze(1).repeat(1, 1 + self.eval_sample_size, 1).to(self.eval_device)  # (batch_size, 1 + eval_sample_size, 2)

                new_head_triples = torch.cat((test_heads, no_heads), dim=2).view(-1, 3).to(self.eval_device)  # size: (batch_size * (1 + eval_sample_size), 3)

                new_head_scores = model.eval_decode(x=x, r=r, triples=new_head_triples)  # size: (batch_size * (1 + eval_sample_size))
                new_head_scores = new_head_scores.view(triples.size(0), 1 + self.eval_sample_size)  # size: (batch_size, (1 + eval_sample_size))
                correct_scores = new_head_scores[:, 0].unsqueeze(1)  # (batch_size, 1)
                if self.eval_device.type == "cuda":
                    false_positives = torch.nonzero(torch.cuda.BoolTensor(new_head_scores < correct_scores), as_tuple=True)[0]  # indices of random entities having higher scores than correct ones, size: (batch_size * num_false_positive_per_batch)
                    false_equals = torch.nonzero(torch.cuda.BoolTensor(new_head_scores == correct_scores), as_tuple=True)[0]
                else:
                    false_positives = torch.nonzero(torch.BoolTensor(new_head_scores < correct_scores), as_tuple=True)[0]  # indices of random entities having higher scores than correct ones
                    false_equals = torch.nonzero(torch.BoolTensor(new_head_scores == correct_scores), as_tuple=True)[0]
                false_positives = torch.cat((false_positives, torch.arange(correct_scores.size(0)).to(self.eval_device)), dim=0)
                head_ranks = torch_scatter.scatter(src=torch.ones(false_positives.size(0)).to(torch.long).to(self.eval_device), index=false_positives, dim=0)  # number of false positives for each valid/test triple, (batch_size)
                head_equals = torch_scatter.scatter(src=torch.ones(false_equals.size(0)).to(torch.long).to(self.eval_device), index=false_equals, dim=0)
                head_equals = head_equals - 2

                if all_head_ranks is None:
                    all_head_ranks = head_ranks.to(torch.float)
                    all_head_equals = head_equals.to(torch.float)
                    all_head_ranks2 = (head_ranks + head_equals).to(torch.float)
                else:
                    all_head_ranks = torch.cat((all_head_ranks, head_ranks.to(torch.float)), dim=0)
                    all_head_equals = torch.cat((all_head_equals, head_equals.to(torch.float)), dim=0)
                    all_head_ranks2 = torch.cat((all_head_ranks2, (head_ranks + head_equals).to(torch.float)), dim=0)

                # tail prediction
                tails = triples[:, 2].view(-1, 1).to(self.eval_device)  # size: (batch_size, 1)
                test_tails = torch.cat((tails, candidate_entities), dim=1).unsqueeze(2)  # size: (batch_size, 1 + eval_sample_size, 1)

                no_tails = triples[:, 0:2].unsqueeze(1).repeat(1, 1 + self.eval_sample_size, 1).to(self.eval_device)  # size: (batch_size, 1 + eval_sample_size, 2)

                new_tail_triples = torch.cat((no_tails, test_tails), dim=2).view(-1, 3).to(self.eval_device)  # size: (batch_size * (1 + eval_sample_size)), 3)

                new_tail_scores = model.eval_decode(x=x, r=r, triples=new_tail_triples)  # size: (batch_size * (1 + eval_sample_size)))
                new_tail_scores = new_tail_scores.view(triples.size(0), (1 + self.eval_sample_size))  # size: (batch_size, (1 + eval_sample_size))
                correct_scores = new_tail_scores[:, 0].unsqueeze(1)  # size: (batch_size, 1)
                if self.eval_device.type == "cuda":
                    false_positives = torch.nonzero(torch.cuda.BoolTensor(new_tail_scores < correct_scores), as_tuple=True)[0]  # indices of sampled entities having higher scores than correct ones
                    false_equals = torch.nonzero(torch.cuda.BoolTensor(new_tail_scores == correct_scores), as_tuple=True)[0]
                else:
                    false_positives = torch.nonzero(torch.BoolTensor(new_tail_scores < correct_scores), as_tuple=True)[0]  # indices of sampled entities having higher scores than correct ones
                    false_equals = torch.nonzero(torch.BoolTensor(new_tail_scores == correct_scores), as_tuple=True)[0]
                false_positives = torch.cat((false_positives, torch.arange(correct_scores.size(0)).to(self.eval_device)), dim=0)
                tail_ranks = torch_scatter.scatter(src=torch.ones(false_positives.size(0)).to(torch.long).to(self.eval_device), index=false_positives,dim=0)  # number of false positives for each valid/test triple, (batch_size)
                tail_equals = torch_scatter.scatter(src=torch.ones(false_equals.size(0)).to(torch.long).to(self.eval_device), index=false_equals, dim=0)
                tail_equals = tail_equals - 2

                if all_tail_ranks is None:
                    all_tail_ranks = tail_ranks.to(torch.float)
                    all_tail_equals = tail_equals.to(torch.float)
                    all_tail_ranks2 = (tail_ranks + tail_equals).to(torch.float)
                else:
                    all_tail_ranks = torch.cat((all_tail_ranks, tail_ranks.to(torch.float)), dim=0)
                    all_tail_equals = torch.cat((all_tail_equals, tail_equals.to(torch.float)), dim=0)
                    all_tail_ranks2 = torch.cat((all_tail_ranks2, (tail_ranks + tail_equals).to(torch.float)), dim=0)

            h_mr = torch.mean(all_head_ranks)  # mean head rank
            h_mrr = torch.mean(1. / all_head_ranks)  # mean head reciprocal rank
            h_me = torch.mean(all_head_equals)  # number of candidate head entities having the same score
            h_mr2 = torch.mean(all_head_ranks2)  # mean head rank
            h_mrr2 = torch.mean(1. / all_head_ranks2)  # mean head reciprocal rank
            if self.eval_device.type == "cuda":
                h_hit1 = torch.nonzero(torch.cuda.BoolTensor(all_head_ranks <= 1)).size(0) / all_head_ranks.size(0)  # head hit@1
                h_hit3 = torch.nonzero(torch.cuda.BoolTensor(all_head_ranks <= 3)).size(0) / all_head_ranks.size(0)  # head hit@3
                h_hit10 = torch.nonzero(torch.cuda.BoolTensor(all_head_ranks <= 10)).size(0) / all_head_ranks.size(0)  # head hit@10
            else:
                h_hit1 = torch.nonzero(torch.BoolTensor(all_head_ranks <= 1)).size(0) / all_head_ranks.size(0)  # head hit@1
                h_hit3 = torch.nonzero(torch.BoolTensor(all_head_ranks <= 3)).size(0) / all_head_ranks.size(0)  # head hit@3
                h_hit10 = torch.nonzero(torch.BoolTensor(all_head_ranks <= 10)).size(0) / all_head_ranks.size(0)  # head hit@10

            t_mr = torch.mean(all_tail_ranks)  # mean tail rank
            t_mrr = torch.mean(1. / all_tail_ranks)  # mean tail reciprocal rank
            t_me = torch.mean(all_tail_equals)  # number of candidate tail entities having the same score
            t_mr2 = torch.mean(all_tail_ranks2)  # mean tail rank
            t_mrr2 = torch.mean(1. / all_tail_ranks2)  # mean tail reciprocal rank
            if self.eval_device.type == "cuda":
                t_hit1 = torch.nonzero(torch.cuda.BoolTensor(all_tail_ranks <= 1)).size(0) / all_tail_ranks.size(0)  # tail hit@1
                t_hit3 = torch.nonzero(torch.cuda.BoolTensor(all_tail_ranks <= 3)).size(0) / all_tail_ranks.size(0)  # tail hit@3
                t_hit10 = torch.nonzero(torch.cuda.BoolTensor(all_tail_ranks <= 10)).size(0) / all_tail_ranks.size(0)  # tail hit@10
            else:
                t_hit1 = torch.nonzero(torch.BoolTensor(all_tail_ranks <= 1)).size(0) / all_tail_ranks.size(0)  # tail hit@1
                t_hit3 = torch.nonzero(torch.BoolTensor(all_tail_ranks <= 3)).size(0) / all_tail_ranks.size(0)  # tail hit@3
                t_hit10 = torch.nonzero(torch.BoolTensor(all_tail_ranks <= 10)).size(0) / all_tail_ranks.size(0)  # tail hit@10

            print_dic = {"valid": "validation results (raw)", "test": "testing results (raw)"}
            if mode == "valid":
                print("\t * {}  at epoch `{}`".format(print_dic[mode], epoch))
            else:
                print("- {}  ".format(print_dic[mode]))
            print("   ")
            print("\t\t|  metric  |  head  |  tail  |  mean  |  ")
            print("\t\t|  ----  |  ----  |  ----  |  ----  |  ")
            print("\t\t|  mean reciprocal rank (MRR)  |  `{}`  |  `{}`  |  `{}`  |  ".format(h_mrr, t_mrr, (h_mrr + t_mrr) / 2))
            print("\t\t|  mean rank (MR)  |  `{}`  |  `{}`  |  `{}`  |  ".format(h_mr, t_mr, (h_mr + t_mr) / 2))
            print("\t\t|  mean equal (ME)  |  `{}`  |  `{}`  |  `{}`  |  ".format(h_me, t_me, (h_me + t_me) / 2))
            print("\t\t|  mrr considering equals  |  `{}`  |  `{}`  |  `{}`  |  ".format(h_mrr2, t_mrr2, (h_mrr2 + t_mrr2) / 2))
            print("\t\t|  mr considering equals  |  `{}`  |  `{}`  |  `{}`  |  ".format(h_mr2, t_mr2, (h_mr2 + t_mr2) / 2))
            print("\t\t|  hits@1  |  `{}`  |  `{}`  |  `{}`  |  ".format(h_hit1, t_hit1, (h_hit1 + t_hit1) / 2))
            print("\t\t|  hits@3  |  `{}`  |  `{}`  |  `{}`  |  ".format(h_hit3, t_hit3, (h_hit3 + t_hit3) / 2))
            print("\t\t|  hits@10  |  `{}`  |  `{}`  |  `{}`  |  ".format(h_hit10, t_hit10, (h_hit10 + t_hit10) / 2))
            print("   ")

            if mode == "test":
                wandb.log({"epoch loss": 0.}, step=epoch)
            wandb.log({"MR": (h_mr + t_mr) / 2,
                       "MRR": (h_mrr + t_mrr) / 2,
                       "hits@1": (h_hit1 + t_hit1) / 2,
                       "hits@3": (h_hit3 + t_hit3) / 2,
                       "hits@10": (h_hit10 + t_hit10) / 2,
                       "ME": (h_me + t_me) / 2,
                       "MR_ME": (h_mr2 + t_mr2) / 2,
                       "MRR_ME": (h_mrr2 + t_mrr2) / 2
                       }, step=epoch)

        if mode == "valid":
            if self.highest_mrr < (h_mrr + t_mrr) / 2:
                self.highest_mrr = (h_mrr + t_mrr) / 2
                torch.save(model.state_dict(), self.model_path)
                print("\t * model saved to `{}` at epoch `{}`   ".format(self.model_path, epoch))
        model.train()
        model.to(self.device1)


if __name__ == "__main__":
    wandb.login()

    num_subgraphs = [100]#[100, 150, 200]
    drop_outs = [0.2]
    cluster_sizes = [20]#[20]
    learning_rate = [0.001] #[0.01, 0.005, 0.001, 0.0005]
    weight_decay = [0.]
    params = list(product(num_subgraphs, drop_outs, cluster_sizes, learning_rate, weight_decay))

    for param in params:
        compgcn_main = CompgcnMain(num_subgraphs=param[0], dropout=param[1], cluster_size=param[2], lr=param[3], weight_decay=param[4])
        config = {
            "data_path": compgcn_main.data_path,
            "model_path": compgcn_main.model_path,
            "from_pre": compgcn_main.from_pre,
            "num_epochs": compgcn_main.num_epochs,
            "valid_freq": compgcn_main.valid_freq,
            "learning_rate": compgcn_main.lr,
            "weight decay": compgcn_main.weight_decay,
            "dropout": compgcn_main.dropout,
            "aggr": compgcn_main.aggr,
            "embed_dim": compgcn_main.embed_dim,
            "norm": compgcn_main.norm,
            "num_bases": compgcn_main.num_bases,
            "num_subgraphs": compgcn_main.num_subgraphs,
            "cluster_size": compgcn_main.cluster_size,
            "batch_size": compgcn_main.batch_size,
            "vt_batch_size": compgcn_main.vt_batch_size,
            "highest_mrr": compgcn_main.highest_mrr,
            "evaluation sampling": compgcn_main.eval_sampling,
            "sampling size": compgcn_main.eval_sample_size,
            "training device": compgcn_main.device1,
            "second training device": compgcn_main.device2,
            "evaluation device": compgcn_main.eval_device,
        }
        with wandb.init(entity="ruijie", project="test", config=config, save_code=True, name="NS{}LR{}".format(compgcn_main.num_subgraphs, compgcn_main.lr)):
            compgcn_main.print_config()
            compgcn_main.data_pre()
            compgcn_main.train()
            compgcn_main.test()
            wandb.finish()