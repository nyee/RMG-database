#!/usr/bin/env python
# encoding: utf-8

name = "publishedIBuOH"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29812,0.000824944,-8.14302e-07,-9.47543e-11,4.13487e-13,-1012.52,-3.29409], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.99142,0.000700064,-5.63383e-08,-9.23158e-12,1.58275e-15,-835.034,-1.35511], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "CO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.27572,0.00992207,-1.04091e-05,6.86669e-09,-2.11728e-12,-48373.1,10.1885], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.45362,0.00314017,-1.27841e-06,2.394e-10,-1.66903e-14,-48967,-0.955396], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CO",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26245,0.00151194,-3.88176e-06,5.58194e-09,-2.47495e-12,-14310.5,4.8489], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.02508,0.00144269,-5.63083e-07,1.01858e-10,-6.91095e-15,-14268.4,6.10822], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.14988,-0.013671,4.91801e-05,-4.84743e-08,1.66694e-11,-10246.6,-4.6413], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.0748515,0.0133909,-5.73286e-06,1.22293e-09,-1.01815e-13,-9468.34,18.4373], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/88
CH3               L11/89C   1H   3          G   200.000  3500.000  1000.000    1
2.28571772E+00 7.23990037E-03-2.98714348E-06 5.95684644E-10-4.67154394E-14    2
1.67755843E+04 8.48007179E+00 3.67359040E+00 2.01095175E-03 5.73021856E-06    3
-6.87117425E-09 2.54385734E-12 1.64449988E+04 1.60456433E+00                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9592,-0.00757052,5.7099e-05,-6.91589e-08,2.69884e-11,5089.78,4.09733], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.03611,0.0146454,-6.71078e-06,1.47223e-09,-1.25706e-13,4939.89,10.3054], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.808681,0.0233616,-3.55172e-05,2.80152e-08,-8.50073e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14757,0.00596167,-2.37295e-06,4.67412e-10,-3.61235e-14,25936,-1.23028], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.29142,-0.00550154,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66682], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.07188,0.0216853,-1.00256e-05,2.21412e-09,-1.90003e-13,-11426.4,15.1156], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/88
C2H5              L12/92C   2H   5          G   200.000  3500.000  1000.000    1
1.95465642E+00 1.73972722E-02-7.98206668E-06 1.75217689E-09-1.49641576E-13    2
1.28575200E+04 1.34624343E+01 4.30646568E+00-4.18658892E-03 4.97142807E-05    3
-5.99126606E-08 2.30509004E-11 1.28416265E+04 4.70720924E+00                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64256,0.00389758,4.5491e-05,-5.49011e-08,1.92836e-11,778.192,8.61458], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.4256,0.0175791,-6.56312e-06,1.032e-09,-5.99721e-14,-608.799,-5.16515], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
aC3H5 ATcT              C   3H   5    0    0G   200.000  6000.000 1000.        1
0.70094568E+01 0.13106629E-01-0.46533442E-05 0.74514323E-09-0.44350051E-13    2
0.16412909E+05-0.13946114E+02 0.14698036E+01 0.19034365E-01 0.14480425E-04    3
-0.35468652E-07 0.16647594E-10 0.18325831E+05 0.16724114E+02 0.19675772E+05    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.933554,0.0264246,6.10597e-06,-2.19775e-08,9.51493e-12,-13958.5,19.2017], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.53414,0.0188722,-6.27185e-06,9.14756e-10,-4.78381e-14,-16467.5,-17.8923], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""L 4/85""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "aC3H4",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56619,0.00429173,3.37755e-05,-4.29088e-08,1.54512e-11,22025.5,7.34163], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.2021,0.0116035,-4.24253e-06,6.49614e-10,-3.68734e-14,20614.4,-9.81678], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "pC3H4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68039,0.0157997,2.50706e-06,-1.36576e-08,6.61543e-12,20802.4,9.87694], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.02524,0.0113365,-4.02234e-06,6.43761e-10,-3.82996e-14,19620.9,-8.60438], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
pC3H4 RMG         101993H   4C   3          g   300.00   4000.00  1400.00      1
6.49915743E+00 1.03333141E-02-3.44377558E-06 5.31758469E-10-3.09746438E-14    2
1.95733009E+04-1.12322911E+01 3.23861443E+00 1.03401230E-02 1.62943646E-05    3
-2.59237505E-08 9.94012980E-12 2.08707158E+04 7.74058985E+00                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "CH3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.7154,-0.0152309,6.52441e-05,-7.10807e-08,2.61353e-11,-25642.8,-1.5041], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.78971,0.0140938,-6.36501e-06,1.38171e-09,-1.1706e-13,-25374.9,14.5024], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/88
CH3O              121686C   1H   3O   1     G   300.00   3000.00   1000.000    1
0.03770799E+02 0.07871497E-01-0.02656384E-04 0.03944431E-08-0.02112616E-12    2
0.12783252E+03 0.02929575E+02 0.02106204E+02 0.07216595E-01 0.05338472E-04    3
-0.07377636E-07 0.02075610E-10 0.09786011E+04 0.13152177E+02                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "C4H8-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38887,0.0116753,5.39188e-05,-7.10068e-08,2.57553e-11,-1932.89,12.4275], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.06996,0.0230144,-8.63502e-06,1.36144e-09,-7.92543e-14,-4357.38,-17.6346], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
C4H6-13 ATcT            C  4.H  6.   0.   0.G   200.000  6000.000 1000.        1
7.62637466E+00 1.72523403E-02-6.09184911E-06 9.70800102E-10-5.76169721E-14    2
9.55306395E+03-1.48325259E+01 4.10599669E+00 5.05575563E-03 5.83885454E-05    3
-8.05950198E-08 3.27447711E-11 1.15092468E+04 8.42978067E+00 1.33302095E+04    4
C4H6-13 UGhent          C   4H   6O   0     G   300.000  1500.000 1388.000     1
1.26945000e+01-4.20000000e-02 1.29300000e-04-1.13500000e-07 3.22800000e-11    2
1.06000000e+04-3.12800000e+01 1.26945000e+01-4.20000000e-02 1.29300000e-04    3
-1.13500000e-07 3.22800000e-11 1.06000000e+04-3.12800000e+01                   4
Primary Thermo Library: Franklin (Species ID: CH2CHCHCH2)
C4H6-13                 C   4H   6          G   300.000  5000.000   995.043    1
1.19566649E+01 1.22667289E-02-3.93178071E-06 5.85264319E-10-3.30283117E-14    2
9.08784501E+03-4.17705168E+01 3.25557260E+00 4.77664223E-03 7.13784514E-05    3
-9.27637286E-08 3.41969166E-11 1.29218292E+04 1.07283147E+01                   4
C4H7-21 ATcT            C  4.H  7.   0.   0.G   200.000  6000.000 1000.        1
8.08107449E+00 1.95526544E-02-6.93149115E-06 1.10889183E-09-6.59584410E-14    2
1.22822959E+04-1.67137903E+01 4.54746808E+00 4.63771460E-03 6.61340221E-05    3
-8.97456502E-08 3.61716165E-11 1.43843217E+04 7.30313471E+00 1.63702936E+04    4
C4H7-14 RMG             C   4H   7O   0     G   300.000  5000.000   995.043    1
7.94091392E+00 2.03706945E-02-7.60359212E-06 1.19148613E-09-6.90032547E-14    2
2.05614959E+04-1.41946431E+01 3.39149547E+00 1.24899595E-02 4.37255626E-05    3
-5.96288908E-08 2.18523756E-11 2.27623820E+04 1.42408981E+01                   4
C4H7-14 ATcT            C  4.H  7.   0.   0.G   200.000  6000.000 1000.        1
8.49073768E+00 1.91056974E-02-6.74370664E-06 1.07343267E-09-6.36251837E-14    2
2.04659294E+04-1.74555814E+01 5.07355313E+00 5.27619329E-03 6.23441322E-05    3
-8.54203458E-08 3.45890031E-11 2.24615054E+04 5.60318035E+00 2.46070249E+04    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C4H6-13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73145,0.0139064,4.30538e-05,-6.34108e-08,2.42036e-11,11425,12.4058], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.9678,0.0129511,-3.97761e-06,5.74948e-10,-3.17795e-14,8194.12,-35.2875], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""RMG       120189
C4H6-12 ATcT            C  4.H  6.   0.   0.G   200.000  6000.000 1000.        1
8.13872997E+00 1.68655431E-02-5.97324908E-06 9.54915173E-10-5.67693708E-14    2
1.55467985E+04-1.77959041E+01 2.90828336E+00 1.79025349E-02 2.61486503E-05    3
-4.81598832E-08 2.11295844E-11 1.75928783E+04 1.23118106E+01 1.94015186E+04    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "nC4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30539,0.0169397,5.26457e-05,-7.16205e-08,2.60936e-11,-17321.9,12.2504], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.14176,0.0281602,-1.04914e-05,1.64919e-09,-9.58549e-14,-19802.3,-18.6858], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
C4H9-1 ATcT             C  4.H  9.   0.   0.G   200.000  6000.000 1000.        1
8.97401527E+00 2.39704154E-02-8.48703645E-06 1.35644127E-09-8.06234913E-14    2
5.19161526E+03-2.31075609E+01 4.73737837E+00 9.69051565E-03 6.63846383E-05    3
-9.24799302E-08 3.74006099E-11 7.57382332E+03 4.91063455E+00 9.83838903E+03    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44486e-12,-1020.9,3.95037], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C2H5OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u0 p2 c0 {2,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.8587,-0.00374017,6.95554e-05,-8.86548e-08,3.51688e-11,-29996.1,4.80185], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.56244,0.0152042,-5.38968e-06,8.6225e-10,-5.12898e-14,-31525.6,-9.47302], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "benzene",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68313,0.00229289,0.000101785,-1.27824e-07,4.65089e-11,8443.58,13.6039], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.799,0.0176656,-5.86431e-06,8.97295e-10,-5.17334e-14,3656.25,-49.0892], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""FULVENE    98 MARINOVC&FC   6H   6    0    0G   300.000  3000.000 1000.00      1
0.55099388E+01 0.33879936E-01-0.17737071E-04 0.44769284E-08-0.44127372E-12    2
0.24921871E+05-0.67757489E+01-0.56096307E+01 0.73064757E-01-0.70326923E-04    3
0.36580449E-07-0.80201931E-11 0.27468885E+05 0.48339178E+02                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "nC4H10O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70583,0.0235896,4.52853e-05,-6.96971e-08,2.63176e-11,-35691,13.63], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.8813,0.0280003,-1.14955e-05,1.93299e-09,-1.17933e-13,-38765.3,-29.2243], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
C4H9O-5 ATcT            C  4.H  9.O  1.   0.G   200.000  6000.000 1000.        1
1.21336180E+01 2.43954328E-02-9.04409323E-06 1.48350965E-09-8.96467065E-14    2
-1.29883091E+04-3.89685328E+01 5.61984431E+00 2.12772932E-03 1.02679749E-04    3
-1.34097807E-07 5.25493048E-11-9.21442557E+03 4.46683857E+00-6.77732206E+03    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {4,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21247,0.00151479,2.59209e-05,-3.57658e-08,1.47151e-11,34859.8,8.51054], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.01672,0.0103302,-4.68082e-06,1.01763e-09,-8.62607e-14,34612.9,7.78732], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 2/92""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "CH2CO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13584,0.0181189,-1.73947e-05,9.34398e-09,-2.01458e-12,-7042.92,12.2156], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5113,0.0090036,-4.1694e-06,9.23346e-10,-7.94838e-14,-7551.05,0.632247], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 5/90""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C2H4O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35283,0.00395169,3.77359e-05,-4.90583e-08,1.79706e-11,-16315.5,10.092], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.49771,0.0091834,-3.15511e-06,4.50623e-10,-2.39651e-14,-18224.3,-15.3304], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
nC4H10 ATcT             C  4.H 10.   0.   0.G   200.000  6000.000 1000.        1
9.44547835E+00 2.57856620E-02-9.23613194E-06 1.48631762E-09-8.87891206E-14    2
-2.01383773E+04-2.63477585E+01 6.14474013E+00 1.64500242E-04 9.67848789E-05    3
-1.25486208E-07 4.97846257E-11-1.75989467E+04-1.08058878E+00-1.51289733E+04    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "CH3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9768,0.00129697,3.42853e-05,-4.02528e-08,1.40451e-11,-21395.3,7.45498], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.07429,0.0118656,-4.22924e-06,6.81522e-10,-4.08544e-14,-22355.3,-1.56091], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""DO NOT WANT TO USE GRI-MECH DEFINED C3H7 SPECIES
C3H7              L 9/84C   3H   7          G   300.000  5000.000  1000.000    1
0.77026987E+01 0.16044203E-01-0.52833220E-05 0.76298590E-09-0.39392284E-13    2
0.82984336E+04-0.15480180E+02 0.10515518E+01 0.25991980E-01 0.23800540E-05    3
-0.19609569E-07 0.93732470E-11 0.10631863E+05 0.21122559E+02                   4
Primary Thermo Library: CFG (Species ID: CH3CHO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38684,0.00347498,-6.3547e-06,6.96858e-09,-2.50659e-12,-30208.1,2.59023], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67215,0.00305629,-8.73026e-07,1.201e-10,-6.39162e-15,-29899.2,6.86282], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""20387
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "nC4H8O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76176,0.0257748,2.18481e-05,-4.22257e-08,1.6587e-11,-27243.7,11.5658], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.57363,0.0246958,-1.01185e-05,1.69849e-09,-1.03515e-13,-29503.5,-21.9876], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""nC4H10O ATcT            C   4H  10O   1    0G   200.000  6000.000 1000.        1
0.13084060E+02 0.26489386E-01-0.10030766E-04 0.16703993E-08-0.10204842E-12    2
-0.39853115E+05-0.42581058E+02 0.59455772E+01 0.23216158E-02 0.10865741E-03    3
-0.14026051E-06 0.54446937E-10-0.35620542E+05 0.52265747E+01-0.33036174E+05    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C4H7OJ(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05234,0.0347294,-1.5277e-05,7.61892e-10,7.02869e-13,-8611.42,14.7975], Tmin=(300,'K'), Tmax=(1364,'K')),
            NASAPolynomial(coeffs=[15.2901,0.0133897,-4.84843e-06,7.86687e-10,-4.7023e-14,-13587.4,-53.5024], Tmin=(1364,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C4H7OJ(12)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11301,0.0323671,-1.20232e-05,-6.30292e-10,8.23641e-13,-3769.49,16.6844], Tmin=(300,'K'), Tmax=(1681,'K')),
            NASAPolynomial(coeffs=[12.6854,0.0166345,-6.42017e-06,1.08565e-09,-6.67287e-14,-7539.3,-36.8209], Tmin=(1681,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C4H7OJ(13)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {1,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96746,0.0279614,-6.47489e-06,-3.14935e-09,1.22946e-12,-3872.66,13.2567], Tmin=(300,'K'), Tmax=(1682,'K')),
            NASAPolynomial(coeffs=[11.209,0.0184045,-6.89653e-06,1.14207e-09,-6.9254e-14,-6955.6,-28.0688], Tmin=(1682,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C4H7OJ(16)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {9,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05986,0.0349346,-1.57986e-05,1.15659e-09,6.0868e-13,-2529.33,15.8709], Tmin=(300,'K'), Tmax=(1365,'K')),
            NASAPolynomial(coeffs=[15.2575,0.0133941,-4.83289e-06,7.82499e-10,-4.67126e-14,-7462.29,-52.1097], Tmin=(1365,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7355,0.0017672,3.31718e-05,-4.14499e-08,1.49827e-11,817.239,8.17764], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.63717,0.00780248,-2.60811e-06,3.98832e-10,-2.29715e-14,-636.455,-10.2098], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: CFG (Species ID: vinoxy)""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C3H6O-enol2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60783,0.0130136,3.0533e-05,-4.37468e-08,1.61506e-11,-16841,12.0012], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.08051,0.0185215,-7.11737e-06,1.14076e-09,-6.72318e-14,-18495.9,-9.57809], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
