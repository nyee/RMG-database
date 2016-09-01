#!/usr/bin/env python
# encoding: utf-8

name = "isobutanol1"
shortDesc = u"Library using rates from Shamel's paper"
longDesc = u"""
This library is a test created to showcase the createKineticsLibrary.py script
"""
entry(
    index = 0,
    label = "C4H10O + HO <=> C4H9O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3610, 'cm^3/(mol*s)'), n=2.89, Ea=(-2.29, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""Analogous rate for n-butanol extended to isobutanol""",
    longDesc = 
u"""
Rate comes from quantum calculation by J. Zador at CCSD(T) level
[ This rate was obtained by personal communication as of Sept 2012]
""",
)

entry(
    index = 1,
    label = "C4H10O + HO <=> C4H9O-2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.54, 'cm^3/(mol*s)'), n=3.7, Ea=(-4.94, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""Evans Polyani like correlation on beta H-abstraction from n-butanol""",
    longDesc = 
u"""
Evans-Polyani type correlations E_iso = E_n + 0.4 (BDE_n - BdE_iso)to get
energy barrier using bond dissociation energies. CalculatedS. Merchant.
Original rate parameters for n-butanol from Zhou et aland calculated with
VRC-TST at CCSD(T)/cc-pVQZ/MP2/6-311G(d,p)
""",
)

entry(
    index = 2,
    label = "C4H10O + HO <=> C4H9O-3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(0.51, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Eric S. Kwok", "Roger Atkinson"],
        title = u'Estimation of Hydroxyl Radical Reaction Rate Constants for Gas-Phase Organic Compounds using a Structure-Reactivity Relationship: An Update',
        journal = "Atmos. Environ.",
        volume = "29",
        pages = """1685-1695""",
        year = "1995",
    ),
    referenceType = "Article",
    shortDesc = u"""Structure-reactivity approach proposed by Atkins for OH hydrogen abstraction from organic compounds""",
)

entry(
    index = 3,
    label = "C4H10O + HO <=> C4H9O-4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-0.58, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Chong-Wen Zhou", "John M. Simmie", "Henry J. Curran"],
        title = u'Rate constants for hydrogen-abstraction by OH from n-butanol',
        journal = "Combust. Flame.",
        volume = "158",
        pages = """726-731""",
        year = "2011",
    ),
    referenceType = "Article",
    shortDesc = u"""Analagous n-butanol rate calculated with conventional TST at CCSD(T)/cc-pVQZ/MP2/6-311G(d,p) by Zhou et al""",
    longDesc = 
u"""
Rate calculated by TST at CCSD(T)/cc-pVQZ/MP2/6-311G(d,p).
""",
)

entry(
    index = 4,
    label = "C4H10O + H <=> C4H9O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.09e+07, 'cm^3/(mol*s)'),
        n = 1.59,
        Ea = (3.35, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 5,
    label = "C4H10O + H <=> C4H9O-2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+07, 'cm^3/(mol*s)'),
        n = 1.48,
        Ea = (3.44, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 6,
    label = "C4H10O + H <=> C4H9O-3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+07, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (7.45, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 7,
    label = "C4H10O + H <=> C4H9O-4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40500, 'cm^3/(mol*s)'), n=2.38, Ea=(9.34, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 8,
    label = "C4H10O + CH3 <=> C4H9O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.87, 'cm^3/(mol*s)'), n=3.5, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 9,
    label = "C4H10O + CH3 <=> C4H9O-2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(414, 'cm^3/(mol*s)'), n=2.87, Ea=(4.89, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 10,
    label = "C4H10O + CH3 <=> C4H9O-3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.61, 'cm^3/(mol*s)'), n=3.59, Ea=(7.7, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 11,
    label = "C4H10O + CH3 <=> C4H9O-4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.32, 'cm^3/(mol*s)'), n=3.49, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 12,
    label = "C4H10O + C2H3 <=> C4H9O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0519, 'cm^3/(mol*s)'), n=3.9, Ea=(0.86, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 13,
    label = "C4H10O + C2H3 <=> C4H9O-2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0269, 'cm^3/(mol*s)'), n=3.9, Ea=(0.68, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 14,
    label = "C4H10O + C2H3 <=> C4H9O-3 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0011, 'cm^3/(mol*s)'), n=4.55, Ea=(3.5, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 15,
    label = "C4H9O + H2O2 <=> C4H10O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(56.9, 'cm^3/(mol*s)'), n=3.04, Ea=(1.2, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 16,
    label = "C4H9O-2 + H2O2 <=> C4H10O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.91, 'cm^3/(mol*s)'), n=3.31, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 17,
    label = "C4H9O-3 + H2O2 <=> C4H10O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01, 'cm^3/(mol*s)'), n=3.28, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Shamel S. Merchant", "Everton Fernando Zanoelo", "Raymond L. Speth", "Michael R. Harper", "Kevin M. Van Geem", "William H. Green"],
        title = u'Combustion and pyrolysis of iso-butanol: Experimental and chemical kinetic modeling study',
        journal = "Combust. Flame.",
        volume = "160",
        pages = """1907-1929""",
        year = "2013",
    ),
    referenceType = "Article",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
""",
)

