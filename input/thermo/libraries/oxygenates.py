#!/usr/bin/env python
# encoding: utf-8

name = "oxygenates"
shortDesc = u"Oxygenates calculated at B3LYP/6-311G(d,p)/CBS-QB3 level of theory with 1DH-rotors"
longDesc = u"""
Citation: Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452
"""
entry(
    index = 1,
    label = "2-methoxy-propane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([111.9,138.7,163.4,184.8,218.8,244.4],'J/(mol*K)'),
        H298 = (-253.5,'kJ/mol'),
        S298 = (370.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "2-ethoxy-propane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {12,S}
5  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([137.9,170.4,200.2,226,266.9,297.4],'J/(mol*K)'),
        H298 = (-287.5,'kJ/mol'),
        S298 = (407.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "2-propyl-ethanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132.7,166.7,197.1,223,263.9,294],'J/(mol*K)'),
        H298 = (-483.9,'kJ/mol'),
        S298 = (418.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "propane-2,2-diol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([118.3,149,171,186.1,206.4,221.4],'J/(mol*K)'),
        H298 = (-489.1,'kJ/mol'),
        S298 = (339.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "2-methoxy-propan-2-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.3,174.6,201.8,221.8,250.4,271.6],'J/(mol*K)'),
        H298 = (-461,'kJ/mol'),
        S298 = (381.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "2,2-dimethoxy-propane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([155.2,195.9,232.1,260.4,299.5,326.3],'J/(mol*K)'),
        H298 = (-435.2,'kJ/mol'),
        S298 = (423.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "2-hydroxy-2-methyl-propanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {13,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([125,154.9,178.3,196.6,223.8,243.5],'J/(mol*K)'),
        H298 = (-398.5,'kJ/mol'),
        S298 = (360.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "2-methoxy-2-methyl-propanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {17,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.6,174.3,202.3,225.8,262,288.5],'J/(mol*K)'),
        H298 = (-362.6,'kJ/mol'),
        S298 = (418.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "2-methyl-1-oxopropan-2-yl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {13,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {2,S} {7,S}
7  C u0 p0 c0 {6,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([175.2,212.1,242.7,268.1,307.8,337.3],'J/(mol*K)'),
        H298 = (-590.2,'kJ/mol'),
        S298 = (454.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "2-methyl-propanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([102,123.6,144,161.9,191,213],'J/(mol*K)'),
        H298 = (-213.6,'kJ/mol'),
        S298 = (354.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "3-methyl-butan-2-one",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.1,150.9,177,199.6,235.8,263],'J/(mol*K)'),
        H298 = (-263.8,'kJ/mol'),
        S298 = (394.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "2-methyl-propanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([113.1,139.8,163.7,184.2,216.6,240.3],'J/(mol*K)'),
        H298 = (-480.4,'kJ/mol'),
        S298 = (374.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "methyl-2-methyl-propanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132.5,163.3,191.9,216.9,257.3,288],'J/(mol*K)'),
        H298 = (-459.8,'kJ/mol'),
        S298 = (423,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "3-methyl-but-1-en-1-one",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([115.7,141.8,164.7,184,214.2,236.6],'J/(mol*K)'),
        H298 = (-114.5,'kJ/mol'),
        S298 = (375.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "dimethyl-propanedial",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {14,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {2,S} {7,D} {15,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132.9,156.6,178.8,198.4,230.1,253.9],'J/(mol*K)'),
        H298 = (-317.9,'kJ/mol'),
        S298 = (392.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "2,2-dimethyl-3-oxobutanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([159.1,188.3,215.1,238.5,276.3,304.8],'J/(mol*K)'),
        H298 = (-369.7,'kJ/mol'),
        S298 = (445.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "33-dimethyl-pentane-2,4-dione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {4,S} {8,S} {9,D}
8  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
9  O u0 p2 c0 {7,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([187.2,220.7,251.4,278.4,322.2,355.3],'J/(mol*K)'),
        H298 = (-420.6,'kJ/mol'),
        S298 = (487.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "tert-butyl-methyl-ether",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([137,170.2,199.8,224.9,265,295.3],'J/(mol*K)'),
        H298 = (-288.1,'kJ/mol'),
        S298 = (406.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "tert-butyl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  O u0 p2 c0 {2,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([161.9,202.2,236.9,265.8,310.6,344],'J/(mol*K)'),
        H298 = (-515.2,'kJ/mol'),
        S298 = (447.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "2-methyl-propan-2-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.4,145.5,169.8,190.2,221.9,245.8],'J/(mol*K)'),
        H298 = (-317.6,'kJ/mol'),
        S298 = (364.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "2,2-dimethyl-propanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {6,D} {16,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.7,155.6,181.4,203.5,238.8,265.5],'J/(mol*K)'),
        H298 = (-248.6,'kJ/mol'),
        S298 = (380.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "3,3-dimethyl-butan-2-one",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([144.6,180.9,213,240.2,283.1,315.2],'J/(mol*K)'),
        H298 = (-295,'kJ/mol'),
        S298 = (435.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "2,2-dimethyl-propanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.1,172.1,201.6,226.4,265,293.3],'J/(mol*K)'),
        H298 = (-513.2,'kJ/mol'),
        S298 = (408.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "methyl-2,2-dimethyl-propanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([157.6,195.7,229.8,258.8,304.3,338.5],'J/(mol*K)'),
        H298 = (-492.5,'kJ/mol'),
        S298 = (457.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "4,4-dimethyl-penta-1,2-dien-1-one",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {6,D} {18,S}
6  C u0 p0 c0 {5,D} {7,D}
7  C u0 p0 c0 {6,D} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.4,174,202.8,226.6,263.3,290.3],'J/(mol*K)'),
        H298 = (-150.9,'kJ/mol'),
        S298 = (406.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "but-3-en-2-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([113.1,136.9,156.6,172.9,198.2,217.3],'J/(mol*K)'),
        H298 = (-168.1,'kJ/mol'),
        S298 = (341.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "3-methoxy-but-1-ene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([133.6,164.7,191.1,212.7,246,270.7],'J/(mol*K)'),
        H298 = (-148.1,'kJ/mol'),
        S298 = (377.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "but-3-en-2-yl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {12,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([154.4,191.2,223.7,251.1,293.5,324.2],'J/(mol*K)'),
        H298 = (-371,'kJ/mol'),
        S298 = (438.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "3-ethoxy-but-1-ene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([159.8,196.3,227.7,253.7,293.9,323.7],'J/(mol*K)'),
        H298 = (-182,'kJ/mol'),
        S298 = (415.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "2-methyl-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.7,144.4,164.9,183.2,212.9,235.5],'J/(mol*K)'),
        H298 = (-105,'kJ/mol'),
        S298 = (371,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "2-methyl-but-3-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([129.8,158.9,184.3,205.5,237.5,260.6],'J/(mol*K)'),
        H298 = (-369.9,'kJ/mol'),
        S298 = (396.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "3-methyl-pent-4-en-2-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,S} {7,D}
6  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
7  O u0 p2 c0 {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([144,173.9,200.4,223.2,259.5,286.9],'J/(mol*K)'),
        H298 = (-157.9,'kJ/mol'),
        S298 = (412.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "methyl-2-methyl-but-3-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {12,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([149.1,180.8,210.5,236.6,278.5,309.9],'J/(mol*K)'),
        H298 = (-349.9,'kJ/mol'),
        S298 = (443.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "3-methyl-penta-14-dien-1-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132.2,160.8,185.1,205.1,236.2,259.1],'J/(mol*K)'),
        H298 = (-8.4,'kJ/mol'),
        S298 = (391.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "3-methoxy-3-methyl-but-1-ene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([160.5,197.8,228.1,252.9,291.7,321.1],'J/(mol*K)'),
        H298 = (-180.2,'kJ/mol'),
        S298 = (413.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "2-methyl-but-3-en-2-yl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([174.8,217.2,254,284.5,331.4,365.9],'J/(mol*K)'),
        H298 = (-399.1,'kJ/mol'),
        S298 = (466.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "2-methyl-but-3-en-2-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([136.6,167,192.3,213,245,269.1],'J/(mol*K)'),
        H298 = (-207.8,'kJ/mol'),
        S298 = (377.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "2,2-dimethyl-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {17,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([143.6,173.6,200.7,223.8,260.4,287.8],'J/(mol*K)'),
        H298 = (-137.9,'kJ/mol'),
        S298 = (407.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "3,3-dimethyl-pent-4-en-2-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([163.1,200.5,233.9,262.1,306.1,338.7],'J/(mol*K)'),
        H298 = (-187.7,'kJ/mol'),
        S298 = (438.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "2,2-dimethyl-but-3-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([153.7,188.6,219.8,246,286.2,315],'J/(mol*K)'),
        H298 = (-400.5,'kJ/mol'),
        S298 = (426.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "methyl-2,2-dimethyl-but-3-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {19,S} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([173.3,211.9,247.4,277.7,325.2,360.6],'J/(mol*K)'),
        H298 = (-380.4,'kJ/mol'),
        S298 = (474.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "3,3-dimethyl-penta-1,4-dien-1-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158.6,193.1,222.7,247.1,284.6,312.2],'J/(mol*K)'),
        H298 = (-38,'kJ/mol'),
        S298 = (428.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "prop-2-en-1-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89,105.9,119.8,131.4,150.1,164.6],'J/(mol*K)'),
        H298 = (-127.6,'kJ/mol'),
        S298 = (303.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "3-methoxy-prop-1-ene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.6,129.1,148.3,165.2,193.1,214.3],'J/(mol*K)'),
        H298 = (-105.3,'kJ/mol'),
        S298 = (353.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "prop-2-en-1-yl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([119.1,148.5,175.2,198.2,234.4,261.1],'J/(mol*K)'),
        H298 = (-333,'kJ/mol'),
        S298 = (404.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "3-ethoxy-prop-1-ene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([133.1,160.2,185,206.7,241.5,267.8],'J/(mol*K)'),
        H298 = (-139.9,'kJ/mol'),
        S298 = (385.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89.4,109.4,127.3,142.7,166.7,184.5],'J/(mol*K)'),
        H298 = (-76,'kJ/mol'),
        S298 = (335.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "but-3-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([104,127,147.4,164.8,191.9,211.4],'J/(mol*K)'),
        H298 = (-343,'kJ/mol'),
        S298 = (357.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "pent-4-en-2-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  O u0 p2 c0 {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.9,137.1,160.5,180.4,211.5,234.5],'J/(mol*K)'),
        H298 = (-128.6,'kJ/mol'),
        S298 = (379,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "methyl-but-3-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.6,149.8,175.1,197.2,232.8,259.4],'J/(mol*K)'),
        H298 = (-322.2,'kJ/mol'),
        S298 = (405.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "penta-1,4-dien-1-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.3,129.1,147.7,163.4,188.1,206.4],'J/(mol*K)'),
        H298 = (22.7,'kJ/mol'),
        S298 = (356.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "but-3-ene-2,2-diol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([131,163.8,188.3,206,229.6,245.8],'J/(mol*K)'),
        H298 = (-375.7,'kJ/mol'),
        S298 = (356.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "2-methoxy-but-3-en-2-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {14,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([153.5,188.7,218.3,241.4,273.9,296.4],'J/(mol*K)'),
        H298 = (-349.7,'kJ/mol'),
        S298 = (398.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "3,3-dimethoxy-but-1-ene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
7  O u0 p2 c0 {3,S} {8,S}
8  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([168.4,209.3,246.7,277.9,323.1,353],'J/(mol*K)'),
        H298 = (-324,'kJ/mol'),
        S298 = (436,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "2-hydroxy-2-methyl-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {15,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.9,175.6,200.9,220.2,248.1,268],'J/(mol*K)'),
        H298 = (-287.8,'kJ/mol'),
        S298 = (375.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "2-methoxy-2-methyl-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {15,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {3,S} {8,S}
8  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([163.5,198.2,228,252.4,289,315.2],'J/(mol*K)'),
        H298 = (-251.9,'kJ/mol'),
        S298 = (427.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "2-methyl-1-oxobut-3-en-2-yl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,D} {17,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {3,S} {8,S}
8  C u0 p0 c0 {7,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 C u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([190,232.3,267,294.5,335.1,364.2],'J/(mol*K)'),
        H298 = (-478.1,'kJ/mol'),
        S298 = (466.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "2-hydroxy-2-methyl-but-3-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([159.5,195.1,221.9,242.7,273.2,294.3],'J/(mol*K)'),
        H298 = (-550.8,'kJ/mol'),
        S298 = (393.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "2-methoxy-2-methyl-but-3-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {3,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([178,214.7,245.3,270.2,307.7,334.9],'J/(mol*K)'),
        H298 = (-508.8,'kJ/mol'),
        S298 = (456.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "methyl-2-hydroxy-2-methyl-but-3-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([178.6,218.3,249.7,274.6,312.4,340.1],'J/(mol*K)'),
        H298 = (-532.5,'kJ/mol'),
        S298 = (440.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "methyl-2-methoxy-2-methyl-but-3-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {10,S}
10 C u0 p0 c0 {9,S} {22,S} {23,S} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([194.3,235.6,271.8,301.9,348.4,383],'J/(mol*K)'),
        H298 = (-490.2,'kJ/mol'),
        S298 = (500.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "ethenyl-methyl-propanedial",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {15,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {3,S} {8,D} {16,S}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([150.5,181.2,206.2,226.4,257.6,280.5],'J/(mol*K)'),
        H298 = (-207.5,'kJ/mol'),
        S298 = (417.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "2-acetyl-2-methyl-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {3,S} {8,S} {9,D}
8  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
9  O u0 p2 c0 {7,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([175.1,209,238.4,263.2,301.9,330.4],'J/(mol*K)'),
        H298 = (-259.4,'kJ/mol'),
        S298 = (459.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "3-ethenyl-3-methyl-pentane-2,4-dione",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,S} {7,D}
6  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
7  O u0 p2 c0 {5,D}
8  C u0 p0 c0 {3,S} {9,S} {10,D}
9  C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
10 O u0 p2 c0 {8,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([200.3,238.6,272.7,301.6,347,380.4],'J/(mol*K)'),
        H298 = (-310.1,'kJ/mol'),
        S298 = (502.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "prop-1-en-2-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([85.1,105.3,121.4,134.2,153.3,167.3],'J/(mol*K)'),
        H298 = (-171,'kJ/mol'),
        S298 = (299.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "2-methoxy-prop-1-ene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([101.2,127.9,152.4,172.5,201.5,221.2],'J/(mol*K)'),
        H298 = (-151.3,'kJ/mol'),
        S298 = (337.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "prop-1-en-2-yl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([124.6,153.8,180.3,203,237.9,262.1],'J/(mol*K)'),
        H298 = (-349.2,'kJ/mol'),
        S298 = (401.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "2-methyl-prop-2-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([87.9,108.3,126.8,142.8,167.9,186.5],'J/(mol*K)'),
        H298 = (-106.7,'kJ/mol'),
        S298 = (320.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "2-methyl-prop-2-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([111.7,135.7,156.7,174.7,202.8,222.9],'J/(mol*K)'),
        H298 = (-362.2,'kJ/mol'),
        S298 = (353.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "2-methyl-but-3-en-2-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([112.4,137.9,161.2,181.3,213.1,236.7],'J/(mol*K)'),
        H298 = (-150.4,'kJ/mol'),
        S298 = (366.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "methyl-2-methyl-prop-2-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.2,151.3,177.1,199.4,234.7,261],'J/(mol*K)'),
        H298 = (-340.7,'kJ/mol'),
        S298 = (394.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "3-methyl-buta-1,3-dien-1-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([112.2,134.9,153.4,168.6,192.2,209.6],'J/(mol*K)'),
        H298 = (-11.1,'kJ/mol'),
        S298 = (347.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "penta-1,4-dien-3-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
4  O u0 p2 c0 {3,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.9,147.4,169.8,188.4,216.9,237.9],'J/(mol*K)'),
        H298 = (-55.5,'kJ/mol'),
        S298 = (366.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "3-methoxy-penta-1,4-diene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([146.5,178.6,206.7,229.9,265.7,292],'J/(mol*K)'),
        H298 = (-34.9,'kJ/mol'),
        S298 = (399,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "3-ethoxy-penta-1,4-diene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {16,S} {17,S}
8  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([174.1,211.5,244.3,271.6,314,345.1],'J/(mol*K)'),
        H298 = (-69.3,'kJ/mol'),
        S298 = (437.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "penta-1,4-dien-3-yl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {13,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
8  C u0 p0 c0 {3,S} {9,D} {17,S}
9  C u0 p0 c0 {8,D} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([162.4,200.8,234.7,263.2,307.2,338.5],'J/(mol*K)'),
        H298 = (-258.1,'kJ/mol'),
        S298 = (456.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "2-ethenyl-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {15,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([133,161.1,185.2,205.2,236.4,259.4],'J/(mol*K)'),
        H298 = (6.2,'kJ/mol'),
        S298 = (388.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "2-ethenyl-but-3-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([143.2,173.5,200.7,223.6,258.7,283.7],'J/(mol*K)'),
        H298 = (-258.7,'kJ/mol'),
        S298 = (419.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "3-ethenyl-pent-4-en-2-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158.4,191.1,219.6,243.7,281.4,309.4],'J/(mol*K)'),
        H298 = (-48.8,'kJ/mol'),
        S298 = (428.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "methyl-2-ethenyl-but-3-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([164,197.7,229.1,256.3,299.7,332.1],'J/(mol*K)'),
        H298 = (-239.3,'kJ/mol'),
        S298 = (465.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "3-ethenyl-penta-1,4-dien-1-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([148.7,179.5,205,225.7,257.7,281.3],'J/(mol*K)'),
        H298 = (100.7,'kJ/mol'),
        S298 = (412.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "penta-1,4-diene-3,3-diol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  O u0 p2 c0 {3,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  C u0 p0 c0 {3,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([147,183.6,211.5,231.1,255.7,271.7],'J/(mol*K)'),
        H298 = (-262.3,'kJ/mol'),
        S298 = (367.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "3-methoxy-penta-1,4-dien-3-ol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  O u0 p2 c0 {3,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  O u0 p2 c0 {3,S} {8,S}
8  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([167,205.9,238.2,263.2,298.1,321.7],'J/(mol*K)'),
        H298 = (-236.3,'kJ/mol'),
        S298 = (412.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "3,3-dimethoxy-penta-1,4-diene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
8  O u0 p2 c0 {3,S} {9,S}
9  C u0 p0 c0 {8,S} {19,S} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([185.1,225.9,263.7,296.2,345.1,378],'J/(mol*K)'),
        H298 = (-213.3,'kJ/mol'),
        S298 = (449.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "2-ethenyl-2-hydroxy-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  O u0 p2 c0 {3,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  C u0 p0 c0 {3,S} {8,D} {16,S}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([156.3,186.9,211.9,232.1,262.3,283.9],'J/(mol*K)'),
        H298 = (-167,'kJ/mol'),
        S298 = (413.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "2-ethenyl-2-methoxy-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {3,S} {9,S}
9  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([178.2,213.7,244.3,269.5,308,335.8],'J/(mol*K)'),
        H298 = (-137.7,'kJ/mol'),
        S298 = (447.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "3-formyl-penta-1,4-dien-3-yl-acetate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {12,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {3,S} {9,D} {18,S}
9  O u0 p2 c0 {8,D}
10 C u0 p0 c0 {3,S} {11,D} {19,S}
11 C u0 p0 c0 {10,D} {20,S} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([204,248.5,284.7,313.5,356.4,386.7],'J/(mol*K)'),
        H298 = (-362.7,'kJ/mol'),
        S298 = (495.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "2-ethenyl-2-hydroxy-but-3-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  O u0 p2 c0 {3,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  C u0 p0 c0 {3,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([179,216.5,244.5,266.3,297.6,318.9],'J/(mol*K)'),
        H298 = (-438.1,'kJ/mol'),
        S298 = (412.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "2-ethenyl-2-methoxy-but-3-enoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {3,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p2 c0 {8,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([191.2,233.1,267.7,295.2,335.7,364.5],'J/(mol*K)'),
        H298 = (-395.3,'kJ/mol'),
        S298 = (478.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "methyl-2-ethenyl-2-hydroxy-but-3-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  O u0 p2 c0 {3,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  C u0 p0 c0 {3,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {10,S}
10 C u0 p0 c0 {9,S} {18,S} {19,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([197,238.8,271.5,297.7,336.8,364.9],'J/(mol*K)'),
        H298 = (-420.4,'kJ/mol'),
        S298 = (461,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "methyl-2-ethenyl-2-methoxy-but-3-enoate",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {12,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {15,S}
5  C u0 p0 c0 {4,D} {16,S} {17,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {3,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p2 c0 {8,S} {11,S}
11 C u0 p0 c0 {10,S} {21,S} {22,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([204.8,250.1,289.5,322.1,372.2,408.7],'J/(mol*K)'),
        H298 = (-375.1,'kJ/mol'),
        S298 = (518.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "diethenyl-propanedial",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {3,S} {9,D} {17,S}
9  O u0 p2 c0 {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([175,209,234.1,253.8,284,306.3],'J/(mol*K)'),
        H298 = (-96.8,'kJ/mol'),
        S298 = (426,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "2-acetyl-2-ethenyl-but-3-enal",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {17,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {3,S} {9,S} {10,D}
9  C u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
10 O u0 p2 c0 {8,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([192.2,234.8,268.4,294.1,331.6,358.5],'J/(mol*K)'),
        H298 = (-148.8,'kJ/mol'),
        S298 = (465.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "3,3-diethenyl-pentane-2,4-dione",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {12,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {15,S}
5  C u0 p0 c0 {4,D} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
8  O u0 p2 c0 {6,D}
9  C u0 p0 c0 {3,S} {10,S} {11,D}
10 C u0 p0 c0 {9,S} {21,S} {22,S} {23,S}
11 O u0 p2 c0 {9,D}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([218.1,264.1,301.8,332.1,377.5,410],'J/(mol*K)'),
        H298 = (-198.9,'kJ/mol'),
        S298 = (501.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "prop-2-enal",
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
        Cpdata = ([66.6,81.5,94.9,106.3,123.9,136.8],'J/(mol*K)'),
        H298 = (-65.1,'kJ/mol'),
        S298 = (278.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "but-3-en-2-one",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {3,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.5,109.3,127.9,143.7,168.4,186.6],'J/(mol*K)'),
        H298 = (-111.4,'kJ/mol'),
        S298 = (323.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "buta-1,3-dien-1-one",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {9,S}
4 C u0 p0 c0 {3,D} {5,D}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([82.3,100,114.8,126.9,145.4,158.9],'J/(mol*K)'),
        H298 = (26.6,'kJ/mol'),
        S298 = (301.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "methoxy-methane",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([66,79.5,92.8,104.9,125,140.5],'J/(mol*K)'),
        H298 = (-184.6,'kJ/mol'),
        S298 = (291.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "methoxy-ethane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([93.7,112,129.7,145.7,172.4,192.8],'J/(mol*K)'),
        H298 = (-218.4,'kJ/mol'),
        S298 = (329.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "ethoxy-ethane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([120.9,143.9,166.2,186.3,219.6,245.1],'J/(mol*K)'),
        H298 = (-252.2,'kJ/mol'),
        S298 = (367.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "1-ethoxy-propane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([141.1,172.2,201,226.3,267.1,297.9],'J/(mol*K)'),
        H298 = (-273.7,'kJ/mol'),
        S298 = (406.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "1-propoxy-propane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([161.7,200.9,236.2,266.5,314.6,350.6],'J/(mol*K)'),
        H298 = (-295.2,'kJ/mol'),
        S298 = (446.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "dimethoxy-methane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([107.5,135.2,157.6,174.4,199,217.4],'J/(mol*K)'),
        H298 = (-352.5,'kJ/mol'),
        S298 = (354.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "methanol",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.7,52,59.8,67.2,79.5,89.1],'J/(mol*K)'),
        H298 = (-203.2,'kJ/mol'),
        S298 = (248.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "ethanol",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([66.4,81.1,95,107,126.3,140.9],'J/(mol*K)'),
        H298 = (-236.2,'kJ/mol'),
        S298 = (289.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "1-propanol",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.5,109.2,128.5,145.3,172,192],'J/(mol*K)'),
        H298 = (-256.9,'kJ/mol'),
        S298 = (331.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "methane-diol",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([64,82,95.4,103.9,113,118.5],'J/(mol*K)'),
        H298 = (-396.6,'kJ/mol'),
        S298 = (262.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "1,2-ethanediol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([84.8,109.2,129.1,143.1,160.3,171.3],'J/(mol*K)'),
        H298 = (-394.8,'kJ/mol'),
        S298 = (304.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "1,3-propanediol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([107.5,136.7,163.6,184.7,211.8,228],'J/(mol*K)'),
        H298 = (-416,'kJ/mol'),
        S298 = (337,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "1,4-butanediol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
6  O u0 p2 c0 {5,S} {16,S}
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
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123,159,193.5,222.7,264.1,289],'J/(mol*K)'),
        H298 = (-442.2,'kJ/mol'),
        S298 = (362,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "methoxy-methanol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([87.8,109.7,126.2,138.1,154.5,166.7],'J/(mol*K)'),
        H298 = (-373.7,'kJ/mol'),
        S298 = (309.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "2-propanone",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  O u0 p2 c0 {2,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([73.5,90.6,106.7,120.8,143.5,160.6],'J/(mol*K)'),
        H298 = (-216.7,'kJ/mol'),
        S298 = (318.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "2-butanone",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {3,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([102.1,123.1,143,160.7,189.7,211.7],'J/(mol*K)'),
        H298 = (-238.6,'kJ/mol'),
        S298 = (359.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "2-pentanone",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.3,151,177,199.8,236.4,263.9],'J/(mol*K)'),
        H298 = (-258.7,'kJ/mol'),
        S298 = (398.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "3-pentanone",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([128.2,153.6,177.9,199.6,235.4,262.6],'J/(mol*K)'),
        H298 = (-260.2,'kJ/mol'),
        S298 = (398.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "2,3-butanedione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  O u0 p2 c0 {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([102.5,124.2,144.4,161.8,188.9,208],'J/(mol*K)'),
        H298 = (-328.5,'kJ/mol'),
        S298 = (370.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "2,3-pentanedione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {7,D}
6  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
7  O u0 p2 c0 {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([130.3,155.9,180.2,201.5,235.1,259.3],'J/(mol*K)'),
        H298 = (-349.9,'kJ/mol'),
        S298 = (410.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "2,4-pentanedione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {7,D}
6  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
7  O u0 p2 c0 {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([130.1,155.6,178.9,198.9,230.5,254],'J/(mol*K)'),
        H298 = (-363.7,'kJ/mol'),
        S298 = (419.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "2,3-hexanedione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([151,183.5,214,240.5,281.8,311.3],'J/(mol*K)'),
        H298 = (-370.2,'kJ/mol'),
        S298 = (451.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "3,4-hexanedione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158,187.6,216.3,241.6,281.9,311],'J/(mol*K)'),
        H298 = (-371.5,'kJ/mol'),
        S298 = (448.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "2,3,4-pentanetrione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([136.6,159.3,179.6,196.9,224.2,244.1],'J/(mol*K)'),
        H298 = (-419.3,'kJ/mol'),
        S298 = (437.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "2,3,4-hexanetrione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {8,S} {9,D}
8  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
9  O u0 p2 c0 {7,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([166.2,192.2,216.1,237,270.5,295.3],'J/(mol*K)'),
        H298 = (-441.3,'kJ/mol'),
        S298 = (472.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "2,3,4-heptanetrione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {9,S} {10,D}
9  C u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
10 O u0 p2 c0 {8,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([186.8,219.8,249.9,275.9,316.9,346.8],'J/(mol*K)'),
        H298 = (-461.7,'kJ/mol'),
        S298 = (514.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "3,4,5-heptanetrione",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  C u0 p0 c0 {7,S} {10,S} {16,S} {17,S}
10 C u0 p0 c0 {9,S} {18,S} {19,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([195.2,225.1,252.9,277.4,317,346.4],'J/(mol*K)'),
        H298 = (-463.8,'kJ/mol'),
        S298 = (512.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "1-hydroxy-2-propanone",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89.9,113.3,134.6,151.9,176.5,192.6],'J/(mol*K)'),
        H298 = (-376.2,'kJ/mol'),
        S298 = (328,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "1-methoxy-2-propanone",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  O u0 p2 c0 {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.6,141.5,163.9,183.2,213.5,235.7],'J/(mol*K)'),
        H298 = (-341.2,'kJ/mol'),
        S298 = (383.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "ethanal",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([53.9,64.5,74.9,84.2,99.5,111.1],'J/(mol*K)'),
        H298 = (-164.9,'kJ/mol'),
        S298 = (271.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "propanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  O u0 p2 c0 {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([82.3,95.7,109.8,122.9,144.9,161.7],'J/(mol*K)'),
        H298 = (-185.9,'kJ/mol'),
        S298 = (313.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "ethanedial",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([60.4,71.2,81.2,89.6,101.7,109],'J/(mol*K)'),
        H298 = (-212.2,'kJ/mol'),
        S298 = (277.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "2-oxo-propanal",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,D} {9,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([80.7,97.2,112.4,125.5,145.2,158.5],'J/(mol*K)'),
        H298 = (-271.6,'kJ/mol'),
        S298 = (325.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "propanedial",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u0 p0 c0 {3,S} {5,D} {9,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([78.4,94.1,108.3,120.3,139.2,152.9],'J/(mol*K)'),
        H298 = (-253.4,'kJ/mol'),
        S298 = (327.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "3-oxo-butanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([100.9,122.4,141.7,158.1,183.9,202.8],'J/(mol*K)'),
        H298 = (-308,'kJ/mol'),
        S298 = (377.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "2-oxo-propanedial",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 C u0 p0 c0 {3,S} {6,D} {8,S}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89.9,101.7,111.8,120.5,134.1,143.8],'J/(mol*K)'),
        H298 = (-296.5,'kJ/mol'),
        S298 = (346.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "2,3-dioxo-butanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {11,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([112.2,128.7,143.8,157,177.9,193.1],'J/(mol*K)'),
        H298 = (-357.3,'kJ/mol'),
        S298 = (397.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "2-hydroxy-ethanal",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([72.9,89.4,104.6,116.7,133.1,143],'J/(mol*K)'),
        H298 = (-321.1,'kJ/mol'),
        S298 = (287.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "2-methoxy-ethanal",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([94.5,112.8,129.9,144.7,168.2,185.3],'J/(mol*K)'),
        H298 = (-286,'kJ/mol'),
        S298 = (346.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "methyl-methanoate",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([63.7,77.6,91.5,104,123.8,137.7],'J/(mol*K)'),
        H298 = (-358.1,'kJ/mol'),
        S298 = (296.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "methyl-ethanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {3,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([84.3,103.7,122.3,138.9,165.9,186.3],'J/(mol*K)'),
        H298 = (-411.9,'kJ/mol'),
        S298 = (342.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "methyl-propanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([109.7,133.2,156.3,177.1,211.1,236.9],'J/(mol*K)'),
        H298 = (-432.2,'kJ/mol'),
        S298 = (385.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "ethyl-methanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([86.2,107.4,127.5,144.9,171.7,190.6],'J/(mol*K)'),
        H298 = (-391.8,'kJ/mol'),
        S298 = (335.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "ethyl-ethanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  O u0 p2 c0 {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([106.7,133.4,158.1,179.7,214.2,239.8],'J/(mol*K)'),
        H298 = (-445.4,'kJ/mol'),
        S298 = (380,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "ethyl-propanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132,162.8,192,217.7,259.2,290.1],'J/(mol*K)'),
        H298 = (-466.1,'kJ/mol'),
        S298 = (424.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "ethyl-butanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {16,S} {17,S}
8  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([153,191.1,226.5,257.1,306.1,342.4],'J/(mol*K)'),
        H298 = (-487.2,'kJ/mol'),
        S298 = (462.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "methyl-2-oxoethanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([96,112.9,128.8,142.8,165.1,181],'J/(mol*K)'),
        H298 = (-448,'kJ/mol'),
        S298 = (351.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "methyl-2-oxopropanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {7,D}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  O u0 p2 c0 {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([119.2,141.3,161.8,180,209.4,230.4],'J/(mol*K)'),
        H298 = (-505.3,'kJ/mol'),
        S298 = (398.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "ethyl-2-oxopropanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.5,171.7,198.1,221.1,257.5,283.7],'J/(mol*K)'),
        H298 = (-539.5,'kJ/mol'),
        S298 = (438.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "ethyl-2-oxobutanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {9,S} {15,S} {16,S}
9  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([170.5,203.4,233.8,260.6,303.7,335],'J/(mol*K)'),
        H298 = (-562.1,'kJ/mol'),
        S298 = (474.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "methyl-3-oxo-propanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([113.1,135.7,157,175.6,205.7,228],'J/(mol*K)'),
        H298 = (-500.5,'kJ/mol'),
        S298 = (398,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "methyl-3-oxo-butanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.9,162.1,188.7,212.3,250.1,277.7],'J/(mol*K)'),
        H298 = (-552,'kJ/mol'),
        S298 = (446.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "2-hydroxy-methyl-ethanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([106.1,129.8,150.7,168.2,195.1,214.1],'J/(mol*K)'),
        H298 = (-562.6,'kJ/mol'),
        S298 = (356.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "2-methoxy-methyl-ethanoate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  O u0 p2 c0 {5,S} {7,S}
7  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([129.9,154.2,177.4,198.1,232.2,258],'J/(mol*K)'),
        H298 = (-528.4,'kJ/mol'),
        S298 = (412.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "methyl-hydrogen-carbonate",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([83.6,101.5,117,129.7,148.4,161.1],'J/(mol*K)'),
        H298 = (-592.1,'kJ/mol'),
        S298 = (321.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "dimethyl-carbonate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([100.9,125,147.1,165.7,193.2,211.8],'J/(mol*K)'),
        H298 = (-570.5,'kJ/mol'),
        S298 = (366.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "ethyl-methyl-carbonate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.6,154.8,183,206.4,241.1,264.8],'J/(mol*K)'),
        H298 = (-605.4,'kJ/mol'),
        S298 = (404.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "diethyl-carbonate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([146.4,185,219.2,247.3,289.1,317.8],'J/(mol*K)'),
        H298 = (-640.2,'kJ/mol'),
        S298 = (447.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "methyl-hydrogen-ethadionate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {11,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.7,134.4,154.8,171.5,195.4,210.4],'J/(mol*K)'),
        H298 = (-708.1,'kJ/mol'),
        S298 = (363.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "dimethyl-ethadionate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([124.9,149.5,173.8,195.8,231.5,256.4],'J/(mol*K)'),
        H298 = (-682.3,'kJ/mol'),
        S298 = (427.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "methyl-hydrogen-propadionate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.8,152.6,178.7,201.1,235.8,260.1],'J/(mol*K)'),
        H298 = (-768.9,'kJ/mol'),
        S298 = (395.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "dimethyl-propadionate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.4,171.5,201.8,228.4,271,302],'J/(mol*K)'),
        H298 = (-745.6,'kJ/mol'),
        S298 = (474.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "methyl-hydrogen-2-oxo-propadionate",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {13,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.8,162.9,184.1,202.2,229.5,247.8],'J/(mol*K)'),
        H298 = (-798,'kJ/mol'),
        S298 = (432.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "methanoic-anhydride",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,D} {7,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([75.8,91.1,103.3,112.5,124.4,131.5],'J/(mol*K)'),
        H298 = (-472.7,'kJ/mol'),
        S298 = (302.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "methanoic-ethanoic-anhydride",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([95.2,115.8,133.9,148.5,169.7,183.5],'J/(mol*K)'),
        H298 = (-532.2,'kJ/mol'),
        S298 = (348.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "ethanoic-anhydride",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,D}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  O u0 p2 c0 {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([109.4,132.3,153.2,171,198.8,219],'J/(mol*K)'),
        H298 = (-576.3,'kJ/mol'),
        S298 = (422.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "ethanoic-propanoic-anhydride",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {8,D}
7  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([137.1,163.2,188,209.7,244.2,269.6],'J/(mol*K)'),
        H298 = (-597.6,'kJ/mol'),
        S298 = (462.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "propanoic-anhydride",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {9,S} {15,S} {16,S}
9  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([165.3,194.3,222.9,248.5,289.6,320.1],'J/(mol*K)'),
        H298 = (-619,'kJ/mol'),
        S298 = (502.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "methanoic-acid",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([45,53.8,62.1,69.4,80.5,88.1],'J/(mol*K)'),
        H298 = (-378.5,'kJ/mol'),
        S298 = (248.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "ethanoic-acid",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([65.2,80.3,93.9,105.7,124.4,137.9],'J/(mol*K)'),
        H298 = (-432.4,'kJ/mol'),
        S298 = (295,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "propanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([91.6,110.4,128.4,144.4,169.9,188.6],'J/(mol*K)'),
        H298 = (-453.4,'kJ/mol'),
        S298 = (336.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "2-oxoethanoic-acid",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p2 c0 {3,S} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([75.1,87.8,98.6,107.8,122.4,132.9],'J/(mol*K)'),
        H298 = (-471.5,'kJ/mol'),
        S298 = (296.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "2-oxopropanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([95.3,115.7,132.7,146.6,167.8,183.3],'J/(mol*K)'),
        H298 = (-535.1,'kJ/mol'),
        S298 = (337.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "2-oxo-butanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.6,147.1,168.5,186.4,214.3,234.8],'J/(mol*K)'),
        H298 = (-557.3,'kJ/mol'),
        S298 = (376.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "3-oxo-propanoic-acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {10,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([94.9,113.1,129.3,143.2,164.8,180.1],'J/(mol*K)'),
        H298 = (-519.8,'kJ/mol'),
        S298 = (353.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "3-oxo-butanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.7,136.5,160.7,181,212.1,233.8],'J/(mol*K)'),
        H298 = (-576.1,'kJ/mol'),
        S298 = (372.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "2,3-dioxo-propanoic-acid",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 C u0 p0 c0 {3,S} {6,D} {7,S}
6 O u0 p2 c0 {5,D}
7 O u0 p2 c0 {5,S} {9,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([107.9,121.6,132.9,142.5,157.1,167.3],'J/(mol*K)'),
        H298 = (-554.9,'kJ/mol'),
        S298 = (366,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "2,3-dioxo-butanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {12,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([128.1,149.8,167.5,181.8,203.1,218],'J/(mol*K)'),
        H298 = (-617.3,'kJ/mol'),
        S298 = (411.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "2,3-dioxo-pentanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {15,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([154.4,179.8,201.8,220.3,248.6,268.7],'J/(mol*K)'),
        H298 = (-638,'kJ/mol'),
        S298 = (451.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "2-hydroxy-ethanoic-acid",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {6,S}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 O u0 p2 c0 {4,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([86,106.2,122.7,135.7,153.9,165.6],'J/(mol*K)'),
        H298 = (-582.2,'kJ/mol'),
        S298 = (306.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "2-methoxy-ethanoic-acid",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.1,126.8,146.6,163.8,191.4,211.7],'J/(mol*K)'),
        H298 = (-549.6,'kJ/mol'),
        S298 = (351.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "carbonic-acid",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {5,S}
4 O u0 p2 c0 {2,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([66.3,79.4,88.6,95.4,104.7,110.9],'J/(mol*K)'),
        H298 = (-612.8,'kJ/mol'),
        S298 = (272.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "ethadionic-acid",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p2 c0 {4,S} {8,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.8,108,122.2,132.7,147,156.6],'J/(mol*K)'),
        H298 = (-735,'kJ/mol'),
        S298 = (310.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "propanedionic-acid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {11,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([104.6,129.3,150.7,168.5,195,212.3],'J/(mol*K)'),
        H298 = (-785.5,'kJ/mol'),
        S298 = (350.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "2-oxo-propanedionic-acid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {10,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([116.1,140.1,158.7,172.8,191.7,203.1],'J/(mol*K)'),
        H298 = (-814.2,'kJ/mol'),
        S298 = (351.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "2-methoxy-ethanol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.9,139.9,163.8,181.7,206.2,223.2],'J/(mol*K)'),
        H298 = (-375.9,'kJ/mol'),
        S298 = (341.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "3-methoxy-propanol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132.6,167.4,197.5,221.4,256,279.8],'J/(mol*K)'),
        H298 = (-399.6,'kJ/mol'),
        S298 = (371.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "4-methoxy-butanol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  O u0 p2 c0 {6,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([148.9,192.6,233.4,267.5,315.2,344.4],'J/(mol*K)'),
        H298 = (-423.8,'kJ/mol'),
        S298 = (392.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "2-propanol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([90.8,112.3,131.6,148,173.8,193.2],'J/(mol*K)'),
        H298 = (-274.7,'kJ/mol'),
        S298 = (328.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "2-butanol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.3,143.4,167.3,187.8,220.3,244.9],'J/(mol*K)'),
        H298 = (-295,'kJ/mol'),
        S298 = (366.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "3-pentanol",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {12,S}
4  O u0 p2 c0 {3,S} {13,S}
5  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([144.3,174.9,203.3,227.8,267,296.6],'J/(mol*K)'),
        H298 = (-315.1,'kJ/mol'),
        S298 = (404.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "methyl-ketene",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([68.8,81.7,93.6,103.8,120.3,132.7],'J/(mol*K)'),
        H298 = (-59.4,'kJ/mol'),
        S298 = (295.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "ethyl-ketene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([91.6,111,128.4,143.2,166.7,184.2],'J/(mol*K)'),
        H298 = (-81.6,'kJ/mol'),
        S298 = (336.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "propyl-ketene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([114.4,139.9,162.8,182.2,212.9,235.7],'J/(mol*K)'),
        H298 = (-103.3,'kJ/mol'),
        S298 = (378.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "dimethyl-ketene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,D} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([93.2,110.6,126.9,141.4,165,183],'J/(mol*K)'),
        H298 = (-85.1,'kJ/mol'),
        S298 = (339,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "ethyl-methyl-ketene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,D} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([114.7,138.9,161.1,180.3,211.3,234.4],'J/(mol*K)'),
        H298 = (-107.8,'kJ/mol'),
        S298 = (380.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "diethyl-ketene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {5,D}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([135.2,166.2,194.4,218.6,257,285.6],'J/(mol*K)'),
        H298 = (-126.1,'kJ/mol'),
        S298 = (420.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "methoxy-ethene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([82.8,103,119.4,132.6,152.6,167.3],'J/(mol*K)'),
        H298 = (-105.9,'kJ/mol'),
        S298 = (297.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "1-ethoxy-propene-trans",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.2,162.6,187.4,208.6,242.6,268.5],'J/(mol*K)'),
        H298 = (-165.2,'kJ/mol'),
        S298 = (378.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "ethenol",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([61.6,76.1,87.3,95.8,108,116.7],'J/(mol*K)'),
        H298 = (-125.4,'kJ/mol'),
        S298 = (257.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "ethene-1,1-diol",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {7,S}
4 O u0 p2 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([80.8,98.4,110.8,119.4,130.5,138.2],'J/(mol*K)'),
        H298 = (-322.5,'kJ/mol'),
        S298 = (282.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "1-methoxy-ethenol",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {8,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([99.6,123.3,142.4,156.9,177,190.6],'J/(mol*K)'),
        H298 = (-303.9,'kJ/mol'),
        S298 = (323.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "1-ethoxy-1-propenol-trans",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {11,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {12,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([148.8,182.3,209.5,231.4,264.8,289.7],'J/(mol*K)'),
        H298 = (-362.3,'kJ/mol'),
        S298 = (402.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "2-formylpropan-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([94.6,115,134.5,151.8,179.4,199.9],'J/(mol*K)'),
        H298 = (-73.5,'kJ/mol'),
        S298 = (351.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "2-methyl-3-oxobutan-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([113.1,140.3,165.8,187.9,223.1,249.2],'J/(mol*K)'),
        H298 = (-115.7,'kJ/mol'),
        S298 = (395.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "2-carboxypropan-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.6,130.6,153.3,172.9,204.1,226.8],'J/(mol*K)'),
        H298 = (-322.4,'kJ/mol'),
        S298 = (374.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "1-methoxy-2-methyl-1-oxopropan-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([125.3,154.4,181.9,205.9,244.5,273.5],'J/(mol*K)'),
        H298 = (-300.5,'kJ/mol'),
        S298 = (422.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "3-methyl-1-oxobut-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.6,131.8,152.9,171.1,200.1,221.5],'J/(mol*K)'),
        H298 = (29.3,'kJ/mol'),
        S298 = (379.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "3-formyl-but-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([106.1,131.9,154.8,174.1,203.9,225.5],'J/(mol*K)'),
        H298 = (1.1,'kJ/mol'),
        S298 = (357.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "3-carboxy-but-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([120.9,150.1,175.5,196.9,229.9,253.5],'J/(mol*K)'),
        H298 = (-250,'kJ/mol'),
        S298 = (376.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "3-methyl-4-oxopent-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([129.1,160.3,188.2,211.9,248.6,275.5],'J/(mol*K)'),
        H298 = (-35.4,'kJ/mol'),
        S298 = (398.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "4-methoxy-3-methyl-4-oxobut-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.7,173.8,203.9,229.5,269.8,299.5],'J/(mol*K)'),
        H298 = (-228.6,'kJ/mol'),
        S298 = (422,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "3-methyl-1-oxopenta-14-dien-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([125.4,152.6,176.2,195.8,226.1,248.1],'J/(mol*K)'),
        H298 = (87,'kJ/mol'),
        S298 = (392,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "1-oxopenta-14-dien-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([102.8,125.3,144,159.1,182,198.3],'J/(mol*K)'),
        H298 = (122.7,'kJ/mol'),
        S298 = (334.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "3-formyl-penta-14-dien-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {6,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {3,S} {7,D} {12,S}
7  C u0 p0 c0 {6,D} {13,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.8,151.2,176.6,197.5,229.1,251.7],'J/(mol*K)'),
        H298 = (84.2,'kJ/mol'),
        S298 = (369.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "3-carboxy-penta-14-dien-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {12,S}
7  C u0 p0 c0 {3,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {14,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([135.5,168.9,197.2,220.5,255.5,279.7],'J/(mol*K)'),
        H298 = (-168,'kJ/mol'),
        S298 = (381.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "3-acetyl-penta-14-dien-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {8,D} {15,S}
8  C u0 p0 c0 {7,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([145.2,180.1,210.4,235.6,274.1,301.9],'J/(mol*K)'),
        H298 = (48,'kJ/mol'),
        S298 = (406.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "3-methoxy-carbonyl-penta-14-dien-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u1 p0 c0 {2,S} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
8  C u0 p0 c0 {3,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([156.2,193.4,226.1,253.4,295.3,325.8],'J/(mol*K)'),
        H298 = (-147.1,'kJ/mol'),
        S298 = (431.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "3-ethenyl-1-oxopenta-14-dien-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,D}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {3,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {14,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138,170.2,196.9,218.5,250.9,274.1],'J/(mol*K)'),
        H298 = (169.8,'kJ/mol'),
        S298 = (384.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "2-methoxy-propan-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.2,132,153.1,171.9,202.8,226.5],'J/(mol*K)'),
        H298 = (-72.2,'kJ/mol'),
        S298 = (382.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "2-ethoxy-propan-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([136,163.1,189.2,212.3,250.1,278.7],'J/(mol*K)'),
        H298 = (-106.2,'kJ/mol'),
        S298 = (419.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "2-acetyloxy-propan-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([129.7,158,185.4,209.5,247.1,273.7],'J/(mol*K)'),
        H298 = (-283.5,'kJ/mol'),
        S298 = (441.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "2-methoxypropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([120.1,142.7,163.1,180.9,209.4,231.2],'J/(mol*K)'),
        H298 = (-41,'kJ/mol'),
        S298 = (375.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "2-ethoxypropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([146.9,174.9,200.3,222.2,257.4,284.1],'J/(mol*K)'),
        H298 = (-75.1,'kJ/mol'),
        S298 = (413.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "2-acetyloxypropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.1,165.1,192.5,215.7,252,278.8],'J/(mol*K)'),
        H298 = (-268.1,'kJ/mol'),
        S298 = (425.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "propan-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  O u1 p2 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([86.4,106.7,124.6,139.7,163.5,181.3],'J/(mol*K)'),
        H298 = (-46.5,'kJ/mol'),
        S298 = (320.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "22-dihydroxypropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  O u0 p2 c0 {4,S} {8,S}
6  O u0 p2 c0 {4,S} {9,S}
7  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([120.1,147,165.9,179,196.1,208.2],'J/(mol*K)'),
        H298 = (-271.4,'kJ/mol'),
        S298 = (347.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "2-hydroxy-2-methoxy-propyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  O u0 p2 c0 {4,S} {9,S}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
8  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([141.4,171.2,195.2,213.5,239.7,258.4],'J/(mol*K)'),
        H298 = (-243.3,'kJ/mol'),
        S298 = (388.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "22-dimethoxypropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
7  O u0 p2 c0 {4,S} {8,S}
8  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
9  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158.5,196.7,228.8,253.6,288.1,312],'J/(mol*K)'),
        H298 = (-218.6,'kJ/mol'),
        S298 = (432.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "2-hydroxypropan-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u1 p2 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([106.8,130.8,150.3,165.7,188.4,204.8],'J/(mol*K)'),
        H298 = (-255.7,'kJ/mol'),
        S298 = (348,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "2-methoxypropan-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
6  O u1 p2 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.8,152.4,177.7,198.8,231.4,255],'J/(mol*K)'),
        H298 = (-229.5,'kJ/mol'),
        S298 = (390.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "2-formyl-2-hydroxypropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
8  O u0 p2 c0 {7,S} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([128.6,156.7,177.9,193.8,216,231.5],'J/(mol*K)'),
        H298 = (-185.7,'kJ/mol'),
        S298 = (368,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "2-formyl-2-methoxypropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
8  O u0 p2 c0 {7,S} {9,S}
9  C u0 p0 c0 {8,S} {14,S} {15,S} {16,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([152.1,182.6,207.6,227.5,257,278.5],'J/(mol*K)'),
        H298 = (-151,'kJ/mol'),
        S298 = (416.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    label = "2-acetyloxy-2-formylpropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
8  O u0 p2 c0 {4,S} {9,S}
9  C u0 p0 c0 {8,S} {10,D} {11,S}
10 O u0 p2 c0 {9,D}
11 C u0 p0 c0 {9,S} {16,S} {17,S} {18,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([181.8,217.3,244.8,266.6,300.2,325.4],'J/(mol*K)'),
        H298 = (-375.8,'kJ/mol'),
        S298 = (459.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    label = "2-hydroxy-2-methylpropanoyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {13,S}
5  C u1 p0 c0 {2,S} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.4,144.5,164,179.8,204.1,221.9],'J/(mol*K)'),
        H298 = (-233.2,'kJ/mol'),
        S298 = (383.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    label = "2-methoxy-2-methylpropanoyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
6  C u1 p0 c0 {2,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([147.4,174.2,197.7,217.6,249,272.5],'J/(mol*K)'),
        H298 = (-207.9,'kJ/mol'),
        S298 = (426.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "2-acetyloxy-2-methylpropanoyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u1 p0 c0 {2,S} {9,D}
9  O u0 p2 c0 {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([171.1,206.6,236.1,260.2,296.9,323.7],'J/(mol*K)'),
        H298 = (-430.6,'kJ/mol'),
        S298 = (461.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "2-methyl-1-oxopropan-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  O u1 p2 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.4,141.4,162,179.1,205.4,224.6],'J/(mol*K)'),
        H298 = (-158,'kJ/mol'),
        S298 = (375.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "2-formylpropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {7,D} {12,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.4,123.9,141,156.1,180.5,199.1],'J/(mol*K)'),
        H298 = (-2.3,'kJ/mol'),
        S298 = (361.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "2-methyl-3-oxobutyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
7  O u0 p2 c0 {6,S} {8,S}
8  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([128.9,153.1,175.2,194.5,225.7,249.4],'J/(mol*K)'),
        H298 = (-54.6,'kJ/mol'),
        S298 = (401.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "2-carboxypropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([115.6,139.6,161,178.8,206.1,225.7],'J/(mol*K)'),
        H298 = (-267.6,'kJ/mol'),
        S298 = (385.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "3-methoxy-2-methyl-3-oxopropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {14,S} {15,S} {16,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.3,161.7,187.4,209.9,246.3,273.9],'J/(mol*K)'),
        H298 = (-247.2,'kJ/mol'),
        S298 = (432.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "2-methylpropanoyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([96.5,117.4,136.2,152.3,178,197.4],'J/(mol*K)'),
        H298 = (-56.4,'kJ/mol'),
        S298 = (359,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "3-methyl-1-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.7,140.2,159.9,176.4,202.3,221.6],'J/(mol*K)'),
        H298 = (98.1,'kJ/mol'),
        S298 = (386.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "3-methyl-1-oxobut-1-en-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([114.3,138.2,158.9,176.4,203.9,224.3],'J/(mol*K)'),
        H298 = (91.3,'kJ/mol'),
        S298 = (375.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "22-diformylpropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {4,S} {8,D} {11,S}
8  O u0 p2 c0 {7,D}
9  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([143.1,165.8,184.7,200.4,225.5,244.4],'J/(mol*K)'),
        H298 = (-107.1,'kJ/mol'),
        S298 = (406.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "2-formyl-2-methyl-3-oxobutyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {4,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
10 C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([157.7,187.9,213.8,235.5,269.2,294],'J/(mol*K)'),
        H298 = (-161.8,'kJ/mol'),
        S298 = (450,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    label = "2-acetyl-2-methyl-3-oxobutyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {4,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
11 C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {11,S}
19 H u0 p0 c0 {11,S}
20 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([186.7,219.4,248.6,273.6,313.3,342.9],'J/(mol*K)'),
        H298 = (-212.3,'kJ/mol'),
        S298 = (496.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    label = "2-formyl-2-methylpropanoyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {14,S}
5  O u0 p2 c0 {4,D}
6  C u1 p0 c0 {2,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.9,157.4,177,193.8,220.6,240.8],'J/(mol*K)'),
        H298 = (-161.1,'kJ/mol'),
        S298 = (408.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 247,
    label = "22-dimethyl-3-oxobutanoyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  C u1 p0 c0 {2,S} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([154.2,183,208.7,230.5,265,290.6],'J/(mol*K)'),
        H298 = (-211.7,'kJ/mol'),
        S298 = (452.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "2-methoxy-2-methylpropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  O u0 p2 c0 {4,S} {8,S}
8  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.2,172.9,199.3,221.4,256.3,282.8],'J/(mol*K)'),
        H298 = (-76.2,'kJ/mol'),
        S298 = (411.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "2-acetyloxy-2-methylpropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  O u0 p2 c0 {4,S} {8,S}
8  C u0 p0 c0 {7,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([165.2,202.1,233.5,259.7,300.6,331.1],'J/(mol*K)'),
        H298 = (-301.4,'kJ/mol'),
        S298 = (456.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "2-hydroxy-2-methylpropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.2,146.3,167.3,184.6,211.5,232],'J/(mol*K)'),
        H298 = (-103.9,'kJ/mol'),
        S298 = (366,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "tertbutyloxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([112.8,139.3,162,180.9,210.7,233.2],'J/(mol*K)'),
        H298 = (-86.2,'kJ/mol'),
        S298 = (357.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "2-formyl-2-methylpropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {4,S} {8,D} {15,S}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.6,160.6,182.4,200.7,230.2,252.7],'J/(mol*K)'),
        H298 = (-38.3,'kJ/mol'),
        S298 = (392.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "22-dimethyl-3-oxobutyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
8  O u0 p2 c0 {7,S} {9,S}
9  C u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([152.3,185.2,213.4,237.1,274.4,302.5],'J/(mol*K)'),
        H298 = (-86.5,'kJ/mol'),
        S298 = (435.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "2-carboxy-2-methylpropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {16,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.6,173.4,199.8,221.5,254.4,278.2],'J/(mol*K)'),
        H298 = (-299.4,'kJ/mol'),
        S298 = (418.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "3-methoxy-22-dimethyl-3-oxopropyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {4,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {10,S}
10 C u0 p0 c0 {9,S} {17,S} {18,S} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([161.1,195.1,225.8,252,293.5,324.9],'J/(mol*K)'),
        H298 = (-279.2,'kJ/mol'),
        S298 = (466.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "22-dimethylpropanoyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.1,149.9,174,194.2,226.1,250.1],'J/(mol*K)'),
        H298 = (-92.3,'kJ/mol'),
        S298 = (393.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "33-dimethyl-1-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {9,D}
9  O u0 p2 c0 {8,D}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([144.7,174.1,199.1,219.7,251.7,275.4],'J/(mol*K)'),
        H298 = (62.5,'kJ/mol'),
        S298 = (417,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "33-dimethyl-1-oxobut-1-en-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {2,S} {6,D}
6  C u0 p0 c0 {5,D} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.9,171.5,197.7,219.4,253.1,277.8],'J/(mol*K)'),
        H298 = (56.9,'kJ/mol'),
        S298 = (411.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "3-methoxy-3-methyl-but-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
7  C u1 p0 c0 {3,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([156,190.9,219.7,243,278.8,305.7],'J/(mol*K)'),
        H298 = (34.7,'kJ/mol'),
        S298 = (431.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "3-acetyloxy-3-methyl-but-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {12,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
9  C u1 p0 c0 {3,S} {10,S} {11,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([180.9,219.5,252.1,279.1,321.2,352.5],'J/(mol*K)'),
        H298 = (-186.8,'kJ/mol'),
        S298 = (473.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 261,
    label = "3-hydroxy-3-methyl-but-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  C u1 p0 c0 {3,S} {7,S} {8,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([136.4,163.6,186.1,204.5,232.8,254.1],'J/(mol*K)'),
        H298 = (6.6,'kJ/mol'),
        S298 = (379.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 262,
    label = "2-methyl-but-3-en-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([128.6,156.5,180.8,201,232.3,255.6],'J/(mol*K)'),
        H298 = (24.9,'kJ/mol'),
        S298 = (378.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    label = "3-formyl-3-methyl-but-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  O u0 p2 c0 {5,D}
7  C u1 p0 c0 {3,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([146.3,173.6,197.4,217.6,249.5,273.5],'J/(mol*K)'),
        H298 = (74.3,'kJ/mol'),
        S298 = (416.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 264,
    label = "3-acetyl-3-methyl-but-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  C u1 p0 c0 {3,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([168.9,202.7,232.1,256.8,295.5,324.5],'J/(mol*K)'),
        H298 = (23.1,'kJ/mol'),
        S298 = (452.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "3-carboxy-3-methyl-but-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {17,S}
8  C u1 p0 c0 {3,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([155.4,189.4,217.8,240.8,275.5,300.3],'J/(mol*K)'),
        H298 = (-186.6,'kJ/mol'),
        S298 = (435.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "3-methoxycarbonyl-3-methyl-but-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {12,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
9  C u1 p0 c0 {3,S} {10,S} {11,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([174.3,211.2,243.8,271.3,314.1,346.1],'J/(mol*K)'),
        H298 = (-166.7,'kJ/mol'),
        S298 = (480.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    label = "33-dimethyl-4-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u1 p0 c0 {3,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140,168.3,193.4,214.7,248,272.7],'J/(mol*K)'),
        H298 = (17,'kJ/mol'),
        S298 = (412.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "3-ethenyl-3-methyl-1-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {3,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  C u0 p0 c0 {3,S} {9,D} {17,S}
9  C u0 p0 c0 {8,D} {10,D}
10 O u0 p2 c0 {9,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([161.9,193,218.8,239.9,272.7,297.1],'J/(mol*K)'),
        H298 = (172.2,'kJ/mol'),
        S298 = (436.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "33-dimethyl-1-oxopenta-14-dien-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {3,S} {7,D}
7  C u0 p0 c0 {6,D} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([157.1,188.5,215.7,238.4,273.4,299.2],'J/(mol*K)'),
        H298 = (166.5,'kJ/mol'),
        S298 = (428.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "33-dihydroxybut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  O u0 p2 c0 {3,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  C u1 p0 c0 {3,S} {7,S} {8,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([131.2,163.3,186.9,203,222.3,234.5],'J/(mol*K)'),
        H298 = (-161.4,'kJ/mol'),
        S298 = (361.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    label = "3-hydroxy-3-methoxybut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  O u0 p2 c0 {3,S} {13,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
7  C u1 p0 c0 {3,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([155.4,190.1,217.3,237.7,265.6,284.6],'J/(mol*K)'),
        H298 = (-135.6,'kJ/mol'),
        S298 = (402.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "33-dimethoxybut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
8  C u1 p0 c0 {3,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([169.2,207.8,243.1,272.5,314.3,341.2],'J/(mol*K)'),
        H298 = (-111.1,'kJ/mol'),
        S298 = (447,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 273,
    label = "2-hydroxybut-3-en-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  O u0 p2 c0 {3,S} {10,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.7,152.9,173.1,188.8,211.6,228.2],'J/(mol*K)'),
        H298 = (-143.3,'kJ/mol'),
        S298 = (360,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 274,
    label = "2-methoxybut-3-en-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
7  O u1 p2 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.9,170.9,197.9,220.1,253.7,277.9],'J/(mol*K)'),
        H298 = (-114.7,'kJ/mol'),
        S298 = (410.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
    label = "3-formyl-3-hydroxybut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  O u0 p2 c0 {3,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  O u0 p2 c0 {5,D}
7  C u1 p0 c0 {3,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([146.3,175.8,198.2,215,238.5,254.6],'J/(mol*K)'),
        H298 = (-73.9,'kJ/mol'),
        S298 = (383.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
    label = "3-formyl-3-methoxybut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {17,S}
7  O u0 p2 c0 {6,D}
8  C u1 p0 c0 {3,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([167.1,198.3,224.4,245.6,277.5,300.5],'J/(mol*K)'),
        H298 = (-39,'kJ/mol'),
        S298 = (436.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    label = "3-acetyloxy-3-formylbut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {13,S} {14,S}
2  C u0 p0 c0 {1,D} {3,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {3,S} {9,D} {19,S}
9  O u0 p2 c0 {8,D}
10 C u1 p0 c0 {3,S} {11,S} {12,S}
11 H u0 p0 c0 {10,S}
12 H u0 p0 c0 {10,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([190.7,230.5,262.4,287.3,324.1,350.4],'J/(mol*K)'),
        H298 = (-262.2,'kJ/mol'),
        S298 = (474.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 278,
    label = "3-carboxy-3-hydroxymethylbut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  O u0 p2 c0 {3,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {15,S}
8  C u1 p0 c0 {3,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([163.5,196,219.4,237,261.6,278.4],'J/(mol*K)'),
        H298 = (-333.5,'kJ/mol'),
        S298 = (407.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "3-carboxy-3-methoxybut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {12,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {18,S}
9  C u1 p0 c0 {3,S} {10,S} {11,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([179.4,214.8,244,267.8,303.6,329.1],'J/(mol*K)'),
        H298 = (-298.9,'kJ/mol'),
        S298 = (451.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 280,
    label = "3-hydroxy-3-methoxycarbonylbut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {12,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  O u0 p2 c0 {3,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
9  C u1 p0 c0 {3,S} {10,S} {11,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([182.9,218.9,246.5,268.2,301.1,325.6],'J/(mol*K)'),
        H298 = (-315.7,'kJ/mol'),
        S298 = (452.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 281,
    label = "3-methoxy-3-methoxycarbonylbut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {13,S} {14,S}
2  C u0 p0 c0 {1,D} {3,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {19,S} {20,S} {21,S}
10 C u1 p0 c0 {3,S} {11,S} {12,S}
11 H u0 p0 c0 {10,S}
12 H u0 p0 c0 {10,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([204.8,241.7,273,299.1,339.7,370.2],'J/(mol*K)'),
        H298 = (-276.7,'kJ/mol'),
        S298 = (502.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "3-hydroxy-3-methyl-4-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {14,S}
6  C u1 p0 c0 {3,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([143.4,167.4,187,202.9,227.2,245.2],'J/(mol*K)'),
        H298 = (-122.1,'kJ/mol'),
        S298 = (396.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    label = "3-methoxy-3-methyl-4-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
7  C u1 p0 c0 {3,S} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([164.2,194.6,219.8,240.5,272.6,296.3],'J/(mol*K)'),
        H298 = (-96.3,'kJ/mol'),
        S298 = (439.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    label = "3-acetyloxy-3-methyl-4-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  C u1 p0 c0 {3,S} {10,D}
10 O u0 p2 c0 {9,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([188.4,226.3,257.6,282.8,320.7,347.9],'J/(mol*K)'),
        H298 = (-316.4,'kJ/mol'),
        S298 = (477.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    label = "2-methyl-1-oxobut-3-en-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  O u0 p2 c0 {5,D}
7  O u1 p2 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.3,166.5,188.3,205.7,231.7,250.4],'J/(mol*K)'),
        H298 = (-49.2,'kJ/mol'),
        S298 = (384.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "2-carboxybut-3-en-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {15,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([152.2,184,208.3,227.3,255.5,275.9],'J/(mol*K)'),
        H298 = (-304.9,'kJ/mol'),
        S298 = (397.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "1-methoxy-2-methyl-1-oxobut-3-en-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([171.5,203.5,232.1,256.8,295.8,323.7],'J/(mol*K)'),
        H298 = (-280.8,'kJ/mol'),
        S298 = (458.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "33-diformylbut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {11,S} {12,S}
2  C u0 p0 c0 {1,D} {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {3,S} {7,D} {15,S}
7  O u0 p2 c0 {6,D}
8  C u1 p0 c0 {3,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([156.3,181.2,202,219.2,246.1,266],'J/(mol*K)'),
        H298 = (5.9,'kJ/mol'),
        S298 = (427,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "3-acetyl-3-formylbut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {12,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {15,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {3,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
9  C u1 p0 c0 {3,S} {10,S} {11,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([180.8,214.2,241.2,263.2,296.4,320.6],'J/(mol*K)'),
        H298 = (-48.7,'kJ/mol'),
        S298 = (460.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    label = "33-diacetylbut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {13,S} {14,S}
2  C u0 p0 c0 {1,D} {3,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {3,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
10 C u1 p0 c0 {3,S} {11,S} {12,S}
11 H u0 p0 c0 {10,S}
12 H u0 p0 c0 {10,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([207.5,246.9,279.2,305.3,344.6,373.1],'J/(mol*K)'),
        H298 = (-103.9,'kJ/mol'),
        S298 = (494.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 291,
    label = "3-formyl-3-methyl-4-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {15,S}
6  O u0 p2 c0 {5,D}
7  C u1 p0 c0 {3,S} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158.7,185.3,205.1,221,246.4,265.8],'J/(mol*K)'),
        H298 = (-52.9,'kJ/mol'),
        S298 = (417,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "3-acetyl-3-methyl-4-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u1 p0 c0 {3,S} {9,D}
9  O u0 p2 c0 {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([182,210.5,234.6,255.4,288.9,314.3],'J/(mol*K)'),
        H298 = (-102.3,'kJ/mol'),
        S298 = (462.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "2-hydroxyprop-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {9,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([82.2,101.1,115.6,126.8,143.1,154.9],'J/(mol*K)'),
        H298 = (-12.5,'kJ/mol'),
        S298 = (295.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    label = "2-methoxyprop-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {5,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {2,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103,127.2,146.7,162.4,186.5,204.4],'J/(mol*K)'),
        H298 = (12.5,'kJ/mol'),
        S298 = (334.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    label = "2-acetyloxyprop-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  C u1 p0 c0 {2,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([120.7,151.9,178.1,199.3,230.1,250.8],'J/(mol*K)'),
        H298 = (-195,'kJ/mol'),
        S298 = (395.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 296,
    label = "prop-1-en-2-yl-oxidanyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 O u1 p2 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([74,91,105.7,117.9,136.9,150.9],'J/(mol*K)'),
        H298 = (-35,'kJ/mol'),
        S298 = (305.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    label = "2-formylprop-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  O u0 p2 c0 {3,D}
5  C u1 p0 c0 {2,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89.2,110,127.1,141,162.1,177.3],'J/(mol*K)'),
        H298 = (51.7,'kJ/mol'),
        S298 = (308.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "2-carboxyprop-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {11,S}
6  C u1 p0 c0 {2,S} {7,S} {8,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103,127.6,147.5,163.6,187.9,205],'J/(mol*K)'),
        H298 = (-207.2,'kJ/mol'),
        S298 = (329.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 299,
    label = "2-methylidene-3-oxobutyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
6  C u1 p0 c0 {5,S} {7,S} {8,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([113.1,139.4,161.4,179.5,207.3,227.6],'J/(mol*K)'),
        H298 = (6.2,'kJ/mol'),
        S298 = (354.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
    label = "2-methoxycarbonyl-prop-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
7  C u1 p0 c0 {2,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.8,151.5,176.1,196.5,228.3,251.9],'J/(mol*K)'),
        H298 = (-186.8,'kJ/mol'),
        S298 = (377.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "2-methyl-3-oxoprop-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([87.2,105,120.8,134.3,155.6,171.3],'J/(mol*K)'),
        H298 = (57.6,'kJ/mol'),
        S298 = (327.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "3-methylidene-1-oxobut-1-en-4-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  H u0 p0 c0 {3,S}
6  C u0 p0 c0 {2,S} {7,D} {11,S}
7  C u0 p0 c0 {6,D} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([106,129.3,147.7,162.2,184,199.6],'J/(mol*K)'),
        H298 = (145.8,'kJ/mol'),
        S298 = (339,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    label = "3-methyl-1-oxobuta-13-dien-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {5,D}
5  C u0 p0 c0 {4,D} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([100.7,121.2,138.8,153.6,176.5,193.3],'J/(mol*K)'),
        H298 = (174.9,'kJ/mol'),
        S298 = (352.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 304,
    label = "2-hydroxy-ethyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 O u0 p2 c0 {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([71.8,83,93.1,101.8,116.1,127.2],'J/(mol*K)'),
        H298 = (-24.9,'kJ/mol'),
        S298 = (295.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
    label = "2-methoxy-ethyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.3,105.9,122.5,137,160.4,178.2],'J/(mol*K)'),
        H298 = (-6,'kJ/mol'),
        S298 = (340.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "3-oxo-propyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5 C u0 p0 c0 {4,S} {6,D} {9,S}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([79.9,92.9,105.6,116.7,134.8,148.4],'J/(mol*K)'),
        H298 = (24.7,'kJ/mol'),
        S298 = (317.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    label = "3-oxo-butyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([98.1,118.3,136.9,153,178.6,197.8],'J/(mol*K)'),
        H298 = (-28.4,'kJ/mol'),
        S298 = (361.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "1-hydroxy-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89.7,106.9,122.8,136.7,159.2,176.5],'J/(mol*K)'),
        H298 = (-58.2,'kJ/mol'),
        S298 = (343.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    label = "1-methoxy-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103.8,127.8,150.5,170.5,202.6,226.8],'J/(mol*K)'),
        H298 = (-39.9,'kJ/mol'),
        S298 = (390.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "4-oxo-but-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([96.5,115.9,134.7,151.2,177.9,197.8],'J/(mol*K)'),
        H298 = (-9.2,'kJ/mol'),
        S298 = (367.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "4-oxo-pent-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.7,142.8,166.9,188.1,222,247.4],'J/(mol*K)'),
        H298 = (-61.5,'kJ/mol'),
        S298 = (404.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "13-dimethoxy-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
7  O u0 p2 c0 {6,S} {8,S}
8  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.9,172.7,201.4,226.8,267.4,297.7],'J/(mol*K)'),
        H298 = (-161.9,'kJ/mol'),
        S298 = (469.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 313,
    label = "hydroxy-methyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([46.7,53.2,59.1,64,71.7,77.5],'J/(mol*K)'),
        H298 = (-15.9,'kJ/mol'),
        S298 = (248.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "methoxy-methyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([64.6,76.3,87.7,97.9,114.4,126.9],'J/(mol*K)'),
        H298 = (3.1,'kJ/mol'),
        S298 = (297.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 315,
    label = "methanoyl-oxyl-methyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {7,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([71.5,84.2,95.5,104.9,118.4,127.2],'J/(mol*K)'),
        H298 = (-155.1,'kJ/mol'),
        S298 = (299.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "ethanoyl-oxyl-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([91.8,109.7,125.8,139.8,161.6,177.2],'J/(mol*K)'),
        H298 = (-210.4,'kJ/mol'),
        S298 = (345.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([53.7,64.4,73.7,81.5,93.3,102],'J/(mol*K)'),
        H298 = (15.7,'kJ/mol'),
        S298 = (265.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "carboxy-methyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p2 c0 {4,S} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([69.3,83.5,95.2,104.8,119.4,129.5],'J/(mol*K)'),
        H298 = (-235.3,'kJ/mol'),
        S298 = (288.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "methyloxycarbonyl-methyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.7,107.2,123.9,138.3,161.4,178.3],'J/(mol*K)'),
        H298 = (-214.5,'kJ/mol'),
        S298 = (336.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "2-oxo-propyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([74.5,91.5,106.2,118.5,137.6,151.6],'J/(mol*K)'),
        H298 = (-32.3,'kJ/mol'),
        S298 = (313.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "2-oxo-butyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([100.9,122,141.1,157.4,183.2,202.4],'J/(mol*K)'),
        H298 = (-53,'kJ/mol'),
        S298 = (354,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "23-dioxo-propyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 C u0 p0 c0 {4,S} {7,D} {8,S}
7 O u0 p2 c0 {6,D}
8 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([81.9,98.3,112.3,123.7,139.9,150.1],'J/(mol*K)'),
        H298 = (-92.2,'kJ/mol'),
        S298 = (313.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "23-dioxo-butyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103.4,124.8,143.5,159.2,183.2,199.7],'J/(mol*K)'),
        H298 = (-149.1,'kJ/mol'),
        S298 = (361.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "2-carboxy-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 C u0 p0 c0 {4,S} {7,D} {8,S}
7 O u0 p2 c0 {6,D}
8 O u0 p2 c0 {6,S} {9,S}
9 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([95.5,115.8,131.4,143.5,160.9,173.3],'J/(mol*K)'),
        H298 = (-355.6,'kJ/mol'),
        S298 = (328.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "2-methyloxycarbonyl-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([119.3,142.8,162.8,179.5,205.1,223],'J/(mol*K)'),
        H298 = (-326.6,'kJ/mol'),
        S298 = (385.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "1-hydroxy-ethyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 O u0 p2 c0 {1,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([65.5,78,89.6,99.5,115.2,127.1],'J/(mol*K)'),
        H298 = (-56.2,'kJ/mol'),
        S298 = (295.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "1-methoxy-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([92.4,108.6,123.8,137.3,159.8,177.3],'J/(mol*K)'),
        H298 = (-36.5,'kJ/mol'),
        S298 = (339.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "1-methanoyl-oxyl-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  O u0 p2 c0 {1,D}
3  O u0 p2 c0 {1,S} {4,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([90.2,110.9,128.7,143,163.6,177.7],'J/(mol*K)'),
        H298 = (-197.3,'kJ/mol'),
        S298 = (337.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 329,
    label = "1-ethanoyl-oxyl-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([109.4,135.4,158.5,177.8,207.3,228.2],'J/(mol*K)'),
        H298 = (-251.8,'kJ/mol'),
        S298 = (382.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "1-oxo-prop-2-yl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {9,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([73.5,89.1,103.7,116.3,136.3,151],'J/(mol*K)'),
        H298 = (-27.5,'kJ/mol'),
        S298 = (311.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 331,
    label = "1-carboxy-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89.6,108.4,125.3,139.8,162.5,178.7],'J/(mol*K)'),
        H298 = (-278.5,'kJ/mol'),
        S298 = (334.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "1-methyloxycarbonyl-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([109.5,132.4,154.1,173.4,204.6,227.7],'J/(mol*K)'),
        H298 = (-256.9,'kJ/mol'),
        S298 = (381.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "3-oxo-but-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([96.4,118.6,138.4,155.3,181.9,201.7],'J/(mol*K)'),
        H298 = (-75.6,'kJ/mol'),
        S298 = (355.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "3-oxo-pent-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.7,148.7,173.2,194.2,227.7,252.8],'J/(mol*K)'),
        H298 = (-96.4,'kJ/mol'),
        S298 = (394.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "34-dioxo-but-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {11,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([102.3,125.1,145.2,161.8,186,201.9],'J/(mol*K)'),
        H298 = (-139,'kJ/mol'),
        S298 = (354.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "34-dioxo-pent-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.2,151.2,176.5,197.8,230.2,252.4],'J/(mol*K)'),
        H298 = (-195.3,'kJ/mol'),
        S298 = (400.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "1-carboxy-1-oxo-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {12,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([116.5,143.1,164.7,181.8,206.7,224.4],'J/(mol*K)'),
        H298 = (-404.1,'kJ/mol'),
        S298 = (369.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "1-methyloxycarbonyl-1-oxo-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.3,170.1,197,219.4,252.8,275.7],'J/(mol*K)'),
        H298 = (-373.2,'kJ/mol'),
        S298 = (425.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "dihydroxy-methyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([65.2,74.9,81.9,86.9,93.5,98.4],'J/(mol*K)'),
        H298 = (-206,'kJ/mol'),
        S298 = (278.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "hydroxy-methoxy-methyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.5,102.5,113.8,122.9,137.2,148.3],'J/(mol*K)'),
        H298 = (-185,'kJ/mol'),
        S298 = (321.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "dimethoxy-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.6,125,140.3,154.2,177.5,195.7],'J/(mol*K)'),
        H298 = (-160.7,'kJ/mol'),
        S298 = (372.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "1-hydroxy-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {7,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([66.5,80.7,92.4,102.1,117.1,128.5],'J/(mol*K)'),
        H298 = (-203.2,'kJ/mol'),
        S298 = (280.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "carboxy-hydroxy-methyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p2 c0 {4,S} {8,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([83.7,101.7,116.1,127.8,145.4,157.4],'J/(mol*K)'),
        H298 = (-444.7,'kJ/mol'),
        S298 = (303.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 344,
    label = "methyl-oxycarbonyl-hydroxy-methyl",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([102.7,124.9,144.4,161.1,187.3,206],'J/(mol*K)'),
        H298 = (-423.7,'kJ/mol'),
        S298 = (352.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 345,
    label = "1-methoxy-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([92.2,109,124.6,138,158.9,174],'J/(mol*K)'),
        H298 = (-156.7,'kJ/mol'),
        S298 = (339.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 346,
    label = "carboxy-methoxy-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {11,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([109.9,129.7,147,161.2,182.6,197.5],'J/(mol*K)'),
        H298 = (-399.6,'kJ/mol'),
        S298 = (367.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 347,
    label = "methyloxycarbonyl-methoxy-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.1,149.4,172.1,192.3,225,248.6],'J/(mol*K)'),
        H298 = (-377.3,'kJ/mol'),
        S298 = (414.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 348,
    label = "13-dioxo-prop-2-yl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {7,S}
2 O u0 p2 c0 {1,D}
3 C u1 p0 c0 {1,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,D} {8,S}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([79.1,93.7,106.8,117.9,134.7,146.2],'J/(mol*K)'),
        H298 = (-104.3,'kJ/mol'),
        S298 = (319.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 349,
    label = "1-carboxy-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {8,S}
2 O u0 p2 c0 {1,D}
3 C u1 p0 c0 {1,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,S} {6,D} {7,S}
6 O u0 p2 c0 {5,D}
7 O u0 p2 c0 {5,S} {9,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([95.6,114.2,130.6,144.3,164.4,177.1],'J/(mol*K)'),
        H298 = (-357.6,'kJ/mol'),
        S298 = (335.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "1-methyloxycarbonyl-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {9,S}
2  O u0 p2 c0 {1,D}
3  C u1 p0 c0 {1,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {10,S}
6  O u0 p2 c0 {5,S} {11,S}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([115,137.8,159.1,177.5,206,225.7],'J/(mol*K)'),
        H298 = (-339.4,'kJ/mol'),
        S298 = (382,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "dicarboxy-methyl",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {10,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.1,129.5,149.9,166.2,189.4,204.3],'J/(mol*K)'),
        H298 = (-612.4,'kJ/mol'),
        S298 = (343.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "carboxy-methyloxycarbonyl-methyl",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {11,S} {12,S} {13,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([124.6,152.9,178,199,230.6,252.6],'J/(mol*K)'),
        H298 = (-595.8,'kJ/mol'),
        S298 = (390.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "ethoxyl",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([65.5,78.3,90.3,100.7,117.7,130.5],'J/(mol*K)'),
        H298 = (-12.9,'kJ/mol'),
        S298 = (293.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "propoxyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  O u1 p2 c0 {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([85.1,105.5,123.6,139,163.4,181.6],'J/(mol*K)'),
        H298 = (-33.7,'kJ/mol'),
        S298 = (322.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "hydroxy-methoxyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([54.6,65.8,75.4,83,93.9,101.3],'J/(mol*K)'),
        H298 = (-171.6,'kJ/mol'),
        S298 = (269.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 356,
    label = "methoxy-methoxyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([72.8,88.6,103.2,115.7,135.1,149.3],'J/(mol*K)'),
        H298 = (-148,'kJ/mol'),
        S298 = (318.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 357,
    label = "ethoxy-methoxyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  O u1 p2 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([97.2,119,139.2,156.2,182.6,201.8],'J/(mol*K)'),
        H298 = (-181.9,'kJ/mol'),
        S298 = (357.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "2-oxo-ethoxyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 O u0 p2 c0 {1,D}
3 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([66.2,79.8,91.3,100.4,113.8,123],'J/(mol*K)'),
        H298 = (-76.5,'kJ/mol'),
        S298 = (294.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "2-oxo-propoxyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  O u1 p2 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([87.4,106.3,123.1,137.2,158.4,173.3],'J/(mol*K)'),
        H298 = (-134,'kJ/mol'),
        S298 = (339.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 360,
    label = "carboxy-methoxyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5 O u1 p2 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([83.9,100.2,113,123,138,148.6],'J/(mol*K)'),
        H298 = (-335.6,'kJ/mol'),
        S298 = (307.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 362,
    label = "carboxy-oxyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u1 p2 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([55.8,65.8,73.6,79.7,87.7,92.4],'J/(mol*K)'),
        H298 = (-368.9,'kJ/mol'),
        S298 = (279.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "methyloxycarbonyl-methoxyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u1 p2 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([74.1,88.9,102.4,113.6,130.2,141.3],'J/(mol*K)'),
        H298 = (-347.5,'kJ/mol'),
        S298 = (327.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 364,
    label = "ethanoyl-oxyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u1 p2 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([61,73.7,84.9,94.3,108.5,118.5],'J/(mol*K)'),
        H298 = (-190.6,'kJ/mol'),
        S298 = (298.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 365,
    label = "propanoyl-oxyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u1 p2 c0 {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([82.9,101,117.4,131.3,152.9,168.6],'J/(mol*K)'),
        H298 = (-210.7,'kJ/mol'),
        S298 = (340.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 366,
    label = "dioxo-ethyl-oxyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {6,S}
2 O u0 p2 c0 {1,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u1 p2 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([70.8,81.8,90.5,97.2,106.6,112.5],'J/(mol*K)'),
        H298 = (-209.9,'kJ/mol'),
        S298 = (310,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 367,
    label = "12-dioxo-propyl-oxyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u1 p2 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([92,108.9,123.1,134.6,151.2,162.5],'J/(mol*K)'),
        H298 = (-272.4,'kJ/mol'),
        S298 = (355.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 368,
    label = "carboxy-carbonyl-oxyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u1 p2 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.5,103.2,113.8,121.3,131.1,137.1],'J/(mol*K)'),
        H298 = (-468.4,'kJ/mol'),
        S298 = (330.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "methyloxycarbonyl-carbonyl-oxyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u1 p2 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([104.1,123,139.5,153.3,174.4,188.9],'J/(mol*K)'),
        H298 = (-454.3,'kJ/mol'),
        S298 = (377.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 370,
    label = "propanoyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 C u1 p0 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([74.7,88,101,112.6,131.5,145.9],'J/(mol*K)'),
        H298 = (-28.3,'kJ/mol'),
        S298 = (319.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 371,
    label = "butanoyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u1 p0 c0 {3,S} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([96.9,116.9,135.7,152.1,178.3,197.9],'J/(mol*K)'),
        H298 = (-49.3,'kJ/mol'),
        S298 = (360.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 372,
    label = "2-oxo-butyl-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u1 p0 c0 {5,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([137.6,158.6,177,193.2,219.7,239.9],'J/(mol*K)'),
        H298 = (-171.8,'kJ/mol'),
        S298 = (412.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 373,
    label = "ethoxy-methyl-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u1 p0 c0 {4,S} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([120.4,143.3,162.6,178.6,203.6,222.1],'J/(mol*K)'),
        H298 = (-164.4,'kJ/mol'),
        S298 = (384.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 374,
    label = "hydroxy-methyl-carbonyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([72.9,84.1,93.3,100.7,111.6,119.3],'J/(mol*K)'),
        H298 = (-150.9,'kJ/mol'),
        S298 = (303.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 375,
    label = "methoxy-methyl-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u1 p0 c0 {3,S} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([93.4,110.7,125.4,137.3,155.8,169.5],'J/(mol*K)'),
        H298 = (-129.4,'kJ/mol'),
        S298 = (347.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 376,
    label = "2-oxo-ethyl-carbonyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {6,S}
2 O u0 p2 c0 {1,D}
3 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4 C u1 p0 c0 {3,S} {5,D}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([83.9,95.1,105.1,113.8,127.8,138.1],'J/(mol*K)'),
        H298 = (-94,'kJ/mol'),
        S298 = (334.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 377,
    label = "2-oxo-propyl-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u1 p0 c0 {4,S} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.5,125.5,140.2,152.9,173.2,188.6],'J/(mol*K)'),
        H298 = (-149.5,'kJ/mol'),
        S298 = (373.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 378,
    label = "carboxy-methyl-carbonyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5 C u1 p0 c0 {4,S} {6,D}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([99.6,114.4,126.3,136,150.7,161.2],'J/(mol*K)'),
        H298 = (-357,'kJ/mol'),
        S298 = (355.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 379,
    label = "methyloxycarbonyl-methyl-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
6  C u1 p0 c0 {5,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([115.1,133.9,151.8,167.7,193.5,212.7],'J/(mol*K)'),
        H298 = (-339.5,'kJ/mol'),
        S298 = (402.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 380,
    label = "methoxy-methanoyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([62.4,73.4,83.9,93.2,107.8,118.2],'J/(mol*K)'),
        H298 = (-156.4,'kJ/mol'),
        S298 = (307.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 381,
    label = "ethoxy-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u1 p0 c0 {3,S} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([85.5,103.5,119.9,133.9,155.5,171],'J/(mol*K)'),
        H298 = (-192.1,'kJ/mol'),
        S298 = (346.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 382,
    label = "methanoyl-oxyl-carbonyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {6,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 C u1 p0 c0 {3,S} {5,D}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([75.4,86.8,95.3,101.3,109,113.5],'J/(mol*K)'),
        H298 = (-279.1,'kJ/mol'),
        S298 = (311.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 383,
    label = "ethanoyl-oxyl-carbonyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {5,S}
5 C u1 p0 c0 {4,S} {6,D}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([99.9,118.2,131.9,141.9,155.3,164.1],'J/(mol*K)'),
        H298 = (-338.8,'kJ/mol'),
        S298 = (354.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 384,
    label = "carboxy-oxyl-carbonyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {5,S}
5 C u1 p0 c0 {4,S} {6,D}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([92,104.8,114.3,121.5,131.4,137.4],'J/(mol*K)'),
        H298 = (-494.6,'kJ/mol'),
        S298 = (327.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 385,
    label = "methyloxycarbonyl-oxyl-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {6,S}
6  C u1 p0 c0 {5,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([111.5,131.7,148.7,161.7,179.2,189.7],'J/(mol*K)'),
        H298 = (-496.2,'kJ/mol'),
        S298 = (378.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 386,
    label = "carboxy-carbonyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u1 p0 c0 {2,S} {5,D}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([74.4,85.8,95,102.1,111.5,116.6],'J/(mol*K)'),
        H298 = (-302.6,'kJ/mol'),
        S298 = (310.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 387,
    label = "methyloxydicarbonyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 C u1 p0 c0 {3,S} {6,D}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([93.3,108.9,123.1,135.3,153.6,165.5],'J/(mol*K)'),
        H298 = (-285.9,'kJ/mol'),
        S298 = (359.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 388,
    label = "ethanoyl-carbonyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u1 p0 c0 {2,S} {5,D}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([79.1,91.9,103.3,113.1,128.5,139.7],'J/(mol*K)'),
        H298 = (-115,'kJ/mol'),
        S298 = (326.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 389,
    label = "propanoyl-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u1 p0 c0 {3,S} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([101.7,120.3,137.1,151.4,173.9,190.4],'J/(mol*K)'),
        H298 = (-136.9,'kJ/mol'),
        S298 = (370.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 390,
    label = "2-oxo-ethanoyl-carbonyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {7,S}
2 O u0 p2 c0 {1,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 C u1 p0 c0 {3,S} {6,D}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([85.9,98.4,109,117.8,130.7,138.9],'J/(mol*K)'),
        H298 = (-185.1,'kJ/mol'),
        S298 = (327.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 391,
    label = "2-oxo-propanoyl-carbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u1 p0 c0 {4,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([106.5,124.5,140.1,153.5,174.6,189.5],'J/(mol*K)'),
        H298 = (-249.1,'kJ/mol'),
        S298 = (372.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 392,
    label = "carboxy-dicarbonyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 C u1 p0 c0 {4,S} {7,D}
7 O u0 p2 c0 {6,D}
8 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([101.6,116,127.3,136.3,149.8,159.5],'J/(mol*K)'),
        H298 = (-445.1,'kJ/mol'),
        S298 = (346.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 393,
    label = "methyloxytricarbonyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u1 p0 c0 {5,S} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.2,142.8,160.4,175.6,198.6,213.5],'J/(mol*K)'),
        H298 = (-420.8,'kJ/mol'),
        S298 = (396.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 394,
    label = "2-ketenyl-ethyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([90.6,107.7,122.7,135.2,154.9,169.6],'J/(mol*K)'),
        H298 = (128.2,'kJ/mol'),
        S298 = (348.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 395,
    label = "2-methyl-ketenyl-ethyl",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {8,S}
6  C u0 p0 c0 {5,D} {7,D}
7  O u0 p2 c0 {6,D}
8  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([114.5,135.9,155.4,172.4,199.4,219.7],'J/(mol*K)'),
        H298 = (102.8,'kJ/mol'),
        S298 = (395.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 396,
    label = "1-ketenyl-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.2,130.8,151.6,169.4,197.7,218.6],'J/(mol*K)'),
        H298 = (93.5,'kJ/mol'),
        S298 = (397.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 397,
    label = "1-methyl-ketenyl-prop-2-yl",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  H u0 p0 c0 {2,S}
4  H u0 p0 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {7,D} {9,S}
7  C u0 p0 c0 {6,D} {8,D}
8  O u0 p2 c0 {7,D}
9  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132.9,160.2,185.4,207.4,242.6,268.7],'J/(mol*K)'),
        H298 = (67.8,'kJ/mol'),
        S298 = (438.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 398,
    label = "2-hydroxy-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([90.1,107.8,124.1,138.3,160.9,178],'J/(mol*K)'),
        H298 = (-98.8,'kJ/mol'),
        S298 = (336.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 399,
    label = "2-hydroxy-but-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([113.3,136,157.3,175.8,205.6,228.1],'J/(mol*K)'),
        H298 = (-118.3,'kJ/mol'),
        S298 = (382.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 400,
    label = "3-hydroxy-pent-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {12,S}
5  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([133.7,163.1,190.2,213.5,250.6,278.6],'J/(mol*K)'),
        H298 = (-136.5,'kJ/mol'),
        S298 = (426.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 401,
    label = "11-dihydroxy-ethyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([87.9,103.3,115.9,125.6,139.4,149.5],'J/(mol*K)'),
        H298 = (-255.9,'kJ/mol'),
        S298 = (321.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 402,
    label = "1-hydroxy-1-methoxy-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {9,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.5,129.4,146.7,161.2,183.4,199.7],'J/(mol*K)'),
        H298 = (-231.5,'kJ/mol'),
        S298 = (364.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 403,
    label = "1-oxo-2-hydroxy-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {9,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89.7,108,124.4,138.3,160.7,177.7],'J/(mol*K)'),
        H298 = (-256.3,'kJ/mol'),
        S298 = (325.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 404,
    label = "1-carboxy-1-hydroxy-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {10,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([104.7,127,145.7,161.6,186.6,204.9],'J/(mol*K)'),
        H298 = (-495.3,'kJ/mol'),
        S298 = (348.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 405,
    label = "1-methoxy-1-oxo-2-hydroxy-prop-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.5,149.7,173.2,193.5,226.3,251.2],'J/(mol*K)'),
        H298 = (-473.7,'kJ/mol'),
        S298 = (398.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 406,
    label = "dihydroxy-methoxy-methyl",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {7,S}
4  O u0 p2 c0 {2,S} {5,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103.2,117.6,129.8,139.8,155.2,166.7],'J/(mol*K)'),
        H298 = (-393.5,'kJ/mol'),
        S298 = (358.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 407,
    label = "hydroxy-dimethoxy-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {10,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([125.2,143.5,160.6,175.5,199.1,216.9],'J/(mol*K)'),
        H298 = (-369.4,'kJ/mol'),
        S298 = (402.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 408,
    label = "11-dihydroxy-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {7,S}
4 C u0 p0 c0 {2,S} {5,D} {8,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([84.1,103.6,118.7,130.1,145.5,155.5],'J/(mol*K)'),
        H298 = (-418.6,'kJ/mol'),
        S298 = (295.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 409,
    label = "carboxy-dihydroxy-methyl",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 O u0 p2 c0 {4,S} {8,S}
6 O u0 p2 c0 {4,S} {9,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103.7,123.4,139.1,151.5,168,177.1],'J/(mol*K)'),
        H298 = (-639.4,'kJ/mol'),
        S298 = (324.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 410,
    label = "methyloxycarbonyl-dihydroxy-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u1 p0 c0 {3,S} {6,S} {7,S}
6  O u0 p2 c0 {5,S} {11,S}
7  O u0 p2 c0 {5,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.8,147.4,168.3,185.2,209,224.2],'J/(mol*K)'),
        H298 = (-619.6,'kJ/mol'),
        S298 = (384.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 411,
    label = "1-methoxy-1-hydroxy-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.8,128,146.6,161.6,184.4,201.2],'J/(mol*K)'),
        H298 = (-389.8,'kJ/mol'),
        S298 = (352.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 412,
    label = "carboxy-hydroxy-methoxy-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([127.9,152.8,172.6,188.1,210.8,226.2],'J/(mol*K)'),
        H298 = (-608.1,'kJ/mol'),
        S298 = (380.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 413,
    label = "methyloxycarbonyl-hydroxy-methoxy-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([144.5,171.9,196.5,217.9,251.7,275.4],'J/(mol*K)'),
        H298 = (-585.2,'kJ/mol'),
        S298 = (429.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 414,
    label = "13-dioxo-2-hydroxy-prop-2-yl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {7,S}
2 O u0 p2 c0 {1,D}
3 C u1 p0 c0 {1,S} {4,S} {5,S}
4 O u0 p2 c0 {3,S} {8,S}
5 C u0 p0 c0 {3,S} {6,D} {9,S}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([92.9,111.8,127.4,140,159,173.1],'J/(mol*K)'),
        H298 = (-331.3,'kJ/mol'),
        S298 = (325,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 415,
    label = "1-carboxy-1-hydroxy-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  O u0 p2 c0 {1,D}
3  C u1 p0 c0 {1,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {9,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {10,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([101.5,123,141,155.8,178.4,194.9],'J/(mol*K)'),
        H298 = (-590.3,'kJ/mol'),
        S298 = (335.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 416,
    label = "1-methyloxycarbonyl-1-hydroxy-2-oxo-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {9,S}
2  O u0 p2 c0 {1,D}
3  C u1 p0 c0 {1,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.6,152.5,176,196.2,228.1,250.7],'J/(mol*K)'),
        H298 = (-550.1,'kJ/mol'),
        S298 = (399.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 417,
    label = "dicarboxy-hydroxy-methyl",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  O u0 p2 c0 {4,S} {10,S}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {11,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.2,146.9,167.9,184.9,209.7,225.8],'J/(mol*K)'),
        H298 = (-834.5,'kJ/mol'),
        S298 = (359.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 418,
    label = "1-carboxy-1-hydroxy-2-methyloxycarbonyl-ethyl",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  O u0 p2 c0 {4,S} {11,S}
6  C u0 p0 c0 {4,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {9,S}
9  C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([148.6,178.9,204.9,226.2,257.5,277.9],'J/(mol*K)'),
        H298 = (-793.5,'kJ/mol'),
        S298 = (421.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 419,
    label = "dimethyloxycarbonyl-hydroxy-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u1 p0 c0 {3,S} {6,S} {7,S}
6  O u0 p2 c0 {5,S} {14,S}
7  C u0 p0 c0 {5,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,S} {10,S}
10 C u0 p0 c0 {9,S} {15,S} {16,S} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([164.7,198.4,229.6,256.5,298.4,327.3],'J/(mol*K)'),
        H298 = (-773.6,'kJ/mol'),
        S298 = (468.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 420,
    label = "ketenyl-methyl",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {7,S}
5 C u0 p0 c0 {4,D} {6,D}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([72.3,84.4,94.1,101.9,114,123],'J/(mol*K)'),
        H298 = (99.4,'kJ/mol'),
        S298 = (292.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 421,
    label = "methyl-ketenyl-methyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  H u0 p0 c0 {3,S}
6  C u0 p0 c0 {2,D} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([92,109.3,124.3,137.1,157.2,172.2],'J/(mol*K)'),
        H298 = (72.2,'kJ/mol'),
        S298 = (334.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 422,
    label = "1-ketenyl-ethyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,D} {9,S}
4 H u0 p0 c0 {2,S}
5 C u0 p0 c0 {3,D} {10,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
10 O u0 p2 c0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([89,106.9,122.5,135.7,156.5,171.8],'J/(mol*K)'),
        H298 = (67.5,'kJ/mol'),
        S298 = (341.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 423,
    label = "1-methyl-ketenyl-ethyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {4,D} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([113,134.6,154.6,172.2,200.3,221.4],'J/(mol*K)'),
        H298 = (41.1,'kJ/mol'),
        S298 = (388.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 424,
    label = "ethyl-ketenyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([90.5,107.9,123.2,136.3,157,172.5],'J/(mol*K)'),
        H298 = (122.1,'kJ/mol'),
        S298 = (334.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 425,
    label = "propyl-ketenyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {5,D}
5  C u0 p0 c0 {4,D} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([112,136.6,157.8,175.7,203.6,224.2],'J/(mol*K)'),
        H298 = (98.6,'kJ/mol'),
        S298 = (375,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 426,
    label = "ethenoxy-methyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {7,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {9,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u1 p0 c0 {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([78.3,95.8,110.4,122.2,139.5,152],'J/(mol*K)'),
        H298 = (90.7,'kJ/mol'),
        S298 = (306.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 427,
    label = "1-ethenoxy-ethyl",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103,126.6,146.8,162.9,186.9,204.1],'J/(mol*K)'),
        H298 = (49.4,'kJ/mol'),
        S298 = (349.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 428,
    label = "1-hydroxy-allyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([83.8,101.1,115.2,126.5,143.1,155.3],'J/(mol*K)'),
        H298 = (-12.8,'kJ/mol'),
        S298 = (299.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 429,
    label = "1-methoxy-allyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([97.4,121.8,143.3,160.8,186.9,205.5],'J/(mol*K)'),
        H298 = (9.8,'kJ/mol'),
        S298 = (344.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 430,
    label = "1-oxo-but-3-en-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.3,110,128.4,143.2,164.9,180.2],'J/(mol*K)'),
        H298 = (33.4,'kJ/mol'),
        S298 = (316,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 431,
    label = "1-carboxy-prop-2-en-1-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {11,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([107.5,130.4,149.5,165.3,189.4,206.3],'J/(mol*K)'),
        H298 = (-221,'kJ/mol'),
        S298 = (338.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 432,
    label = "methyloxycarbonyl-prop-1-en-1-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([127.4,154.4,178.3,198.7,231,254.8],'J/(mol*K)'),
        H298 = (-200.5,'kJ/mol'),
        S298 = (385.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 433,
    label = "2-hydroxy-but-3-en-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([109.3,131.1,149.5,164.7,188.2,205.6],'J/(mol*K)'),
        H298 = (-59,'kJ/mol'),
        S298 = (342,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 434,
    label = "3-hydroxy-pent-1-en-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {10,S}
5  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([130.1,157.7,181.9,202.1,233.8,257.4],'J/(mol*K)'),
        H298 = (-79.9,'kJ/mol'),
        S298 = (388.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 435,
    label = "3-hydroxy-pent-14-dien-3-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.8,147.8,171.3,189.4,215.4,233.7],'J/(mol*K)'),
        H298 = (10.9,'kJ/mol'),
        S298 = (350.1,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 436,
    label = "11-dihydroxy-allyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {9,S}
5  O u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.7,125.7,140.1,150.7,165.6,176.5],'J/(mol*K)'),
        H298 = (-207.5,'kJ/mol'),
        S298 = (320.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 437,
    label = "1-hydroxy-1-methoxy-allyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {10,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([129.5,153.6,171.9,186.5,208.9,225.9],'J/(mol*K)'),
        H298 = (-181.4,'kJ/mol'),
        S298 = (364.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 438,
    label = "1-oxo-2-hydroxy-but-3-en-2-yl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([106,131.2,151.3,167.2,191.3,208.7],'J/(mol*K)'),
        H298 = (-181.9,'kJ/mol'),
        S298 = (329.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 439,
    label = "1-carboxy-1-hydroxy-allyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123,150.7,172.5,190.1,216.8,235.6],'J/(mol*K)'),
        H298 = (-425.3,'kJ/mol'),
        S298 = (351.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 440,
    label = "1-methyloxycarbonyl-1-hydroxy-allyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {8,S}
8  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([141.9,173.6,200.1,222,256,281.2],'J/(mol*K)'),
        H298 = (-405,'kJ/mol'),
        S298 = (399.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 441,
    label = "1-hydroxy-ethenyl",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([59.5,68.5,75.8,81.7,90.9,98],'J/(mol*K)'),
        H298 = (113.9,'kJ/mol'),
        S298 = (275.5,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 442,
    label = "1-methoxy-ethenyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([76.9,90.3,103.1,114.4,132.7,146.6],'J/(mol*K)'),
        H298 = (135.6,'kJ/mol'),
        S298 = (320.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 443,
    label = "1-ethoxy-ethenyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u1 p0 c0 {1,D} {3,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([99.6,119.8,138.2,154,179.2,198.2],'J/(mol*K)'),
        H298 = (100.4,'kJ/mol'),
        S298 = (367.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 444,
    label = "1-oxo-prop-2-en-2-yl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([68.5,80.8,91.3,100.1,113.6,123.4],'J/(mol*K)'),
        H298 = (169.1,'kJ/mol'),
        S298 = (288.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 445,
    label = "1-carboxy-ethenyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p2 c0 {3,S} {8,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([84.9,101.4,114.8,125.4,140.4,150.3],'J/(mol*K)'),
        H298 = (-72.2,'kJ/mol'),
        S298 = (317.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 446,
    label = "1-methyloxycarbonyl-ethenyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103.4,123.8,142.5,158.8,183.6,200.4],'J/(mol*K)'),
        H298 = (-52.1,'kJ/mol'),
        S298 = (364.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 447,
    label = "vinyloxyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([53.1,63.8,73.1,80.8,92.6,101.2],'J/(mol*K)'),
        H298 = (14.6,'kJ/mol'),
        S298 = (258.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 448,
    label = "oxo-allyl",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u1 p0 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([71.2,83.5,93.4,101.5,113.9,123],'J/(mol*K)'),
        H298 = (96.1,'kJ/mol'),
        S298 = (285.7,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