C3H5O-enol2 ATcT        C  3.H  5.O  1.   0.G   200.000  6000.000 1000.        1
8.15052559E+00 1.42542561E-02-5.05387276E-06 8.08732845E-10-4.81184188E-14    2
8.72987262E+03-1.69520239E+01 3.53458477E+00 8.02398508E-03 4.85256807E-05    3
-7.23549959E-08 3.03822687E-11 1.08059525E+04 1.11545728E+01 1.25165081E+04    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C3H5O-enol2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u1 p0 c0 {1,S} {4,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13007,0.0134496,3.49205e-05,-5.31008e-08,2.03491e-11,-2438.66,12.1074], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.1157,0.012472,-4.46478e-06,6.61849e-10,-3.64167e-14,-5170.68,-28.3022], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "CH2O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14309,0.602813], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.76069,0.0092,-4.42259e-06,1.00641e-09,-8.83856e-14,-13995.8,13.6563], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C4H8O-enol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02259,0.0225385,3.99445e-05,-6.3769e-08,2.45176e-11,-23377.3,15.71], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.2861,0.0218492,-8.05366e-06,1.24364e-09,-7.11119e-14,-26632.2,-32.2078], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C4H8O-enol2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53995,0.023068,2.70715e-05,-4.54541e-08,1.73263e-11,-21209.7,13.8844], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.41562,0.0255319,-9.90297e-06,1.60238e-09,-9.51731e-14,-23272.3,-15.1022], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C4H8O-enol3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.717,0.0183395,4.70727e-05,-6.98841e-08,2.63134e-11,-20279.2,14.2488], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.9703,0.0224915,-9.39987e-06,1.59436e-09,-9.7772e-14,-23371.7,-28.9944], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C4H9O-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77054,0.0242311,3.54432e-05,-5.86575e-08,2.25158e-11,-11014.1,15.1788], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.7502,0.0254791,-1.06158e-05,1.80002e-09,-1.10422e-13,-13853.9,-25.7497], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C4H9O-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00332,0.0234903,2.90104e-05,-4.7613e-08,1.79376e-11,-12321.8,15.1263], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.23856,0.0285144,-1.18024e-05,2.00079e-09,-1.22853e-13,-14256.2,-10.7703], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C4H9O-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {2,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01144,0.0222255,3.64658e-05,-5.74781e-08,2.16898e-11,-12316.1,14.8532], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.60366,0.0268533,-1.1375e-05,1.95358e-09,-1.20939e-13,-14771,-18.8417], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C4H9O-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {5,S} {13,S}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65743,0.0303469,2.02315e-05,-4.49332e-08,1.82206e-11,-14011.3,13.3051], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.5948,0.0244705,-1.01513e-05,1.71398e-09,-1.04819e-13,-16879.5,-31.4239], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C4H9O-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75053,0.0218565,4.49757e-05,-6.87947e-08,2.59903e-11,-9458.76,13.194], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.9425,0.025889,-1.07648e-05,1.8234e-09,-1.11774e-13,-12520.9,-29.6622], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C3H7O-N1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85194,0.0123322,3.73777e-05,-5.16977e-08,1.90454e-11,-9371.24,13.8699], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.05957,0.018474,-6.63766e-06,1.07862e-09,-6.50761e-14,-11350,-12.1441], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""C3H6O-enol2 ATcT        C  3.H  6.O  1.   0.G   200.000  6000.000 1000.        1
8.01491079E+00 1.73919953E-02-6.26027968E-06 1.01188256E-09-6.06239111E-14    2
-1.51980838E+04-1.88279964E+01 3.42806676E+00 6.25176642E-03 6.13196311E-05    3
-8.60387185E-08 3.51371393E-11-1.28446646E+04 1.04244994E+01-1.11564001E+04    4
To have the right decomposition rate for nBuOH we have to use consistent
thermo
C3H7O-N1 RMG            C   3H   7O   1     G   300.000  5000.000   995.043    1
8.80032645E+00 1.91143969E-02-8.13211711E-06 1.39545792E-09-8.62604933E-14    2
-1.03103341E+04-1.71908542E+01 3.92707025E+00 1.37424883E-02 3.75954967E-05    3
-5.44528754E-08 2.02796269E-11-8.10475568E+03 1.25051479E+01                   4
Primary Thermo Library: Burcat (Species ID: C3H7O-N1)""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C3H5OJ(8)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86275,0.0248427,-1.13352e-05,1.07716e-09,2.97933e-13,-5684.69,13.9175], Tmin=(300,'K'), Tmax=(1685,'K')),
            NASAPolynomial(coeffs=[10.3845,0.011178,-4.32037e-06,7.32674e-10,-4.51362e-14,-8520.75,-27.6583], Tmin=(1685,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C3H5OJ(12)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {8,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97527,0.0166991,2.57202e-06,-8.2559e-09,2.46621e-12,-1029.13,11.1276], Tmin=(300,'K'), Tmax=(1572,'K')),
            NASAPolynomial(coeffs=[11.7474,0.0092615,-3.5884e-06,6.07198e-10,-3.72177e-14,-4804.72,-34.4275], Tmin=(1572,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C3H5OJ(13)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {6,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88398,0.0249687,-1.16951e-05,1.34153e-09,2.3905e-13,345.317,14.9303], Tmin=(300,'K'), Tmax=(2012,'K')),
            NASAPolynomial(coeffs=[10.3854,0.0111389,-4.28565e-06,7.24994e-10,-4.46002e-14,-2474.81,-26.4676], Tmin=(2012,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C3H6O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.07996,0.0296842,-1.44301e-05,2.13726e-09,1.48023e-13,-24211.9,16.5089], Tmin=(300,'K'), Tmax=(2018,'K')),
            NASAPolynomial(coeffs=[10.6712,0.013404,-5.04778e-06,8.42755e-10,-5.14369e-14,-27399,-30.7467], Tmin=(2018,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.24186,-0.00356905,4.82667e-05,-5.85401e-08,2.25805e-11,12969,4.44704], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.32196,0.0123931,-4.39681e-06,7.0352e-10,-4.18435e-14,12175.9,0.171104], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ethyl radic  IU1/07
Burcat""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25471.6,-0.460118], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25471.6,-0.460118], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94643,-0.00163817,2.42103e-06,-1.60284e-09,3.8907e-13,29147.6,2.964], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54206,-2.75506e-05,-3.1028e-09,4.55107e-12,-4.36805e-16,29230.8,4.92031], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186
The following NASA-7 polynomials are from the GRI-Mech 3.0 mechanism, unless otherwise noted
The "Burcat" reference corresponds to:
Third Millennium Thermodynamic Database for Combustion and Air-Pollution Use
with updates from  Active Thermochemical Tables.
Elke Goos, Alexander Burcat, and Branko Ruscic
http://garfield.chem.elte.hu/Burcat/BURCAT.THR
GRI-Mech Version 3.0 Thermodynamics released 7/30/99
NASA Polynomial format for CHEMKIN-II
see README file for disclaimer
O                 L 1/90O   1               G   200.000  3500.000  1000.000    1
2.56942078E+00-8.59741137E-05 4.19484589E-08-1.00177799E-11 1.22833691E-15    2
2.92175791E+04 4.78433864E+00 3.16826710E+00-3.27931884E-03 6.64306396E-06    3
-6.12806624E-09 2.11265971E-12 2.91222592E+04 2.05193346E+00                   4
Primary Thermo Library: CFG (Species ID: O)
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21294,0.00112749,-5.75615e-07,1.31388e-09,-8.76855e-13,-1005.25,6.03474], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.69758,0.00061352,-1.25884e-07,1.77528e-11,-1.13644e-15,-1233.93,3.18917], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121386
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12531,-0.00322545,6.52765e-06,-5.79854e-09,2.06237e-12,3346.31,-0.690433], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.86473,0.0010565,-2.59083e-07,3.05219e-11,-1.33196e-15,3683.63,5.70164], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""S 9/01
OH                RUS 78O   1H   1          G   200.000  3500.000  1000.000    1
3.09288767E+00 5.48429716E-04 1.26505228E-07-8.79461556E-11 1.17412376E-14    2
3.85865700E+03 4.47669610E+00 3.99201543E+00-2.40131752E-03 4.61793841E-06    3
-3.88113333E-09 1.36411470E-12 3.61508056E+03-1.03925458E-01                   4
Primary Thermo Library: CFG (Species ID: OH)
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,294.808,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01721,0.00223982,-6.33658e-07,1.14246e-10,-1.07909e-14,111.857,3.7851], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 5/89
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38875,0.00656923,-1.48501e-07,-4.62581e-09,2.47151e-12,-17663.2,6.78536], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57317,0.00433614,-1.47469e-06,2.3489e-10,-1.43165e-14,-18007,0.501137], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C",
    molecule = 
