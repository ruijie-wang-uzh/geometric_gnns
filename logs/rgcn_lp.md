-----
### Running Time: `2021-06-21 22:33:49`
#### configuration
- load data from `../data/FB15K237/`
- continue training: `False`
- embedding dimension: `100` 
- number of bases: `64`
- rgcn aggregation scheme: `add`
- train batch size: `20480`
- validation/test batch size: `500`
- learning rate: `0.01`
- number of epochs: `100`
- number of negative triples: `16`
- number of entities: `14541`
- number of relations: `238`
- number of training triples: `272115`
- number of validation triples: `17535`
- number of testing triples: `20466`
- model parameters: `['entity_embeds', 'rgcn.bases', 'rgcn.coefficients']`
#### training
- epoch `0`, loss `5.5177531242370605`, time `2021-06-21 22:35:45`  
- validation results  at epoch `0`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `4149.54296875`  |  `2638.64892578125`  |  `3394.095947265625`  |  
|  mean reciprocal rank (MRR)  |  `0.0069151087664067745`  |  `0.05595729872584343`  |  `0.03143620491027832`  |  
|  hit@1  |  `0.0036111106164753437`  |  `0.03919985890388489`  |  `0.021405484527349472`  |  
|  hit@3  |  `0.004833333194255829`  |  `0.054145295172929764`  |  `0.029489314183592796`  |  
|  hit@10  |  `0.009888888336718082`  |  `0.07975742220878601`  |  `0.04482315480709076`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `0`   
- epoch `1`, loss `2.437528133392334`, time `2021-06-21 22:58:08`  
- epoch `2`, loss `1.5579560995101929`, time `2021-06-21 23:00:04`  
- epoch `3`, loss `1.1969972848892212`, time `2021-06-21 23:02:00`  
- epoch `4`, loss `1.0298793315887451`, time `2021-06-21 23:03:55`  
- epoch `5`, loss `0.9211077094078064`, time `2021-06-21 23:05:51`  
- validation results  at epoch `5`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `627.3189086914062`  |  `260.2661437988281`  |  `443.79254150390625`  |  
|  mean reciprocal rank (MRR)  |  `0.06380626559257507`  |  `0.20992490649223328`  |  `0.13686558604240417`  |  
|  hit@1  |  `0.03067045472562313`  |  `0.15303155779838562`  |  `0.09185100346803665`  |  
|  hit@3  |  `0.05698321387171745`  |  `0.20894691348075867`  |  `0.1329650580883026`  |  
|  hit@10  |  `0.12291329354047775`  |  `0.3204575777053833`  |  `0.22168543934822083`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `5`   
- epoch `6`, loss `0.8454558253288269`, time `2021-06-21 23:28:38`  
- epoch `7`, loss `0.7937612533569336`, time `2021-06-21 23:30:34`  
- epoch `8`, loss `0.7530921101570129`, time `2021-06-21 23:32:29`  
- epoch `9`, loss `0.7219417691230774`, time `2021-06-21 23:34:23`  
- epoch `10`, loss `0.698844850063324`, time `2021-06-21 23:36:18`  
- validation results  at epoch `10`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `604.5474243164062`  |  `236.56396484375`  |  `420.5556945800781`  |  
|  mean reciprocal rank (MRR)  |  `0.07490208745002747`  |  `0.23454901576042175`  |  `0.1547255516052246`  |  
|  hit@1  |  `0.03828088566660881`  |  `0.17480581998825073`  |  `0.10654335469007492`  |  
|  hit@3  |  `0.06618932634592056`  |  `0.2345932126045227`  |  `0.15039126574993134`  |  
|  hit@10  |  `0.14323030412197113`  |  `0.35471728444099426`  |  `0.2489737868309021`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `10`   
- epoch `11`, loss `0.6735981702804565`, time `2021-06-21 23:58:58`  
- epoch `12`, loss `0.6544276475906372`, time `2021-06-22 00:00:53`  
- epoch `13`, loss `0.6391499638557434`, time `2021-06-22 00:02:47`  
- epoch `14`, loss `0.6305556893348694`, time `2021-06-22 00:04:41`  
- epoch `15`, loss `0.6192314624786377`, time `2021-06-22 00:06:37`  
- validation results  at epoch `15`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `619.8837890625`  |  `248.67996215820312`  |  `434.2818603515625`  |  
|  mean reciprocal rank (MRR)  |  `0.07941894978284836`  |  `0.23674005270004272`  |  `0.15807950496673584`  |  
|  hit@1  |  `0.041397131979465485`  |  `0.17444351315498352`  |  `0.1079203188419342`  |  
|  hit@3  |  `0.06980711966753006`  |  `0.23681817948818207`  |  `0.15331265330314636`  |  
|  hit@10  |  `0.15267014503479004`  |  `0.3659602403640747`  |  `0.2593151926994324`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `15`   
- epoch `16`, loss `0.6054534316062927`, time `2021-06-22 00:29:10`  
- epoch `17`, loss `0.5926709771156311`, time `2021-06-22 00:31:05`  
- epoch `18`, loss `0.5839212536811829`, time `2021-06-22 00:32:59`  
- epoch `19`, loss `0.5797284841537476`, time `2021-06-22 00:34:54`  
- epoch `20`, loss `0.5726441740989685`, time `2021-06-22 00:36:49`  
- validation results  at epoch `20`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `640.803955078125`  |  `252.76483154296875`  |  `446.7843933105469`  |  
|  mean reciprocal rank (MRR)  |  `0.08080001175403595`  |  `0.242530956864357`  |  `0.16166548430919647`  |  
|  hit@1  |  `0.04161890223622322`  |  `0.17905205488204956`  |  `0.11033547669649124`  |  
|  hit@3  |  `0.07254533469676971`  |  `0.24335676431655884`  |  `0.15795105695724487`  |  
|  hit@10  |  `0.15778189897537231`  |  `0.3769742548465729`  |  `0.2673780918121338`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `20`   
- epoch `21`, loss `0.5652570128440857`, time `2021-06-22 00:59:19`  
- epoch `22`, loss `0.5584658980369568`, time `2021-06-22 01:01:17`  
- epoch `23`, loss `0.5483394265174866`, time `2021-06-22 01:03:12`  
- epoch `24`, loss `0.5443773865699768`, time `2021-06-22 01:05:07`  
- epoch `25`, loss `0.5398072004318237`, time `2021-06-22 01:07:03`  
- validation results  at epoch `25`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `664.2083129882812`  |  `269.1316223144531`  |  `466.66998291015625`  |  
|  mean reciprocal rank (MRR)  |  `0.08164182305335999`  |  `0.24135886132717133`  |  `0.16150033473968506`  |  
|  hit@1  |  `0.04318777844309807`  |  `0.1792200803756714`  |  `0.11120393127202988`  |  
|  hit@3  |  `0.07174667716026306`  |  `0.2410956472158432`  |  `0.15642115473747253`  |  
|  hit@10  |  `0.15701089799404144`  |  `0.37476852536201477`  |  `0.2658897042274475`  |  
   
