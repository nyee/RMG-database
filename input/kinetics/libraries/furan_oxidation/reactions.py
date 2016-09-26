#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""
Mostly taken from Tian et al
"An experimental and kinetic investigation of premixed/furan/oxygen/argon flames"  Combustion and Flame, 158, 2011, 756-773
"""
entry(
    index = 1,
    label = "furan <=> FA",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+12, 'cm^3/(mol*s)'),
        n = 0.416,
        Ea = (70.891, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "furan <=> C2H2 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+14, 'cm^3/(mol*s)'),
        n = 0.534,
        Ea = (86.591, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "furan + O2 <=> furyl-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.0e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (70.68, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "furan + O2 <=> furyl-3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.0e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (70.88, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "furan + H <=> C4H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "furan + H <=> C4H5O-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 7,
    label = "furan + OH <=> C2H3CHO + CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.04, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "furan + H <=> furyl-2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.2e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (12.28, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "furan + H <=> furyl-3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.2e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (12.28, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "furan + O <=> furyl-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8.96, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "furan + O <=> furyl-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8.96, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = "furan + OH <=> furyl-2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (2.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 13,
    label = "furan + OH <=> furyl-3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (2.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 14,
    label = "furan + CH3 <=> furyl-2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+00, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (12.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 15,
    label = "furan + CH3 <=> furyl-3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+00, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (12.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 16,
    label = "furyl-2 <=> CHCHCHCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0.341,
        Ea = (34.511, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 17,
    label = "furyl-3 <=> CHCCHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0.306,
        Ea = (31.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 18,
    label = "furyl-2 + O2 <=> CH2CHCO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 19,
    label = "furyl-2 + O2 <=> CHCHCHO + CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+11, 'cm^3/(mol*s)'),
        n = -0.29,
        Ea = (10.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = "furyl-3 + O2 <=> CH2CHCO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = "furyl-3 + O2 <=> CHCHCHO + CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+11, 'cm^3/(mol*s)'),
        n = -0.29,
        Ea = (10.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 22,
    label = "C4H5O-2 <=> C2H2 + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.1e+12, 'cm^3/(mol*s)'),
        n = 0.246,
        Ea = (34.925, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = "C4H5O-3 <=> CH2CHCHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0.085,
        Ea = (22.555, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "furfural <=> furan + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.0e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),

	
)