"""
1 C u0 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85443.9,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49267,4.79889e-05,-7.24335e-08,3.74291e-11,-4.87278e-15,85451.3,4.8015], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L11/88""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48982,0.000323836,-1.68899e-06,3.16217e-09,-1.40609e-12,70797.3,2.08401], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.87846,0.000970914,1.44446e-07,-1.30688e-10,1.76079e-14,71012.4,5.48498], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""TPIS79""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76268,0.000968872,2.7949e-06,-3.85091e-09,1.68742e-12,46004,1.56253], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.8741,0.00365639,-1.40895e-06,2.6018e-10,-1.87728e-14,46263.6,6.17119], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L S/93""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1986,-0.00236661,8.23296e-06,-6.68816e-09,1.94315e-12,50496.8,-0.769119], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.29204,0.00465589,-2.01192e-06,4.17906e-10,-3.39716e-14,50926,8.6265], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L S/93""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96854,-8.71549e-05,1.02169e-05,-1.03048e-08,3.29151e-12,16392.1,0.374585], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[3.30136,0.0051803,-1.62114e-06,2.37832e-10,-1.33299e-14,16396.9,2.94688], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: Burcat (Species ID: CH3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22119,-0.00324393,1.37799e-05,-1.33144e-08,4.33769e-12,3839.56,3.39437], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.77217,0.00495696,-2.48446e-06,5.89162e-10,-5.33509e-14,4011.92,9.79834], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L12/89""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47832,-0.0013507,2.78484e-05,-3.64867e-08,1.47907e-11,-3524.77,3.30912], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09312,0.00594759,-2.06497e-06,3.23007e-10,-1.88125e-14,-4058.13,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""RADICAL     IU2/03
Burcat""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1307.72,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,390.139,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""METHOXY RAD IU1/03
CH2OH             GUNL93C   1H   3O   1     G   200.000  3500.000  1000.000    1
3.69266569E+00 8.64576797E-03-3.75101120E-06 7.87234636E-10-6.48554201E-14    2
-3.24250627E+03 5.81043215E+00 3.86388918E+00 5.59672304E-03 5.93271791E-06    3
-1.04532012E-08 4.36967278E-12-3.19391367E+03 5.47302243E+00                   4
Burcat""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88966,0.01341,-2.8477e-05,2.94791e-08,-1.09332e-11,66839.4,6.22296], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16781,0.00475222,-1.83787e-06,3.0419e-10,-1.77233e-14,67121.1,6.63589], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25172,0.017655,-2.37291e-05,1.72758e-08,-5.06648e-12,20059.4,12.4904], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.62821,0.00408534,-1.59345e-06,2.86261e-10,-1.94078e-14,19327.2,-3.93026], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""SRIC91""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "HCCOH",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24237,0.0310722,-5.08669e-05,4.31371e-08,-1.40146e-11,8031.61,13.8743], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92383,0.00679236,-2.56586e-06,4.49878e-10,-2.99401e-14,7264.63,-7.60177], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""SRI91""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186
from Dryer/Klippenstein:""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C2O",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36885,0.0082418,-8.76514e-06,5.56926e-09,-1.54001e-12,33170.8,6.71331], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.84981,0.00294758,-1.09073e-06,1.79256e-10,-1.11576e-14,32820.6,-0.645323], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286
The following are from the Marinov mechanism""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "HOC2H4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u1 p2 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58812,0.0299414,-2.35157e-05,1.12636e-08,-2.28664e-12,-21740.9,14.2167], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[9.2234,0.0141346,-4.75283e-06,7.28796e-10,-4.1897e-14,-23598.4,-15.3847], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C3H2",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,D}
2 C u1 p0 c0 {1,D} {4,S}
3 C u1 p0 c0 {1,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1992,0.0106185,1.72193e-07,-5.94901e-09,2.73624e-12,59472.8,10.7513], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.23659,0.00717558,-1.79403e-06,1.6298e-10,-4.00857e-15,58832.4,-0.248722], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
The following were added for n-butanol chemistry, as computed by RMG
Note: all ATcT data are as of 05/27/2008
ftp://ftp.technion.ac.il/pub/supported/aetdd/thermodynamics/THERM.DAT""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "pC3H3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35111,0.0327411,-4.73827e-05,3.7631e-08,-1.18541e-11,40768,15.2059], Tmin=(200,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.14222,0.00761902,-2.6746e-06,4.24915e-10,-2.51475e-14,39571,-12.5849], Tmin=(995,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""C3H2 ATcT               C  3.H  2.   0.   0.G   200.000  6000.000 1000.        1
7.47247827E+00 4.57765160E-03-1.56482125E-06 2.43991965E-10-1.42462924E-14    2
8.83321441E+04-1.27113314E+01 3.74356467E+00 2.51955211E-02-4.62608277E-05    3
4.34360520E-08-1.53992558E-11 8.89297787E+04 4.22612394E+00 9.08356403E+04    4
pC3H3 RMG               C   3H   3O   0     G   300.000  5000.000   995.043    1
6.09017276E+00 9.08825474E-03-3.34402914E-06 5.09016554E-10-2.86908485E-14    2
3.84826145E+04-8.18254441E+00 3.60098848E+00 7.42708673E-03 1.67485896E-05    3
-2.47368473E-08 9.27490802E-12 3.95555894E+04 6.71637833E+00                   4
pC3H3 ATcT              C   3H   3    0    0G   200.000  6000.000 1000.        1
7.14221880E+00 7.61902005E-03-2.67459950E-06 4.24914801E-10-2.51475415E-14    2
3.89087427E+04-1.25848435E+01 1.35110927E+00 3.27411223E-02-4.73827135E-05    3
3.76309808E-08-1.18540923E-11 4.01057783E+04 1.52058924E+01 4.16139977E+04    4
Primary Thermo Library: Franklin (Species ID: C3H3)
pC3H3                   C   3H   3          G   300.000  5000.000   995.043    1
7.52141010E+00 6.49532827E-03-1.96121786E-06 2.78061412E-10-1.51245167E-14    2
4.04743871E+04-1.51280254E+01 3.60683149E+00 1.22049797E-02 4.54657273E-06    3
-1.42089043E-08 6.16897899E-12 4.17497971E+04 6.23234158E+00                   4
pC3H3 TMTD""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "aC3H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41168,0.00234105,5.00533e-05,-6.16298e-08,2.20556e-11,19079.3,9.38985], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.9611,0.0134091,-4.82565e-06,7.27992e-10,-4.07881e-14,17118.7,-14.0191], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
aC3H4 ATcT              C   3H   4    0    0G   200.000  6000.000 1000.        1
0.63168722E+01 0.11133728E-01-0.39629378E-05 0.63564238E-09-0.37875540E-13    2
0.20117495E+05-0.10995766E+02 0.26130445E+01 0.12122575E-01 0.18539880E-04    3
-0.34525149E-07 0.15335079E-10 0.21541567E+05 0.10226139E+02 0.22962267E+05    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "pC3H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16186,0.015181,2.72266e-06,-5.17711e-09,5.43529e-14,30955.5,11.9797], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.20976,0.00787141,-7.72452e-07,-4.49736e-10,8.37727e-14,28539.7,-22.3237], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "sC3H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85096,0.00632881,3.01801e-05,-3.89089e-08,1.40203e-11,29553.7,8.06213], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.16015,0.013222,-4.59617e-06,7.28286e-10,-4.31606e-14,28293.4,-7.09085], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""sC3H5              82489C   3H   5          g  0300.00   4000.00  1000.00      1
0.09101018e+02 0.07964168e-01-0.07884945e-05-0.04562036e-08 0.08529212e-12    2
0.02670680e+06-0.02150559e+03 0.03385811e+02 0.01404534e+00 0.03204127e-04    3
-0.03824120e-07-0.09053742e-11 0.02909066e+06 0.01126649e+03                   4
sC3H5  CH3C*=CH2  T 6/96C   3H   5    0    0G   200.000  6000.000 1000.        1
0.61101805E+01 0.14673395E-01-0.53676822E-05 0.86904932E-09-0.51932006E-13    2
0.25532442E+05-0.83555712E+01 0.25544033E+01 0.10986798E-01 0.30174305E-04    3
-0.47253568E-07 0.19771073E-10 0.27150242E+05 0.13207592E+02 0.28582707E+05    4
Primary Thermo Library: Franklin (Species ID: propen1yl)""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C3H7-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08211,0.0052324,5.13554e-05,-6.99344e-08,2.81819e-11,10407.5,8.39535], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.49637,0.0177338,-6.24898e-06,9.95389e-10,-5.902e-14,8859.74,-8.5639], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
C3H6 ATcT               C  3.H  6.   0.   0.G   200.000  6000.000 1000.        1
6.03870234E+00 1.62963931E-02-5.82130800E-06 9.35936829E-10-5.58603143E-14    2
-7.41715057E+02-8.43825992E+00 3.83464468E+00 3.29078952E-03 5.05228001E-05    3
-6.66251176E-08 2.63707473E-11 7.88717123E+02 7.53408013E+00 2.40543339E+03    4
C3H7-1 RMG         mar97C   3H   7    0    0g   300.     5000.    1390.        1
9.43799350e 00 1.47160681e-02-5.03338420e-06 7.81317497e-10-4.35209260e-14    2
7.27396508e 03-2.60136738e 01 1.13366571e-01 3.54171389e-02-2.28073697e-05    3
7.88746806e-09-1.16856961e-12 1.06821595e 04 2.45520758e 01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C3H7-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.586358,0.0321021,-1.69517e-05,3.98986e-09,-2.8751e-13,9260.04,22.6633], Tmin=(300,'K'), Tmax=(1373,'K')),
            NASAPolynomial(coeffs=[9.73564,0.0143304,-4.88106e-06,7.56305e-10,-4.3838e-14,5670.01,-27.8415], Tmin=(1373,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C2H5O-1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47893,0.00759782,2.81795e-05,-4.26953e-08,1.78879e-11,-4714.46,6.38921], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.02825,0.0120038,-4.21306e-06,6.69471e-10,-3.96372e-14,-5924.93,-9.40356], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
C2H4O ATcT              C   2H   4O   1    0G   200.000  6000.000 1000.        1
0.68220305E+01 0.11059739E-01-0.39224574E-05 0.62778505E-09-0.37355714E-13    2
-0.18038769E+05-0.83716090E+01 0.30137746E+01 0.10203771E-01 0.25405637E-04    3
-0.42341002E-07 0.18267561E-10-0.16497347E+05 0.13873511E+02-0.14995857E+05    4
C2H5O-1 RMG             C   2H   5O   1     G   300.000  5000.000   995.043    1
6.67286681E+00 1.30733710E-02-5.80233812E-06 1.01962181E-09-6.39796503E-14    2
-6.75820504E+03-7.61486633E+00 4.11522893E+00 3.19445102E-03 3.94811812E-05    3
-4.96816053E-08 1.77902884E-11-5.25116047E+03 9.72667252E+00                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C2H5O-2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76834,0.00800814,2.66645e-05,-3.6694e-08,1.3552e-11,-8341.76,9.49833], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.95952,0.011775,-4.03081e-06,6.32486e-10,-3.72304e-14,-9798.39,-10.0097], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: HOCHCH3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C2H5O-3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.271296,0.029884,-1.97091e-05,6.3734e-09,-7.77965e-13,-3163.97,24.7706], Tmin=(300,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[8.31182,0.0103426,-3.39186e-06,5.12213e-10,-2.91602e-14,-6130.98,-21.3986], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C3H4O-enone",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69187,0.0249761,-1.61712e-05,5.46391e-09,-7.62497e-13,-11875.9,11.9898], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[9.40387,0.00990995,-3.34131e-06,5.13787e-10,-2.96102e-14,-14277.1,-24.2902], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "C3H4O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73321,0.00988832,2.98807e-05,-4.3124e-08,1.62334e-11,-8884.73,7.68774], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.44341,0.0117203,-4.18611e-06,6.74425e-10,-4.03915e-14,-10850.2,-20.1788], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""C2H5O-2 RMG             C   2H   5O   1     G   300.000  5000.000   995.043    1
7.50435989E+00 1.20168556E-02-5.27797411E-06 9.19053674E-10-5.73034248E-14    2
-9.77453818E+03-1.31946344E+01 3.97920014E+00 9.45869880E-03 2.37969581E-05    3
-3.54569452E-08 1.33270819E-11-8.24482143E+03 7.95623387E+00                   4
C2H5O-2 ATcT            C  2.H  5.O  1.   0.G   200.000  6000.000 1000.        1
6.35842302E+00 1.24356276E-02-4.33096839E-06 6.84530381E-10-4.03713238E-14    2
-9.37900432E+03-6.05106112E+00 4.22283250E+00 5.12174798E-03 3.48386522E-05    3
-4.91943637E-08 2.01183723E-11-8.20503939E+03 8.01675700E+00-6.49827831E+03    4
C3H4O RMG               C   3H   4O   1     G   300.000  5000.000   995.043    1
9.33734630E+00 1.14535118E-02-4.85398188E-06 8.19830986E-10-4.99696582E-14    2
-1.43262690E+04-2.45001170E+01 3.67436693E+00 8.66086526E-03 3.78829655E-05    3
-5.36261068E-08 2.01146499E-11-1.19340550E+04 9.15002255E+00                   4
C3H4O ATcT              C  3.H  4.O  1.   0.G   200.000  6000.000 1000.        1
7.31820729E+00 1.27398510E-02-4.60112009E-06 7.44735077E-10-4.46993049E-14    2
-1.16137229E+04-1.11884734E+01 3.98487241E+00 3.40751550E-03 4.81227535E-05    3
-6.61399005E-08 2.67817331E-11-9.83297241E+03 1.03960574E+01-8.18632872E+03    4
Primary Thermo Library: Franklin (Species ID: acrolein)""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "C4H7O-13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75031,0.0144303,5.20292e-05,-7.368e-08,2.74536e-11,-3299.33,13.073], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.7043,0.0206018,-8.71847e-06,1.48716e-09,-9.14924e-14,-6372.66,-28.9307], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C4H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {5,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.584768,0.0533507,-9.50806e-05,8.3796e-08,-2.80912e-11,53611.1,20.9879], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.68978,0.00669732,-2.34775e-06,3.72759e-10,-2.20555e-14,51994.3,-22.001], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
C4H2 RMG                C   4H   2O   0     G   300.000  5000.000   995.043    1
9.37421267E+00 5.20349912E-03-1.47494871E-06 1.97502945E-10-1.02254888E-14    2
4.94560974E+04-2.49964595E+01 2.93118262E+00 2.52824972E-02-2.29677151E-05    3
8.71773148E-09-6.73654919E-13 5.10265126E+04 7.50358165E+00                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "iC4H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26869,0.0185572,-3.90966e-07,-1.18419e-08,5.64169e-12,57604.9,10.425], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.7744,0.0105572,-3.5758e-06,5.05609e-10,-2.67046e-14,56207.5,-13.8057], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "nC4H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,D} {6,S}
4 C u0 p0 c0 {2,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28145,0.0137795,1.95751e-05,-3.54858e-08,1.42304e-11,62208.7,10.0748], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.80208,0.00816428,-3.0099e-06,4.48882e-10,-2.47165e-14,59891.3,-26.4749], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""rmg
C4H3 ATcT               C  4.H  3.   0.   0.G   200.000  6000.000 1000.        1
8.44631306E+00 9.07291526E-03-3.18681201E-06 5.06725048E-10-3.00149855E-14    2
6.20007365E+04-1.77938854E+01 5.54263934E-01 3.86185425E-02-4.70818280E-05    3
3.06240321E-08-7.90588421E-12 6.37974910E+04 2.10542043E+01 6.53200393E+04    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "C4H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.37369,0.0288801,-1.46864e-05,-3.91045e-09,4.78134e-12,33063.3,17.5941], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.98456,0.0120559,-4.23587e-06,6.73646e-10,-3.9906e-14,31199.3,-16.7959], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
C4H4 RMG                C   4H   4O   0     G   300.000  5000.000   995.043    1
9.53726854E+00 1.11114691E-02-4.09447607E-06 6.20848240E-10-3.48104088E-14    2
3.01377145E+04-2.67780310E+01 3.27449293E+00 1.07223742E-02 3.50306178E-05    3
-5.14128529E-08 1.95256705E-11 3.26496687E+04 9.76468497E+00                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "C4H5-113",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.1591,0.0304425,-1.62521e-05,-1.73751e-10,2.43871e-12,36215.6,14.6845], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.21469,0.013495,-4.82558e-06,7.76744e-10,-4.64081e-14,34084.3,-22.5151], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
C4H5-113 RMG            C   4H   5O   0     G   300.000  5000.000   995.043    1
6.49266056E+00 1.68368773E-02-5.45924754E-06 7.50059603E-10-3.86696159E-14    2
3.43960771E+04-7.96071084E+00 3.03787313E+00 1.96385363E-02 7.02967924E-06    3
-1.88144450E-08 7.69003801E-12 3.56324440E+04 1.14473175E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "nC4H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28606,0.0143352,2.78457e-05,-4.84613e-08,2.10628e-11,41922.3,12.6654], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.11184,0.0142276,-5.0242e-06,8.00817e-10,-4.7546e-14,40013.5,-15.2705], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
nC4H5 RMG               C   4H   5O   0     G   300.000  5000.000   995.043    1
1.04306375E+01 1.18071498E-02-3.95818547E-06 5.51468424E-10-2.86323786E-14    2
3.83019523E+04-3.01376345E+01 2.97255253E+00 1.42343438E-02 3.39194437E-05    3
-5.26550800E-08 2.03311812E-11 4.11502383E+04 1.26605457E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "iC4H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.00881,0.0250341,4.4793e-06,-2.6399e-08,1.34433e-11,36207,15.9914], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.58761,0.0142684,-5.04812e-06,8.06555e-10,-4.79336e-14,34083.7,-19.6197], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
iC4H5    RMG            C   4H   5O   0     G   300.000  5000.000   995.043    1
8.94642571E+00 1.46679861E-02-5.42142561E-06 8.34035913E-10-4.74778835E-14    2
3.35990859E+04-2.27620527E+01 3.30543668E+00 1.32896428E-02 3.29182143E-05    3
-4.91480461E-08 1.86142996E-11 3.59125316E+04 1.04082920E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "C4H6-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {3,T} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42819,0.0249822,6.27371e-06,-2.61748e-08,1.26585e-11,18024.9,13.6684], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.81179,0.0179734,-6.61044e-06,1.05501e-09,-6.19297e-14,16177,-15.9658], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
C4H6-1                  C   4H   6O   0     G   300.000  5000.000   995.043    1
7.11381994E+00 1.86476725E-02-6.42531114E-06 9.39275620E-10-5.13490337E-14    2
1.64515474E+04-1.21508345E+01 3.15157920E+00 1.74587936E-02 2.11700034E-05    3
-3.48370264E-08 1.32807602E-11 1.80874430E+04 1.12029832E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C4H6-12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13591,0.0124386,3.75792e-05,-5.30731e-08,1.97975e-11,18102.6,13.1137], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.36767,0.0162199,-5.52548e-06,8.66951e-10,-5.10674e-14,15833.1,-18.2729], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
C4H5 ATcT               C  4.H  5.   0.   0.G   200.000  6000.000 1000.        1
9.21572256E+00 1.34939872E-02-4.82517726E-06 7.76676426E-10-4.64039105E-14    2
3.43129071E+04-2.25232815E+01 2.15189267E+00 3.05033422E-02-1.64053256E-05    3
-1.54978415E-11 2.38039347E-12 3.64447930E+04 1.47100046E+01 3.82983108E+04    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C4H7-14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62922,0.0163308,3.09993e-05,-4.72284e-08,1.79056e-11,23440.9,11.7925], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.97,0.0179258,-6.17425e-06,9.72337e-10,-5.73788e-14,21236.2,-19.6847], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: C4H5-113)
C4H5-113                C   4H   5          G   300.000  5000.000   995.043    1
9.02577751E+00 1.39818587E-02-5.07003487E-06 8.25067458E-10-4.98015293E-14    2
3.53944834E+04-1.83669800E+01 3.74950555E+00 2.68190415E-02-1.17995959E-05    3
-3.12289209E-09 3.06680917E-12 3.68590187E+04 9.14464700E+00                   4
Primary Thermo Library: MRH (Species ID: C4H7-14)""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C4H7-11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u1 p0 c0 {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1986,0.011962,4.2386e-05,-6.303e-08,2.5948e-11,27525.7,8.5718], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.1565,0.019031,-6.7326e-06,1.0733e-09,-6.3689e-14,25582.6,-16.1429], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT
C4H7-11                 C   4H   7O   0     G   300.000  5000.000   995.043    1
8.42885739E+00 1.98226731E-02-7.37321686E-06 1.15073056E-09-6.64153001E-14    2
2.55215037E+04-1.78308710E+01 3.33891290E+00 1.48283185E-02 3.85292086E-05    3
-5.53131714E-08 2.05793635E-11 2.77946367E+04 1.30322178E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "C4H7-12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,D} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45288,0.0152014,3.3924e-05,-4.89797e-08,1.8131e-11,26666.3,12.6265], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.5159,0.0208851,-7.83357e-06,1.23396e-09,-7.179e-14,24767.8,-12.4319], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C4H7-24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3818,0.0128955,4.46338e-05,-6.11404e-08,2.24467e-11,14690.4,10.9264], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.16993,0.0206436,-7.74201e-06,1.21642e-09,-7.05766e-14,12401.1,-18.8653], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""rmg
C4H7O-14 rmg            C   4H   7O   1     G   300.000  5000.000   995.043    1
1.15249493E+01 1.92022713E-02-8.14314256E-06 1.38924670E-09-8.54790549E-14    2
-1.43719357E+03-3.03571108E+01 3.67882763E+00 2.52555959E-02 2.11533756E-05    3
-4.39811706E-08 1.77812203E-11 1.38602422E+03 1.37971918E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C4H9-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3701,0.0175812,4.28037e-05,-6.0581e-08,2.22918e-11,7355.03,13.7489], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.01072,0.0256389,-9.61172e-06,1.51622e-09,-8.83435e-14,5109.08,-15.2615], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG
C4H8-1 ATcT             C   4H   8    0    0G   300.000  5000.    1000.        1
0.20535841E+01 0.34350507E-01-0.15883197E-04 0.33089662E-08-0.25361045E-12    2
-0.21397231E+04 0.15556360E+02 0.11811380E+01 0.30853380E-01 0.50865247E-05    3
-0.24654888E-07 0.11110193E-10-0.17904004E+04 0.21075639E+02-0.06494670E+03    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C4H9-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60287,0.0168404,3.63709e-05,-4.95365e-08,1.77136e-11,6047.35,13.6963], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.49904,0.0286743,-1.07983e-05,1.71699e-09,-1.00774e-13,4706.8,-0.282131], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C2H3O-1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 O u0 p2 c0 {1,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37355,0.00766274,2.00424e-05,-3.07407e-08,1.18462e-11,13376.7,10.2086], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.68501,0.00634914,-2.12423e-06,2.88819e-10,-1.4546e-14,11725.7,-14.5549], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""rmg""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "C2H3O-2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u1 p0 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37355,0.00766274,2.00424e-05,-3.07407e-08,1.18462e-11,13376.7,10.2086], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.68501,0.00634914,-2.12423e-06,2.88819e-10,-1.4546e-14,11725.7,-14.5549], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""rmg""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "C6H4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,T}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {1,T} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81396,0.00927143,6.46142e-05,-8.77361e-08,3.27578e-11,53690.3,13.1094], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.1408,0.013465,-4.54926e-06,7.05803e-10,-4.11247e-14,49770.4,-42.211], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""CBSQB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C6H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {6,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u1 p0 c0 {4,S} {5,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.491024,0.017267,7.02556e-05,-1.1339e-07,4.89203e-11,39234.1,24.2505], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.9541,0.0182073,-6.63331e-06,1.08126e-09,-6.51737e-14,35109.8,-36.4321], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""phenyl radi  T07/10
Burcat 30-SEPT-2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C4H6-2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {2,S} {3,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87966,0.0178422,1.70203e-05,-2.86863e-08,1.09431e-11,15711.3,11.8552], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.11834,0.0189034,-5.8054e-06,8.2772e-10,-4.51608e-14,14369.7,-7.25608], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C4H7-22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u1 p0 c0 {2,S} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41175,0.0204835,1.50376e-05,-2.89761e-08,1.1334e-11,25004.3,11.3603], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.25107,0.0201442,-7.20543e-06,1.17172e-09,-7.08224e-14,23493,-10.898], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12528,0.00977822,4.52145e-06,-9.00946e-09,3.19372e-12,-4108.51,11.2288], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.61228,0.00844989,-2.85415e-06,4.23838e-10,-2.2684e-14,-5187.86,-3.27495], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C6H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {4,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82778,0.00658222,0.000118283,-1.47954e-07,5.34532e-11,-2431.86,15.9093], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.9788,0.0287324,-1.00126e-05,1.58808e-09,-9.40765e-14,-7568.69,-48.6741], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""KVG, UGhent""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C6H9_1_2_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  C u0 p0 c0 {4,D} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.18695,0.0681745,-5.32243e-05,2.18127e-08,-3.63902e-12,25026.1,38.6524], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[16.9217,0.0202745,-6.64939e-06,1.00413e-09,-5.72454e-14,18747.2,-62.7656], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C6H9_CYC_1_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {3,S} {5,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.55973,0.0583176,-2.95503e-05,5.47122e-09,5.32998e-14,21527.8,44.6225], Tmin=(300,'K'), Tmax=(1375,'K')),
            NASAPolynomial(coeffs=[13.9824,0.0247191,-8.41817e-06,1.30256e-09,-7.54309e-14,14708.4,-52.192], Tmin=(1375,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C6H8_CYC_1_4",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {2,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.3458,0.0695507,-5.12381e-05,1.92721e-08,-2.92116e-12,12154.6,50.8884], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[15.2457,0.0205599,-6.84211e-06,1.04457e-09,-6.00125e-14,5157.99,-59.2777], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C6H7_CYC_1_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u1 p0 c0 {4,S} {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.989769,0.020823,7.09545e-05,-1.1472e-07,4.92347e-11,23712.1,22.0322], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.4417,0.0228023,-8.21084e-06,1.32793e-09,-7.96047e-14,19509.7,-38.918], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Ene T 8/10
Burcat 30-SEPT-2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C6H10_CYC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {3,S} {5,D} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.481125,0.05987,-3.59e-05,8.942e-09,-2.851e-13,8173,32.22], Tmin=(300,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[-0.481125,0.05987,-3.59e-05,8.942e-09,-2.851e-13,8173,32.22], Tmin=(1500,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C7H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u1 p0 c0 {1,S} {2,S} {5,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {3,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u0 p0 c0 {5,D} {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.49639,0.0799172,-5.94936e-05,2.30449e-08,-3.63905e-12,20304.8,50.5508], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.2345,0.0248844,-8.27016e-06,1.25495e-09,-7.17094e-14,12651.1,-70.7658], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C8H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,D} {6,S} {13,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {3,S} {5,D} {12,S}
7  C u0 p0 c0 {1,S} {8,D} {14,S}
8  C u0 p0 c0 {7,D} {15,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.18176,0.0334878,6.92369e-05,-1.24491e-07,5.49387e-11,15604,22.6626], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.9193,0.0294554,-1.02698e-05,1.31096e-09,-6.16742e-14,10934.5,-49.7233], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Styrene      P 4/89""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C8H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {11,S}
4  C u0 p0 c0 {2,D} {7,S} {15,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {4,S} {6,D} {14,S}
8  C u1 p0 c0 {1,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.733299,0.0459053,3.78257e-05,-9.12367e-08,4.2559e-11,26157.3,25.0411], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1327,0.0282904,-1.01802e-05,1.64177e-09,-9.81375e-14,20879.1,-60.0115], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""C6H5CH2CH2*  A11/04""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "C7H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {11,S}
4  C u0 p0 c0 {2,D} {7,S} {15,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {4,S} {6,D} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.612,0.021118,8.5324e-05,-1.32569e-07,5.59411e-11,4096.55,20.297], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.9394,0.0266922,-9.68422e-06,1.57392e-09,-9.46672e-14,-676.971,-46.725], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Toluene     g 1/93""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "C3H7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5146,0.0272103,1.27748e-05,-3.40401e-08,1.42738e-11,-6753.06,13.8564], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.9424,0.0189567,-7.35344e-06,1.26726e-09,-7.95918e-14,-9300.88,-27.3164], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "CH2CH2CH2OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50572,0.0298664,1.16655e-05,-3.63547e-08,1.56644e-11,-363.207,14.7902], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.7661,0.0174577,-7.03982e-06,1.24261e-09,-7.91833e-14,-3434.68,-36.0131], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "aC3H5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21714,0.0271581,-4.01795e-06,-1.23874e-08,6.34366e-12,9208.13,15.0973], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.92185,0.0162632,-5.74054e-06,9.24532e-10,-5.55133e-14,7476.91,-15.3908], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "nSPC(301)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13616,0.0474715,-1.89969e-06,-3.19493e-08,1.55437e-11,-30111.1,19.6962], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.1719,0.0235747,-8.848e-06,1.49674e-09,-9.29611e-14,-34116.5,-50.2202], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "nSPC(351)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {6,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03484,0.0562438,-1.83942e-05,-2.0286e-08,1.25361e-11,-26728.5,18.6463], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.7966,0.0211602,-8.13426e-06,1.39997e-09,-8.79317e-14,-31265.2,-64.351], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "nSPC(385)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12526,0.0516363,-1.66625e-05,-1.75883e-08,1.08676e-11,-39986.4,17.0371], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.6196,0.0217458,-8.31898e-06,1.42065e-09,-8.87178e-14,-43877.7,-54.057], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "nSPC(447)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32349,0.0367974,1.87333e-06,-2.89026e-08,1.35164e-11,-21533.5,15.1946], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.5728,0.019292,-7.45895e-06,1.28258e-09,-8.04358e-14,-24746.2,-40.0959], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "nSPC(543)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.98164,0.00841512,4.84231e-05,-6.8411e-08,2.60253e-11,-12140.6,19.1511], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.972,0.00695582,-1.65824e-06,1.70655e-10,-6.11046e-15,-15646.7,-32.8049], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: Lee&Bozzelli_JPCA_107_19_3778 (Species ID: nSPC(543))""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "nSPC(801)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08442,0.0249456,-8.13898e-07,-1.96058e-08,9.71313e-12,-19952,14.7435], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.9359,0.0078587,-2.93713e-06,4.96883e-10,-3.08572e-14,-22629.1,-32.5166], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "nSPC(879)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {10,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u1 p2 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19206,0.0323705,1.37067e-05,-4.68626e-08,2.10821e-11,-35091.7,24.7943], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.9003,0.00578664,-1.3354e-06,1.4282e-10,-5.62969e-15,-40027.8,-60.0061], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "nSPC(1064)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 O u1 p2 c0 {2,S}
8 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81907,0.0162404,3.07373e-05,-5.47253e-08,2.21743e-11,-17929.9,19.4789], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.9157,0.0046455,-1.54987e-06,2.49509e-10,-1.50364e-14,-21772.5,-42.2134], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "nSPC(102)",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37295,0.0137364,-1.11404e-05,5.33432e-09,-1.04487e-12,24191.8,9.39468], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.24522,0.00708443,-2.43091e-06,3.82229e-10,-2.25634e-14,23775.9,0.153855], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "C4H8-2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53637,0.014019,4.20055e-05,-5.66753e-08,2.05059e-11,-3566.63,10.6978], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.81445,0.0244229,-9.22688e-06,1.46696e-09,-8.60241e-14,-5386.42,-10.9669], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "C3H3O-enone",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71355,0.00915555,2.31136e-05,-3.4439e-08,1.30836e-11,10682.5,9.53677], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.83073,0.00966335,-3.3673e-06,5.31896e-10,-3.14004e-14,9018.66,-14.5493], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: Franklin (Species ID: CH2CHCO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "FULVENE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,D}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {9,S}
6  C u0 p0 c0 {1,D} {11,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.509715,0.0258196,5.06505e-05,-9.32594e-08,4.15964e-11,24431.9,23.0638], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.4345,0.0199371,-7.13567e-06,1.14952e-09,-6.87264e-14,20441.1,-38.68], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T12/10
The following NASA-7 polynomials are from study by:
Sharma, S. "Modeling of 1,3-hexadiene, 2,4-hexadiene, and 1,4-hexadiene doped
methane flames: Flame modeling, Benzene, and Styrene Formation"
Burcat 13-JAN-2011""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "C6H5O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24732,0.0199044,5.75006e-05,-8.73852e-08,3.3564e-11,3029.45,11.4048], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.8502,0.0180685,-7.27702e-06,1.26941e-09,-8.00651e-14,-1497.81,-55.6609], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "C5H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u1 p0 c0 {1,S} {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1663,0.00301934,7.75425e-05,-9.92005e-08,3.64098e-11,29419,11.0463], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.0766,0.0120549,-3.69509e-06,5.30002e-10,-2.9015e-14,25425.2,-43.0544], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""C5H5                    C   5H   5O   0     G   300.000  5000.000   995.043    1
1.19820938E+01 1.21872945E-02-3.76158670E-06 5.45206715E-10-3.01508977E-14    2
2.65295823E+04-4.29105872E+01 2.66966211E+00 6.42151685E-03 7.00546223E-05    3
-9.25433638E-08 3.43204252E-11 3.05215272E+04 1.27169645E+01                   4
C5H5 from Lindstedt Combustion&Flame 2011""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "C6H5OH",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {3,D} {5,S} {11,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.39146,0.0393196,1.7771e-06,-2.27767e-08,8.30966e-12,-14721.8,19.1781], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.2163,0.0114243,-1.09668e-06,-6.42744e-10,1.19889e-13,-20536.6,-73.0423], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""82489""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "cyC5H6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88558,-0.00954959,0.000121026,-1.42699e-07,5.06837e-11,14854.7,9.56173], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.3963,0.0178132,-6.98599e-06,1.19766e-09,-7.46598e-14,10510.7,-40.9532], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""cyC5H6                  C   5H   6O   0     G   300.000  5000.000   995.043    1
1.16960721E+01 1.59448522E-02-5.20901194E-06 7.87058917E-10-4.49443430E-14    2
1.05765973E+04-4.12952705E+01 2.73255616E+00 1.33819634E-03 9.31475596E-05    3
-1.16255819E-07 4.22115401E-11 1.48673400E+04 1.45010456E+01                   4
cyC5H6 from Lindstedt Combustion&Flame 2011""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "C5H5CH3_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52789,0.0137352,8.64248e-05,-1.1686e-07,4.34908e-11,11719.9,15.8958], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.4605,0.0206645,-6.77766e-06,1.03031e-09,-5.9187e-14,6627.52,-55.2693], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""From Burcat
cyC5H6                  C   5H   6O   0     G   200.000  6000.000   995.043    1
9.88465785E+00 1.89943852E-02-6.87485480E-06 1.11556894E-09-6.70255571E-14    2
7.13511201E+03-3.17238367E+01 9.77484017E-01 1.39109570E-02 7.36279225E-05    3
-1.14340239E-07 4.88766069E-11 1.08249663E+04 2.08861411E+01 1.21823174E+04    4""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "C5H5CH3_2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {14,S}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79945,0.011541,8.68321e-05,-1.14217e-07,4.20056e-11,10269.1,15.8701], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.8115,0.0228104,-7.81704e-06,1.22818e-09,-7.23125e-14,5726.19,-45.1979], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "C5H5CH3_3",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76131,0.0114295,8.78824e-05,-1.15636e-07,4.2554e-11,10127.7,16.035], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.0105,0.0225225,-7.67174e-06,1.20005e-09,-7.04289e-14,5499.16,-46.3691], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "C8H6",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {3,D} {5,S} {12,S}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {14,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.74708,0.0778284,-6.6971e-05,2.37972e-08,-8.4328e-13,36113.1,35.4221], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.3583,0.0211974,-7.65817e-06,1.24135e-09,-7.45328e-14,31037.5,-62.252], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""C6H5CCH     T12/06
C8H6                    C   8H   6    0    0G   300.000  5000.000 1389.00      1
1.91822134e+01 1.76449850e-02-6.18210588e-06 9.75697439e-10-5.72698125e-14    2
2.89847171e+04-8.01903000e+01-3.13527908e+00 7.15153321e-02-5.60924468e-05    3
2.20854359e-08-3.49225990e-12 3.65086712e+04 3.89669546e+01                   4
Active Thermochemical Tables (17-DEC-2010)""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "C6H5CH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {3,D} {5,S} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.481115,0.0385128,3.28615e-05,-7.69727e-08,3.54231e-11,23307,23.5488], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.044,0.0234939,-8.53754e-06,1.38908e-09,-8.36144e-14,18564.2,-51.6656], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""rad   T08/90
Burcat 30-SEPT-2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "C6H5CCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {3,D} {5,S} {12,S}
7  C u0 p0 c0 {8,D} {14,S} {15,S}
8  C u1 p0 c0 {1,S} {7,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.595576,0.0431716,3.39695e-05,-8.55153e-08,4.02635e-11,41975.6,25.7012], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1678,0.023487,-8.45465e-06,1.36664e-09,-8.19389e-14,36735.7,-59.8456], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T12/07
Burcat 30-SEPT-2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "C5H4CH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.564034,0.0384202,1.94959e-05,-5.95545e-08,2.8687e-11,25330.4,22.7464], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.8997,0.0212183,-7.67565e-06,1.24496e-09,-7.47732e-14,21205.4,-44.7535], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""A03/05
Burcat 13-JAN-2011""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "C5H5CH2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  C u1 p0 c0 {1,S} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.42356,0.0705976,-6.11471e-05,2.68157e-08,-4.69274e-12,37506.7,42.9354], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[17.5855,0.0158083,-5.49672e-06,8.63067e-10,-5.04754e-14,30817.5,-67.8115], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""C5H4CH3                 C   6H   7O   0     G   300.000  5000.000   995.043    1
1.36818475E+01 1.90575918E-02-6.35439667E-06 9.78951164E-10-5.68197013E-14    2
2.03302521E+04-4.83556513E+01 2.65912829E+00 1.56456975E-02 7.07292077E-05    3
-9.88652457E-08 3.71383922E-11 2.48863905E+04 1.66392834E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "C5H5CH2-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {10,S}
6  C u1 p0 c0 {2,S} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.39417,0.0751044,-6.7769e-05,3.16887e-08,-5.9196e-12,25613.3,48.5136], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[15.2938,0.0184305,-6.35987e-06,9.93249e-10,-5.78638e-14,19196.3,-59.7459], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "C5H5CH2-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {2,D} {10,S}
4  C u0 p0 c0 {1,S} {5,D} {9,S}
5  C u0 p0 c0 {2,S} {4,D} {11,S}
6  C u1 p0 c0 {2,S} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.34258,0.0755933,-6.88889e-05,3.24826e-08,-6.10433e-12,28558.9,48.117], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[15.3787,0.0183356,-6.32189e-06,9.86758e-10,-5.74627e-14,22177.9,-60.147], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "ME2CYBE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,D}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {1,S} {3,D} {8,S}
5  C u0 p0 c0 {1,D} {9,S} {10,S}
6  C u0 p0 c0 {2,D} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75611,-0.00508654,0.000122516,-1.46071e-07,5.20578e-11,29534.1,14.9694], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.047,0.0212672,-7.18107e-06,1.10332e-09,-6.36893e-14,24929.5,-39.8346], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "c5h4chchch2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {5,D} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {1,D} {7,S} {13,S}
5  C u0 p0 c0 {2,D} {6,S} {10,S}
6  C u0 p0 c0 {3,D} {5,S} {11,S}
7  C u0 p0 c0 {4,S} {8,D} {14,S}
8  C u0 p0 c0 {7,D} {15,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.1156,0.0938484,-8.53807e-05,4.02613e-08,-7.59499e-12,31703.6,59.3518], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[19.1124,0.0223573,-7.79982e-06,1.2271e-09,-7.18532e-14,23481.1,-78.1136], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "CTCCCCTC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,T}
4  C u0 p0 c0 {2,S} {6,T}
5  C u0 p0 c0 {3,T} {11,S}
6  C u0 p0 c0 {4,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.36805,0.0407008,-1.59371e-05,-7.65989e-09,5.95826e-12,47708.5,16.7535], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.7384,0.0183573,-5.35667e-06,7.29192e-10,-3.82059e-14,45085.1,-32.2188], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "C*C*CC*C*C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,D} {7,S}
2  C u0 p0 c0 {1,S} {6,D} {8,S}
3  C u0 p0 c0 {5,D} {9,S} {10,S}
4  C u0 p0 c0 {6,D} {11,S} {12,S}
5  C u0 p0 c0 {1,D} {3,D}
6  C u0 p0 c0 {2,D} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5575,0.035692,8.95669e-06,-3.87075e-08,1.74491e-11,45194.6,14.9539], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.1317,0.0150145,-4.90068e-06,7.45117e-10,-4.28887e-14,41213.4,-53.0775], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "CH3CCCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {4,D} {8,S} {9,S}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54856,0.012842,2.4325e-05,-3.58909e-08,1.34239e-11,34452.8,10.1108], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.04689,0.0155623,-5.07616e-06,7.58447e-10,-4.29252e-14,32925.7,-10.9242], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""CH3CCCH2                C   4H   50   00   0G   300.000  5000.000 1678.000     1
-5.72844989E+00 4.53800905E-02-1.62861273E-05 2.61784277E-09-1.55735959E-13    2
3.64135561E+04 5.47011215E+01 5.79092559E+00-1.26233816E-02 6.80832493E-05    3
-4.51738347E-08 9.18508455E-12 3.57411849E+04 4.47042121E+00                   4
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "C4H4-123",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {5,S} {6,S}
2 C u0 p0 c0 {4,D} {7,S} {8,S}
3 C u0 p0 c0 {1,D} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05797,0.0172821,1.16475e-05,-2.61981e-08,1.08357e-11,37615.7,9.32272], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.65692,0.011109,-3.67008e-06,5.61934e-10,-3.25097e-14,35692.9,-21.7245], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""82489""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "C5H10_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.03155,0.0571908,-3.69342e-05,1.2298e-08,-1.667e-12,-4447.96,32.1337], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[14.8559,0.0217591,-7.19194e-06,1.09245e-09,-6.25176e-14,-10135.7,-53.7935], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "C5H9_1_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.258381,0.0526374,-3.44776e-05,1.1693e-08,-1.62205e-12,20143.5,30.6933], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[14.4005,0.0197093,-6.52672e-06,9.92647e-10,-5.68527e-14,14917.9,-48.5076], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "C5H8_CYC_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {2,S} {4,D} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.40494,0.0630369,-4.53166e-05,1.65992e-08,-2.44212e-12,3556.87,49.4543], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.1886,0.0193242,-6.37806e-06,9.6972e-10,-5.55803e-14,-2807.96,-50.1996], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "C5H9_CYC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  C u1 p0 c0 {3,S} {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.77657,0.0520634,-2.53274e-05,4.68184e-09,6.16802e-15,13118,46.9884], Tmin=(300,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[10.4169,0.0249465,-8.24607e-06,1.24922e-09,-7.1312e-14,7577.97,-31.3942], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "C5H7_CYC_1_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,D} {10,S}
4  C u1 p0 c0 {1,S} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.04929,0.0637056,-5.15076e-05,2.14163e-08,-3.57197e-12,19450.7,46.9702], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[13.4371,0.0166929,-5.43077e-06,8.17275e-10,-4.65279e-14,13488.5,-50.8315], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "C4H7O_1_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85054,0.0214634,3.85378e-05,-6.27824e-08,2.44841e-11,-6429.99,15.1459], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.2648,0.0172544,-5.82185e-06,9.09556e-10,-5.3431e-14,-9968.65,-38.5927], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "sBuOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44609,0.0333125,1.77706e-05,-4.26431e-08,1.75966e-11,-38071.2,11.773], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.0856,0.0246802,-8.55828e-06,1.35548e-09,-8.03463e-14,-41082.5,-36.3568], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG computed NASA-7 polynomials, for s-butanol chemistry
Primary Thermo Library: sBuOH (Species ID: sBuOH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "CH3C(OH)C2H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {5,S}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54088,0.0243263,3.97619e-05,-6.29219e-08,2.40491e-11,-16757.3,12.2457], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.1132,0.0252738,-8.98252e-06,1.43738e-09,-8.56525e-14,-19818.1,-32.0566], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: sBuOH-radicals (Species ID: CH3C(OH)C2H5)""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "CH3CH(OH)CHCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47588,0.0280589,3.08366e-05,-5.50825e-08,2.1638e-11,-13875.3,12.9525], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.7211,0.0245992,-8.69775e-06,1.38693e-09,-8.24492e-14,-16985.8,-34.1693], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: sBuOH-radicals (Species ID: CH3CH(OH)CHCH3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "CH3CH(O)C2H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50034,0.0187537,5.72892e-05,-8.07773e-08,3.00789e-11,-10822.8,12.4934], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.2336,0.0251548,-8.87272e-06,1.41314e-09,-8.39235e-14,-14217.7,-34.1024], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: sBuOH-radicals (Species ID: CH3CH(O)C2H5)""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "CH2CH(OH)C2H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35702,0.0274981,3.44131e-05,-5.96954e-08,2.33932e-11,-12857,12.2209], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.2911,0.0236846,-8.22922e-06,1.29585e-09,-7.63418e-14,-16224.1,-38.8217], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: sBuOH-radicals (Species ID: CH2CH(OH)C2H5)""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "CH3CH(OH)CH2CH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4421,0.0297544,2.76239e-05,-5.26874e-08,2.0987e-11,-13182,11.8867], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.1483,0.0242621,-8.5762e-06,1.36699e-09,-8.12358e-14,-16375.3,-37.4123], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: sBuOH-radicals (Species ID: CH3CH(OH)CH2CH2)""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "CH3CH(OH)CH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45944,0.0267858,3.07852e-06,-2.15094e-08,9.76694e-12,-9653.91,10.8085], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.3367,0.0157197,-5.2336e-06,8.05258e-10,-4.67635e-14,-11843.3,-26.4606], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: HOCH(CH3)CH2)""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "HOCHC2H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {10,S}
4  O u0 p2 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54748,0.0162026,3.24288e-05,-4.96766e-08,1.89414e-11,-11063.3,12.9218], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.59295,0.016688,-5.6697e-06,8.84285e-10,-5.18176e-14,-13493.5,-22.3803], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
New work for sec- and tert-butanol paper:                                   !
"Accurate Reaction Networks for Alternative Fuels: Butanol Isomers"      !
K.M. Van Geem, M.R. Harper, S.P. Pyl, G.B. Marin, W.H. Green             !
To be submitted to Industrial & Engineering Chemical Research            !
for the ISCRE-21 conference                                           !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Primary Thermo Library: MRH (Species ID: HOCHCH2CH3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "H2CCCH3(OH)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31481,0.0183931,1.69403e-05,-3.1888e-08,1.26275e-11,-21428.4,11.6759], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.29438,0.0158754,-5.64468e-06,9.18221e-10,-5.55546e-14,-23285.7,-16.6762], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""CH3CH(OH)CH2            C   3H   7O   1     G   300.000  5000.000   995.043    1
9.77349379E+00 1.64188798E-02-5.42302225E-06 8.35595432E-10-4.86468599E-14    2
-1.27504154E+04-2.31244729E+01 2.98550534E+00 1.99464635E-02 2.50762522E-05    3
-4.35955166E-08 1.71435984E-11-1.02233146E+04 1.55003786E+01                   4
HOCHC2H5                C   3H   7O   1     G   300.000  5000.000   995.043    1
1.06227801E+01 1.58439620E-02-6.29817026E-06 1.10707477E-09-7.04376940E-14    2
-1.35923367E+04-2.78896852E+01 3.58171453E+00 2.27311779E-02 1.56056258E-05    3
-3.51994938E-08 1.44861872E-11-1.11308272E+04 1.13721922E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "CH3CH-O-CH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3354,0.0214318,2.44649e-05,-4.63715e-08,1.86753e-11,-6252.05,11.7662], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.8175,0.0143161,-5.48285e-06,9.44521e-10,-5.93744e-14,-9275.81,-35.825], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "CH3C(OH)CH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  O u0 p2 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05849,0.0259725,5.40167e-06,-2.30702e-08,1.01201e-11,-13697.6,12.675], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.37394,0.0169532,-5.67678e-06,8.84041e-10,-5.18942e-14,-15764.7,-21.8339], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "acetone",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61211,0.0117333,3.44375e-05,-4.79046e-08,1.7637e-11,-27762.4,10.0482], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.35983,0.0178808,-6.80771e-06,1.15403e-09,-7.16532e-14,-29558.4,-13.2907], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "C2H5CHCHCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8798,0.023413,4.70088e-05,-7.27965e-08,2.78949e-11,11966.7,15.5891], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.1966,0.0228773,-7.83515e-06,1.23415e-09,-7.28951e-14,8284.97,-38.4962], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "CH2C(OH)CH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,S} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.10982,0.0172615,1.97166e-05,-3.64805e-08,1.46008e-11,-3167.13,12.2117], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.56878,0.0122119,-4.2002e-06,6.67392e-10,-3.97143e-14,-5487.93,-24.1198], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "CH2C(O)CH3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65911,0.010936,3.37162e-05,-4.82026e-08,1.80914e-11,-5256.4,11.4847], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.78204,0.0133569,-4.62748e-06,7.31834e-10,-4.32985e-14,-7415.26,-18.9301], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: CFG (Species ID: propen2oxy)""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "CH3-O-C(CH3)2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13909,0.0363541,-1.77814e-06,-1.96846e-08,9.3601e-12,-11056.3,14.1299], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.1721,0.0244515,-8.51236e-06,1.36048e-09,-8.13061e-14,-13266.3,-23.8377], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "C3H6O-enol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32296,0.0145061,3.23163e-05,-4.85689e-08,1.83617e-11,-20704.5,11.6789], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.70653,0.0164178,-6.07148e-06,9.39049e-10,-5.37536e-14,-22941.9,-20.1262], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""rmg
Primary Thermo Library: Franklin (Species ID: CH2CHCCH2)
iC4H5                   C   4H   5          G   300.000  5000.000   995.043    1
9.10109944E+00 1.34516723E-02-4.57980040E-06 7.12492366E-10-4.16245209E-14    2
3.93833754E+04-7.53014693E+00 3.57286186E+00 1.30717177E-02 3.00664857E-05    3
-4.53289459E-08 1.72617226E-11 4.16025184E+04 2.47356863E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "MEK",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40613,0.0261008,2.14086e-05,-4.19808e-08,1.66958e-11,-30912.9,12.9908], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.0247,0.0226795,-8.3843e-06,1.39638e-09,-8.57606e-14,-33377.8,-24.6743], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "sC4H8O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92775,0.0231555,4.0634e-05,-6.67231e-08,2.60624e-11,-21893,16.2989], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.0087,0.0184994,-6.41762e-06,1.02768e-09,-6.14948e-14,-25674.8,-41.2083], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "C4H6O(717)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28295,0.0183744,3.43525e-05,-5.46291e-08,2.10591e-11,-17298.9,13.3868], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.5344,0.017324,-6.42391e-06,1.07118e-09,-6.57979e-14,-20133.1,-28.5513], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "cH2C(O)C2H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91742,0.023678,1.80897e-05,-3.64814e-08,1.45595e-11,-6280.37,12.622], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.76241,0.0204773,-7.68087e-06,1.28311e-09,-7.88458e-14,-8448.33,-20.5965], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "CH3C(O)cHCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  C u1 p0 c0 {2,S} {3,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9855,0.0237989,1.37642e-05,-2.97788e-08,1.18661e-11,-7739.14,10.1295], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.44948,0.0221127,-8.20349e-06,1.36034e-09,-8.32012e-14,-9432.4,-15.429], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "CH3C(O)CH2cH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91742,0.023678,1.80897e-05,-3.64814e-08,1.45595e-11,-6280.37,12.622], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.76241,0.0204773,-7.68087e-06,1.28311e-09,-7.88458e-14,-8448.33,-20.5965], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "MEKenol2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57566,0.022878,3.23299e-05,-5.41428e-08,2.10539e-11,-24196.8,13.28], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.2047,0.0206883,-7.29961e-06,1.17135e-09,-7.00593e-14,-27124.9,-30.572], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "CH2C(OH)cHCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {4,D} {5,S}
3  C u1 p0 c0 {1,S} {2,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58128,0.0241088,2.29162e-05,-4.40571e-08,1.76383e-11,-7587.12,11.7239], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.1873,0.0186173,-6.61927e-06,1.06604e-09,-6.38976e-14,-10342.6,-31.173], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "CH2C(OH)CH2cH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61013,0.0238016,2.16536e-05,-4.21728e-08,1.69128e-11,482.269,14.904], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.9496,0.0183984,-6.53257e-06,1.05318e-09,-6.32036e-14,-2171.47,-26.4634], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "cHC(OH)C2H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u1 p0 c0 {3,D} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55104,0.0261168,1.6477e-05,-3.7833e-08,1.56244e-11,5517.28,13.7253], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.4113,0.0178712,-6.29561e-06,1.00968e-09,-6.03802e-14,2796.97,-29.9658], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "MEKenol",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78628,0.0252404,2.014e-05,-3.94647e-08,1.56651e-11,-25848.4,11.188], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.91291,0.0222807,-8.06375e-06,1.31687e-09,-7.97378e-14,-28140.4,-23.7294], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "CH3CHcOH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u1 p0 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49744,0.0173182,1.72338e-05,-3.35069e-08,1.35558e-11,8974.68,11.0911], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.88045,0.0114619,-3.79051e-06,5.79916e-10,-3.35082e-14,6724.05,-24.5977], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "CH3C(OH)cH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77363,0.0182668,8.48832e-06,-2.2111e-08,9.23095e-12,8237.68,10.0948], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.52773,0.0130726,-4.66091e-06,7.54755e-10,-4.54574e-14,6602.61,-16.2793], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "CH3C(OH)cCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u1 p0 c0 {2,S} {3,D}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89725,0.0290106,-1.02286e-06,-1.60209e-08,7.49908e-12,2728.68,11.0921], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.15924,0.0206094,-7.58087e-06,1.25184e-09,-7.63887e-14,1050.22,-17.4399], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "CH3C(OH)CHcH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58128,0.0241088,2.29162e-05,-4.40571e-08,1.76383e-11,-7587.12,11.7239], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.1873,0.0186173,-6.61927e-06,1.06604e-09,-6.38976e-14,-10342.6,-31.173], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "cH2CH(OH)C2H3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43904,0.0207327,3.73152e-05,-6.12237e-08,2.39261e-11,2739.56,15.9301], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.7464,0.0162972,-5.71419e-06,9.1442e-10,-5.458e-14,-745.358,-37.1305], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "CH3CH(OH)cCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,D} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {3,D}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51555,0.0235793,2.68286e-05,-4.97499e-08,1.99012e-11,6637.55,14.2101], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.2479,0.0169158,-5.99836e-06,9.6755e-10,-5.80866e-14,3491.82,-34.9495], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "CH3CH(OH)CHcH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  C u1 p0 c0 {3,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37996,0.0230479,3.21386e-05,-5.68839e-08,2.26376e-11,7774.57,14.7514], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.2081,0.01577,-5.47723e-06,8.70919e-10,-5.17566e-14,4223.08,-40.6328], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "CH3CH(o)C2H3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44098,0.018203,4.72454e-05,-7.17474e-08,2.75242e-11,4272.32,13.8643], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.9329,0.0167584,-5.91937e-06,9.51232e-10,-5.69196e-14,565.895,-41.0141], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "CH3CHCHCHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8099,0.0185437,3.4384e-05,-5.58308e-08,2.16893e-11,-16349.6,9.9193], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.7479,0.0160438,-6.18294e-06,1.05277e-09,-6.54739e-14,-19385.3,-35.6539], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8APR2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "CHCHCHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 C u1 p0 c0 {1,D} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79724,0.0115702,2.27323e-05,-3.84771e-08,1.52552e-11,17736.5,8.82614], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.3627,0.00683571,-2.7801e-06,4.90649e-10,-3.11935e-14,15357.7,-28.2038], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "CH3CCHCHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,D} {8,S}
3  C u0 p0 c0 {2,S} {9,D} {10,S}
4  C u1 p0 c0 {1,S} {2,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92087,0.0223139,1.32211e-05,-3.2387e-08,1.35233e-11,12227.5,9.82341], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.9943,0.0143725,-5.70007e-06,9.87732e-10,-6.21247e-14,9805.3,-29.3643], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "CH3CHCHCO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48793,0.0245706,7.94827e-06,-2.71908e-08,1.18601e-11,4921.18,10.4669], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.9774,0.0137179,-4.71706e-06,7.41678e-10,-4.3712e-14,2477.5,-30.4182], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: CH3CHCHCO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "C4H7O-14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u1 p0 c0 {1,S} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92516,0.0246634,2.24211e-05,-4.58989e-08,1.86835e-11,1331.07,12.514], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.7295,0.0165976,-6.6151e-06,1.15513e-09,-7.30598e-14,-1773.93,-36.7162], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "tBuOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20127,0.031949,2.61305e-05,-5.32325e-08,2.15879e-11,-40694.7,10.1937], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.2889,0.022871,-7.63004e-06,1.17452e-09,-6.81884e-14,-44260.4,-46.2525], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: tBuOH_species_MRH (Species ID: tBuOH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "iC4H8",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68976,0.0167587,3.61833e-05,-5.27991e-08,1.97188e-11,-3981.86,8.01871], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.71464,0.0211045,-7.36932e-06,1.17118e-09,-6.95539e-14,-6196.99,-22.3044], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "HOC(CH2)(CH3)2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31715,0.0273287,3.1594e-05,-5.68883e-08,2.25427e-11,-15515.1,14.0786], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.6393,0.021498,-7.31827e-06,1.14214e-09,-6.69477e-14,-18936.8,-38.7206], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "OC(CH3)3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26391,0.0312339,2.07769e-05,-4.61869e-08,1.89904e-11,-13090.7,10.1956], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.7021,0.0215518,-7.2266e-06,1.1159e-09,-6.49266e-14,-16367.9,-42.3207], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: tBuOH_species_MRH (Species ID: OC(CH3)3)""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "iC4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.3874,0.0206785,2.893e-05,-5.37553e-08,2.3567e-11,14758.4,15.5529], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.3497,0.0192508,-6.8136e-06,1.08485e-09,-6.42422e-14,12440.7,-18.7061], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "HCC(CH3)2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u1 p0 c0 {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66514,0.0199975,2.03304e-05,-3.64893e-08,1.42892e-11,25732.3,9.15713], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.92125,0.0182874,-6.36531e-06,1.00951e-09,-5.98748e-14,23724.9,-21.0051], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "tC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9921,0.0192506,2.67723e-05,-3.99728e-08,1.46696e-11,3777.99,8.03403], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.51964,0.0261732,-9.41586e-06,1.52671e-09,-9.19529e-14,2429.27,-8.39699], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "iC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34837,0.0176634,4.26157e-05,-6.06193e-08,2.25257e-11,6252.39,12.6622], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.95093,0.0230275,-7.50786e-06,1.12743e-09,-6.4137e-14,3756.93,-21.276], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "iC4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49481,0.0142425,6.18152e-05,-8.22823e-08,3.01064e-11,-18427.4,9.20248], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.90139,0.0246641,-8.42861e-06,1.31706e-09,-7.72354e-14,-21493.3,-30.6728], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "sSPC(116)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91112,0.0474937,-5.4377e-07,-3.27136e-08,1.57512e-11,-32254.6,19.9149], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.0488,0.0234687,-7.72308e-06,1.17145e-09,-6.72081e-14,-36294.3,-50.5626], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "sSPC(46)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27948,0.031328,1.90991e-05,-4.60863e-08,1.93154e-11,4110.03,16.4306], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.8672,0.0184946,-6.36935e-06,1.00249e-09,-5.91133e-14,531.285,-41.9914], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "sSPC(56)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68861,0.0340055,-8.18299e-07,-1.99641e-08,9.38119e-12,4788.14,14.6094], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.5404,0.0226686,-8.15961e-06,1.32318e-09,-7.96966e-14,2622.26,-22.444], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "sSPC(752)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57886,0.0365605,1.31349e-05,-4.26149e-08,1.8457e-11,-24512,17.2541], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.814,0.0209509,-7.88758e-06,1.32021e-09,-8.11962e-14,-28211,-44.2454], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "sSPC(332)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59977,0.0441622,5.37078e-06,-3.82956e-08,1.74921e-11,-30154.9,17.7704], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.097,0.0238092,-8.99835e-06,1.51505e-09,-9.36198e-14,-34121.4,-49.8936], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "sSPC(1013)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {6,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65727,0.052863,-1.54566e-05,-2.00228e-08,1.1831e-11,-27237.9,16.6054], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.4872,0.0229178,-8.98184e-06,1.54555e-09,-9.68176e-14,-31260,-56.428], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "sSPC(1072)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11746,0.0426621,2.08846e-06,-3.37826e-08,1.57534e-11,-41569.3,13.8176], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.7883,0.0231044,-9.67066e-06,1.72739e-09,-1.10647e-13,-45246.2,-49.2352], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "sSPC(1151)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3289,0.027786,2.07112e-05,-4.52212e-08,1.84586e-11,-23119.1,11.908], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.8092,0.0205039,-8.72389e-06,1.57591e-09,-1.01647e-13,-26133.9,-35.6313], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "sSPC(1356)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23105,0.0167354,4.56392e-05,-6.96621e-08,2.68697e-11,-18269.6,20.4233], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.062,0.0136066,-4.50254e-06,6.86701e-10,-3.95108e-14,-22027.6,-36.0092], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "sSPC(1697)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9583,0.00812809,5.6411e-06,-9.7528e-09,3.60672e-12,590.147,7.46942], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[4.5071,0.0100592,-3.5067e-06,5.54663e-10,-3.28241e-14,276.115,3.79532], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "sSPC(1735)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {6,S} {7,S}
6 O u0 p2 c0 {1,S} {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90835,0.00987919,1.51646e-05,-2.39753e-08,9.11022e-12,-17697.7,6.8127], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.55193,0.0109234,-4.00349e-06,6.54883e-10,-3.96302e-14,-18801.6,-8.83125], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "sSPC(1909)",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {3,S} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20145,0.0054319,2.36611e-05,-3.40634e-08,1.28665e-11,-2839.56,7.36822], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.01193,0.00665857,-3.12848e-06,5.9507e-10,-3.94869e-14,-4416.92,-15.1118], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "sSPC(3071)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94137,0.00840453,1.03906e-05,-2.05331e-08,8.41698e-12,-14380.6,11.0029], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.20785,0.00385484,-1.74687e-06,3.26012e-10,-2.13957e-14,-15853.5,-12.6939], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "sSPC(3121)",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {5,S} {6,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89142,0.0101556,1.99141e-05,-3.47556e-08,1.39205e-11,-37766.1,10.3461], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.2527,0.00471906,-2.24366e-06,4.26231e-10,-2.82018e-14,-40028.9,-25.3205], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "sSPC(2810)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88443,-0.00282937,2.92849e-05,-3.40948e-08,1.20699e-11,-16079.5,7.85043], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.61541,0.0038558,-1.36009e-06,2.16778e-10,-1.28581e-14,-17099.4,-3.8859], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""sSPC(2810)              C   1H   1O   2     G   300.000  5000.000   995.043    1
6.33586637E+00 3.43117948E-03-2.37139468E-06 5.19512848E-10-3.68906227E-14    2
-2.17926651E+04-7.88494751E+00 4.53163202E+00-6.01162662E-03 3.70316909E-05    3
-4.27425448E-08 1.50691240E-11-2.06070781E+04 4.96370739E+00                   4
Primary Thermo Library: Franklin (Species ID: formyloxy)""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "sSPC(1474)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {11,S} {12,S}
11 O u0 p2 c0 {1,S} {10,S}
12 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18111,0.0184865,5.51627e-05,-8.38846e-08,3.23732e-11,-36557.5,19.7666], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.1069,0.0144708,-4.99933e-06,7.8692e-10,-4.6317e-14,-41105.3,-48.6358], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "sSPC(1590)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u1 p2 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39255,0.00361039,7.37855e-05,-9.53232e-08,3.50785e-11,-18107.3,17.857], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.1278,0.0118703,-4.05256e-06,6.35443e-10,-3.73172e-14,-21993,-35.0319], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "tSPC(54)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59416,0.037416,-8.23637e-06,-1.38105e-08,7.56701e-12,4427.08,13.8913], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.2235,0.0219432,-7.82038e-06,1.2594e-09,-7.54969e-14,2156.45,-26.6585], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "tSPC(77)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33922,0.0380354,4.06336e-06,-3.26254e-08,1.50438e-11,4400.55,13.7705], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.5428,0.019144,-6.87269e-06,1.10879e-09,-6.64628e-14,876.569,-46.7287], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "tSPC(122)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44862,0.0598243,-4.31325e-05,1.09556e-08,9.18772e-13,-5451.81,18.4142], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.7773,0.0236461,-8.76824e-06,1.44784e-09,-8.82461e-14,-8567.81,-44.3322], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "tSPC(157)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {6,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {5,S} {14,S}
8  O u0 p2 c0 {6,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92383,0.0614395,-2.97848e-05,-1.1335e-08,1.00669e-11,-5762.36,18.8087], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[20.4965,0.0184402,-6.63312e-06,1.07113e-09,-6.4239e-14,-10627.9,-72.7578], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "tSPC(213)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {9,D} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55006,0.0443261,-7.59946e-06,-2.5437e-08,1.34455e-11,-25864.4,13.6814], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.1062,0.0167732,-6.67824e-06,1.15678e-09,-7.26917e-14,-29896,-58.3539], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "tSPC(97)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {14,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {2,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56714,0.0445617,6.06932e-06,-3.99671e-08,1.82331e-11,-32516.1,15.9309], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.6203,0.0232609,-8.81127e-06,1.48619e-09,-9.19423e-14,-36657,-54.7328], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "tSPC(439)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55166,0.0472364,4.91654e-06,-4.22195e-08,1.95955e-11,-26124.9,16.8982], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.4101,0.0218352,-8.54102e-06,1.46825e-09,-9.18928e-14,-30781.3,-63.2508], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "tSPC(343)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,D} {11,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39014,0.0283395,2.09474e-05,-4.84021e-08,2.02864e-11,-5605.08,12.4221], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.6588,0.0144039,-5.32453e-06,8.76473e-10,-5.32276e-14,-9400.29,-49.6885], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: tSPC(343))""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "tSPC(346)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,D} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {4,D} {7,S}
3 C u1 p0 c0 {1,D} {2,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7848,0.0121631,1.42825e-05,-2.5523e-08,1.00686e-11,21625,9.73634], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.77377,0.0100911,-3.64332e-06,5.89867e-10,-3.5438e-14,20139.9,-12.9618], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: Franklin (Species ID: CH2CCHO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "tSPC(878)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86586,0.0338732,-2.47443e-05,4.65884e-09,1.42211e-12,-1478.21,11.4928], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.0076,0.0107772,-4.44943e-06,7.90917e-10,-5.05605e-14,-3575.39,-30.1423], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    label = "H2CCCO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80672,0.0121373,4.31444e-06,-1.338e-08,5.72662e-12,14927.5,7.84494], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.10621,0.00785761,-2.77708e-06,4.44957e-10,-2.65746e-14,13826.1,-10.2917], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: Franklin (Species ID: CH2CCO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    label = "tSPC(1286)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56609,0.0260115,5.78317e-06,-2.79816e-08,1.27e-11,-7756.58,12.0738], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.7918,0.0107508,-4.1134e-06,6.92705e-10,-4.27126e-14,-10673.1,-37.8183], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: tSPC(1286))""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    label = "tSPC(1416)",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,D} {6,S} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  C u0 p0 c0 {1,D} {3,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {9,S} {10,S}
9  O u0 p2 c0 {4,S} {8,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1982,0.0276343,1.5748e-05,-4.32536e-08,1.87548e-11,-32960.9,16.3149], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.3109,0.0096233,-3.35217e-06,5.31083e-10,-3.14074e-14,-36890.3,-49.6942], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "tSPC(1553)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {5,S} {6,D}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {3,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51999,0.0129819,2.9844e-05,-4.75741e-08,1.85642e-11,-11502,11.9065], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.8282,0.00926776,-3.24512e-06,5.15798e-10,-3.05787e-14,-14226.9,-29.6992], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: tSPC(1553))""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "C8H14",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 C u0 p0 c0 {13,D} {16,S} {17,S}
13 C u0 p0 c0 {12,D} {14,S} {15,S}
14 C u0 p0 c0 {3,S} {13,S} {18,S} {19,S}
15 C u0 p0 c0 {13,S} {20,S} {21,S} {22,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {12,S}
18 H u0 p0 c0 {14,S}
19 H u0 p0 c0 {14,S}
20 H u0 p0 c0 {15,S}
21 H u0 p0 c0 {15,S}
22 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11484,0.0538392,3.04725e-05,-7.27909e-08,3.01484e-11,-1810.72,18.0148], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.3366,0.0377743,-1.33356e-05,2.13642e-09,-1.27597e-13,-7073.95,-66.5714], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "tSPC(3683)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85191,0.0359949,-1.69307e-05,-3.96886e-09,4.2133e-12,-13246.1,13.1138], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.4114,0.0174246,-6.75251e-06,1.14833e-09,-7.13491e-14,-15335.5,-26.2588], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "C4H8O2(62)",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {13,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {13,S} {14,S}
13 O u0 p2 c0 {3,S} {12,S}
14 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54421,0.0391671,1.28715e-06,-2.8033e-08,1.30705e-11,-13860.8,13.2346], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.2684,0.0228074,-8.31717e-06,1.35962e-09,-8.23031e-14,-16921.2,-39.285], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "C4H7OJ(79)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49728,0.0199059,3.65224e-05,-5.77103e-08,2.22063e-11,5135.02,12.4492], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.1051,0.0189071,-6.56905e-06,1.04001e-09,-6.15731e-14,2156.43,-31.5756], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: C4H7OJ(79))""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "tSPC(110)",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {8,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40987,0.0251291,1.78678e-05,-3.96136e-08,1.635e-11,10898.1,10.9435], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.7598,0.0161131,-5.54938e-06,8.70883e-10,-5.1212e-14,8021.04,-35.4055], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "C4H6O(105)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15235,0.00207768,9.3085e-05,-1.17019e-07,4.26071e-11,-2710.31,13.9743], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.5359,0.0158065,-5.17047e-06,7.74774e-10,-4.3851e-14,-7124.79,-44.0482], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "C5H10_iso",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.53433,0.0405357,2.68412e-06,-2.77844e-08,1.29415e-11,-6601.98,20.1089], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.1696,0.0291427,-1.1304e-05,2.04262e-09,-1.39646e-13,-9718.58,-27.8265], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""T11/95
!! New species with ReservoirState t-butanol oxidation chemistry""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "C5H9J(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u1 p0 c0 {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44256,0.0278474,2.8319e-05,-5.22112e-08,2.06826e-11,23011.9,12.7876], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.8048,0.023086,-8.00001e-06,1.26443e-09,-7.47975e-14,19919.3,-34.6916], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "C5H9J(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  C u1 p0 c0 {3,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26218,0.023477,4.69482e-05,-7.31135e-08,2.80854e-11,11559,12.8781], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.8726,0.0222396,-7.55954e-06,1.17527e-09,-6.86364e-14,7795.19,-42.7414], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "C5H9J(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u1 p0 c0 {3,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4728,0.0258394,3.47583e-05,-5.84354e-08,2.26966e-11,9907.46,10.7861], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.5808,0.023832,-8.32367e-06,1.3208e-09,-7.83149e-14,6779.7,-35.8988], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    label = "C5H9J(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50164,0.0255323,3.34956e-05,-5.6551e-08,2.19711e-11,17976.8,13.9663], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.3431,0.0236132,-8.23697e-06,1.30793e-09,-7.7621e-14,14950.8,-31.1892], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    label = "C5H11J(10)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87955,0.0295797,2.52342e-05,-4.51235e-08,1.73229e-11,1296.66,11.5431], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.86924,0.031713,-1.14346e-05,1.85721e-09,-1.1199e-13,-794.928,-18.0248], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 247,
    label = "C5H11J(11)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {1,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23582,0.0279925,4.10776e-05,-6.577e-08,2.5179e-11,3771.07,15.0727], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.3005,0.0285672,-9.52656e-06,1.45793e-09,-8.41744e-14,532.727,-32.0024], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "C5H8(95)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11507,0.0241456,3.88788e-05,-6.48961e-08,2.54552e-11,6818.69,11.7034], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.3033,0.0185577,-6.01409e-06,9.03112e-10,-5.14042e-14,3040.21,-46.1968], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""New thermo from C5H10_iso RMG run""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "SPC(482)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,D} {17,S}
6  C u1 p0 c0 {1,S} {18,S} {19,S}
7  C u0 p0 c0 {8,D} {20,S} {21,S}
8  C u0 p0 c0 {5,D} {7,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0215,0.052555,3.50135e-05,-8.03201e-08,3.3314e-11,29306.2,18.9389], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[20.3145,0.0333518,-1.18844e-05,1.91698e-09,-1.15011e-13,23374,-76.9201], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "SPC(483)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u1 p0 c0 {1,S} {2,S} {4,S}
6  C u0 p0 c0 {2,S} {8,D} {19,S}
7  C u0 p0 c0 {8,D} {20,S} {21,S}
8  C u0 p0 c0 {6,D} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54707,0.0560807,6.14857e-06,-4.22066e-08,1.88115e-11,27800.6,18.6999], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.419,0.0389588,-1.41731e-05,2.31692e-09,-1.40329e-13,23922.9,-46.1292], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "C5H7J(504)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,D} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  C u0 p0 c0 {5,D} {11,S} {12,S}
5  C u0 p0 c0 {2,D} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5215,0.0228027,2.81094e-05,-4.93643e-08,1.94235e-11,39589.2,14.0644], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.1544,0.0189877,-6.64388e-06,1.05733e-09,-6.28392e-14,36740,-29.4061], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "SPC(493)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u1 p0 c0 {1,S} {14,S} {15,S}
6  C u0 p0 c0 {3,D} {16,S} {17,S}
7  C u0 p0 c0 {8,D} {18,S} {19,S}
8  C u0 p0 c0 {4,D} {7,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1107,0.0499837,2.64828e-05,-6.8827e-08,2.91131e-11,44132.5,18.443], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[19.5449,0.0292191,-1.0503e-05,1.70521e-09,-1.0277e-13,38619.4,-72.0294], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "SPC(494)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {6,D}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u1 p0 c0 {1,S} {14,S} {15,S}
6  C u0 p0 c0 {3,D} {16,S} {17,S}
7  C u0 p0 c0 {8,D} {18,S} {19,S}
8  C u0 p0 c0 {4,D} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.07595,0.0611153,-1.56911e-05,-2.1292e-08,1.22398e-11,43416.4,17.2629], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.6651,0.0323061,-1.11819e-05,1.76286e-09,-1.041e-13,39434,-54.6517], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "SPC(495)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {14,S}
5  C u0 p0 c0 {1,S} {8,D} {15,S}
6  C u1 p0 c0 {3,S} {16,S} {17,S}
7  C u0 p0 c0 {8,D} {18,S} {19,S}
8  C u0 p0 c0 {5,D} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00282,0.0497889,2.56157e-05,-6.66467e-08,2.81441e-11,36734.5,18.6439], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.7492,0.0301404,-1.05675e-05,1.68271e-09,-1.00026e-13,31439.9,-68.1039], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "SPC(496)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {6,D} {14,S}
5  C u0 p0 c0 {1,S} {8,D} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u0 p0 c0 {8,D} {18,S} {19,S}
8  C u0 p0 c0 {5,D} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05655,0.0427203,4.18814e-05,-8.00349e-08,3.20668e-11,36596.6,18.8551], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.0746,0.0321521,-1.12048e-05,1.773e-09,-1.04877e-13,31540.3,-60.0935], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "SPC(498)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {7,D} {17,S} {18,S}
7  C u0 p0 c0 {5,D} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65961,0.0457515,7.68673e-06,-3.70559e-08,1.61582e-11,30281.9,15.5962], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.0694,0.033419,-1.21544e-05,1.98642e-09,-1.20291e-13,27147.1,-36.096], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "SPC(499)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u1 p0 c0 {1,S} {15,S} {16,S}
6  C u0 p0 c0 {7,D} {17,S} {18,S}
7  C u0 p0 c0 {4,D} {6,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13404,0.0422259,3.65516e-05,-7.51694e-08,3.06607e-11,31787.6,16.5283], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.9649,0.0278121,-9.86569e-06,1.58648e-09,-9.49739e-14,26598.2,-66.1937], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "C6H7J(511)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {6,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {1,D} {10,S} {11,S}
5  C u0 p0 c0 {6,D} {12,S} {13,S}
6  C u0 p0 c0 {2,D} {5,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82351,0.0339072,2.46495e-05,-5.71921e-08,2.40713e-11,41959.3,13.1578], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.6641,0.0159344,-5.03612e-06,7.38346e-10,-4.11838e-14,37340.3,-62.9157], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "C6H7J(512)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,D} {9,S}
3  C u0 p0 c0 {5,D} {10,S} {11,S}
4  C u0 p0 c0 {6,D} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {3,D}
6  C u0 p0 c0 {2,D} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43716,0.0308556,1.74972e-05,-4.26763e-08,1.78099e-11,56155.4,15.6532], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.8544,0.0200759,-7.07067e-06,1.13138e-09,-6.75139e-14,52940.8,-36.4685], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "C6H7J(505)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u0 p0 c0 {2,S} {5,D} {10,S}
4  C u0 p0 c0 {5,D} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {4,D}
6  C u1 p0 c0 {2,D} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00389,0.0382776,6.02042e-06,-3.62898e-08,1.66685e-11,53412.1,13.0673], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.5963,0.0167807,-5.47659e-06,8.27508e-10,-4.7345e-14,49464.4,-54.8659], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 261,
    label = "C6H7J(506)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {5,D} {10,S}
3  C u0 p0 c0 {2,S} {6,D} {11,S}
4  C u0 p0 c0 {6,D} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {2,D}
6  C u0 p0 c0 {3,D} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23393,0.0353985,8.12855e-06,-3.53094e-08,1.57462e-11,52460,13.4001], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.9528,0.0186519,-6.33695e-06,9.87925e-10,-5.78746e-14,49022.8,-44.812], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 262,
    label = "C8H15J(44)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {23,S}
6  C u0 p0 c0 {4,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {6,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52722,0.0588103,1.15348e-05,-4.93933e-08,2.13591e-11,6188.2,17.9087], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.6077,0.0435842,-1.57662e-05,2.56753e-09,-1.55111e-13,2133.74,-48.6054], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""New species from C8H14 RMG run""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    label = "SPC(425)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {5,S} {9,D}
7  C u0 p0 c0 {1,S} {11,D} {22,S}
8  C u1 p0 c0 {1,S} {23,S} {24,S}
9  C u0 p0 c0 {6,D} {25,S} {26,S}
10 C u0 p0 c0 {11,D} {27,S} {28,S}
11 C u0 p0 c0 {7,D} {10,D}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66916,0.0817856,2.1314e-05,-8.45899e-08,3.73502e-11,34197.8,25.3045], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[27.053,0.045223,-1.6216e-05,2.6273e-09,-1.58132e-13,26302.6,-107.501], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 264,
    label = "SPC(426)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {6,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {7,S} {21,S} {22,S} {23,S}
6  C u1 p0 c0 {1,S} {3,S} {4,S}
7  C u0 p0 c0 {2,S} {5,S} {9,D}
8  C u0 p0 c0 {3,S} {11,D} {24,S}
9  C u0 p0 c0 {7,D} {25,S} {26,S}
10 C u0 p0 c0 {11,D} {27,S} {28,S}
11 C u0 p0 c0 {8,D} {10,D}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19473,0.0853112,-7.55084e-06,-4.64764e-08,2.28478e-11,32692.1,25.0655], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[22.1575,0.05083,-1.85047e-05,3.02724e-09,-1.83449e-13,26851.6,-76.7098], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "C7H10(454)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {7,T}
7  C u0 p0 c0 {6,T} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00021,0.0456574,1.05324e-05,-4.2925e-08,1.88505e-11,22919.5,16.6143], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.9671,0.028232,-9.44959e-06,1.44993e-09,-8.38814e-14,19019.2,-48.6918], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "C12H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,D} {9,S} {19,S}
4  C u0 p0 c0 {1,S} {10,D} {20,S}
5  C u0 p0 c0 {2,D} {11,S} {21,S}
6  C u0 p0 c0 {2,S} {12,D} {22,S}
7  C u0 p0 c0 {9,D} {10,S} {13,S}
8  C u0 p0 c0 {11,D} {12,S} {14,S}
9  C u0 p0 c0 {3,S} {7,D} {15,S}
10 C u0 p0 c0 {4,D} {7,S} {16,S}
11 C u0 p0 c0 {5,S} {8,D} {17,S}
12 C u0 p0 c0 {6,D} {8,S} {18,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.1946,0.053526,8.55001e-05,-1.63904e-07,7.29976e-11,19002.1,27.2149], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[22.8964,0.0368453,-1.35016e-05,2.20803e-09,-1.33358e-13,10739.6,-100.51], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""biphenyl   g 8/00
Burcat 30-SEPT-2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    label = "biC5H5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,D} {13,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {8,S} {17,S}
8  C u0 p0 c0 {4,D} {7,S} {18,S}
9  C u0 p0 c0 {5,D} {10,S} {19,S}
10 C u0 p0 c0 {6,D} {9,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46682,0.0498067,5.879e-05,-1.11659e-07,4.52341e-11,29606.1,-2.84787], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[24.2358,0.0288286,-9.88028e-06,1.54551e-09,-9.06125e-14,21980.2,-124.313], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10Jul2010
RMG estimate""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "C5H4C5H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,D} {9,S} {18,S}
6  C u1 p0 c0 {2,S} {10,S} {19,S}
7  C u0 p0 c0 {3,D} {8,S} {14,S}
8  C u0 p0 c0 {4,D} {7,S} {15,S}
9  C u0 p0 c0 {5,S} {10,D} {16,S}
10 C u0 p0 c0 {6,S} {9,D} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47331,0.0328096,9.63596e-05,-1.46047e-07,5.62772e-11,47854.1,19.8669], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[22.9745,0.0265227,-8.92156e-06,1.37686e-09,-7.98954e-14,40005.5,-97.8749], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: C5H4C5H5)""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "C10H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,D} {9,S} {18,S}
6  C u0 p0 c0 {2,S} {10,D} {19,S}
7  C u0 p0 c0 {3,S} {9,D} {14,S}
8  C u0 p0 c0 {4,D} {10,S} {16,S}
9  C u0 p0 c0 {5,S} {7,D} {15,S}
10 C u0 p0 c0 {6,D} {8,S} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.21356,0.0548914,5.55281e-05,-1.24861e-07,5.75105e-11,25257.5,32.8078], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.6879,0.032052,-1.16715e-05,1.90182e-09,-1.14604e-13,18010,-82.9834], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""2-hydro Rad T 7/98
RMG estimate
C10H9                   C  10H   9          G   300.000  5000.000   995.043    1
2.50288494E+01 2.58118605E-02-8.02693596E-06 1.15108671E-09-6.28380917E-14    2
3.08581976E+04-1.28597031E+02 1.89792700E+00 3.64615840E-02 1.00036541E-04    3
-1.54407467E-07 5.99134478E-11 3.95374805E+04 3.36303786E+00                   4
Active Thermochemical Tables (17-DEC-2010)""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "fulvalene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {15,S}
4  C u0 p0 c0 {1,S} {8,D} {16,S}
5  C u0 p0 c0 {2,S} {9,D} {17,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {3,D} {8,S} {11,S}
8  C u0 p0 c0 {4,D} {7,S} {12,S}
9  C u0 p0 c0 {5,D} {10,S} {13,S}
10 C u0 p0 c0 {6,D} {9,S} {14,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {10,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5107,0.0254744,0.000109016,-1.56552e-07,5.94832e-11,43175,17.0924], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[22.1716,0.0248738,-8.31664e-06,1.27754e-09,-7.38517e-14,35379.4,-97.1735], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: fulvalene)""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    label = "C10H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {1,D} {8,S} {13,S}
4  C u0 p0 c0 {1,S} {9,D} {14,S}
5  C u0 p0 c0 {2,S} {10,D} {17,S}
6  C u0 p0 c0 {2,D} {7,S} {18,S}
7  C u0 p0 c0 {6,S} {8,D} {11,S}
8  C u0 p0 c0 {3,S} {7,D} {12,S}
9  C u0 p0 c0 {4,D} {10,S} {15,S}
10 C u0 p0 c0 {5,D} {9,S} {16,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.04919,0.0462971,7.07592e-05,-1.38408e-07,6.20475e-11,15984.9,30.2122], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.613,0.0304494,-1.11225e-05,1.81615e-09,-1.09601e-13,8915.79,-80.023], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Naphthalene T 7/98
RMG estimate
C10H8                   C  10H   8          G   300.000  5000.000   995.043    1
2.69189602E+01 2.15713834E-02-6.55235633E-06 9.17630326E-10-4.90147707E-14    2
2.64510808E+04-1.57796580E+02 1.76738172E+00 4.47088189E-02 7.61063843E-05    3
-1.33211637E-07 5.34356643E-11 3.53164089E+04-1.71838511E+01                   4
Active Thermochemical Tables (17-DEC-2010)""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "iBuOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43413,0.0242081,4.71925e-05,-7.409e-08,2.84309e-11,-36753.8,13.6121], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.8027,0.0240684,-9.15947e-06,1.56144e-09,-9.7397e-14,-40475.7,-40.8734], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 273,
    label = "C3H7O-N2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20675,0.0116221,3.8595e-05,-5.29952e-08,1.93037e-11,-9463.85,12.042], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.4995,0.0208102,-9.06039e-06,1.582e-09,-9.89891e-14,-11229.3,-9.40563], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""RMG""",
    longDesc = 
