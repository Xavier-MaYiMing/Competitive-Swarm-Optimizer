### Competitive Swarm Optimizer

##### Reference: Cheng R, Jin Y. A competitive swarm optimizer for large scale optimization[J]. IEEE Transactions on Cybernetics, 2014, 45(2): 191-204.

CSO is a powerful algorithm for large scale optimization. Large scale optimization contains a huge number of decision variables.

| Variables | Meaning                                                 |
| --------- | ------------------------------------------------------- |
| npop      | population size                                         |
| iter      | iteration number                                        |
| lb        | lower bound                                             |
| ub        | upper bound                                             |
| phi       | a pre-defined parameter to control the social component |
| opt       | the shifted value of sphere function                    |
| dim       | dimension                                               |
| pos       | the position of particles                               |
| vel       | velocity                                                |
| objs      | objectives                                              |
| gbest     | the global best                                         |
| iter_best | the global best of each iteration                       |
| con_iter  | convergence iteration                                   |
| center    | the center position of all particles                    |

#### Test problem: shifted sphere function (dimension = 1000)

$$
\nonumber f(x) = \sum_{i=1}^{dim}(x_i - opt_i)^2
$$




#### Example

```python
if __name__ == '__main__':
    t_npop = 500
    t_iter = 4000
    t_lb = np.array([-100] * 1000)
    t_ub = np.array([100] * 1000)
    t_phi = 0.15
    t_opt = np.random.uniform(-100, 100, 1000)
    print(main(t_npop, t_iter, t_lb, t_ub, t_phi, t_opt))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Competitive-Swarm-Optimizer/blob/main/convergence%20curve.png)

The CSO converges at its **3,999-th** iteration, and the global best value is **3.381813579426321e-05**. 

```python
Iteration 20: gbest is 5938245.981462865
Iteration 40: gbest is 4895269.212959823
Iteration 60: gbest is 4121488.061213823
Iteration 80: gbest is 3547963.930919267
Iteration 100: gbest is 3023251.9079930573
Iteration 120: gbest is 2581085.1271176343
Iteration 140: gbest is 2180216.203772705
Iteration 160: gbest is 1858914.6887389487
Iteration 180: gbest is 1584794.8048512558
Iteration 200: gbest is 1346522.3520201216
Iteration 220: gbest is 1153968.5141699857
Iteration 240: gbest is 982362.6728243511
Iteration 260: gbest is 848397.0649723038
Iteration 280: gbest is 696540.6210040661
Iteration 300: gbest is 602280.6453506339
Iteration 320: gbest is 510628.07862172835
Iteration 340: gbest is 438370.9889391544
Iteration 360: gbest is 370846.7917446213
Iteration 380: gbest is 325232.9219113686
Iteration 400: gbest is 271355.9276420551
Iteration 420: gbest is 239365.94532632944
Iteration 440: gbest is 202871.0342581668
Iteration 460: gbest is 172724.98930493873
Iteration 480: gbest is 150192.28309012818
Iteration 500: gbest is 124395.80336593278
Iteration 520: gbest is 110830.09978587294
Iteration 540: gbest is 98650.6102144665
Iteration 560: gbest is 85123.33498105613
Iteration 580: gbest is 75282.12121008245
Iteration 600: gbest is 63209.38309751457
Iteration 620: gbest is 55256.62649830444
Iteration 640: gbest is 50761.498131319924
Iteration 660: gbest is 43679.67701369888
Iteration 680: gbest is 37711.901870535134
Iteration 700: gbest is 33880.55139676248
Iteration 720: gbest is 29491.378114105886
Iteration 740: gbest is 25420.94617364251
Iteration 760: gbest is 23312.686109096016
Iteration 780: gbest is 19803.594194740428
Iteration 800: gbest is 17976.969065539044
Iteration 820: gbest is 15647.149368889028
Iteration 840: gbest is 13520.137761126074
Iteration 860: gbest is 12166.158303063581
Iteration 880: gbest is 10797.676090600582
Iteration 900: gbest is 9542.40717887508
Iteration 920: gbest is 8447.270247165407
Iteration 940: gbest is 7461.406475549846
Iteration 960: gbest is 6544.373020719863
Iteration 980: gbest is 5771.530434238332
Iteration 1000: gbest is 5182.661750197643
Iteration 1020: gbest is 4549.676271437019
Iteration 1040: gbest is 3957.522801961396
Iteration 1060: gbest is 3475.371259485106
Iteration 1080: gbest is 3072.111482816191
Iteration 1100: gbest is 2659.8795924861965
Iteration 1120: gbest is 2327.399480425812
Iteration 1140: gbest is 2065.1206792405087
Iteration 1160: gbest is 1774.9502057230045
Iteration 1180: gbest is 1572.6544496674248
Iteration 1200: gbest is 1456.8312101615168
Iteration 1220: gbest is 1206.464363635384
Iteration 1240: gbest is 1089.5181839933782
Iteration 1260: gbest is 947.365419429776
Iteration 1280: gbest is 833.7380034392424
Iteration 1300: gbest is 716.2113811113624
Iteration 1320: gbest is 657.7575868433785
Iteration 1340: gbest is 578.2575866262886
Iteration 1360: gbest is 514.6419556404402
Iteration 1380: gbest is 456.6710153621861
Iteration 1400: gbest is 392.3645720978081
Iteration 1420: gbest is 338.8704531296519
Iteration 1440: gbest is 298.67028915194635
Iteration 1460: gbest is 273.1882058321936
Iteration 1480: gbest is 225.07556060955022
Iteration 1500: gbest is 216.26279781293556
Iteration 1520: gbest is 190.69421467631588
Iteration 1540: gbest is 161.00480907018107
Iteration 1560: gbest is 148.08625294106358
Iteration 1580: gbest is 127.05986909003147
Iteration 1600: gbest is 106.42798652020876
Iteration 1620: gbest is 99.16063333206925
Iteration 1640: gbest is 89.65613227119977
Iteration 1660: gbest is 79.31603041016895
Iteration 1680: gbest is 68.37416098034912
Iteration 1700: gbest is 62.096085270663
Iteration 1720: gbest is 55.003974116009026
Iteration 1740: gbest is 46.752415394738726
Iteration 1760: gbest is 41.22429142899353
Iteration 1780: gbest is 37.84008943943226
Iteration 1800: gbest is 31.91572969299857
Iteration 1820: gbest is 28.70344283718289
Iteration 1840: gbest is 26.096482694796183
Iteration 1860: gbest is 21.68991770474911
Iteration 1880: gbest is 20.522825932229345
Iteration 1900: gbest is 17.226060074284305
Iteration 1920: gbest is 15.274543984880914
Iteration 1940: gbest is 13.835330791809575
Iteration 1960: gbest is 11.794545552976158
Iteration 1980: gbest is 10.718860319584783
Iteration 2000: gbest is 9.521352026016581
Iteration 2020: gbest is 8.105314776165761
Iteration 2040: gbest is 7.137583940468036
Iteration 2060: gbest is 6.4447976744760505
Iteration 2080: gbest is 5.597763805431914
Iteration 2100: gbest is 4.813397121579495
Iteration 2120: gbest is 4.46455802556717
Iteration 2140: gbest is 3.8621926787485648
Iteration 2160: gbest is 3.4288562291136437
Iteration 2180: gbest is 2.940423726147907
Iteration 2200: gbest is 2.610324768616438
Iteration 2220: gbest is 2.3438280076954072
Iteration 2240: gbest is 2.133124474072049
Iteration 2260: gbest is 1.8158355452243313
Iteration 2280: gbest is 1.6227698980440013
Iteration 2300: gbest is 1.4270624756303125
Iteration 2320: gbest is 1.2304473224969688
Iteration 2340: gbest is 1.122098097542913
Iteration 2360: gbest is 0.9899044492860042
Iteration 2380: gbest is 0.8833423802436599
Iteration 2400: gbest is 0.7690377466908728
Iteration 2420: gbest is 0.6808298781050224
Iteration 2440: gbest is 0.5943950715442403
Iteration 2460: gbest is 0.5025619952883158
Iteration 2480: gbest is 0.46868283863207727
Iteration 2500: gbest is 0.4071089358456748
Iteration 2520: gbest is 0.370942213360687
Iteration 2540: gbest is 0.3216873141962989
Iteration 2560: gbest is 0.2945415450685435
Iteration 2580: gbest is 0.2606963454923335
Iteration 2600: gbest is 0.22402227929893176
Iteration 2620: gbest is 0.2013166063689436
Iteration 2640: gbest is 0.16808623623977287
Iteration 2660: gbest is 0.1533103046038206
Iteration 2680: gbest is 0.1378614672082706
Iteration 2700: gbest is 0.11986352317375898
Iteration 2720: gbest is 0.1085215999977062
Iteration 2740: gbest is 0.09576593191488869
Iteration 2760: gbest is 0.08454846363843936
Iteration 2780: gbest is 0.0732384524740587
Iteration 2800: gbest is 0.06152310885894064
Iteration 2820: gbest is 0.05611615289405173
Iteration 2840: gbest is 0.051310071619664846
Iteration 2860: gbest is 0.042775505436373394
Iteration 2880: gbest is 0.038690794369156754
Iteration 2900: gbest is 0.03378633616883895
Iteration 2920: gbest is 0.029471968381144124
Iteration 2940: gbest is 0.02713532848639155
Iteration 2960: gbest is 0.02403105411598375
Iteration 2980: gbest is 0.020928183930818706
Iteration 3000: gbest is 0.0181372485687862
Iteration 3020: gbest is 0.016397014175886834
Iteration 3040: gbest is 0.014506454796547339
Iteration 3060: gbest is 0.012136954303810605
Iteration 3080: gbest is 0.010850413316009505
Iteration 3100: gbest is 0.009342105824056006
Iteration 3120: gbest is 0.008414210576890117
Iteration 3140: gbest is 0.007044002135049117
Iteration 3160: gbest is 0.006459441710016715
Iteration 3180: gbest is 0.005676904931097837
Iteration 3200: gbest is 0.0050512901181104545
Iteration 3220: gbest is 0.004539549125217875
Iteration 3240: gbest is 0.0038390048801048146
Iteration 3260: gbest is 0.003531825892045131
Iteration 3280: gbest is 0.002981164825127384
Iteration 3300: gbest is 0.002604223145322422
Iteration 3320: gbest is 0.0022782214218586144
Iteration 3340: gbest is 0.0021507243437279416
Iteration 3360: gbest is 0.0017892123732017684
Iteration 3380: gbest is 0.0015942917632605295
Iteration 3400: gbest is 0.0014530614747080449
Iteration 3420: gbest is 0.0012395138474270279
Iteration 3440: gbest is 0.001108465192560528
Iteration 3460: gbest is 0.0010185162265368075
Iteration 3480: gbest is 0.000857200959324919
Iteration 3500: gbest is 0.0007668402885041707
Iteration 3520: gbest is 0.0006922625621047983
Iteration 3540: gbest is 0.0005905336288496709
Iteration 3560: gbest is 0.0005445442301598931
Iteration 3580: gbest is 0.000474141610942058
Iteration 3600: gbest is 0.0004252465296185931
Iteration 3620: gbest is 0.00037798206884196854
Iteration 3640: gbest is 0.0003114401723811033
Iteration 3660: gbest is 0.00028759817714387923
Iteration 3680: gbest is 0.0002539371660806658
Iteration 3700: gbest is 0.00021692922732206065
Iteration 3720: gbest is 0.0001910691902594241
Iteration 3740: gbest is 0.0001750478870631841
Iteration 3760: gbest is 0.0001532766743290729
Iteration 3780: gbest is 0.00013591800454445475
Iteration 3800: gbest is 0.00011776028426676655
Iteration 3820: gbest is 0.00010397536809999654
Iteration 3840: gbest is 9.269587391810464e-05
Iteration 3860: gbest is 8.375458455096237e-05
Iteration 3880: gbest is 7.276766673693633e-05
Iteration 3900: gbest is 6.429705991797652e-05
Iteration 3920: gbest is 5.535113538315996e-05
Iteration 3940: gbest is 4.7956699353642054e-05
Iteration 3960: gbest is 4.441530656834307e-05
Iteration 3980: gbest is 3.7787391270890426e-05
Iteration 4000: gbest is 3.381813579426321e-05
{
  'gbest': 3.381813579426321e-05, 
  'convergence iteration': 3999
}
```

