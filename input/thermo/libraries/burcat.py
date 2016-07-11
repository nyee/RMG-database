#!/usr/bin/env python
# encoding: utf-8

name = "Burcat_Hydrocarbons"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C9H18",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,D} {5,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {9,S} {24,S} {25,S}
9  C u0 p0 c0 {7,S} {8,S} {26,S} {27,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([288.472,318.908,346.954,372.748,418.112,456.02,524.262],'J/(mol*K)'),
        H298 = (-454.048,'kJ/mol'),
        S298 = (456.581,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "C4H9A",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([131.188,145.885,159.484,172.045,194.269,212.984,247.012],'J/(mol*K)'),
        H298 = (66.2084,'kJ/mol'),
        S298 = (287.512,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C9H12A",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {3,S} {4,D} {7,S}
6  C u0 p0 c0 {1,S} {7,D} {8,S}
7  C u0 p0 c0 {5,S} {6,D} {21,S}
8  C u0 p0 c0 {6,S} {9,D} {19,S}
9  C u0 p0 c0 {4,S} {8,D} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([229.959,254.679,277.381,298.187,334.567,364.699,417.955],'J/(mol*K)'),
        H298 = (-33.4285,'kJ/mol'),
        S298 = (352.871,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "C7H8A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,T}
5  C u0 p0 c0 {3,S} {7,T}
6  C u0 p0 c0 {4,T} {14,S}
7  C u0 p0 c0 {5,T} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([166.012,182.833,198.514,213.114,239.296,261.816,304.711],'J/(mol*K)'),
        H298 = (390.079,'kJ/mol'),
        S298 = (366.028,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C12H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,D} {4,S} {13,S}
2  C u0 p0 c0 {5,D} {6,S} {14,S}
3  C u0 p0 c0 {1,D} {7,S} {15,S}
4  C u0 p0 c0 {1,S} {8,D} {16,S}
5  C u0 p0 c0 {2,D} {9,S} {17,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {3,S} {11,D} {19,S}
8  C u0 p0 c0 {4,D} {11,S} {20,S}
9  C u0 p0 c0 {5,S} {12,D} {21,S}
10 C u1 p0 c0 {6,D} {12,S}
11 C u0 p0 c0 {7,D} {8,S} {12,S}
12 C u0 p0 c0 {9,D} {10,S} {11,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([264.814,286.78,307.028,325.652,358.383,385.662,434.175],'J/(mol*K)'),
        H298 = (405.272,'kJ/mol'),
        S298 = (353.813,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "C12H8",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {5,S} {13,S}
2  C u0 p0 c0 {4,D} {6,S} {14,S}
3  C u0 p0 c0 {1,D} {9,S} {15,S}
4  C u0 p0 c0 {2,D} {9,S} {16,S}
5  C u0 p0 c0 {1,S} {10,D} {17,S}
6  C u0 p0 c0 {2,S} {11,D} {18,S}
7  C u0 p0 c0 {8,D} {10,S} {19,S}
8  C u0 p0 c0 {7,D} {11,S} {20,S}
9  C u0 p0 c0 {3,S} {4,S} {12,D}
10 C u0 p0 c0 {5,D} {7,S} {12,S}
11 C u0 p0 c0 {6,D} {8,S} {12,S}
12 C u0 p0 c0 {9,D} {10,S} {11,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([246.41,270.268,291.993,311.72,345.698,373.194,419.457],'J/(mol*K)'),
        H298 = (240.254,'kJ/mol'),
        S298 = (313.88,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C11H10",
    molecule = 
"""
1  C u0 p0 c0 {9,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {3,D} {6,S} {15,S}
3  C u0 p0 c0 {2,D} {8,S} {16,S}
4  C u0 p0 c0 {5,S} {7,D} {17,S}
5  C u0 p0 c0 {4,S} {9,D} {18,S}
6  C u0 p0 c0 {2,S} {10,D} {19,S}
7  C u0 p0 c0 {4,D} {10,S} {20,S}
8  C u0 p0 c0 {3,S} {11,D} {21,S}
9  C u0 p0 c0 {1,S} {5,D} {11,S}
10 C u0 p0 c0 {6,D} {7,S} {11,S}
11 C u0 p0 c0 {8,D} {9,S} {10,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([261.568,284.42,305.471,324.821,358.792,387.059,437.154],'J/(mol*K)'),
        H298 = (92.6512,'kJ/mol'),
        S298 = (328.059,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C18H12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {11,D}
2  C u0 p0 c0 {1,S} {8,S} {12,D}
3  C u0 p0 c0 {4,S} {9,D} {13,S}
4  C u0 p0 c0 {3,S} {10,D} {14,S}
5  C u0 p0 c0 {6,S} {7,D} {9,S}
6  C u0 p0 c0 {5,S} {8,D} {10,S}
7  C u0 p0 c0 {1,S} {5,D} {27,S}
8  C u0 p0 c0 {2,S} {6,D} {28,S}
9  C u0 p0 c0 {3,D} {5,S} {29,S}
10 C u0 p0 c0 {4,D} {6,S} {30,S}
11 C u0 p0 c0 {1,D} {15,S} {23,S}
12 C u0 p0 c0 {2,D} {16,S} {24,S}
13 C u0 p0 c0 {3,S} {17,D} {25,S}
14 C u0 p0 c0 {4,S} {18,D} {26,S}
15 C u0 p0 c0 {11,S} {16,D} {19,S}
16 C u0 p0 c0 {12,S} {15,D} {20,S}
17 C u0 p0 c0 {13,D} {18,S} {21,S}
18 C u0 p0 c0 {14,D} {17,S} {22,S}
19 H u0 p0 c0 {15,S}
20 H u0 p0 c0 {16,S}
21 H u0 p0 c0 {17,S}
22 H u0 p0 c0 {18,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {13,S}
26 H u0 p0 c0 {14,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([374.745,410.709,443.504,473.329,524.827,566.661,637.612],'J/(mol*K)'),
        H298 = (259.969,'kJ/mol'),
        S298 = (372.467,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C5H8A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {3,S} {4,D} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.464,149.978,164.31,177.523,200.833,220.378,255.599],'J/(mol*K)'),
        H298 = (21.4835,'kJ/mol'),
        S298 = (263.294,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C12H12O1",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {4,S} {14,S}
2  C u0 p0 c0 {1,D} {7,S} {15,S}
3  C u0 p0 c0 {5,D} {6,S} {16,S}
4  C u0 p0 c0 {1,S} {10,D} {17,S}
5  C u0 p0 c0 {3,D} {10,S} {18,S}
6  C u0 p0 c0 {3,S} {11,D} {19,S}
7  C u0 p0 c0 {2,S} {12,D} {20,S}
8  C u0 p0 c0 {9,S} {11,S} {21,S} {22,S}
9  C u0 p0 c0 {8,S} {13,S} {23,S} {24,S}
10 C u0 p0 c0 {4,D} {5,S} {12,S}
11 C u0 p0 c0 {6,D} {8,S} {12,S}
12 C u0 p0 c0 {7,D} {10,S} {11,S}
13 O u0 p2 c0 {9,S} {25,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {13,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([305.599,331.516,355.432,377.455,416.234,448.648,506.65],'J/(mol*K)'),
        H298 = (-76.616,'kJ/mol'),
        S298 = (393.034,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "C6H8A",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([153.043,169.531,184.746,198.756,223.425,244.045,280.949],'J/(mol*K)'),
        H298 = (95.3385,'kJ/mol'),
        S298 = (265.413,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C16H34",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
2  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
3  C u0 p0 c0 {1,S} {5,S} {23,S} {24,S}
4  C u0 p0 c0 {2,S} {6,S} {25,S} {26,S}
5  C u0 p0 c0 {3,S} {7,S} {27,S} {28,S}
6  C u0 p0 c0 {4,S} {8,S} {29,S} {30,S}
7  C u0 p0 c0 {5,S} {9,S} {31,S} {32,S}
8  C u0 p0 c0 {6,S} {10,S} {33,S} {34,S}
9  C u0 p0 c0 {7,S} {11,S} {35,S} {36,S}
10 C u0 p0 c0 {8,S} {12,S} {37,S} {38,S}
11 C u0 p0 c0 {9,S} {13,S} {39,S} {40,S}
12 C u0 p0 c0 {10,S} {14,S} {41,S} {42,S}
13 C u0 p0 c0 {11,S} {15,S} {43,S} {44,S}
14 C u0 p0 c0 {12,S} {16,S} {45,S} {46,S}
15 C u0 p0 c0 {13,S} {16,S} {47,S} {48,S}
16 C u0 p0 c0 {14,S} {15,S} {49,S} {50,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {6,S}
30 H u0 p0 c0 {6,S}
31 H u0 p0 c0 {7,S}
32 H u0 p0 c0 {7,S}
33 H u0 p0 c0 {8,S}
34 H u0 p0 c0 {8,S}
35 H u0 p0 c0 {9,S}
36 H u0 p0 c0 {9,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {10,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {12,S}
42 H u0 p0 c0 {12,S}
43 H u0 p0 c0 {13,S}
44 H u0 p0 c0 {13,S}
45 H u0 p0 c0 {14,S}
46 H u0 p0 c0 {14,S}
47 H u0 p0 c0 {15,S}
48 H u0 p0 c0 {15,S}
49 H u0 p0 c0 {16,S}
50 H u0 p0 c0 {16,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([530.161,587.944,641.2,690.19,776.378,848.436,978.294],'J/(mol*K)'),
        H298 = (-413.149,'kJ/mol'),
        S298 = (694.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "C10H20A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {10,S} {21,S} {22,S}
6  C u0 p0 c0 {8,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
8  C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
9  C u0 p0 c0 {6,S} {10,D} {29,S}
10 C u0 p0 c0 {5,S} {9,D} {30,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([318.856,352.997,384.456,413.389,464.27,506.787,583.316],'J/(mol*K)'),
        H298 = (-159.78,'kJ/mol'),
        S298 = (488.749,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C8H10A",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,D} {6,S}
4  C u0 p0 c0 {2,S} {7,D} {8,S}
5  C u0 p0 c0 {3,D} {7,S} {15,S}
6  C u0 p0 c0 {3,S} {8,D} {16,S}
7  C u0 p0 c0 {4,D} {5,S} {17,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([203.064,224.363,243.791,261.441,291.782,316.102,354.926],'J/(mol*K)'),
        H298 = (-1.64583,'kJ/mol'),
        S298 = (308.699,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "H8C10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,S} {6,D}
3  C u0 p0 c0 {1,D} {8,S} {15,S}
4  C u0 p0 c0 {2,S} {9,D} {16,S}
5  C u0 p0 c0 {1,S} {10,D} {17,S}
6  C u0 p0 c0 {2,D} {10,S} {18,S}
7  C u0 p0 c0 {8,D} {9,S} {11,S}
8  C u0 p0 c0 {3,S} {7,D} {12,S}
9  C u0 p0 c0 {4,D} {7,S} {13,S}
10 C u0 p0 c0 {5,D} {6,S} {14,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {10,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([223.269,241.845,259.064,274.993,303.24,327.091,370.564],'J/(mol*K)'),
        H298 = (259.041,'kJ/mol'),
        S298 = (290.157,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C7H10",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {8,S}
2  C u0 p0 c0 {1,D} {7,S} {9,S}
3  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {6,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {3,S} {5,S} {16,S}
7  C u0 p0 c0 {2,S} {4,S} {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([185.292,205.635,224.41,241.701,272.153,297.618,343.226],'J/(mol*K)'),
        H298 = (71.5573,'kJ/mol'),
        S298 = (264.083,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C7H12",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([183.832,207.32,229,248.968,284.143,313.564,366.291],'J/(mol*K)'),
        H298 = (-72.7414,'kJ/mol'),
        S298 = (264.707,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C4H9",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([128.353,143.749,157.991,171.141,194.393,213.958,249.464],'J/(mol*K)'),
        H298 = (73.6494,'kJ/mol'),
        S298 = (289.314,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C7H15",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {3,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {6,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([225.91,251.714,275.519,297.431,335.994,368.205,425.785],'J/(mol*K)'),
        H298 = (-9.80467,'kJ/mol'),
        S298 = (415.681,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C7H16",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {2,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([249.227,272.352,293.979,314.182,350.604,382.177,443.271],'J/(mol*K)'),
        H298 = (-207.903,'kJ/mol'),
        S298 = (382.626,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "C10H7O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {12,S}
2  C u0 p0 c0 {1,D} {4,S} {13,S}
3  C u0 p0 c0 {1,S} {8,D} {14,S}
4  C u0 p0 c0 {2,S} {9,D} {15,S}
5  C u0 p0 c0 {6,D} {8,S} {16,S}
6  C u0 p0 c0 {5,D} {10,S} {17,S}
7  C u0 p0 c0 {9,S} {10,D} {18,S}
8  C u0 p0 c0 {3,D} {5,S} {9,S}
9  C u0 p0 c0 {4,D} {7,S} {8,S}
10 C u0 p0 c0 {6,S} {7,D} {11,S}
11 O u1 p2 c0 {10,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([238.217,256.201,272.788,288.052,314.902,337.312,377.291],'J/(mol*K)'),
        H298 = (95.8977,'kJ/mol'),
        S298 = (328.054,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C16H10",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {4,S} {17,S}
2  C u0 p0 c0 {5,D} {6,S} {18,S}
3  C u0 p0 c0 {1,D} {11,S} {19,S}
4  C u0 p0 c0 {1,S} {12,D} {20,S}
5  C u0 p0 c0 {2,D} {13,S} {21,S}
6  C u0 p0 c0 {2,S} {14,D} {22,S}
7  C u0 p0 c0 {9,D} {11,S} {23,S}
8  C u0 p0 c0 {10,D} {12,S} {24,S}
9  C u0 p0 c0 {7,D} {13,S} {25,S}
10 C u0 p0 c0 {8,D} {14,S} {26,S}
11 C u0 p0 c0 {3,S} {7,S} {15,D}
12 C u0 p0 c0 {4,D} {8,S} {15,S}
13 C u0 p0 c0 {5,S} {9,S} {16,D}
14 C u0 p0 c0 {6,D} {10,S} {16,S}
15 C u0 p0 c0 {11,D} {12,S} {16,S}
16 C u0 p0 c0 {13,D} {14,S} {15,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([343.911,371.002,395.968,418.923,459.244,492.822,552.436],'J/(mol*K)'),
        H298 = (195.061,'kJ/mol'),
        S298 = (337.315,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C5H7A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {2,S} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.535,135.879,149.139,161.371,182.976,201.121,233.918],'J/(mol*K)'),
        H298 = (214.458,'kJ/mol'),
        S298 = (269.113,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C4H10",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([136.269,152.777,168.031,182.099,206.927,227.754,265.311],'J/(mol*K)'),
        H298 = (-135.171,'kJ/mol'),
        S298 = (288.936,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C5H5O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.237,152.904,162.743,171.8,187.738,201.048,224.822],'J/(mol*K)'),
        H298 = (48.7216,'kJ/mol'),
        S298 = (282.224,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C7H6O1",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {9,S}
2  C u0 p0 c0 {1,D} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {7,D} {12,S}
5  C u0 p0 c0 {3,D} {7,S} {13,S}
6  C u0 p0 c0 {7,S} {8,D} {14,S}
7  C u0 p0 c0 {4,D} {5,S} {6,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([170.149,185.987,200.449,213.622,236.423,255.013,286.771],'J/(mol*K)'),
        H298 = (-49.0564,'kJ/mol'),
        S298 = (307.707,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "H4C3",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([75.5059,82.7831,89.5136,95.7263,106.709,115.945,132.687],'J/(mol*K)'),
        H298 = (181.967,'kJ/mol'),
        S298 = (240.515,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C4H6A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {2,S} {3,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.703,117.252,127.915,137.74,155.058,169.556,195.593],'J/(mol*K)'),
        H298 = (147.179,'kJ/mol'),
        S298 = (240.483,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C10H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {8,D} {11,S} {12,S}
2  C u0 p0 c0 {3,D} {4,S} {13,S}
3  C u0 p0 c0 {2,D} {5,S} {14,S}
4  C u0 p0 c0 {2,S} {9,D} {15,S}
5  C u0 p0 c0 {3,S} {10,D} {16,S}
6  C u1 p0 c0 {8,S} {9,S} {17,S}
7  C u0 p0 c0 {8,S} {10,S} {18,S} {19,S}
8  C u0 p0 c0 {1,D} {6,S} {7,S}
9  C u0 p0 c0 {4,D} {6,S} {10,S}
10 C u0 p0 c0 {5,D} {7,S} {9,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([234.859,255.262,274.076,291.386,321.825,347.215,392.445],'J/(mol*K)'),
        H298 = (318.029,'kJ/mol'),
        S298 = (319.103,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C4H8O4",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {8,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {2,S} {4,S}
8  O u0 p2 c0 {3,S} {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([176.729,197.315,216.114,233.236,262.875,287.044,328.368],'J/(mol*K)'),
        H298 = (-634.2,'kJ/mol'),
        S298 = (308.545,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C4H8O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([150.06,166.977,182.58,196.94,222.203,243.292,280.924],'J/(mol*K)'),
        H298 = (-328.373,'kJ/mol'),
        S298 = (263.228,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C4H8O1",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.47,152.93,166.308,178.661,200.51,218.899,252.294],'J/(mol*K)'),
        H298 = (-169.98,'kJ/mol'),
        S298 = (296.149,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C5H5O1A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.589,135.659,148.468,160.09,180.073,196.18,222.963],'J/(mol*K)'),
        H298 = (214.087,'kJ/mol'),
        S298 = (285.015,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C6H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([223.703,241.958,259.193,275.46,305.296,331.858,386.303],'J/(mol*K)'),
        H298 = (-187.038,'kJ/mol'),
        S298 = (343.807,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C6H13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {4,S} {18,S} {19,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([193.598,215.808,236.302,255.17,288.389,316.151,365.839],'J/(mol*K)'),
        H298 = (13.0433,'kJ/mol'),
        S298 = (380.932,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C6H12",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,D} {17,S}
6  C u0 p0 c0 {2,S} {5,D} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
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
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([176.006,197.304,216.977,235.109,267.083,293.87,342.02],'J/(mol*K)'),
        H298 = (-61.7992,'kJ/mol'),
        S298 = (340.317,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C6H11",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {5,S} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([168.781,190.304,210.184,228.51,260.835,287.928,336.695],'J/(mol*K)'),
        H298 = (60.7365,'kJ/mol'),
        S298 = (283.543,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C6H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {15,S}
6  C u0 p0 c0 {4,S} {5,D} {16,S}
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([167.08,186.819,205.036,221.814,251.361,276.068,320.318],'J/(mol*K)'),
        H298 = (-20.084,'kJ/mol'),
        S298 = (275.69,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([86.7076,97.149,106.8,115.702,131.423,144.621,168.462],'J/(mol*K)'),
        H298 = (14.3997,'kJ/mol'),
        S298 = (254.18,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C3H7",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {3,S} {4,S} {5,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([86.6648,98.8484,110.116,120.515,138.896,154.349,182.348],'J/(mol*K)'),
        H298 = (84.4275,'kJ/mol'),
        S298 = (277.404,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C3H4",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([77.4674,84.6081,91.2105,97.3029,108.067,117.113,133.484],'J/(mol*K)'),
        H298 = (186.748,'kJ/mol'),
        S298 = (233.965,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C3H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([87.6545,96.0665,103.846,111.027,123.719,134.391,153.732],'J/(mol*K)'),
        H298 = (158.342,'kJ/mol'),
        S298 = (246.882,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C3H2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([61.9739,66.1512,70.0089,73.5637,79.8309,85.0796,94.5123],'J/(mol*K)'),
        H298 = (473.04,'kJ/mol'),
        S298 = (227.211,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C3H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,T} {4,S}
2 C u1 p0 c0 {3,S} {5,S} {6,S}
3 C u0 p0 c0 {1,T} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([76.4805,81.3857,85.9269,90.123,97.5533,103.818,115.236],'J/(mol*K)'),
        H298 = (343.826,'kJ/mol'),
        S298 = (251.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([101.611,114.816,127.02,138.277,158.155,174.842,204.979],'J/(mol*K)'),
        H298 = (-111.709,'kJ/mol'),
        S298 = (254.639,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C10H8O1",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {12,S}
2  C u0 p0 c0 {1,D} {4,S} {13,S}
3  C u0 p0 c0 {1,S} {8,D} {14,S}
4  C u0 p0 c0 {2,S} {9,D} {15,S}
5  C u0 p0 c0 {6,D} {8,S} {16,S}
6  C u0 p0 c0 {5,D} {10,S} {17,S}
7  C u0 p0 c0 {9,S} {10,D} {18,S}
8  C u0 p0 c0 {3,D} {5,S} {9,S}
9  C u0 p0 c0 {4,D} {7,S} {8,S}
10 C u0 p0 c0 {6,S} {7,D} {11,S}
11 O u0 p2 c0 {10,S} {19,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([243.032,262.756,280.934,297.65,327.017,351.479,394.936],'J/(mol*K)'),
        H298 = (-50.559,'kJ/mol'),
        S298 = (323.706,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C12H12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {10,S} {16,S} {17,S}
3  C u0 p0 c0 {4,D} {6,S} {18,S}
4  C u0 p0 c0 {3,D} {9,S} {19,S}
5  C u0 p0 c0 {7,S} {8,D} {20,S}
6  C u0 p0 c0 {3,S} {11,D} {21,S}
7  C u0 p0 c0 {5,S} {10,D} {22,S}
8  C u0 p0 c0 {5,D} {11,S} {23,S}
9  C u0 p0 c0 {4,S} {12,D} {24,S}
10 C u0 p0 c0 {2,S} {7,D} {12,S}
11 C u0 p0 c0 {6,D} {8,S} {12,S}
12 C u0 p0 c0 {9,D} {10,S} {11,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([301.191,326.849,350.484,372.206,410.332,442.042,498.181],'J/(mol*K)'),
        H298 = (69.9167,'kJ/mol'),
        S298 = (344.945,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C12H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u0 p0 c0 {1,S} {5,D} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {9,S} {17,S}
5  C u0 p0 c0 {2,D} {11,S} {18,S}
6  C u0 p0 c0 {3,S} {11,D} {19,S}
7  C u0 p0 c0 {1,D} {10,S} {20,S}
8  C u0 p0 c0 {2,S} {12,D} {13,S}
9  C u0 p0 c0 {4,S} {10,D} {14,S}
10 C u0 p0 c0 {7,S} {9,D} {15,S}
11 C u0 p0 c0 {5,S} {6,D} {16,S}
12 C u0 p0 c0 {8,D} {21,S} {22,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {12,S}
22 H u0 p0 c0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([277.161,300.143,321.349,340.873,375.245,403.966,455.317],'J/(mol*K)'),
        H298 = (192.873,'kJ/mol'),
        S298 = (349.937,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C14H10A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {19,S}
6  C u0 p0 c0 {4,D} {12,S} {20,S}
7  C u0 p0 c0 {1,D} {13,S} {21,S}
8  C u0 p0 c0 {2,D} {14,S} {22,S}
9  C u0 p0 c0 {3,S} {10,D} {23,S}
10 C u0 p0 c0 {4,S} {9,D} {24,S}
11 C u0 p0 c0 {5,S} {13,D} {15,S}
12 C u0 p0 c0 {6,S} {14,D} {16,S}
13 C u0 p0 c0 {7,S} {11,D} {17,S}
14 C u0 p0 c0 {8,S} {12,D} {18,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {13,S}
18 H u0 p0 c0 {14,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([310.006,335.304,358.631,380.094,417.835,449.318,505.417],'J/(mol*K)'),
        H298 = (180.443,'kJ/mol'),
        S298 = (333.536,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C7H7A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u1 p0 c0 {1,S} {5,S} {11,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {5,D} {6,S} {8,S}
5  C u0 p0 c0 {2,S} {4,D} {9,S}
6  C u0 p0 c0 {3,D} {4,S} {10,S}
7  C u0 p0 c0 {1,D} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([173.827,188.457,201.939,214.337,236.117,254.257,286.469],'J/(mol*K)'),
        H298 = (193.962,'kJ/mol'),
        S298 = (286.244,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C10H16",
    molecule = 
"""
1  C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
2  C u0 p0 c0 {12,S} {18,S} {19,S} {20,S}
3  C u0 p0 c0 {13,S} {21,S} {22,S} {23,S}
4  C u0 p0 c0 {14,S} {24,S} {25,S} {26,S}
5  C u0 p0 c0 {6,S} {7,S} {27,S} {28,S}
6  C u0 p0 c0 {5,S} {13,S} {29,S} {30,S}
7  C u0 p0 c0 {5,S} {14,S} {31,S} {32,S}
8  C u0 p0 c0 {9,S} {11,S} {33,S} {34,S}
9  C u0 p0 c0 {8,S} {12,S} {35,S} {36,S}
10 C u0 p0 c0 {11,S} {12,S} {37,S} {38,S}
11 C u0 p0 c0 {1,S} {8,S} {10,S} {13,S}
12 C u0 p0 c0 {2,S} {9,S} {10,S} {14,S}
13 C u0 p0 c0 {3,S} {6,S} {11,S} {14,S}
14 C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {6,S}
30 H u0 p0 c0 {6,S}
31 H u0 p0 c0 {7,S}
32 H u0 p0 c0 {7,S}
33 H u0 p0 c0 {8,S}
34 H u0 p0 c0 {8,S}
35 H u0 p0 c0 {9,S}
36 H u0 p0 c0 {9,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([282.24,314.064,343.445,370.513,418.212,458.133,529.771],'J/(mol*K)'),
        H298 = (-116.165,'kJ/mol'),
        S298 = (289.208,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C4H3A",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([91.0383,96.8517,102.233,107.205,116.006,123.424,136.936],'J/(mol*K)'),
        H298 = (498.995,'kJ/mol'),
        S298 = (298.873,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "C10H10A",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {7,D}
4  C u0 p0 c0 {2,S} {5,S} {6,D}
5  C u0 p0 c0 {3,S} {4,S} {8,D}
6  C u0 p0 c0 {1,S} {4,D} {16,S}
7  C u0 p0 c0 {3,D} {9,S} {19,S}
8  C u0 p0 c0 {5,D} {10,S} {20,S}
9  C u0 p0 c0 {7,S} {10,D} {17,S}
10 C u0 p0 c0 {8,S} {9,D} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([233.094,255.362,275.921,294.863,328.246,356.19,406.352],'J/(mol*K)'),
        H298 = (153.773,'kJ/mol'),
        S298 = (320.437,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C5H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.658,155.548,169.274,181.897,204.077,222.556,255.374],'J/(mol*K)'),
        H298 = (73.0194,'kJ/mol'),
        S298 = (293.283,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C11H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {9,D} {12,S} {13,S}
2  C u0 p0 c0 {3,D} {6,S} {14,S}
3  C u0 p0 c0 {2,D} {8,S} {15,S}
4  C u0 p0 c0 {5,D} {7,S} {16,S}
5  C u0 p0 c0 {4,D} {9,S} {17,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u1 p0 c0 {4,S} {10,S} {19,S}
8  C u0 p0 c0 {3,S} {11,D} {20,S}
9  C u0 p0 c0 {1,D} {5,S} {11,S}
10 C u0 p0 c0 {6,D} {7,S} {11,S}
11 C u0 p0 c0 {8,D} {9,S} {10,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([254.974,275.772,294.967,312.644,343.777,369.809,416.435],'J/(mol*K)'),
        H298 = (252.177,'kJ/mol'),
        S298 = (331.393,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C5H12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([190.618,205.945,220.439,234.143,259.357,281.922,328.736],'J/(mol*K)'),
        H298 = (-164.894,'kJ/mol'),
        S298 = (309.293,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "C5H10",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([155.943,172.181,187.216,201.112,225.735,246.523,284.574],'J/(mol*K)'),
        H298 = (-32.5572,'kJ/mol'),
        S298 = (321.612,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C5H11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
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
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([160.291,179.144,196.529,212.525,240.658,264.133,306.017],'J/(mol*K)'),
        H298 = (36.2204,'kJ/mol'),
        S298 = (346.892,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "C6H14A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([188.026,215.498,240.889,264.316,305.731,340.61,404.409],'J/(mol*K)'),
        H298 = (-187.623,'kJ/mol'),
        S298 = (341.238,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C6H6A",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([145.893,157.281,167.812,177.53,194.702,209.136,235.27],'J/(mol*K)'),
        H298 = (410.007,'kJ/mol'),
        S298 = (320.457,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C11H24",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {6,S} {20,S} {21,S}
5  C u0 p0 c0 {3,S} {7,S} {22,S} {23,S}
6  C u0 p0 c0 {4,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {5,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {6,S} {10,S} {28,S} {29,S}
9  C u0 p0 c0 {7,S} {11,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {11,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {10,S} {34,S} {35,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([397.865,430.801,461.372,489.7,540.103,582.929,662.395],'J/(mol*K)'),
        H298 = (-304.124,'kJ/mol'),
        S298 = (508.441,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C3H6A",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.7363,99.337,109.137,118.177,134.145,147.555,171.797],'J/(mol*K)'),
        H298 = (45.6972,'kJ/mol'),
        S298 = (220.231,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C4H8A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.969,125.546,140.699,154.515,178.475,198.073,231.824],'J/(mol*K)'),
        H298 = (19.2487,'kJ/mol'),
        S298 = (243.731,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C8H18A",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {24,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([262.676,296.463,327.965,357.291,409.838,454.922,539.968],'J/(mol*K)'),
        H298 = (-240.773,'kJ/mol'),
        S298 = (384.961,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C8H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {3,S} {4,S} {21,S}
8  C u0 p0 c0 {2,S} {5,S} {6,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([216.5,245.074,271.463,295.783,338.663,374.581,439.153],'J/(mol*K)'),
        H298 = (-120.846,'kJ/mol'),
        S298 = (278.386,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C7H12A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {7,D} {18,S}
7  C u0 p0 c0 {5,S} {6,D} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([198.676,222.414,244.321,264.494,300.017,329.713,382.872],'J/(mol*K)'),
        H298 = (-27.9564,'kJ/mol'),
        S298 = (282.16,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C8H16",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {8,D} {22,S}
8  C u0 p0 c0 {7,D} {23,S} {24,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([275.445,296.742,316.634,335.193,368.599,397.507,453.4],'J/(mol*K)'),
        H298 = (-106.769,'kJ/mol'),
        S298 = (412.254,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C7H16A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([247.634,273.218,296.782,318.443,356.506,388.275,445.329],'J/(mol*K)'),
        H298 = (-229.306,'kJ/mol'),
        S298 = (351.85,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C14H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,D} {7,S}
2  C u0 p0 c0 {1,S} {6,D} {8,S}
3  C u0 p0 c0 {4,S} {5,S} {9,D}
4  C u0 p0 c0 {3,S} {6,S} {10,D}
5  C u0 p0 c0 {1,D} {3,S} {23,S}
6  C u0 p0 c0 {2,D} {4,S} {24,S}
7  C u0 p0 c0 {1,S} {11,D} {19,S}
8  C u0 p0 c0 {2,S} {12,D} {20,S}
9  C u0 p0 c0 {3,D} {13,S} {21,S}
10 C u0 p0 c0 {4,D} {14,S} {22,S}
11 C u0 p0 c0 {7,D} {12,S} {15,S}
12 C u0 p0 c0 {8,D} {11,S} {16,S}
13 C u0 p0 c0 {9,S} {14,D} {17,S}
14 C u0 p0 c0 {10,S} {13,D} {18,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {13,S}
18 H u0 p0 c0 {14,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([309.761,335.073,358.414,379.89,417.655,449.159,505.301],'J/(mol*K)'),
        H298 = (202.963,'kJ/mol'),
        S298 = (330.542,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C14H12",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {4,S} {15,S}
2  C u0 p0 c0 {5,D} {6,S} {16,S}
3  C u0 p0 c0 {1,D} {7,S} {17,S}
4  C u0 p0 c0 {1,S} {8,D} {18,S}
5  C u0 p0 c0 {2,D} {9,S} {19,S}
6  C u0 p0 c0 {2,S} {10,D} {20,S}
7  C u0 p0 c0 {3,S} {13,D} {21,S}
8  C u0 p0 c0 {4,D} {13,S} {22,S}
9  C u0 p0 c0 {5,S} {14,D} {23,S}
10 C u0 p0 c0 {6,D} {14,S} {24,S}
11 C u0 p0 c0 {12,D} {13,S} {25,S}
12 C u0 p0 c0 {11,D} {14,S} {26,S}
13 C u0 p0 c0 {7,D} {8,S} {11,S}
14 C u0 p0 c0 {9,D} {10,S} {12,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([324.699,351.734,376.664,399.603,439.943,473.599,533.587],'J/(mol*K)'),
        H298 = (196.647,'kJ/mol'),
        S298 = (386.987,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C8H18",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {3,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([273.344,301.838,328.223,352.602,395.743,432.034,497.511],'J/(mol*K)'),
        H298 = (-228.681,'kJ/mol'),
        S298 = (421.983,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C6H4O2",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {9,S}
2  C u0 p0 c0 {1,D} {6,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  C u0 p0 c0 {1,S} {3,S} {7,D}
6  C u0 p0 c0 {2,S} {4,S} {8,D}
7  O u0 p2 c0 {5,D}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([160.167,171.698,182.323,192.093,209.253,223.542,248.908],'J/(mol*K)'),
        H298 = (-134.754,'kJ/mol'),
        S298 = (306.31,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C6H8",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([149.13,165.147,179.95,193.602,217.704,237.932,274.445],'J/(mol*K)'),
        H298 = (100.048,'kJ/mol'),
        S298 = (283.114,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C7H16O1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  O u0 p2 c0 {7,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([253.923,280.593,305.166,327.762,367.492,400.687,460.451],'J/(mol*K)'),
        H298 = (-359.19,'kJ/mol'),
        S298 = (437.738,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C7H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {7,S} {12,S}
6  C u0 p0 c0 {4,D} {7,S} {13,S}
7  C u1 p0 c0 {5,S} {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([166.743,181.644,195.411,208.103,230.496,249.273,283.101],'J/(mol*K)'),
        H298 = (268.13,'kJ/mol'),
        S298 = (303.871,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C12H8O2",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {15,S}
2  C u0 p0 c0 {1,D} {6,S} {16,S}
3  C u0 p0 c0 {4,D} {7,S} {17,S}
4  C u0 p0 c0 {3,D} {8,S} {18,S}
5  C u0 p0 c0 {1,S} {9,D} {19,S}
6  C u0 p0 c0 {2,S} {10,D} {20,S}
7  C u0 p0 c0 {3,S} {11,D} {21,S}
8  C u0 p0 c0 {4,S} {12,D} {22,S}
9  C u0 p0 c0 {5,D} {10,S} {13,S}
10 C u0 p0 c0 {6,D} {9,S} {14,S}
11 C u0 p0 c0 {7,D} {12,S} {13,S}
12 C u0 p0 c0 {8,D} {11,S} {14,S}
13 O u0 p2 c0 {9,S} {11,S}
14 O u0 p2 c0 {10,S} {12,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([294.779,317.059,337.592,356.474,389.646,417.279,466.371],'J/(mol*K)'),
        H298 = (-75.0787,'kJ/mol'),
        S298 = (339.446,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C6H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,T} {7,S}
2 C u0 p0 c0 {4,T} {8,S}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,T} {6,S}
5 C u0 p0 c0 {3,S} {6,D} {9,S}
6 C u1 p0 c0 {4,S} {5,D}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([127.034,134.353,141.113,147.341,158.323,167.521,184.055],'J/(mol*K)'),
        H298 = (676.662,'kJ/mol'),
        S298 = (307.023,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C7H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {6,S} {14,S}
4  C u0 p0 c0 {2,S} {7,D} {15,S}
5  C u0 p0 c0 {6,D} {7,S} {11,S}
6  C u0 p0 c0 {3,S} {5,D} {12,S}
7  C u0 p0 c0 {4,D} {5,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([167.264,184.291,200.007,214.481,239.975,261.296,299.495],'J/(mol*K)'),
        H298 = (35.6007,'kJ/mol'),
        S298 = (287.097,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "C5H6O1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  O u0 p2 c0 {1,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([143.272,155.519,166.829,177.251,195.627,211.017,238.677],'J/(mol*K)'),
        H298 = (-3.33695,'kJ/mol'),
        S298 = (278.859,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "C6H6",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.451,151.664,163.859,175.09,194.87,211.41,241.035],'J/(mol*K)'),
        H298 = (70.3776,'kJ/mol'),
        S298 = (240.608,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C6H4",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {6,D}
6  C u0 p0 c0 {4,D} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.967,132.978,142.219,150.731,165.728,178.275,200.776],'J/(mol*K)'),
        H298 = (451.442,'kJ/mol'),
        S298 = (261.042,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "H14C6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([196.956,222.14,245.439,266.961,305.081,337.284,396.614],'J/(mol*K)'),
        H298 = (-186.869,'kJ/mol'),
        S298 = (352.901,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "O1C5H6A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {5,D} {9,S}
5  C u0 p0 c0 {3,S} {4,D} {11,S}
6  O u0 p2 c0 {3,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([147.457,159.33,170.293,180.396,198.208,213.124,239.932],'J/(mol*K)'),
        H298 = (-38.2422,'kJ/mol'),
        S298 = (279.152,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "C4H6O1",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.561,130.445,142.224,152.965,171.6,186.852,213.169],'J/(mol*K)'),
        H298 = (-118.06,'kJ/mol'),
        S298 = (263.014,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "C8H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {7,S} {17,S}
5  C u0 p0 c0 {3,S} {8,D} {18,S}
6  C u0 p0 c0 {7,D} {8,S} {14,S}
7  C u0 p0 c0 {4,S} {6,D} {15,S}
8  C u0 p0 c0 {5,D} {6,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([202.859,223.534,242.623,260.213,291.215,317.169,363.761],'J/(mol*K)'),
        H298 = (13.5249,'kJ/mol'),
        S298 = (316.67,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C3H8O1",
    molecule = 
"""
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
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([118.009,131.503,143.98,155.494,175.84,192.937,223.885],'J/(mol*K)'),
        H298 = (-263.234,'kJ/mol'),
        S298 = (305.326,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C3H8O2",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  O u0 p2 c0 {1,S} {3,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.148,140.909,154.541,167.104,189.249,207.789,241.061],'J/(mol*K)'),
        H298 = (-352.762,'kJ/mol'),
        S298 = (332.093,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "C3H5A",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([85.6585,94.3982,102.473,109.918,123.056,134.073,153.93],'J/(mol*K)'),
        H298 = (273.239,'kJ/mol'),
        S298 = (236.286,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C14H14",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {4,S} {15,S}
2  C u0 p0 c0 {5,D} {6,S} {16,S}
3  C u0 p0 c0 {1,D} {7,S} {17,S}
4  C u0 p0 c0 {1,S} {8,D} {18,S}
5  C u0 p0 c0 {2,D} {9,S} {19,S}
6  C u0 p0 c0 {2,S} {10,D} {20,S}
7  C u0 p0 c0 {3,S} {13,D} {21,S}
8  C u0 p0 c0 {4,D} {13,S} {22,S}
9  C u0 p0 c0 {5,S} {14,D} {23,S}
10 C u0 p0 c0 {6,D} {14,S} {24,S}
11 C u0 p0 c0 {12,S} {13,S} {25,S} {26,S}
12 C u0 p0 c0 {11,S} {14,S} {27,S} {28,S}
13 C u0 p0 c0 {7,D} {8,S} {11,S}
14 C u0 p0 c0 {9,D} {10,S} {12,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([326.008,355.956,383.613,409.1,454.035,491.672,559.322],'J/(mol*K)'),
        H298 = (108.517,'kJ/mol'),
        S298 = (415.254,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C4H5A",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([106.837,115.481,123.47,130.839,143.849,154.769,174.49],'J/(mol*K)'),
        H298 = (310.865,'kJ/mol'),
        S298 = (280.995,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C22H14A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {11,D}
2  C u0 p0 c0 {1,S} {8,S} {12,D}
3  C u0 p0 c0 {5,S} {9,S} {13,D}
4  C u0 p0 c0 {6,S} {10,S} {14,D}
5  C u0 p0 c0 {3,S} {11,S} {15,D}
6  C u0 p0 c0 {4,S} {12,S} {16,D}
7  C u0 p0 c0 {1,S} {9,D} {17,S}
8  C u0 p0 c0 {2,S} {10,D} {18,S}
9  C u0 p0 c0 {3,S} {7,D} {33,S}
10 C u0 p0 c0 {4,S} {8,D} {34,S}
11 C u0 p0 c0 {1,D} {5,S} {35,S}
12 C u0 p0 c0 {2,D} {6,S} {36,S}
13 C u0 p0 c0 {3,D} {19,S} {27,S}
14 C u0 p0 c0 {4,D} {20,S} {28,S}
15 C u0 p0 c0 {5,D} {21,S} {29,S}
16 C u0 p0 c0 {6,D} {22,S} {30,S}
17 C u0 p0 c0 {7,S} {18,D} {31,S}
18 C u0 p0 c0 {8,S} {17,D} {32,S}
19 C u0 p0 c0 {13,S} {21,D} {23,S}
20 C u0 p0 c0 {14,S} {22,D} {24,S}
21 C u0 p0 c0 {15,S} {19,D} {25,S}
22 C u0 p0 c0 {16,S} {20,D} {26,S}
23 H u0 p0 c0 {19,S}
24 H u0 p0 c0 {20,S}
25 H u0 p0 c0 {21,S}
26 H u0 p0 c0 {22,S}
27 H u0 p0 c0 {13,S}
28 H u0 p0 c0 {14,S}
29 H u0 p0 c0 {15,S}
30 H u0 p0 c0 {16,S}
31 H u0 p0 c0 {17,S}
32 H u0 p0 c0 {18,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([455.139,498.119,537.309,572.946,634.47,684.436,769.135],'J/(mol*K)'),
        H298 = (308.324,'kJ/mol'),
        S298 = (416.779,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "C6H6O1",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  C u0 p0 c0 {4,D} {5,S} {7,S}
7  O u0 p2 c0 {6,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([162.3,175.042,186.811,197.657,216.785,232.811,261.637],'J/(mol*K)'),
        H298 = (-108.807,'kJ/mol'),
        S298 = (286.659,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C6H12A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([189.823,212.569,233.531,252.804,286.659,314.854,364.921],'J/(mol*K)'),
        H298 = (-144.613,'kJ/mol'),
        S298 = (249.774,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C5H12A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
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
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([156.239,181.567,205.053,226.789,265.375,298.024,357.913],'J/(mol*K)'),
        H298 = (-176.388,'kJ/mol'),
        S298 = (287.116,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C3H6O1",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([86.5258,103.122,118.331,132.235,156.447,176.364,210.998],'J/(mol*K)'),
        H298 = (-194.383,'kJ/mol'),
        S298 = (299.518,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C4",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([57.7873,60.9899,63.9811,66.7704,71.7787,76.0844,84.2042],'J/(mol*K)'),
        H298 = (1034.16,'kJ/mol'),
        S298 = (253.301,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "C7H14A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {6,S} {20,S} {21,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([215.638,242.376,267.052,289.777,329.797,363.258,423.176],'J/(mol*K)'),
        H298 = (-138.388,'kJ/mol'),
        S298 = (291.063,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "C5H9A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u1 p0 c0 {4,D} {14,S}
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([153.261,168.239,182.078,194.838,217.354,236.236,270.254],'J/(mol*K)'),
        H298 = (208.175,'kJ/mol'),
        S298 = (310.659,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C3O2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 C u0 p0 c0 {1,D} {4,D}
3 C u0 p0 c0 {1,D} {5,D}
4 O u0 p2 c0 {2,D}
5 O u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([81.0789,84.1196,86.9165,89.4829,93.9759,97.6983,104.232],'J/(mol*K)'),
        H298 = (-96.507,'kJ/mol'),
        S298 = (270.255,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C3H4A",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([77.3911,84.59,91.2433,97.3799,108.214,117.308,133.726],'J/(mol*K)'),
        H298 = (271.701,'kJ/mol'),
        S298 = (231.281,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "H8C4",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([101.749,119.546,135.667,150.225,175.093,194.984,227.844],'J/(mol*K)'),
        H298 = (-20.5593,'kJ/mol'),
        S298 = (289.022,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C8H6O2",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {11,S}
2  C u0 p0 c0 {1,D} {4,S} {12,S}
3  C u0 p0 c0 {1,S} {7,D} {13,S}
4  C u0 p0 c0 {2,S} {8,D} {14,S}
5  C u0 p0 c0 {6,D} {9,S} {15,S}
6  C u0 p0 c0 {5,D} {10,S} {16,S}
7  C u0 p0 c0 {3,D} {8,S} {9,S}
8  C u0 p0 c0 {4,D} {7,S} {10,S}
9  O u0 p2 c0 {5,S} {7,S}
10 O u0 p2 c0 {6,S} {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([208.65,224.612,239.341,252.901,276.774,296.723,332.406],'J/(mol*K)'),
        H298 = (-88.2792,'kJ/mol'),
        S298 = (308.181,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "H8C6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([154.997,171.272,186.293,200.126,224.487,244.855,281.331],'J/(mol*K)'),
        H298 = (92.402,'kJ/mol'),
        S298 = (271.873,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C9H12",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {7,D} {8,S}
5  C u0 p0 c0 {2,S} {7,S} {9,D}
6  C u0 p0 c0 {3,S} {8,D} {9,S}
7  C u0 p0 c0 {4,D} {5,S} {19,S}
8  C u0 p0 c0 {4,S} {6,D} {20,S}
9  C u0 p0 c0 {5,D} {6,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([227.464,252.468,275.428,296.465,333.236,363.677,417.418],'J/(mol*K)'),
        H298 = (-36.3474,'kJ/mol'),
        S298 = (340.564,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C9H10",
    molecule = 
"""
1  C u0 p0 c0 {8,D} {10,S} {11,S}
2  C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,D} {5,S} {15,S}
4  C u0 p0 c0 {3,D} {6,S} {16,S}
5  C u0 p0 c0 {3,S} {7,D} {17,S}
6  C u0 p0 c0 {4,S} {9,D} {18,S}
7  C u0 p0 c0 {5,D} {9,S} {19,S}
8  C u0 p0 c0 {1,D} {2,S} {9,S}
9  C u0 p0 c0 {6,D} {7,S} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([227.222,247.079,265.335,282.084,311.426,335.797,379.122],'J/(mol*K)'),
        H298 = (93.6341,'kJ/mol'),
        S298 = (340.404,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C3H4O1",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89.3457,97.4829,104.996,111.919,124.121,134.337,152.676],'J/(mol*K)'),
        H298 = (-74.0517,'kJ/mol'),
        S298 = (283.546,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C11H8O1",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {13,S}
2  C u0 p0 c0 {1,D} {4,S} {14,S}
3  C u0 p0 c0 {1,S} {10,D} {15,S}
4  C u0 p0 c0 {2,S} {11,D} {16,S}
5  C u0 p0 c0 {6,D} {9,S} {17,S}
6  C u0 p0 c0 {5,D} {10,S} {18,S}
7  C u0 p0 c0 {9,D} {11,S} {19,S}
8  C u0 p0 c0 {9,S} {12,D} {20,S}
9  C u0 p0 c0 {5,S} {7,D} {8,S}
10 C u0 p0 c0 {3,D} {6,S} {11,S}
11 C u0 p0 c0 {4,D} {7,S} {10,S}
12 O u0 p2 c0 {8,D}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([272.103,292.072,310.445,327.308,356.844,381.331,424.382],'J/(mol*K)'),
        H298 = (5.80335,'kJ/mol'),
        S298 = (327.571,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C3H4O2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([114.248,121.955,129.072,135.631,147.195,156.881,174.279],'J/(mol*K)'),
        H298 = (-333.468,'kJ/mol'),
        S298 = (296.509,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C10H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {6,D}
4  C u0 p0 c0 {3,S} {7,S} {8,D}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u0 p0 c0 {3,D} {10,S} {19,S}
7  C u0 p0 c0 {4,S} {5,D} {20,S}
8  C u0 p0 c0 {4,D} {9,S} {18,S}
9  C u0 p0 c0 {8,S} {10,D} {16,S}
10 C u0 p0 c0 {6,S} {9,D} {17,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([238.328,260.72,281.383,300.409,333.91,361.911,412.018],'J/(mol*K)'),
        H298 = (96.2386,'kJ/mol'),
        S298 = (311.657,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C18H12A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u0 p0 c0 {1,S} {5,S} {9,D}
4  C u0 p0 c0 {2,S} {6,S} {10,D}
5  C u0 p0 c0 {3,S} {6,S} {11,D}
6  C u0 p0 c0 {4,S} {5,S} {12,D}
7  C u0 p0 c0 {1,D} {13,S} {25,S}
8  C u0 p0 c0 {2,D} {14,S} {26,S}
9  C u0 p0 c0 {3,D} {15,S} {27,S}
10 C u0 p0 c0 {4,D} {17,S} {28,S}
11 C u0 p0 c0 {5,D} {16,S} {29,S}
12 C u0 p0 c0 {6,D} {18,S} {30,S}
13 C u0 p0 c0 {7,S} {14,D} {19,S}
14 C u0 p0 c0 {8,S} {13,D} {20,S}
15 C u0 p0 c0 {9,S} {16,D} {21,S}
16 C u0 p0 c0 {11,S} {15,D} {22,S}
17 C u0 p0 c0 {10,S} {18,D} {23,S}
18 C u0 p0 c0 {12,S} {17,D} {24,S}
19 H u0 p0 c0 {13,S}
20 H u0 p0 c0 {14,S}
21 H u0 p0 c0 {15,S}
22 H u0 p0 c0 {16,S}
23 H u0 p0 c0 {17,S}
24 H u0 p0 c0 {18,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
30 H u0 p0 c0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([375.378,411.293,444.044,473.828,525.256,567.033,637.888],'J/(mol*K)'),
        H298 = (244.7,'kJ/mol'),
        S298 = (373.719,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C5H8O1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([155.259,171.496,186.482,200.284,224.593,244.922,281.336],'J/(mol*K)'),
        H298 = (-210.715,'kJ/mol'),
        S298 = (279.122,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "C7H8O1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {4,S} {6,D} {8,S}
4  C u0 p0 c0 {2,D} {3,S} {15,S}
5  C u0 p0 c0 {2,S} {7,D} {13,S}
6  C u0 p0 c0 {3,D} {7,S} {14,S}
7  C u0 p0 c0 {5,D} {6,S} {12,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([192.767,209.924,225.737,240.278,265.824,287.102,324.889],'J/(mol*K)'),
        H298 = (-147.409,'kJ/mol'),
        S298 = (321.444,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "C5H6A",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([125.226,137.295,148.437,158.702,176.789,191.927,219.086],'J/(mol*K)'),
        H298 = (123.351,'kJ/mol'),
        S298 = (249.129,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "C12H10A",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([272.659,296.096,317.707,337.589,372.55,401.711,453.659],'J/(mol*K)'),
        H298 = (158.673,'kJ/mol'),
        S298 = (335.346,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "C20H12",
    molecule = 
"""
1  C u0 p0 c0 {5,D} {9,S} {21,S}
2  C u0 p0 c0 {6,D} {11,S} {22,S}
3  C u0 p0 c0 {7,D} {10,S} {23,S}
4  C u0 p0 c0 {8,D} {12,S} {24,S}
5  C u0 p0 c0 {1,D} {13,S} {25,S}
6  C u0 p0 c0 {2,D} {13,S} {26,S}
7  C u0 p0 c0 {3,D} {14,S} {27,S}
8  C u0 p0 c0 {4,D} {14,S} {28,S}
9  C u0 p0 c0 {1,S} {15,D} {29,S}
10 C u0 p0 c0 {3,S} {16,D} {30,S}
11 C u0 p0 c0 {2,S} {17,D} {31,S}
12 C u0 p0 c0 {4,S} {18,D} {32,S}
13 C u0 p0 c0 {5,S} {6,S} {19,D}
14 C u0 p0 c0 {7,S} {8,S} {20,D}
15 C u0 p0 c0 {9,D} {16,S} {19,S}
16 C u0 p0 c0 {10,D} {15,S} {20,S}
17 C u0 p0 c0 {11,D} {18,S} {19,S}
18 C u0 p0 c0 {12,D} {17,S} {20,S}
19 C u0 p0 c0 {13,D} {15,S} {17,S}
20 C u0 p0 c0 {14,D} {16,S} {18,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([429.584,462.706,493.229,521.292,570.584,611.631,684.495],'J/(mol*K)'),
        H298 = (167.091,'kJ/mol'),
        S298 = (388.484,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "C6H13A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  C u1 p0 c0 {3,S} {5,S} {19,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([195.609,217.744,238.176,256.997,290.151,317.881,367.544],'J/(mol*K)'),
        H298 = (16.4892,'kJ/mol'),
        S298 = (402.291,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "C3H3O1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([80.3494,86.9062,92.9666,98.5569,108.428,116.715,131.681],'J/(mol*K)'),
        H298 = (84.0484,'kJ/mol'),
        S298 = (290.541,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "C7H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([234.753,254.526,272.944,290.078,320.766,347.118,397.22],'J/(mol*K)'),
        H298 = (-81.6972,'kJ/mol'),
        S298 = (382.622,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "C4H7A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([112.647,125.623,137.614,148.674,168.198,184.582,214.154],'J/(mol*K)'),
        H298 = (220.974,'kJ/mol'),
        S298 = (265.399,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "C9H20",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {8,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {9,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {8,S} {28,S} {29,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([316.213,345.933,373.469,398.935,444.103,482.296,552.439],'J/(mol*K)'),
        H298 = (-253.929,'kJ/mol'),
        S298 = (449.751,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "C5H12O1",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {2,S} {4,S} {18,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([185.027,206.104,225.58,243.539,275.235,301.822,349.765],'J/(mol*K)'),
        H298 = (-294.673,'kJ/mol'),
        S298 = (328.966,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "C8H16A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {8,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {7,S} {23,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([243.431,274.334,302.86,329.137,375.435,414.175,483.681],'J/(mol*K)'),
        H298 = (-148.455,'kJ/mol'),
        S298 = (312.859,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "C5H10O1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([157.025,177.435,196.284,213.655,244.284,269.941,316.066],'J/(mol*K)'),
        H298 = (-239.068,'kJ/mol'),
        S298 = (268.733,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "C10H22",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {9,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {10,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {9,S} {31,S} {32,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([355.305,386.993,416.366,443.547,491.801,532.661,607.944],'J/(mol*K)'),
        H298 = (-278.407,'kJ/mol'),
        S298 = (480.273,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "C8H6",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {9,S}
2  C u0 p0 c0 {1,T} {8,S}
3  C u0 p0 c0 {4,D} {5,S} {10,S}
4  C u0 p0 c0 {3,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {7,D} {12,S}
6  C u0 p0 c0 {4,S} {8,D} {13,S}
7  C u0 p0 c0 {5,D} {8,S} {14,S}
8  C u0 p0 c0 {2,S} {6,D} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([179.351,193.42,206.402,218.355,239.401,256.992,288.47],'J/(mol*K)'),
        H298 = (314.658,'kJ/mol'),
        S298 = (296.928,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "C22H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,D} {15,S}
2  C u0 p0 c0 {1,S} {10,D} {16,S}
3  C u0 p0 c0 {4,S} {11,S} {17,D}
4  C u0 p0 c0 {3,S} {12,S} {18,D}
5  C u0 p0 c0 {6,S} {9,S} {13,D}
6  C u0 p0 c0 {5,S} {10,S} {14,D}
7  C u0 p0 c0 {8,S} {11,D} {13,S}
8  C u0 p0 c0 {7,S} {12,D} {14,S}
9  C u0 p0 c0 {1,D} {5,S} {31,S}
10 C u0 p0 c0 {2,D} {6,S} {32,S}
11 C u0 p0 c0 {3,S} {7,D} {33,S}
12 C u0 p0 c0 {4,S} {8,D} {34,S}
13 C u0 p0 c0 {5,D} {7,S} {35,S}
14 C u0 p0 c0 {6,D} {8,S} {36,S}
15 C u0 p0 c0 {1,S} {19,D} {27,S}
16 C u0 p0 c0 {2,S} {20,D} {28,S}
17 C u0 p0 c0 {3,D} {21,S} {29,S}
18 C u0 p0 c0 {4,D} {22,S} {30,S}
19 C u0 p0 c0 {15,D} {20,S} {23,S}
20 C u0 p0 c0 {16,D} {19,S} {24,S}
21 C u0 p0 c0 {17,S} {22,D} {25,S}
22 C u0 p0 c0 {18,S} {21,D} {26,S}
23 H u0 p0 c0 {19,S}
24 H u0 p0 c0 {20,S}
25 H u0 p0 c0 {21,S}
26 H u0 p0 c0 {22,S}
27 H u0 p0 c0 {15,S}
28 H u0 p0 c0 {16,S}
29 H u0 p0 c0 {17,S}
30 H u0 p0 c0 {18,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {13,S}
36 H u0 p0 c0 {14,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([453.526,496.791,536.238,572.106,634.019,684.289,769.455],'J/(mol*K)'),
        H298 = (318.577,'kJ/mol'),
        S298 = (410.289,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "C6H10A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {3,S} {5,D} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([165.477,184.808,202.656,219.101,248.088,272.357,315.939],'J/(mol*K)'),
        H298 = (-6.71667,'kJ/mol'),
        S298 = (275.243,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "C8H8",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {8,S} {11,S}
3  C u0 p0 c0 {4,D} {5,S} {12,S}
4  C u0 p0 c0 {3,D} {6,S} {13,S}
5  C u0 p0 c0 {3,S} {7,D} {14,S}
6  C u0 p0 c0 {4,S} {8,D} {15,S}
7  C u0 p0 c0 {5,D} {8,S} {16,S}
8  C u0 p0 c0 {2,S} {6,D} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([181.809,200.716,218.168,234.224,262.379,285.637,325.159],'J/(mol*K)'),
        H298 = (135.545,'kJ/mol'),
        S298 = (315.196,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "C10H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {5,S} {11,S}
2  C u0 p0 c0 {1,D} {6,S} {12,S}
3  C u0 p0 c0 {4,D} {7,S} {13,S}
4  C u0 p0 c0 {3,D} {8,D}
5  C u0 p0 c0 {1,S} {9,D} {14,S}
6  C u0 p0 c0 {2,S} {10,D} {15,S}
7  C u1 p0 c0 {3,S} {9,S} {16,S}
8  C u0 p0 c0 {4,D} {10,S} {17,S}
9  C u0 p0 c0 {5,D} {7,S} {10,S}
10 C u0 p0 c0 {6,D} {8,S} {9,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([214.624,232.314,248.637,263.668,290.134,312.256,351.847],'J/(mol*K)'),
        H298 = (378.655,'kJ/mol'),
        S298 = (311.784,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "C9H8",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {4,S} {10,S}
2  C u0 p0 c0 {1,D} {5,S} {11,S}
3  C u0 p0 c0 {6,D} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,S} {9,D} {14,S}
6  C u0 p0 c0 {3,D} {8,S} {15,S}
7  C u0 p0 c0 {3,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {4,D} {6,S} {9,S}
9  C u0 p0 c0 {5,D} {7,S} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([208.735,227.178,244.187,259.839,287.367,310.339,351.302],'J/(mol*K)'),
        H298 = (145.579,'kJ/mol'),
        S298 = (293.433,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "O1C5H6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {10,S}
6  O u0 p2 c0 {2,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([147.215,159.11,170.095,180.217,198.063,213.008,239.866],'J/(mol*K)'),
        H298 = (-35.3326,'kJ/mol'),
        S298 = (278.961,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "C3H3O1A",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([84.9965,91.0239,96.6006,101.75,110.859,118.527,132.457],'J/(mol*K)'),
        H298 = (90.1017,'kJ/mol'),
        S298 = (285.854,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "C5H10A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([143.269,162.482,180.217,196.552,225.327,249.396,292.534],'J/(mol*K)'),
        H298 = (-91.7716,'kJ/mol'),
        S298 = (260.025,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "C4H10A",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.321,154.643,169.724,183.63,208.173,228.759,265.878],'J/(mol*K)'),
        H298 = (-144.999,'kJ/mol'),
        S298 = (272.989,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "C7H8O1A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {6,S} {14,S}
4  C u0 p0 c0 {2,S} {7,D} {15,S}
5  C u0 p0 c0 {6,D} {7,S} {11,S}
6  C u0 p0 c0 {3,S} {5,D} {12,S}
7  C u0 p0 c0 {4,D} {5,S} {13,S}
8  O u0 p2 c0 {1,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([187.898,205.261,221.289,236.053,262.063,283.824,322.843],'J/(mol*K)'),
        H298 = (-116.589,'kJ/mol'),
        S298 = (293.699,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "C10H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {15,S}
4  C u0 p0 c0 {2,D} {8,S} {16,S}
5  C u0 p0 c0 {1,S} {9,D} {17,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {3,S} {8,D} {11,S}
8  C u0 p0 c0 {4,S} {7,D} {12,S}
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([222.786,242.172,260.054,276.511,305.466,329.64,372.789],'J/(mol*K)'),
        H298 = (130.703,'kJ/mol'),
        S298 = (287.787,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "C3H8O1A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([125.035,137.881,149.759,160.721,180.094,196.376,225.864],'J/(mol*K)'),
        H298 = (-280.878,'kJ/mol'),
        S298 = (290.693,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "C4H8",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([91.5967,111.894,130.17,146.566,174.263,196.024,230.527],'J/(mol*K)'),
        H298 = (-1.13266,'kJ/mol'),
        S298 = (306.103,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "C5H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,T} {6,S}
2 C u0 p0 c0 {4,D} {7,S} {8,S}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,D} {5,D}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([109.037,115.728,121.908,127.603,137.644,146.055,161.176],'J/(mol*K)'),
        H298 = (598.148,'kJ/mol'),
        S298 = (285.023,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "C5H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u1 p0 c0 {2,S} {5,S} {9,S}
5  C u0 p0 c0 {3,D} {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([124.594,134.424,143.5,151.863,166.602,178.941,201.095],'J/(mol*K)'),
        H298 = (256.24,'kJ/mol'),
        S298 = (256.689,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "C5H6",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {5,S} {9,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,T}
5  C u0 p0 c0 {2,S} {4,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132.246,142.06,151.358,160.163,176.383,190.896,220.772],'J/(mol*K)'),
        H298 = (239.991,'kJ/mol'),
        S298 = (298.473,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "C5H7",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {7,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([133.132,147.053,159.872,171.649,192.304,209.458,239.688],'J/(mol*K)'),
        H298 = (196.657,'kJ/mol'),
        S298 = (303.202,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "C4H1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,T} {5,S}
2 C u1 p0 c0 {4,T}
3 C u0 p0 c0 {1,T} {4,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([75.7635,78.9655,81.9276,84.6624,89.4986,93.5681,100.955],'J/(mol*K)'),
        H298 = (801.792,'kJ/mol'),
        S298 = (261.953,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "C5H9",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.423,157.694,173.651,188.363,214.322,236.09,275.315],'J/(mol*K)'),
        H298 = (98.6984,'kJ/mol'),
        S298 = (270.732,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "C4H3",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([90.5846,96.425,101.832,106.827,115.673,123.13,136.72],'J/(mol*K)'),
        H298 = (539.555,'kJ/mol'),
        S298 = (273.481,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "C4H2",
    molecule = 
"""
1 C u0 p0 c0 {3,T} {5,S}
2 C u0 p0 c0 {4,T} {6,S}
3 C u0 p0 c0 {1,T} {4,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([87.2817,91.5952,95.5892,99.2801,105.817,111.331,121.389],'J/(mol*K)'),
        H298 = (456.142,'kJ/mol'),
        S298 = (244.448,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "C4H5",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([99.3512,108.496,116.957,124.771,138.594,150.23,171.369],'J/(mol*K)'),
        H298 = (357.687,'kJ/mol'),
        S298 = (290.733,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "C4H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 C u0 p0 c0 {1,S} {4,D} {7,S}
4 C u0 p0 c0 {2,S} {3,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([94.8713,102.868,110.251,117.054,129.045,139.085,157.113],'J/(mol*K)'),
        H298 = (377.684,'kJ/mol'),
        S298 = (234.673,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "C4H7",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.485,122.71,134.02,144.463,162.928,178.465,206.652],'J/(mol*K)'),
        H298 = (239.465,'kJ/mol'),
        S298 = (296.884,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "C4H6",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.069,116.481,126.994,136.656,153.607,167.685,192.443],'J/(mol*K)'),
        H298 = (160.026,'kJ/mol'),
        S298 = (279.453,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "C12H26",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {3,S} {7,S} {23,S} {24,S}
6  C u0 p0 c0 {4,S} {8,S} {25,S} {26,S}
7  C u0 p0 c0 {5,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {6,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {7,S} {11,S} {31,S} {32,S}
10 C u0 p0 c0 {8,S} {12,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {12,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {11,S} {37,S} {38,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([432.464,468.328,501.583,532.367,587.048,633.396,718.99],'J/(mol*K)'),
        H298 = (-327.318,'kJ/mol'),
        S298 = (541.693,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "C4H8O1A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.775,139.637,155.961,170.844,196.648,217.746,254.043],'J/(mol*K)'),
        H298 = (-195.071,'kJ/mol'),
        S298 = (277.814,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "C10H20",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {4,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {3,S} {21,S} {22,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {10,D} {28,S}
10 C u0 p0 c0 {9,D} {29,S} {30,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([321.695,355.51,386.666,415.317,465.697,507.785,583.516],'J/(mol*K)'),
        H298 = (-148.278,'kJ/mol'),
        S298 = (490.442,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "C4H10O2",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
5  O u0 p2 c0 {6,S} {16,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([178.073,194.271,209.27,223.132,247.687,268.401,306.2],'J/(mol*K)'),
        H298 = (-258.334,'kJ/mol'),
        S298 = (319.689,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "C3H6O1A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([98.8576,110.933,122.087,132.37,150.507,165.709,193.076],'J/(mol*K)'),
        H298 = (-90.1753,'kJ/mol'),
        S298 = (254.239,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "C4H10O1",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([167.723,184.408,199.743,213.8,238.37,258.672,294.082],'J/(mol*K)'),
        H298 = (-289.868,'kJ/mol'),
        S298 = (327.782,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "C4H10O1A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([154.065,170.439,185.571,199.528,224.167,244.845,282.164],'J/(mol*K)'),
        H298 = (-302.79,'kJ/mol'),
        S298 = (340.969,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "C9H18O6",
    molecule = 
"""
1  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
2  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
3  C u0 p0 c0 {8,S} {22,S} {23,S} {24,S}
4  C u0 p0 c0 {8,S} {25,S} {26,S} {27,S}
5  C u0 p0 c0 {9,S} {28,S} {29,S} {30,S}
6  C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
7  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
8  C u0 p0 c0 {3,S} {4,S} {12,S} {14,S}
9  C u0 p0 c0 {5,S} {6,S} {13,S} {15,S}
10 O u0 p2 c0 {7,S} {12,S}
11 O u0 p2 c0 {7,S} {13,S}
12 O u0 p2 c0 {8,S} {10,S}
13 O u0 p2 c0 {9,S} {11,S}
14 O u0 p2 c0 {8,S} {15,S}
15 O u0 p2 c0 {9,S} {14,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([409.967,443.572,474.61,503.216,553.661,595.925,671.941],'J/(mol*K)'),
        H298 = (-418.474,'kJ/mol'),
        S298 = (447.014,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "C3H5O1",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.7761,98.6565,107.789,116.213,131.089,143.578,166.14],'J/(mol*K)'),
        H298 = (-38.3674,'kJ/mol'),
        S298 = (302.011,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "C3H5O1A",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {8,S} {9,S}
4 O u0 p2 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([99.7188,108.871,117.336,125.151,138.967,150.588,171.665],'J/(mol*K)'),
        H298 = (97.6837,'kJ/mol'),
        S298 = (278.64,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "C5H11A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {1,S} {15,S} {16,S}
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
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([215.161,218.225,222.87,229.005,245.382,266.65,336.923],'J/(mol*K)'),
        H298 = (16.7941,'kJ/mol'),
        S298 = (289.768,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