u"""

""",
)

entry(
    index = 274,
    label = "C4H9Oi1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28769,0.0276289,2.79931e-05,-5.2427e-08,2.08502e-11,-12074,15.9732], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.8523,0.0224318,-8.23872e-06,1.3718e-09,-8.42986e-14,-15225.5,-32.5752], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
    label = "C4H9Oi2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93142,0.0292161,1.21497e-05,-3.17805e-08,1.29941e-11,-14548.4,12.4436], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.42101,0.0255776,-1.01467e-05,1.77108e-09,-1.12114e-13,-16553.2,-18.5976], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
    label = "C4H9Oi3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {5,S} {13,S}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37616,0.0312479,2.11311e-05,-4.8142e-08,1.98916e-11,-15082,13.2524], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.3487,0.0208631,-7.99231e-06,1.37115e-09,-8.59205e-14,-18537.1,-42.199], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    label = "C4H9Oi4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46393,0.0226206,4.6403e-05,-7.25815e-08,2.78598e-11,-10540.5,13.2038], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.7002,0.022313,-8.64097e-06,1.48678e-09,-9.32398e-14,-14201.5,-40.4698], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 278,
    label = "C4H8O-i1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24243,0.0292435,1.32986e-05,-3.44473e-08,1.4314e-11,-21575.9,13.7596], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.3651,0.021948,-7.86866e-06,1.28459e-09,-7.78785e-14,-24049.7,-25.8754], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "C4H8O-i2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93882,0.0310487,1.411e-05,-3.82364e-08,1.61709e-11,-25425.9,13.459], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.9559,0.0198569,-6.7905e-06,1.07334e-09,-6.3648e-14,-28460.8,-36.2316], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 280,
    label = "C4H8O-i3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68165,0.0188948,4.80268e-05,-7.23023e-08,2.74848e-11,-27996.8,11.9234], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.0954,0.0206992,-8.40016e-06,1.48597e-09,-9.47605e-14,-31434.9,-37.4889], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 281,
    label = "C4H7O(15)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21065,0.0265706,2.42436e-05,-4.92994e-08,2.0149e-11,-7211.17,12.002], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.2232,0.0162812,-5.40964e-06,8.27419e-10,-4.77486e-14,-10687,-43.7059], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""21Jul2010 : Iso-butanol chemistry
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "C4H7O(17)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51426,0.0247654,2.34322e-05,-4.55104e-08,1.8292e-11,-3361.2,12.3026], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.6323,0.0183723,-6.48779e-06,1.03867e-09,-6.19791e-14,-6275.83,-33.3497], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    label = "C4H7O(30)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99025,0.0246553,1.99014e-05,-4.09452e-08,1.65251e-11,-9181.74,7.88875], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.2106,0.0192469,-7.54744e-06,1.29805e-09,-8.12609e-14,-11787.8,-32.7844], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(Cs(CsRR)RRR), Group:Cs-(Cds-Od)CsCsH, Gauche:Cs(CsCsRR), G
roup:Cds-OdCsH, Group:Od-Cd, Group:Cs-CsHHH, Gauche:Cs(Cs(CsRR)RRR), Radical:C2CJCHO""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    label = "C4H7O(48)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {9,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01204,0.0189692,3.61847e-05,-5.71099e-08,2.19087e-11,-3363.57,12.2917], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.1378,0.0191504,-7.54302e-06,1.30123e-09,-8.16029e-14,-6208.72,-29.2214], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    label = "C4H7O(51)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20683,0.0161343,4.55929e-05,-6.76128e-08,2.5602e-11,-9448.72,10.3883], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.7861,0.0185935,-7.75165e-06,1.38377e-09,-8.85986e-14,-12587.2,-34.331], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "C3H3OH",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 O u0 p2 c0 {1,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44746,0.0147603,2.02824e-05,-3.64764e-08,1.46236e-11,511.857,10.0258], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.1684,0.00892821,-2.8622e-06,4.27195e-10,-2.42059e-14,-1874.45,-27.6353], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "C4H6Oi-12",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63921,0.0220906,1.66654e-05,-3.40358e-08,1.3689e-11,-13125.5,10.0021], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.56306,0.017775,-6.2215e-06,9.90763e-10,-5.8933e-14,-15269.7,-23.3979], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "C4H6Oi-13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69561,0.0219178,2.72967e-05,-5.02031e-08,2.00937e-11,-15985.5,9.15861], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.5525,0.0150703,-5.73038e-06,9.6834e-10,-5.99425e-14,-19171.7,-40.6802], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-Od(Cds-Cds)H, Group:Od-Cd, Group:Cs-(Cds-Cds)HHH, Gauche:Cs(RRRR), Group:C
ds-Cds(Cds-Od)Cs, Gauche:CsOsCd, Group:Cds-CdsHH, Gauche:CsOsCd, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "C4H5O(14)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u1 p0 c0 {2,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35333,0.0267344,1.16533e-06,-2.04143e-08,9.6332e-12,4922.79,11.6297], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.0522,0.0130492,-4.22893e-06,6.35787e-10,-3.62567e-14,2536.01,-29.7689], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: MRH (Species ID: iC4H5OJ(14))""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    label = "C4H5O(15)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u1 p0 c0 {1,S} {9,S} {10,S}
5  O u0 p2 c0 {3,D}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49061,0.0207862,3.00729e-05,-5.47955e-08,2.2067e-11,2275.78,9.69446], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.8269,0.0114068,-4.2859e-06,7.17511e-10,-4.41022e-14,-1373.9,-48.1238], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 291,
    label = "C3H3OJ(9)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,D}