#### testing
- testing results  
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `678.901123046875`  |  `283.6453552246094`  |  `481.27325439453125`  |  
|  mean reciprocal rank (MRR)  |  `0.08253337442874908`  |  `0.2362329214811325`  |  `0.1593831479549408`  |  
|  hit@1  |  `0.04300246015191078`  |  `0.17348645627498627`  |  `0.10824445635080338`  |  
|  hit@3  |  `0.0753936693072319`  |  `0.2368151694536209`  |  `0.1561044156551361`  |  
|  hit@10  |  `0.159179225564003`  |  `0.3666783571243286`  |  `0.2629287838935852`  |  
   
-----
  
-----
### Running Time: `2021-06-22 11:09:11`
#### configuration
- load data from `../data/FB15K237/`
- continue training: `False`
- embedding dimension: `100`
- number of bases: `100`
- rgcn aggregation scheme: `add`
- train batch size: `20480`
- validation/test batch size: `500`
- learning rate: `0.01`
- number of epochs: `100`
- number of negative triples: `32`
- number of entities: `14541`
- number of relations: `238`
- number of training triples: `272115`
- number of validation triples: `17535`
- number of testing triples: `20466`
- model parameters: `['entity_embeds', 'rgcn.bases', 'rgcn.coefficients']`
#### training
- epoch `0`, loss `4.760628700256348`, time `2021-06-22 11:13:19`  
- validation results  at epoch `0`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `2746.4091796875`  |  `2471.517578125`  |  `2608.96337890625`  |  
|  mean reciprocal rank (MRR)  |  `0.015503646805882454`  |  `0.040119629353284836`  |  `0.02781163901090622`  |  
|  hit@1  |  `0.007555665913969278`  |  `0.024753965437412262`  |  `0.0161548163741827`  |  
|  hit@3  |  `0.013944776728749275`  |  `0.03580952435731888`  |  `0.024877149611711502`  |  
|  hit@10  |  `0.025389552116394043`  |  `0.06473015993833542`  |  `0.04505985602736473`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `0`   
- epoch `1`, loss `1.399749517440796`, time `2021-06-22 11:42:30`  
- epoch `2`, loss `0.9937828779220581`, time `2021-06-22 11:46:31`  
- epoch `3`, loss `0.8348767757415771`, time `2021-06-22 11:50:34`  
- validation results  at epoch `3`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `739.360107421875`  |  `312.0843811035156`  |  `525.7222290039062`  |  
|  mean reciprocal rank (MRR)  |  `0.04740706458687782`  |  `0.13845966756343842`  |  `0.09293336421251297`  |  
|  hit@1  |  `0.017849205061793327`  |  `0.07135140895843506`  |  `0.04460030794143677`  |  
|  hit@3  |  `0.03962698578834534`  |  `0.14349065721035004`  |  `0.09155882149934769`  |  
|  hit@10  |  `0.09651586413383484`  |  `0.26698052883148193`  |  `0.1817481964826584`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `3`   
- epoch `4`, loss `0.7539322376251221`, time `2021-06-22 12:19:43`  
- epoch `5`, loss `0.7176157832145691`, time `2021-06-22 12:23:49`  
- epoch `6`, loss `0.6806583404541016`, time `2021-06-22 13:40:40`  
- validation results  at epoch `6`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `660.4166870117188`  |  `235.6698455810547`  |  `448.04327392578125`  |  
|  mean reciprocal rank (MRR)  |  `0.0577998012304306`  |  `0.16725973784923553`  |  `0.11252976953983307`  |  
|  hit@1  |  `0.020448338240385056`  |  `0.09645075350999832`  |  `0.05844954401254654`  |  
|  hit@3  |  `0.05112135037779808`  |  `0.17297989130020142`  |  `0.1120506227016449`  |  
|  hit@10  |  `0.1261969953775406`  |  `0.3082631528377533`  |  `0.21723008155822754`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `6`   
- epoch `7`, loss `0.6506888270378113`, time `2021-06-22 14:09:26`  
- epoch `8`, loss `0.6291739344596863`, time `2021-06-22 14:13:38`  
- epoch `9`, loss `0.6116292476654053`, time `2021-06-22 14:17:42`  
- validation results  at epoch `9`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `640.579345703125`  |  `215.45074462890625`  |  `428.0150451660156`  |  
|  mean reciprocal rank (MRR)  |  `0.06271404772996902`  |  `0.1713772416114807`  |  `0.11704564094543457`  |  
|  hit@1  |  `0.023118680343031883`  |  `0.09265778213739395`  |  `0.05788823217153549`  |  
|  hit@3  |  `0.05527010187506676`  |  `0.1800471842288971`  |  `0.11765864491462708`  |  
|  hit@10  |  `0.13510090112686157`  |  `0.3303181827068329`  |  `0.23270954191684723`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `9`   
- epoch `10`, loss `0.5921932458877563`, time `2021-06-22 14:47:15`  
- epoch `11`, loss `0.5750247836112976`, time `2021-06-22 14:51:17`  
- epoch `12`, loss `0.5631678104400635`, time `2021-06-22 14:55:23`  
- validation results  at epoch `12`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `630.3241577148438`  |  `206.2979278564453`  |  `418.31103515625`  |  
|  mean reciprocal rank (MRR)  |  `0.06827127188444138`  |  `0.18142446875572205`  |  `0.12484787404537201`  |  
|  hit@1  |  `0.02685689367353916`  |  `0.10424772650003433`  |  `0.06555230915546417`  |  
|  hit@3  |  `0.06311854720115662`  |  `0.18903404474258423`  |  `0.12607629597187042`  |  
|  hit@10  |  `0.14870791137218475`  |  `0.33769237995147705`  |  `0.2432001531124115`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `12`   
- epoch `13`, loss `0.5506113171577454`, time `2021-06-22 15:24:29`  
- epoch `14`, loss `0.5415815711021423`, time `2021-06-22 15:28:37`  
- epoch `15`, loss `0.5315135717391968`, time `2021-06-22 15:32:43`  
- validation results  at epoch `15`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `629.7864990234375`  |  `208.18255615234375`  |  `418.9845275878906`  |  
|  mean reciprocal rank (MRR)  |  `0.06928517669439316`  |  `0.18249857425689697`  |  `0.12589187920093536`  |  
|  hit@1  |  `0.02559119649231434`  |  `0.10356876254081726`  |  `0.06457997858524323`  |  
|  hit@3  |  `0.06389141082763672`  |  `0.19029761850833893`  |  `0.12709450721740723`  |  
|  hit@10  |  `0.15221720933914185`  |  `0.3451991081237793`  |  `0.24870815873146057`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `15`   
- epoch `16`, loss `0.5229312777519226`, time `2021-06-22 16:01:30`  
- epoch `17`, loss `0.5165868997573853`, time `2021-06-22 16:05:34`  
- epoch `18`, loss `0.5084328651428223`, time `2021-06-22 16:09:39`  
- validation results  at epoch `18`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `631.59375`  |  `205.7021484375`  |  `418.64794921875`  |  
|  mean reciprocal rank (MRR)  |  `0.07036307454109192`  |  `0.18581125140190125`  |  `0.12808716297149658`  |  
|  hit@1  |  `0.02666967175900936`  |  `0.1066170260310173`  |  `0.06664334982633591`  |  
|  hit@3  |  `0.06426122039556503`  |  `0.19399891793727875`  |  `0.1291300654411316`  |  
|  hit@10  |  `0.15670894086360931`  |  `0.3482162356376648`  |  `0.25246259570121765`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `18`   
- epoch `19`, loss `0.4998975396156311`, time `2021-06-22 16:38:27`  
- epoch `20`, loss `0.4939039945602417`, time `2021-06-22 16:42:31`  
- epoch `21`, loss `0.4863327443599701`, time `2021-06-22 16:46:34`  
- validation results  at epoch `21`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `639.4378051757812`  |  `209.7955780029297`  |  `424.61669921875`  |  
|  mean reciprocal rank (MRR)  |  `0.0700468048453331`  |  `0.188163161277771`  |  `0.12910498678684235`  |  
|  hit@1  |  `0.025114336982369423`  |  `0.11117576062679291`  |  `0.06814505159854889`  |  
|  hit@3  |  `0.06390462070703506`  |  `0.19480931758880615`  |  `0.1293569654226303`  |  
|  hit@10  |  `0.15757404267787933`  |  `0.34263303875923157`  |  `0.25010353326797485`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `21`   
- epoch `22`, loss `0.48008739948272705`, time `2021-06-22 17:15:30`  
- epoch `23`, loss `0.47410786151885986`, time `2021-06-22 17:19:33`  
- epoch `24`, loss `0.4696379601955414`, time `2021-06-22 17:23:38`  
- validation results  at epoch `24`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `649.9506225585938`  |  `213.63401794433594`  |  `431.7923278808594`  |  
|  mean reciprocal rank (MRR)  |  `0.07139761000871658`  |  `0.18594445288181305`  |  `0.12867103517055511`  |  
|  hit@1  |  `0.026280220597982407`  |  `0.10457384586334229`  |  `0.0654270350933075`  |  
|  hit@3  |  `0.06557878106832504`  |  `0.19790299236774445`  |  `0.13174088299274445`  |  
|  hit@10  |  `0.16070930659770966`  |  `0.34731653332710266`  |  `0.25401291251182556`  |  
   
