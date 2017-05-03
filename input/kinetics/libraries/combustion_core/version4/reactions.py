#!/usr/bin/env python
# encoding: utf-8

name = "combustion_core/version4"
shortDesc = u""
longDesc = u"""
4th version of core combustion mechanisms developed at Leeds University
http://mcm.leeds.ac.uk/MCM/
"""
entry(
    index = 0,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+06, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 2.1,
        Ea = (6.57, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.06e+06, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 2.1,
        Ea = (6.57, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "C4H2 + O <=> C3H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.89e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (5.64, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "O2 + CO <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (196.9, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "O2 + CH <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "O2 + CH <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "O2 + CH2 <=> CO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 7,
    label = "O2 + CH2 <=> CO2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "O2 + CH2 <=> CO + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.15e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "O2 + CH2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.48e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "O2 + CH2 <=> CH2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "O2 + CH2(S) <=> CO + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.13e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = "O2 + HCO <=> HO2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.12e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (7.09, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 13,
    label = "O2 + HCCO <=> CO + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+12, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (3.58, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 14,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+07, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 1.3,
        Ea = (-3.2, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 15,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+14, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (99.02, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 16,
    label = "CO + CH <=> HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.77e+11, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-7.15, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 17,
    label = "CO2 + CH <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (2.87, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 18,
    label = "CO2 + CH2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+10, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 19,
    label = "CH2CO + H <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (14.13, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = "CH2CO + O <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+12, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = "CH2CO + O <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 22,
    label = "CH2CO + O <=> HCO + H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = "CH2CO + O <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "CH2CO + OH <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 25,
    label = "CH2CO + OH <=> CH2OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.68e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 26,
    label = "H + HCO <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = "H + HCCO <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+14, 'cm^3/(mol*s)', '*|/', 1.4),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 28,
    label = "CH + O <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 29,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 30,
    label = "C2H + O <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 31,
    label = "C2H + OH <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 32,
    label = "C2H3 + O <=> CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 33,
    label = "H2CCCH + O <=> C2H2 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 34,
    label = "O + HCO <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 35,
    label = "O + HCCO <=> H + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 36,
    label = "OH + HCO <=> H2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+14, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = "OH + HCCO <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 38,
    label = "OH + HCCO <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 39,
    label = "HCO + HCO <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 40,
    label = "HCCO + HCCO <=> C2H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 41,
    label = "CH + HCCO <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 42,
    label = "CH2 + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 43,
    label = "CH2 + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 44,
    label = "CH2 + HCO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 45,
    label = "CH2 + HCCO <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 46,
    label = "O2 + C2H <=> CO2 + CH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 47,
    label = "O + HCO <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 48,
    label = "CH4 + CH <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-1.66, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 49,
    label = "C2H2 + CH <=> C2H + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-0.51, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 50,
    label = "C2H4 + CH <=> C3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-1.44, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 51,
    label = "C2H6 + CH <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-1.1, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 52,
    label = "CH2O + CH <=> CH2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-2.16, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 53,
    label = "H + CH2 <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (-7.48, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 54,
    label = "CH + CH2 <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 55,
    label = "CH + CH3 <=> C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 56,
    label = "CH + C2H3 <=> CH2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 57,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 58,
    label = "CH2 + CH2 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (3.33, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 59,
    label = "CH2 + CH2 <=> C2H2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (3.33, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 60,
    label = "CH2 + CH3 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13, 'cm^3/(mol*s)', '*|/', 1.4),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 61,
    label = "CH2 + C2H3 <=> C2H2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 62,
    label = "CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 63,
    label = "CH2 + HCCO <=> C2H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (8.37, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 64,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (42, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 65,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 66,
    label = "C2H2 + CH2 <=> C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (27.69, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 67,
    label = "C2H2 + CH2(S) <=> H2CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+14, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 68,
    label = "H + CH2(S) <=> CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 69,
    label = "H2 + CH2(S) <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 70,
    label = "C2H4 + CH2(S) <=> C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 71,
    label = "C2H6 + CH2(S) <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 72,
    label = "CH3 + OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (11.64, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 73,
    label = "C2H2 + C2H2 <=> H2CCCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+09, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (242, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 74,
    label = "C2H2 + C2H <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 75,
    label = "C2H4 + O <=> H + CH2HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.74e+06, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 76,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.13e+06, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 77,
    label = "C2H4 + O <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (680000, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 78,
    label = "C4H2 + OH <=> C3H2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.68e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (-1.71, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 79,
    label = "O2 + H + H2O <=> HO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.89e+15, 'cm^6/(mol^2*s)', '*|/', 1.5),
        n = 0,
        Ea = (-8.73, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "O2 + H <=> OH + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.756e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (62.11, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 81,
    label = "O2 + CH3 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+11, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (37.42, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 82,
    label = "O2 + C2H <=> HCCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 83,
    label = "O2 + C3H2 <=> HCO + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 84,
    label = "O2 + H2CCCH <=> CH2CO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+10, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (12, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 85,
    label = "H2O2 + H <=> OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (16.59, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 86,
    label = "CH3 + CH3 <=> C2H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.6),
        n = 0,
        Ea = (56.54, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 87,
    label = "H + HO2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+14, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (3.66, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 88,
    label = "H + HO2 <=> H2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (7.2, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 89,
    label = "H + CH2OH <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 90,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+13, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 91,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 92,
    label = "C2H + OH <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 93,
    label = "C2H5 + O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 94,
    label = "O2 + CH3 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (131.37, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 95,
    label = "OH + OH <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+09, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 1.14,
        Ea = (0.42, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 96,
    label = "H2 + O <=> OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51200, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 2.67,
        Ea = (26.27, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 97,
    label = "H2O + H <=> H2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+08, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 1.6,
        Ea = (77.08, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 98,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+08, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 1.56,
        Ea = (35.5, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 99,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.57e+07, 'cm^3/(mol*s)', '*|/', 1.15),
        n = 1.83,
        Ea = (11.64, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 100,
    label = "C2H2 + OH <=> C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (54.04, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 101,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.42e+14, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (62.36, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 102,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (24.86, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 103,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+09, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.5,
        Ea = (31.01, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 104,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e-07, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 6,
        Ea = (25.3, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 105,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+09, 'cm^3/(mol*s)', '*|/', 1.15),
        n = 1.5,
        Ea = (24.28, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 106,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+06, 'cm^3/(mol*s)', '*|/', 1.1),
        n = 2,
        Ea = (3.62, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 107,
    label = "C2H6 + HO2 <=> H2O2 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (85.63, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 108,
    label = "O2 + CH2O <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (170.11, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 109,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (7.32, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 110,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+12, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (15.71, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 111,
    label = "H2O2 + O <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (16.63, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 112,
    label = "H2O2 + OH <=> H2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.83e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (5.57, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 113,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+08, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 1.62,
        Ea = (9.06, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 114,
    label = "CH2O + CH3 <=> CH4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.09e+12, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (36.95, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 115,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.16e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0.57,
        Ea = (11.56, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 116,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 1.18,
        Ea = (-1.87, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 117,
    label = "H + HO2 <=> H2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e+13, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (5.9, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 118,
    label = "H + CH3O <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 119,
    label = "O + HO2 <=> O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.19e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 120,
    label = "OH + HO2 <=> H2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (-2.08, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 121,
    label = "C4H10 + HO2 <=> C4H9_1 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (81.1, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 122,
    label = "C4H10 + HO2 <=> C4H9_2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.76e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (71.1, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 123,
    label = "C4H10 + OH <=> C4H9_1 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+07, 'cm^3/(mol*s)', '*|/', 2),
        n = 1.8,
        Ea = (3.99, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 124,
    label = "C4H10 + OH <=> C4H9_2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.36e+06, 'cm^3/(mol*s)', '*|/', 2),
        n = 2,
        Ea = (-2.49, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 125,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (4.18, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 126,
    label = "O2 + C2H3 <=> HCO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+16, 'cm^3/(mol*s)', '*|/', 3.16),
        n = -1.39,
        Ea = (4.22, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 127,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.54e+15, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = 0,
            Ea = (12.56, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 128,
    label = "CH2O <=> HCO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.4e+36, 'cm^3/(mol*s)', '*|/', 1.2),
            n = -5.54,
            Ea = (404.58, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 129,
    label = "CH2O <=> H2 + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.26e+36, 'cm^3/(mol*s)', '*|/', 1.2),
            n = -5.54,
            Ea = (404.58, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 130,
    label = "CH2CO <=> CH2 + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.57e+15, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (241.03, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 131,
    label = "CH2(S) <=> CH2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.51e+13, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 0.48, 'O=C=O': 1.5, 'CC': 1.44, 'O': 6.5, '[O][O]': 0.4, '[C]=O': 0.75, 'N#N': 0.4, 'C=C': 1.6, 'C#C': 3.2, '[Ar]': 0.24},
    ),
)

entry(
    index = 132,
    label = "CH3 <=> CH2 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.91e+16, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (379.14, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 133,
    label = "C2H4 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (9.97e+16, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (299.32, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 134,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.4e+13, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = 0,
            Ea = (-7.48, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 135,
    label = "O2 + H <=> HO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.1e+18, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = -0.8,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 0, '[O][O]': 0.4, 'N#N': 0.67, '[C]=O': 0.75, '[Ar]': 0.29},
    ),
)

entry(
    index = 136,
    label = "C2H4 <=> C2H3 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (7.4e+17, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (404.09, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 137,
    label = "H + H <=> H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.87e+18, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = -1,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[H][H]': 0, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 138,
    label = "H + O <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.18e+19, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = -1,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 139,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.53e+22, 'cm^6/(mol^2*s)', '*|/', 1.2),
            n = -2,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 2.55, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.15},
    ),
)

entry(
    index = 140,
    label = "CH3O <=> CH2O + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.55e+14, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (56.46, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 141,
    label = "CH2OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.26e+16, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (125.6, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 142,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.43e+12, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (10.81, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(3.43e+18, 'cm^6/(mol^2*s)'), n=0, Ea=(6.15, 'kJ/mol'), T0=(1, 'K')),
        alpha = 1,
        T3 = (1, 'K'),
        T1 = (1, 'K'),
        T2 = (1231, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 143,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3.97e+09, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 1.28,
            Ea = (5.4, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(1.35e+19, 'cm^6/(mol^2*s)'), n=0, Ea=(3.16, 'kJ/mol'), T0=(1, 'K')),
        alpha = 0.76,
        T3 = (40, 'K'),
        T1 = (1025, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 144,
    label = "OH + OH <=> H2O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (7.23e+13, 'cm^3/(mol*s)', '*|/', 1.2),
            n = -0.37,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.53e+19, 'cm^6/(mol^2*s)'),
            n = -0.76,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1, 'K'),
        T1 = (1, 'K'),
        T2 = (1040, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 145,
    label = "H + CH3 <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.688e+14, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.408e+24, 'cm^6/(mol^2*s)'),
            n = -1.8,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.37,
        T3 = (3315, 'K'),
        T1 = (61, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

entry(
    index = 146,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3.61e+13, 'cm^3/(mol*s)', '*|/', 1.2),
            n = 0,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.63e+41, 'cm^6/(mol^2*s)'),
            n = -7,
            Ea = (11.56, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.62,
        T3 = (73, 'K'),
        T1 = (1180, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
    ),
)