3 O u0 p2 c0 {1,S} {6,S}
4 C u1 p0 c0 {2,D} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23401,0.0180184,3.2633e-06,-1.77345e-08,8.16029e-12,19115.9,11.5233], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.59143,0.0068989,-1.73753e-06,1.97078e-10,-8.35409e-15,17136,-22.7073], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "HCCCHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79681,0.0138712,3.30065e-06,-1.45007e-08,6.48454e-12,10113.8,6.63276], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.23329,0.00691012,-2.59687e-06,4.32414e-10,-2.64777e-14,8692.64,-17.4535], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "C3H3OJ",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93747,0.0150248,-1.96539e-06,-6.07241e-09,2.99531e-12,19257.5,8.48558], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.23462,0.011089,-4.02e-06,6.55742e-10,-3.96704e-14,18538.1,-3.90353], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    label = "C3H5OJ",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93664,0.0160444,1.11124e-05,-2.25839e-08,8.96239e-12,11687.6,10.8505], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.3293,0.0146988,-5.3898e-06,8.87793e-10,-5.40686e-14,10403.9,-8.55819], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    label = "C3H5OJ(17)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {3,D} {4,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63303,0.0178496,1.19238e-05,-2.63729e-08,1.08193e-11,7837.66,10.5499], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.92017,0.0126077,-4.31164e-06,6.76547e-10,-3.98381e-14,5992.79,-18.9144], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 296,
    label = "nC3H7OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  O u0 p2 c0 {3,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.41878,-0.000575566,8.51215e-05,-1.1106e-07,4.43007e-11,-32836.8,5.29974], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.52377,0.0210371,-7.48398e-06,1.19959e-09,-7.14873e-14,-35070.2,-17.7857], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 2/00