#### testing
- testing results  
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `640.1906127929688`  |  `213.71372985839844`  |  `426.9521789550781`  |  
|  mean reciprocal rank (MRR)  |  `0.07189895212650299`  |  `0.18386411666870117`  |  `0.12788152694702148`  |  
|  hit@1  |  `0.02768615633249283`  |  `0.1046917736530304`  |  `0.06618896126747131`  |  
|  hit@3  |  `0.06710715591907501`  |  `0.19382818043231964`  |  `0.13046766817569733`  |  
|  hit@10  |  `0.1575881540775299`  |  `0.3436853289604187`  |  `0.2506367564201355`  |  
   
-----
  
-----
### Running Time: `2021-06-23 22:58:50`
#### configuration
- load data from `../data/FB15K237/`
- continue training: `False`
- embedding dimension: `200`
- number of bases: `50`
- rgcn aggregation scheme: `add`
- train batch size: `10240`
- validation/test batch size: `100`
- learning rate: `0.01`
- number of epochs: `100`
- number of negative triples: `16`
- number of entities: `14541`
- number of relations: `238`
- number of training triples: `272115`
- number of validation triples: `17535`
- number of testing triples: `20466`
- patience: `2`
- model parameters: `['entity_embeds', 'rgcn.bases', 'rgcn.coefficients']`
#### training
- epoch `0`, loss `12.044849395751953`, time `2021-06-23 23:05:53`  
- validation results  at epoch `0`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `899.597900390625`  |  `615.909423828125`  |  `757.753662109375`  |  
|  mean reciprocal rank (MRR)  |  `0.03345899283885956`  |  `0.12089839577674866`  |  `0.07717869430780411`  |  
|  hit@1  |  `0.01015421375632286`  |  `0.07149844616651535`  |  `0.040826328098773956`  |  
|  hit@3  |  `0.025665579363703728`  |  `0.11993977427482605`  |  `0.07280267775058746`  |  
|  hit@10  |  `0.07036526501178741`  |  `0.21863707900047302`  |  `0.14450117945671082`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `0`   
- epoch `1`, loss `2.4342567920684814`, time `2021-06-24 00:47:45`  
- epoch `2`, loss `1.9036471843719482`, time `2021-06-24 00:54:47`  
- epoch `3`, loss `1.6542465686798096`, time `2021-06-24 01:02:26`  
- validation results  at epoch `3`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `414.2619934082031`  |  `268.3785400390625`  |  `341.32025146484375`  |  
|  mean reciprocal rank (MRR)  |  `0.08033743500709534`  |  `0.18932361900806427`  |  `0.1348305344581604`  |  
|  hit@1  |  `0.03306868299841881`  |  `0.1106327697634697`  |  `0.0718507245182991`  |  
|  hit@3  |  `0.07494998723268509`  |  `0.20300878584384918`  |  `0.13897939026355743`  |  
|  hit@10  |  `0.1735212802886963`  |  `0.3529105484485626`  |  `0.26321589946746826`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `3`   
- epoch `4`, loss `1.5301905870437622`, time `2021-06-24 02:43:51`  
- epoch `5`, loss `1.4372949600219727`, time `2021-06-24 02:50:55`  
- epoch `6`, loss `1.375123381614685`, time `2021-06-24 02:58:27`  
- validation results  at epoch `6`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `403.85791015625`  |  `277.0229187011719`  |  `340.4404296875`  |  
|  mean reciprocal rank (MRR)  |  `0.0866672694683075`  |  `0.19560323655605316`  |  `0.14113524556159973`  |  
|  hit@1  |  `0.03506659343838692`  |  `0.1144392192363739`  |  `0.07475290447473526`  |  
|  hit@3  |  `0.08211130648851395`  |  `0.21078497171401978`  |  `0.14644813537597656`  |  
|  hit@10  |  `0.190795436501503`  |  `0.36247581243515015`  |  `0.27663561701774597`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `6`   
- epoch `7`, loss `1.3153523206710815`, time `2021-06-24 04:39:18`  
- epoch `8`, loss `1.2605923414230347`, time `2021-06-24 04:46:14`  
- epoch `9`, loss `1.2285839319229126`, time `2021-06-24 04:54:04`  
- validation results  at epoch `9`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `391.1888427734375`  |  `279.3309020996094`  |  `335.2598876953125`  |  
|  mean reciprocal rank (MRR)  |  `0.0947604700922966`  |  `0.1998434066772461`  |  `0.14730194211006165`  |  
|  hit@1  |  `0.03869256004691124`  |  `0.11645971983671188`  |  `0.07757613807916641`  |  
|  hit@3  |  `0.09245046973228455`  |  `0.21483828127384186`  |  `0.1536443829536438`  |  
|  hit@10  |  `0.20752958953380585`  |  `0.3729853630065918`  |  `0.2902574837207794`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `9`   
- epoch `10`, loss `1.174804449081421`, time `2021-06-24 06:33:18`  
- epoch `11`, loss `1.1306581497192383`, time `2021-06-24 06:41:19`  
- epoch `12`, loss `1.0995570421218872`, time `2021-06-24 06:48:58`  
- validation results  at epoch `12`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `410.2177429199219`  |  `305.877685546875`  |  `358.0477294921875`  |  
|  mean reciprocal rank (MRR)  |  `0.09812421351671219`  |  `0.188721165060997`  |  `0.1434226930141449`  |  
|  hit@1  |  `0.040409792214632034`  |  `0.10437140613794327`  |  `0.0723906010389328`  |  
|  hit@3  |  `0.09735702723264694`  |  `0.20354509353637695`  |  `0.15045106410980225`  |  
|  hit@10  |  `0.21666374802589417`  |  `0.36434584856033325`  |  `0.2905048131942749`  |  
   