ATcT (12/Aug/2010)""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    label = "C4H7OJ(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u1 p0 c0 {1,S} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33394,0.022853,3.03991e-05,-5.35687e-08,2.12376e-11,1219.27,15.9003], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.3023,0.0167877,-5.66217e-06,8.7834e-10,-5.12543e-14,-2050.02,-34.7818], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "C4H9O2(52)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {2,S} {15,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.71174,0.0279408,3.13106e-05,-5.85449e-08,2.32342e-11,-30752.4,14.7389], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.824,0.0234837,-1.04711e-05,1.94319e-09,-1.2732e-13,-34158.5,-37.1807], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 299,
    label = "C4H9O2(53)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {15,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75933,0.0335669,2.35868e-05,-5.3433e-08,2.21027e-11,-31525.3,17.2699], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.9763,0.0216118,-8.34319e-06,1.42698e-09,-8.90866e-14,-35398,-45.0327], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
    label = "C4H9O2(54)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02309,0.0312723,2.5396e-05,-5.29629e-08,2.14934e-11,-32852.1,16.8833], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.7758,0.0231432,-9.19586e-06,1.59959e-09,-1.00908e-13,-36331.4,-37.8496], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "C4H9O2(55)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02309,0.0312723,2.5396e-05,-5.29629e-08,2.14934e-11,-32852.1,16.8833], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.7758,0.0231432,-9.19586e-06,1.59959e-09,-1.00908e-13,-36331.4,-37.8496], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "CH2CHCHCHOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94737,0.0214663,3.57823e-05,-6.19137e-08,2.47218e-11,-10115,13.7933], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.2626,0.0117322,-3.43928e-06,4.73519e-10,-2.50376e-14,-14136.8,-49.6334], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    label = "CHCHCHCHOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u1 p0 c0 {2,D} {9,S}
5  O u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92275,0.0247051,1.99293e-05,-4.56039e-08,1.92922e-11,19599.1,14.2387], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.4692,0.00891511,-2.43528e-06,3.11851e-10,-1.53585e-14,15785.1,-49.0272], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 304,
    label = "CH2CHCCHOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,D} {4,S} {6,S}
2  C u0 p0 c0 {4,D} {5,S} {9,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u1 p0 c0 {1,S} {2,D}
5  O u0 p2 c0 {2,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96387,0.0278509,7.21479e-06,-3.02e-08,1.36087e-11,13794.9,13.1646], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.8766,0.0113932,-3.23659e-06,4.26643e-10,-2.16067e-14,10664.2,-40.428], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
    label = "CH2CHCHCOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u1 p0 c0 {2,D} {5,S}
5  O u0 p2 c0 {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92275,0.0247051,1.99293e-05,-4.56039e-08,1.92922e-11,19599.1,14.2387], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.4692,0.00891511,-2.43528e-06,3.11851e-10,-1.53585e-14,15785.1,-49.0272], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "CHCCHCHOH",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 O u0 p2 c0 {4,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19145,0.021217,2.11002e-05,-4.44058e-08,1.84889e-11,11101.9,11.548], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.4958,0.00838682,-2.66138e-06,3.92428e-10,-2.19786e-14,7635.76,-45.2261], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    label = "CHCCCHOH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {5,T}
4 O u0 p2 c0 {1,S} {7,S}
5 C u0 p0 c0 {3,T} {8,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14745,0.0289116,-1.37422e-05,-5.43802e-09,4.8031e-12,35995.2,12.4419], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.6777,0.00793905,-2.20404e-06,2.83141e-10,-1.3974e-14,33638.3,-31.9826], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "C4H5O3J(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,D}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23619,0.0360955,2.02321e-06,-3.00749e-08,1.42559e-11,-13947.4,18.5102], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.8579,0.0151501,-5.25421e-06,8.31316e-10,-4.92025e-14,-17536.1,-43.9115], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    label = "C4H5O3J(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {4,D} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {10,D}
4  C u1 p0 c0 {1,S} {2,D}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29721,0.0416168,-9.61612e-06,-2.08536e-08,1.15934e-11,-8755.79,17.7576], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.1491,0.0143429,-5.26813e-06,8.66498e-10,-5.26595e-14,-12520.8,-50.2485], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "OCOOH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 C u1 p0 c0 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62512,0.0181644,-1.02432e-05,-4.89599e-09,4.18644e-12,-14234.6,10.9338], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.0894,-0.000212501,-7.07381e-08,3.35962e-11,-2.98066e-15,-16295.8,-27.9326], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "C4H6O3(21)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,D}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18624,0.0378466,1.15467e-05,-4.42974e-08,1.97594e-11,-37332.9,17.8534], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.9027,0.0160143,-5.751e-06,9.31535e-10,-5.60087e-14,-41711.5,-56.538], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "C4H5O2(12)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82645,0.0216794,2.86643e-05,-5.22844e-08,2.0908e-11,-20173.9,12.471], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.9859,0.0147264,-5.87873e-06,1.02482e-09,-6.46975e-14,-23475.3,-39.1025], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 313,
    label = "CH2CHCHCHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u1 p0 c0 {1,S} {4,S} {6,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  O u0 p2 c0 {4,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6049,0.0174121,3.71602e-05,-6.04232e-08,2.36626e-11,1911.69,10.4551], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.0223,0.0123804,-4.73846e-06,8.01939e-10,-4.96336e-14,-1587.51,-43.0975], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "C4H6O3(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77818,0.0380737,8.56188e-06,-4.10782e-08,1.85631e-11,-23932.1,15.2508], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.8938,0.0168988,-7.07692e-06,1.26382e-09,-8.09025e-14,-28104,-55.8076], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 315,
    label = "C4H5O2(13)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98962,0.0231976,2.71846e-05,-5.25168e-08,2.12683e-11,-5481.94,13.3412], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.9147,0.0142983,-6.13015e-06,1.11235e-09,-7.19027e-14,-8991.74,-42.2038], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "C4H7O3J(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {13,D}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25159,0.0436396,-6.91427e-06,-2.29885e-08,1.20393e-11,-27325.2,16.4769], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.1196,0.0197839,-6.90967e-06,1.09929e-09,-6.53514e-14,-30867.8,-46.6537], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "C4H7O3J(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  C u0 p0 c0 {1,S} {5,S} {13,D}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47344,0.0457039,-1.49698e-05,-1.36727e-08,8.63734e-12,-27368.3,17.3507], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.3672,0.0214462,-7.84945e-06,1.28636e-09,-7.80069e-14,-30503.3,-40.0107], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "C4H7O3J(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00537,0.0422716,4.38323e-06,-3.79941e-08,1.77723e-11,-17380.6,19.1849], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.1013,0.0173348,-5.85414e-06,9.09562e-10,-5.31483e-14,-21756.5,-56.6424], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "C4H7O3J(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15464,0.0425811,7.53093e-06,-4.25308e-08,1.94769e-11,-17559.1,17.4697], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.6827,0.0180309,-6.49068e-06,1.05324e-09,-6.34178e-14,-22126.2,-60.9686], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "C4H7O3J(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68903,0.0379658,1.17904e-05,-4.43024e-08,1.96165e-11,-14261.5,17.7823], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.7275,0.0180601,-7.20719e-06,1.25847e-09,-7.95747e-14,-18465.6,-53.1426], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "C4H7O3J(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67548,0.0381108,2.05679e-05,-5.70786e-08,2.4577e-11,-6337.46,16.6839], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.7037,0.0170955,-7.14211e-06,1.27734e-09,-8.18647e-14,-11278.6,-65.5443], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "C3H5O2(54)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u1 p0 c0 {1,S} {4,S} {7,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17578,0.0254084,1.67306e-05,-4.12108e-08,1.75247e-11,8849.57,13.4655], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.6678,0.0110717,-3.62567e-06,5.46026e-10,-3.10882e-14,5383.33,-44.0257], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "C4H5O3J(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82813,0.0363226,-9.61645e-07,-2.68557e-08,1.30596e-11,-5644.22,15.9076], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.849,0.0160346,-6.58013e-06,1.16361e-09,-7.40964e-14,-9026.35,-43.1811], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "CH2CHCH2O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86206,0.0106681,3.15292e-05,-4.45813e-08,1.65854e-11,9322.41,10.5046], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.01433,0.0145413,-5.3108e-06,8.71475e-10,-5.29016e-14,7477.99,-14.6228], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "OCH2CH2CH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69109,0.0187569,2.4159e-05,-4.03898e-08,1.56e-11,-5723.52,26.0262], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.94585,0.0183435,-6.43818e-06,1.02717e-09,-6.1173e-14,-7794.54,-4.45075], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: Franklin (Species ID: npropoxy)""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "HCOOH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.932603,0.01891,-1.55496e-05,7.29003e-09,-1.48369e-12,-47600.7,19.5065], Tmin=(300,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[7.9597,0.00302453,-3.43424e-07,-1.32677e-10,2.52024e-14,-50274.4,-18.7221], Tmin=(1500,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""103190
HCOH              mar94 C   1H   2O   1    0g   300.     5000.    1398.        1
9.18749272e+00 1.52011152e-03-6.27603516e-07 1.09727989e-10-6.89655128e-15    2
7.81364593e+03-2.73434214e+01-2.82157421e+00 3.57331702e-02-3.80861580e-05    3
1.86205951e-08-3.45957838e-12 1.12956672e+04 3.48487757e+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "CH2OOH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81303,0.0121039,5.82748e-06,-1.54831e-08,6.51982e-12,5854.54,6.67809], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.35066,0.00788965,-2.90458e-06,4.73946e-10,-2.85925e-14,4655.13,-12.8606], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "HOCHOOH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.54351,0.0203655,-1.42363e-05,2.59684e-09,6.95111e-13,-15137.7,7.63388], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.41378,0.00944341,-4.76024e-06,9.30384e-10,-6.26299e-14,-16137.4,-12.172], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 329,
    label = "C4H5-114",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38701,0.0173505,1.35555e-05,-2.66852e-08,1.06732e-11,42707.1,11.8727], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.97357,0.0140709,-4.35092e-06,6.21445e-10,-3.39054e-14,41043.9,-14.0027], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "C5H9_2_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73285,0.0216282,3.66741e-05,-5.52431e-08,2.06696e-11,18489.2,15.4629], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.87567,0.0265753,-9.4061e-06,1.50679e-09,-8.99618e-14,16197.4,-15.6961], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 331,
    label = "CHCHCH2OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80105,0.015513,1.64224e-05,-2.97179e-08,1.16988e-11,12824.7,11.3917], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.28958,0.013553,-4.86867e-06,7.91162e-10,-4.77387e-14,11135.2,-14.2415], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "CCCC(OO)OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {16,S}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48091,0.0488223,-8.20243e-06,-2.39092e-08,1.25203e-11,-33065.8,16.8146], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.5312,0.0249167,-9.1526e-06,1.50834e-09,-9.1872e-14,-36678.6,-47.3649], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "CcCC(OOH)OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70276,0.0508866,-1.62579e-05,-1.45933e-08,9.11827e-12,-28011.4,17.6884], Tmin=(300,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.7789,0.026579,-1.00924e-05,1.69542e-09,-1.04527e-13,-31216.5,-40.7219], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "HOOCH2CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 C u1 p0 c0 {1,S} {7,D}