- epoch `13`, loss `1.069536566734314`, time `2021-06-24 08:29:51`  
- epoch `14`, loss `1.0407575368881226`, time `2021-06-24 08:37:30`  
- epoch `15`, loss `1.0127179622650146`, time `2021-06-24 08:45:58`  
- validation results  at epoch `15`
   
|  metric  |  head  |  tail  |  mean  |  
|  ----  |  ----  |  ----  |  ----  |  
|  mean rank (MR)  |  `425.96856689453125`  |  `325.3756408691406`  |  `375.672119140625`  |  
|  mean reciprocal rank (MRR)  |  `0.10357498377561569`  |  `0.19143839180469513`  |  `0.1475066840648651`  |  
|  hit@1  |  `0.044668179005384445`  |  `0.10368581116199493`  |  `0.07417699694633484`  |  
|  hit@3  |  `0.1030416265130043`  |  `0.20968987047672272`  |  `0.1563657522201538`  |  
|  hit@10  |  `0.22400698065757751`  |  `0.3758106231689453`  |  `0.2999088168144226`  |  
   
- model saved to `../pretrained/FB15K237/rgcn_lp.pt` at epoch `15`   
- epoch `16`, loss `0.9911497235298157`, time `2021-06-24 10:24:24`  
- epoch `17`, loss `0.9515782594680786`, time `2021-06-24 10:32:20`  
-----
### Running - `2021-09-01 14:35:08`
#### Configurations
- load data from `../data/FB15K237/`
- new training
- embedding dimension: `100`
- number of negative triples: `1`
- learning rate: `0.0005`
- dropout rate: `0.2`
- regularization loss ratio: `0.01`
- number of bases: `50`
- rgcn aggregation scheme: `add`
- number of subgraphs: `200`
- training subgraph batch size: `24`
- number of epochs: `50`
- validation frequency: `1`
- validation/test triple batch size: `12`
- highest mrr: `0.0`
- device: `cuda:2`
#### Preparing Data
- number of entities: `14541`
- number of original relations: `237`
- number of original training triples: `272115`
- number of validation triples: `17535`
- number of testing triples: `20466`
Computing METIS partitioning...
Done!
#### Model Training and Validation