4 O u0 p2 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50376,0.0229106,3.27814e-06,-2.3145e-08,1.0811e-11,-11934.5,14.397], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.1252,0.00759582,-2.79414e-06,4.59496e-10,-2.78951e-14,-14607.9,-31.9655], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: Lee&Bozzelli_JPCA_107_19_3778 (Species ID: HOOCH2CO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "CH2CHCH2CCH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {5,T}
5  C u0 p0 c0 {4,T} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40891,0.0199917,2.89015e-05,-4.87802e-08,1.90895e-11,31059.2,11.9401], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.7901,0.016594,-5.58429e-06,8.61595e-10,-5.00415e-14,28289.5,-30.1693], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "SPC(181)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {2,S} {7,D}
5  C u0 p0 c0 {3,S} {6,D} {8,S}
6  C u0 p0 c0 {1,S} {5,D} {17,S}
7  C u0 p0 c0 {4,D} {18,S} {19,S}
8  C u1 p0 c0 {5,S} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.98296,0.0525185,3.10019e-05,-7.38334e-08,3.06917e-11,15122.2,18.5457], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.9379,0.0347658,-1.21606e-05,1.93331e-09,-1.14807e-13,9650.71,-69.887], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""!!! Added as submechanism part of C8H14 !!!!
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "SPC(1339)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
6  C u1 p0 c0 {1,S} {3,S} {4,S}
7  C u0 p0 c0 {2,S} {5,S} {8,D}
8  C u0 p0 c0 {3,S} {7,D} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50314,0.0303462,8.4591e-05,-1.20072e-07,4.46733e-11,11040,16.0747], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.6585,0.0408673,-1.47304e-05,2.38997e-09,-1.43901e-13,6079.06,-51.4609], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H13/c1-7-3-5-8(2)6-4-7/h3H,4-6H2,1-2H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "SPC(1354)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  C u0 p0 c0 {3,S} {6,D} {19,S}
8  C u1 p0 c0 {6,S} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80085,0.0242065,0.00012241,-1.66974e-07,6.20835e-11,7095.84,17.0859], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[19.3147,0.0356946,-1.22987e-05,1.92949e-09,-1.13344e-13,-45.675,-81.8733], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H13/c1-7-3-5-8(2)6-4-7/h3,8H,1,4-6H2,2H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "SPC(2001)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {7,D}
5  C u1 p0 c0 {2,S} {3,S} {16,S}
6  C u0 p0 c0 {4,S} {8,D} {17,S}
7  C u0 p0 c0 {4,D} {18,S} {19,S}
8  C u0 p0 c0 {6,D} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9392,0.0529671,2.62122e-05,-6.73811e-08,2.82498e-11,21672.8,21.6855], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.0889,0.0352337,-1.21292e-05,1.90589e-09,-1.12251e-13,16520.8,-62.0663], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H13/c1-4-6-7-8(3)5-2/h4-5H,2-3,6-7H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "SPC(2514)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {8,D}
7  C u1 p0 c0 {2,S} {18,S} {19,S}
8  C u0 p0 c0 {6,D} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69139,0.0236553,0.000119562,-1.6184e-07,5.99788e-11,16171.6,21.5006], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.1174,0.0363445,-1.21757e-05,1.86891e-09,-1.0803e-13,9403.62,-71.4267], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H13/c1-6-4-5-7(2)8(6)3/h7-8H,1,3-5H2,2H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "SPC(1656)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
4  C u1 p0 c0 {1,S} {2,S} {7,S}
5  C u0 p0 c0 {1,S} {6,D} {17,S}
6  C u0 p0 c0 {3,S} {5,D} {18,S}
7  C u0 p0 c0 {4,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13115,0.0420394,5.46856e-05,-9.33752e-08,3.64285e-11,15345.3,19.4751], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.5801,0.037503,-1.31371e-05,2.08739e-09,-1.23858e-13,10216.9,-57.6621], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H13/c1-4-6-7-8(3)5-2/h4-6H,2,7H2,1,3H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "SPC(1356)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {5,S} {8,D}
7  C u1 p0 c0 {1,S} {3,S} {20,S}
8  C u0 p0 c0 {2,S} {6,D} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30408,0.0239671,0.000110767,-1.49942e-07,5.53598e-11,12186.8,17.7875], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.5846,0.0385996,-1.38288e-05,2.23476e-09,-1.3415e-13,6176.55,-63.1381], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H13/c1-7-3-5-8(2)6-4-7/h3,6-7H,4-5H2,1-2H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "SPC(3373)",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {2,S} {4,D} {15,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {1,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21333,0.0175376,9.63844e-05,-1.29309e-07,4.7748e-11,6626.39,16.1124], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.9278,0.0293549,-1.02335e-05,1.62132e-09,-9.59566e-14,1378.79,-54.9993], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H10/c1-7-5-3-2-4-6-7/h2-3,6H,4-5H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 344,
    label = "SPC(224)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u1 p0 c0 {1,S} {7,S} {9,S}
7  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
8  C u0 p0 c0 {7,S} {21,S} {22,S} {23,S}
9  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41467,0.0691394,9.99661e-06,-5.4544e-08,2.40124e-11,3706.87,21.0123], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.9573,0.0491239,-1.77849e-05,2.89802e-09,-1.75148e-13,-1090.46,-58.6387], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C9H17/c1-5-9(4)7-6-8(2)3/h2,5-7H2,1,3-4H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 345,
    label = "SPC(1351)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {6,S} {8,D}
8  C u1 p0 c0 {4,S} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11682,0.0291083,9.8471e-05,-1.38938e-07,5.19442e-11,17411.6,16.4542], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.2866,0.0376867,-1.32603e-05,2.11528e-09,-1.25835e-13,11347.1,-68.1402], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H13/c1-7-3-5-8(2)6-4-7/h7H,3-5H2,1-2H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 346,
    label = "SPC(1341)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {1,S} {5,D} {14,S}
7  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.10692,0.0311604,8.47651e-05,-1.24199e-07,4.69384e-11,1893.35,16.2398], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.2028,0.0350205,-1.22931e-05,1.95798e-09,-1.16358e-13,-3908.15,-66.7508], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H12/c1-7-3-5-8(2)6-4-7/h3,6H,4-5H2,1-2H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 347,
    label = "SPC(4491)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u1 p0 c0 {3,S} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94043,0.0099759,0.000116167,-1.49117e-07,5.44635e-11,18932,17.1662], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.0703,0.0271415,-9.0923e-06,1.39094e-09,-8.01008e-14,13254.3,-57.6929], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H9/c1-7-5-3-2-4-6-7/h2-3,5-6H,4H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 348,
    label = "SPC(182)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u0 p0 c0 {2,S} {7,D} {8,S}
6  C u0 p0 c0 {4,D} {20,S} {21,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  C u1 p0 c0 {5,S} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90985,0.0527076,3.32487e-05,-7.73833e-08,3.21217e-11,16450.6,19.2437], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[19.611,0.0341109,-1.18912e-05,1.88559e-09,-1.11757e-13,10723.9,-73.3219], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C8H13/c1-7(2)5-6-8(3)4/h1-3,5-6H2,4H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 349,
    label = "C6H10(1)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {4,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30633,0.029815,4.40463e-05,-7.33068e-08,2.85235e-11,5965.91,15.651], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.7967,0.0263727,-9.14663e-06,1.44702e-09,-8.56448e-14,1960.96,-44.5411], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""!!!!!!#################!!!!!!!!!!!
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "C7H12(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22125,0.0402164,4.20918e-05,-7.79006e-08,3.0958e-11,2922.32,17.8875], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.0617,0.0321087,-1.1276e-05,1.79975e-09,-1.07195e-13,-1787.02,-54.8199], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H12/c1-4-5-6-7(2)3/h4H,1-2,5-6H2,3H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "C6H9J(181)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u1 p0 c0 {2,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {6,D} {10,S}
5  C u0 p0 c0 {2,D} {14,S} {15,S}
6  C u0 p0 c0 {4,D} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96384,0.0288363,4.62249e-05,-7.63117e-08,2.97746e-11,16514.3,15.0349], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.385,0.0238022,-7.8091e-06,1.17693e-09,-6.70845e-14,12217.7,-50.1778], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H9/c1-4-5-6(2)3/h4-5H,1-2H2,3H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "SPC(1981)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {6,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22829,0.00228029,0.00011856,-1.44938e-07,5.19731e-11,14797.1,13.9903], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.1488,0.0266693,-9.02936e-06,1.39583e-09,-8.10724e-14,10039.2,-43.9892], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H9/c1-6-4-2-3-5-6/h2,4H,3,5H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "SPC(4999)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {6,D}
5  C u1 p0 c0 {3,S} {4,S} {13,S}
6  C u0 p0 c0 {4,D} {14,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32404,-0.000595855,0.000132079,-1.60723e-07,5.7628e-11,16239.6,13.9974], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.2769,0.0262572,-9.19504e-06,1.45915e-09,-8.63787e-14,10948.9,-50.6025], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H9/c1-6-4-2-3-5-6/h4H,1-3,5H2" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "SPC(2002)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u1 p0 c0 {1,S} {2,S} {14,S}
6  C u0 p0 c0 {2,S} {4,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70463,0.0108416,8.20814e-05,-1.03718e-07,3.72894e-11,21325.8,14.7453], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.83063,0.0292086,-1.04173e-05,1.67751e-09,-1.00467e-13,17978.3,-25.4736], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H9/c1-6-4-2-3-5-6/h2,5H,3-4H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "SPC(347)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {6,D}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {7,S} {14,S}
6  C u0 p0 c0 {3,D} {15,S} {16,S}
7  C u1 p0 c0 {5,S} {17,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08937,0.0388957,4.26212e-05,-7.89431e-08,3.15013e-11,19855.2,17.7253], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.6629,0.0291003,-1.0101e-05,1.59664e-09,-9.44058e-14,14937.6,-58.8286], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H11/c1-4-5-6-7(2)3/h4-5H,1-2,6H2,3H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 356,
    label = "SPC(4233)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {3,S} {4,S}
6  C u0 p0 c0 {2,S} {7,D} {17,S}
7  C u0 p0 c0 {3,S} {6,D} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60955,0.0167234,9.62103e-05,-1.25182e-07,4.54829e-11,15773,15.2543], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.3836,0.0352017,-1.26708e-05,2.0533e-09,-1.235e-13,11366,-40.4025], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H11/c1-7-5-3-2-4-6-7/h2-3H,4-6H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 357,
    label = "SPC(4249)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u1 p0 c0 {4,S} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22323,0.0154855,0.00011009,-1.44048e-07,5.27538e-11,22144.7,15.6338], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.0117,0.0320211,-1.12007e-05,1.77862e-09,-1.05433e-13,16634.1,-57.0818], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H11/c1-7-5-3-2-4-6-7/h2,7H,3,5-6H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "SPC(1999)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {2,S} {4,D} {14,S}
6  C u1 p0 c0 {1,S} {4,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33433,0.00685726,0.000106585,-1.34222e-07,4.86172e-11,14985.4,12.818], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.9224,0.0259306,-9.02336e-06,1.4266e-09,-8.42726e-14,10225,-47.7239], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H9/c1-6-4-2-3-5-6/h4-5H,2-3H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "SPC(282)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74617,0.0348583,2.46922e-05,-4.93523e-08,1.95154e-11,13402.6,14.6777], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.9831,0.0323789,-1.16879e-05,1.90036e-09,-1.14672e-13,10644.9,-26.8207], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H11/c1-4-5-6(2)3/h4H,1,5H2,2-3H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 360,
    label = "SPC(342)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u1 p0 c0 {3,S} {15,S} {16,S}
7  C u0 p0 c0 {5,D} {17,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08937,0.0388957,4.26212e-05,-7.89431e-08,3.15013e-11,19855.2,17.7253], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.6629,0.0291003,-1.0101e-05,1.59664e-09,-9.44058e-14,14937.6,-58.8286], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H11/c1-4-5-6-7(2)3/h4,6H,1-2,5H2,3H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 361,
    label = "SPC(4924)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {4,S} {7,D}
6  C u1 p0 c0 {2,S} {3,S} {17,S}
7  C u0 p0 c0 {3,S} {5,D} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6162,0.0169748,9.44684e-05,-1.22712e-07,4.45153e-11,16108,15.4405], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.9567,0.0358081,-1.28559e-05,2.0784e-09,-1.24798e-13,11855.9,-37.7818], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H11/c1-7-5-3-2-4-6-7/h2,5H,3-4,6H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 362,
    label = "C6H8(1987)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,D}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  C u0 p0 c0 {3,D} {13,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.65641,-0.000684514,0.000129819,-1.6015e-07,5.79854e-11,12113.5,17.9684], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.7193,0.0201173,-5.99774e-06,8.31529e-10,-4.4102e-14,6282.43,-57.4057], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H8/c1-6-4-2-3-5-6/h2,4H,1,3,5H2" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "SPC(8211)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  C u0 p0 c0 {4,S} {5,D} {16,S}
7  C u1 p0 c0 {5,S} {17,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01301,0.0156712,0.000116928,-1.54094e-07,5.67063e-11,11045.6,15.1722], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.6226,0.0306021,-1.05612e-05,1.65871e-09,-9.7502e-14,4889.53,-67.7427], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H11/c1-7-5-3-2-4-6-7/h5H,1-4,6H2" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 364,
    label = "SPC(4923)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {4,S} {7,D}
6  C u1 p0 c0 {1,S} {3,S} {17,S}
7  C u0 p0 c0 {2,S} {5,D} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6162,0.0169748,9.44684e-05,-1.22712e-07,4.45153e-11,16108,15.4405], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.9567,0.0358081,-1.28559e-05,2.0784e-09,-1.24798e-13,11855.9,-37.7818], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H11/c1-7-5-3-2-4-6-7/h3,6H,2,4-5H2,1H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 365,
    label = "C5H6(1632)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u0 p0 c0 {1,S} {5,D} {7,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u0 p0 c0 {5,D} {10,S} {11,S}
5  C u0 p0 c0 {2,D} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13492,0.021416,3.34926e-05,-5.77094e-08,2.29076e-11,28254.9,11.9575], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.1147,0.0139322,-4.421e-06,6.52509e-10,-3.66225e-14,24653.3,-44.2577], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C5H6/c1-3-5-4-2/h3,5H,1-2H2" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 366,
    label = "SPC(10039)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u1 p0 c0 {1,S} {2,S} {5,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {3,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {17,S} {18,S}
7  C u0 p0 c0 {5,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14311,0.0318271,5.88869e-05,-9.23314e-08,3.5424e-11,19717.3,17.9366], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.9883,0.031112,-1.07383e-05,1.68693e-09,-9.92571e-14,15038.1,-50.8182], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C7H11/c1-4-6-7(3)5-2/h4-5H,1-2,6H2,3H3" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 367,
    label = "C6H9J(182)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {6,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u1 p0 c0 {2,S} {12,S} {13,S}
6  C u0 p0 c0 {3,D} {14,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.10134,0.0286833,4.68225e-05,-7.78993e-08,3.04967e-11,24227.2,16.1868], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.0711,0.0227093,-7.70216e-06,1.19619e-09,-6.98045e-14,19758.8,-51.9848], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H9/c1-4-5-6(2)3/h4H,1-3,5H2" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 368,
    label = "SPC(2635)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u1 p0 c0 {2,S} {3,S} {13,S}
6  C u0 p0 c0 {4,D} {14,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69434,0.00338845,0.000107576,-1.3022e-07,4.63001e-11,22580.1,15.9247], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.1851,0.0295352,-1.0589e-05,1.71006e-09,-1.02573e-13,18702.2,-28.3523], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""(_ SMILES="InChI=1/C6H9/c1-6-4-2-3-5-6/h2H,1,3-5H2" _)
Estimated by RMG using Group Additivity""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "indene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {6,S} {7,B}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {2,B} {8,B} {13,S}
6  C u0 p0 c0 {3,S} {4,D} {17,S}
7  C u0 p0 c0 {3,B} {9,B} {16,S}
8  C u0 p0 c0 {5,B} {9,B} {14,S}
9  C u0 p0 c0 {7,B} {8,B} {15,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.65651,0.0835993,-5.41866e-05,1.31713e-08,0,18073.9,50.1176], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.9942,0.0345036,-1.19473e-05,1.37705e-09,0,12839.8,-46.8096], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 370,
    label = "C6H5_CHCHCHCH2",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {11,S}
3  C u0 p0 c0 {1,B} {7,B} {15,S}
4  C u0 p0 c0 {1,S} {8,D} {16,S}
5  C u0 p0 c0 {2,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {3,B} {6,B} {14,S}
8  C u0 p0 c0 {4,D} {9,S} {17,S}
9  C u0 p0 c0 {8,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4448,0.0397435,8.11411e-05,-1.31369e-07,5.13985e-11,21575.2,19.5916], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[22.9828,0.0285442,-9.55271e-06,1.46932e-09,-8.5091e-14,13955.1,-97.1426], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 371,
    label = "C6H9CYCC5_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {6,S} {13,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22858,0.00176973,0.000123686,-1.52212e-07,5.4804e-11,14108.1,13.9114], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.3395,0.0253575,-8.70127e-06,1.36072e-09,-7.97126e-14,8916.06,-50.7962], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)CsHH, Group:Cs-CsCsCsH, Group:Cs-(Cds-Cds)CsHH, Group:Cds-CdsCsH
Group:Cds-CdsCsH, Group:Cs-CsHHH, Radical:cyclopentene-allyl, !Ring:Cyclopentene""",
    longDesc = 
u"""

""",
)

entry(
    index = 372,
    label = "C6H9_2D_4D_1J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u1 p0 c0 {5,S} {14,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05829,0.0254258,5.3643e-05,-8.24653e-08,3.15888e-11,16875.3,15.753], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.7019,0.0245276,-8.14833e-06,1.24071e-09,-7.12842e-14,12683.5,-45.9633], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-Cds(Cds-Cds)H, Gauche:CsOsCd, Group:Cds-CdsCsH, Gauche:CsOsCd, Group:Cs-(C
ds-Cds)HHH, Gauche:Cs(RRRR), Group:Cds-Cds(Cds-Cds)H, Gauche:CsOsCd, Group:Cds-CdsCs
H, Gauche:CsOsCd, Group:Cs-(Cds-Cds)HHH, Gauche:Cs(RRRR), Radical:C=CC=CCJ""",
    longDesc = 
u"""

""",
)

