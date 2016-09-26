#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "O(20) + H2(21) <=> H(22) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(38700, 'cm^3/(mol*s)'), n=2.7, Ea=(6.26, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "O(20) + HO2(24) <=> O2(2) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "O(20) + H2O2(25) <=> OH(23) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.63e+06, 'cm^3/(mol*s)'), n=2, Ea=(4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "O(20) + CH(26) <=> H(22) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "O(20) + CH2(28) <=> H(22) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "O(20) + CH2(S)(30) <=> H2(21) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "O(20) + CH2(S)(30) <=> H(22) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "O(20) + CH3(31) <=> H(22) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "O(20) + CH4(33) <=> OH(23) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "O(20) + HCO(29) <=> OH(23) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "O(20) + HCO(29) <=> H(22) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "O(20) + CH2O(32) <=> OH(23) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(3.54, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "O(20) + CH2OH(35) <=> OH(23) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "O(20) + CH3O(36) <=> OH(23) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "O(20) + CH3OH(37) <=> OH(23) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(388000, 'cm^3/(mol*s)'), n=2.5, Ea=(3.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "O(20) + CH3OH(37) <=> OH(23) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(130000, 'cm^3/(mol*s)'), n=2.5, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "O(20) + C2H(38) <=> CH(26) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "O(20) + C2H2(39) <=> H(22) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.35e+07, 'cm^3/(mol*s)'), n=2, Ea=(1.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "O(20) + C2H2(39) <=> OH(23) + C2H(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19, 'cm^3/(mol*s)'),
        n = -1.41,
        Ea = (28.95, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = "O(20) + C2H2(39) <=> CO(27) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.94e+06, 'cm^3/(mol*s)'), n=2, Ea=(1.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "O(20) + C2H3(41) <=> H(22) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "O(20) + C2H4(43) <=> HCO(29) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+07, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (0.22, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = "O(20) + C2H5(44) <=> CH3(31) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.24e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "O(20) + C2H6(45) <=> OH(23) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.98e+07, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (5.69, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 25,
    label = "O(20) + HCCO(40) <=> H(22) + CO(27) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "O(20) + CH2CO(42) <=> OH(23) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "O(20) + CH2CO(42) <=> CH2(28) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+12, 'cm^3/(mol*s)'), n=0, Ea=(1.35, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "O2(2) + CO(27) <=> O(20) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(47.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "O2(2) + CH2O(32) <=> HO2(24) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "O2(2) + O2(2) + H(22) <=> O2(2) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.08e+19, 'cm^6/(mol^2*s)'),
        n = -1.24,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 31,
    label = "O2(2) + H(22) + H2O(46) <=> HO2(24) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.126e+19, 'cm^6/(mol^2*s)'),
        n = -0.76,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 32,
    label = "O2(2) + H(22) <=> O(20) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+16, 'cm^3/(mol*s)'),
        n = -0.671,
        Ea = (17.041, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 33,
    label = "H2(21) + H(22) + H(22) <=> H2(21) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "H(22) + H(22) + H2O(46) <=> H2(21) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+19, 'cm^6/(mol^2*s)'), n=-1.25, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "H(22) + H(22) + CO2(34) <=> H2(21) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+20, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "H(22) + HO2(24) <=> O(20) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.671, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = "H(22) + HO2(24) <=> O2(2) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.48e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.068, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 38,
    label = "H(22) + HO2(24) <=> OH(23) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0.635, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "H(22) + H2O2(25) <=> H2(21) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+07, 'cm^3/(mol*s)'), n=2, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "H(22) + H2O2(25) <=> OH(23) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(3.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "H(22) + CH(26) <=> H2(21) + C(47)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.65e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "H(22) + CH2(S)(30) <=> H2(21) + CH(26)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "H(22) + CH4(33) <=> H2(21) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (10.84, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 44,
    label = "H(22) + HCO(29) <=> H2(21) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "H(22) + CH2O(32) <=> H2(21) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 46,
    label = "H(22) + CH2OH(35) <=> H2(21) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "H(22) + CH2OH(35) <=> OH(23) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (-0.284, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 48,
    label = "H(22) + CH2OH(35) <=> CH2(S)(30) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.28e+13, 'cm^3/(mol*s)'),
        n = -0.09,
        Ea = (0.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 49,
    label = "H(22) + CH3O(36) <=> H(22) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.15e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (1.924, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 50,
    label = "H(22) + CH3O(36) <=> H2(21) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "H(22) + CH3O(36) <=> OH(23) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-0.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 52,
    label = "H(22) + CH3O(36) <=> CH2(S)(30) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (1.07, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 53,
    label = "H(22) + CH3OH(37) <=> H2(21) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+07, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4.87, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 54,
    label = "H(22) + CH3OH(37) <=> H2(21) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4.87, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 55,
    label = "H(22) + C2H3(41) <=> H2(21) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "H(22) + C2H4(43) <=> H2(21) + C2H3(41)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.325e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12.24, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 57,
    label = "H(22) + C2H5(44) <=> H2(21) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "H(22) + C2H6(45) <=> H2(21) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7.53, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 59,
    label = "H(22) + HCCO(40) <=> CO(27) + CH2(S)(30)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "H(22) + CH2CO(42) <=> H2(21) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "H(22) + CH2CO(42) <=> CO(27) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.428, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 62,
    label = "H(22) + HCCOH(48) <=> H(22) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "H2(21) + OH(23) <=> H(22) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3.43, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 64,
    label = "OH(23) + OH(23) <=> O(20) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(35700, 'cm^3/(mol*s)'), n=2.4, Ea=(-2.11, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 65,
    label = "OH(23) + HO2(24) <=> O2(2) + H2O(46)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.45e+13, 'cm^3/(mol*s)'), n=0, Ea=(-0.5, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+15, 'cm^3/(mol*s)'), n=0, Ea=(17.33, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 67,
    label = "OH(23) + H2O2(25) <=> HO2(24) + H2O(46)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0.427, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.7e+18, 'cm^3/(mol*s)'), n=0, Ea=(29.41, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 69,
    label = "OH(23) + C(47) <=> H(22) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 70,
    label = "OH(23) + CH(26) <=> H(22) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "OH(23) + CH2(28) <=> H(22) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "OH(23) + CH2(28) <=> CH(26) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+07, 'cm^3/(mol*s)'), n=2, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "OH(23) + CH2(S)(30) <=> H(22) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "OH(23) + CH3(31) <=> CH2(28) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5.42, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 75,
    label = "OH(23) + CH3(31) <=> CH2(S)(30) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.44e+17, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1.417, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 76,
    label = "OH(23) + CH4(33) <=> CH3(31) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+08, 'cm^3/(mol*s)'), n=1.6, Ea=(3.12, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 77,
    label = "OH(23) + CO(27) <=> H(22) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.76e+07, 'cm^3/(mol*s)'),
        n = 1.228,
        Ea = (0.07, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 78,
    label = "OH(23) + HCO(29) <=> CO(27) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 79,
    label = "OH(23) + CH2O(32) <=> HCO(29) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-0.447, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "OH(23) + CH2OH(35) <=> CH2O(32) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 81,
    label = "OH(23) + CH3O(36) <=> CH2O(32) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "OH(23) + CH3OH(37) <=> CH2OH(35) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.44e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.84, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 83,
    label = "OH(23) + CH3OH(37) <=> CH3O(36) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(1.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 84,
    label = "OH(23) + C2H(38) <=> H(22) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 85,
    label = "OH(23) + C2H2(39) <=> H(22) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.000218, 'cm^3/(mol*s)'), n=4.5, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 86,
    label = "OH(23) + C2H2(39) <=> H(22) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(504000, 'cm^3/(mol*s)'), n=2.3, Ea=(13.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 87,
    label = "OH(23) + C2H2(39) <=> C2H(38) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+07, 'cm^3/(mol*s)'), n=2, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 88,
    label = "OH(23) + C2H2(39) <=> CO(27) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.000483, 'cm^3/(mol*s)'), n=4, Ea=(-2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "OH(23) + C2H3(41) <=> C2H2(39) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "OH(23) + C2H4(43) <=> C2H3(41) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(2.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "OH(23) + C2H6(45) <=> C2H5(44) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.54e+06, 'cm^3/(mol*s)'),
        n = 2.12,
        Ea = (0.87, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 92,
    label = "OH(23) + CH2CO(42) <=> HCCO(40) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 93,
    label = "HO2(24) + HO2(24) <=> O2(2) + H2O2(25)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1.63, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(12, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 95,
    label = "HO2(24) + CH2(28) <=> OH(23) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 96,
    label = "HO2(24) + CH3(31) <=> O2(2) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "HO2(24) + CH3(31) <=> OH(23) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.78e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
    label = "HO2(24) + CO(27) <=> OH(23) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(23.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 99,
    label = "HO2(24) + CH2O(32) <=> H2O2(25) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(12, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "O2(2) + C(47) <=> O(20) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0.576, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "CH2(28) + C(47) <=> H(22) + C2H(38)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "CH3(31) + C(47) <=> H(22) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "O2(2) + CH(26) <=> O(20) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.71e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 104,
    label = "H2(21) + CH(26) <=> H(22) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+14, 'cm^3/(mol*s)'), n=0, Ea=(3.11, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH(26) + H2O(46) <=> H(22) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.71e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.755, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 106,
    label = "CH(26) + CH2(28) <=> H(22) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH(26) + CH3(31) <=> H(22) + C2H3(41)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "CH(26) + CH4(33) <=> H(22) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 109,
    label = "CH(26) + CO2(34) <=> CO(27) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.792, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 110,
    label = "CH(26) + CH2O(32) <=> H(22) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.46e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.515, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 111,
    label = "CH(26) + HCCO(40) <=> CO(27) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
    label = "O2(2) + CH2(28) <=> H(22) + OH(23) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 113,
    label = "H2(21) + CH2(28) <=> H(22) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(500000, 'cm^3/(mol*s)'), n=2, Ea=(7.23, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "CH2(28) + CH2(28) <=> H2(21) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.944, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 115,
    label = "CH2(28) + CH3(31) <=> H(22) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH2(28) + CH4(33) <=> CH3(31) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(8.27, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 117,
    label = "CH2(28) + HCCO(40) <=> CO(27) + C2H3(41)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "O2(2) + CH2(S)(30) <=> H(22) + OH(23) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "O2(2) + CH2(S)(30) <=> CO(27) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "H2(21) + CH2(S)(30) <=> H(22) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "CH2(S)(30) + H2O(46) <=> CH2(28) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "CH2(S)(30) + CH3(31) <=> H(22) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(-0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "CH2(S)(30) + CH4(33) <=> CH3(31) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "CO(27) + CH2(S)(30) <=> CO(27) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "CH2(S)(30) + CO2(34) <=> CH2(28) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 126,
    label = "CH2(S)(30) + CO2(34) <=> CO(27) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 127,
    label = "CH2(S)(30) + C2H6(45) <=> CH3(31) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(-0.55, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "O2(2) + CH3(31) <=> O(20) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.56e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30.48, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 129,
    label = "O2(2) + CH3(31) <=> OH(23) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20.315, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 130,
    label = "H2O2(25) + CH3(31) <=> HO2(24) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(24500, 'cm^3/(mol*s)'), n=2.47, Ea=(5.18, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 131,
    label = "CH3(31) + CH3(31) <=> H(22) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.84e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 132,
    label = "HCO(29) + CH3(31) <=> CO(27) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.648e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 133,
    label = "CH3(31) + CH2O(32) <=> HCO(29) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3320, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
    label = "CH3(31) + CH3OH(37) <=> CH4(33) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(9.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 135,
    label = "CH3(31) + CH3OH(37) <=> CH4(33) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(9.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 136,
    label = "CH3(31) + C2H4(43) <=> CH4(33) + C2H3(41)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(227000, 'cm^3/(mol*s)'), n=2, Ea=(9.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 137,
    label = "CH3(31) + C2H6(45) <=> CH4(33) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10.45, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 138,
    label = "HCO(29) + H2O(46) <=> H(22) + CO(27) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+18, 'cm^3/(mol*s)'), n=-1, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 139,
    label = "O2(2) + HCO(29) <=> HO2(24) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.345e+13, 'cm^3/(mol*s)'), n=0, Ea=(0.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 140,
    label = "O2(2) + CH2OH(35) <=> HO2(24) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 141,
    label = "O2(2) + CH3O(36) <=> HO2(24) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3.53, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 142,
    label = "O2(2) + C2H(38) <=> CO(27) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(-0.755, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "H2(21) + C2H(38) <=> H(22) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68e+10, 'cm^3/(mol*s)'),
        n = 0.9,
        Ea = (1.993, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 144,
    label = "O2(2) + C2H3(41) <=> HCO(29) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1.015, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 145,
    label = "O2(2) + C2H5(44) <=> HO2(24) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(3.875, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "O2(2) + HCCO(40) <=> OH(23) + CO(27) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0.854, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "HCCO(40) + HCCO(40) <=> CO(27) + CO(27) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "O(20) + CH3(31) <=> H2(21) + H(22) + CO(27)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 149,
    label = "O(20) + C2H4(43) <=> C2H3O(18) + H(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+06, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (0.22, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 150,
    label = "O(20) + C2H5(44) <=> H(22) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.096e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "OH(23) + CH3(31) <=> H2(21) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+09, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-1.755, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 152,
    label = "O2(2) + CH2(28) <=> H(22) + H(22) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 153,
    label = "O2(2) + CH2(28) <=> O(20) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "CH2(28) + CH2(28) <=> H(22) + H(22) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(10.989, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 155,
    label = "CH2(S)(30) + H2O(46) <=> H2(21) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.82e+10, 'cm^3/(mol*s)'),
        n = 0.25,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 156,
    label = "O2(2) + C2H3(41) <=> C2H3O(18) + O(20)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.03e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (0.011, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 157,
    label = "O2(2) + C2H3(41) <=> HO2(24) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.337e+06, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-0.384, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 158,
    label = "O(20) + CH3CHO(49) <=> C2H3O(18) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.808, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 159,
    label = "O(20) + CH3CHO(49) <=> OH(23) + CO(27) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.808, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 160,
    label = "O2(2) + CH3CHO(49) <=> HO2(24) + CO(27) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39.15, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 161,
    label = "H(22) + CH3CHO(49) <=> C2H3O(18) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2.405, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 162,
    label = "H(22) + CH3CHO(49) <=> H2(21) + CO(27) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2.405, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 163,
    label = "OH(23) + CH3CHO(49) <=> CO(27) + CH3(31) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.343e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-1.113, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 164,
    label = "HO2(24) + CH3CHO(49) <=> H2O2(25) + CO(27) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.923, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 165,
    label = "CH3(31) + CH3CHO(49) <=> CO(27) + CH3(31) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.72e+06, 'cm^3/(mol*s)'),
        n = 1.77,
        Ea = (5.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 166,
    label = "C2H3O(18) + O(20) <=> H(22) + CH2(28) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 167,
    label = "O2(2) + C2H3O(18) <=> OH(23) + CO(27) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 168,
    label = "O2(2) + C2H3O(18) <=> OH(23) + HCO(29) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 169,
    label = "C2H3O(18) + H(22) <=> HCO(29) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 170,
    label = "C2H3O(18) + H(22) <=> H2(21) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
    label = "C2H3O(18) + OH(23) <=> CH2CO(42) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "C2H3O(18) + OH(23) <=> HCO(29) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "C4H8O3(14) <=> C4H7O2(15) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5, 's^-1'), n=0, Ea=(41.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "C4H8O3(11) <=> C4H7O2(16) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5, 's^-1'), n=0, Ea=(41.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "CH2(S)(30) + C3H8(50) <=> butane(1)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.603e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 176,
    label = "C2H5(44) + C2H5(44) <=> butane(1)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "HO2(24) + CH(26) <=> O2(2) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "HO2(24) + CH2(28) <=> O2(2) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.24e+07, 'cm^3/(mol*s)'),
        n = 1.524,
        Ea = (5.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 179,
    label = "HO2(24) + CH2OH(35) <=> O2(2) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.515, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 180,
    label = "O2(2) + CH3OH(37) <=> HO2(24) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(54.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 181,
    label = "HO2(24) + C2H(38) <=> O2(2) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.108, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 182,
    label = "HO2(24) + HCCO(40) <=> O2(2) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.411, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 183,
    label = "HO2(24) + C2H3(41) <=> O2(2) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.352, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 184,
    label = "HO2(24) + C2H5(44) <=> O2(2) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.472, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 185,
    label = "HO2(24) + HCCO(40) <=> O2(2) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 186,
    label = "butR1(3) + H(22) <=> butane(1)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 187,
    label = "butane(1) + O(20) <=> butR1(3) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5700, 'cm^3/(mol*s)'), n=3.05, Ea=(3.123, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 188,
    label = "butR1(3) + H2(21) <=> butane(1) + H(22)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00384, 'cm^3/(mol*s)'), n=4.34, Ea=(9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 189,
    label = "butR1(3) + H2O(46) <=> butane(1) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+06, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (20.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 190,
    label = "butR1(3) + H2O2(25) <=> butane(1) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.597, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 191,
    label = "butane(1) + CH(26) <=> butR1(3) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 192,
    label = "butane(1) + CH2(28) <=> butR1(3) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.443e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 193,
    label = "butR1(3) + CH2O(32) <=> butane(1) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 194,
    label = "butR1(3) + CH4(33) <=> butane(1) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0864, 'cm^3/(mol*s)'),
        n = 4.14,
        Ea = (12.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 195,
    label = "butR1(3) + CH3O(36) <=> butane(1) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 196,
    label = "butR1(3) + CH2OH(35) <=> butane(1) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 197,
    label = "butR1(3) + CH3OH(37) <=> butane(1) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 198,
    label = "butR1(3) + CH3OH(37) <=> butane(1) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 199,
    label = "butane(1) + C2H(38) <=> butR1(3) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.612e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "butR1(3) + C2H3(41) <=> butane(1) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 201,
    label = "butR1(3) + HCCOH(48) <=> butane(1) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 202,
    label = "butR1(3) + CH2CO(42) <=> butane(1) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0109, 'cm^3/(mol*s)'), n=4.34, Ea=(5.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "butane(1) + C2H3(41) <=> butR1(3) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00108, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 204,
    label = "butR1(3) + C2H5(44) <=> butane(1) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 205,
    label = "butR1(3) + C2H6(45) <=> butane(1) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00552, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 206,
    label = "butR1(3) + HO2(24) <=> butane(1) + O2(2)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.465, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 207,
    label = "C2H4(43) + C2H5(44) <=> butR1(3)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3980, 'cm^3/(mol*s)'), n=2.44, Ea=(5.37, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 208,
    label = "butR2(4) + H(22) <=> butane(1)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 209,
    label = "butane(1) + O(20) <=> butR2(4) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(95600, 'cm^3/(mol*s)'), n=2.71, Ea=(2.11, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "butane(1) + H(22) <=> butR2(4) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.356, 'cm^3/(mol*s)'), n=4.34, Ea=(3.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 211,
    label = "butane(1) + OH(23) <=> butR2(4) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 212,
    label = "butane(1) + HO2(24) <=> butR2(4) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17.686, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 213,
    label = "butane(1) + CH(26) <=> butR2(4) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 214,
    label = "butane(1) + CH2(28) <=> butR2(4) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02, 'cm^3/(mol*s)'), n=3.46, Ea=(7.47, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 215,
    label = "butR2(4) + CH2O(32) <=> butane(1) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+11, 'cm^3/(mol*s)'), n=0, Ea=(6.96, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 216,
    label = "butane(1) + CH3(31) <=> butR2(4) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.03212, 'cm^3/(mol*s)'), n=4.34, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 217,
    label = "butR2(4) + CH3O(36) <=> butane(1) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 218,
    label = "butR2(4) + CH2OH(35) <=> butane(1) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 219,
    label = "butane(1) + CH2OH(35) <=> butR2(4) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120.8, 'cm^3/(mol*s)'),
        n = 2.95,
        Ea = (11.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 220,
    label = "butane(1) + CH3O(36) <=> butR2(4) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 221,
    label = "butane(1) + C2H(38) <=> butR2(4) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 222,
    label = "butR2(4) + C2H3(41) <=> butane(1) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 223,
    label = "butR2(4) + HCCOH(48) <=> butane(1) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 224,
    label = "butane(1) + HCCO(40) <=> butR2(4) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0664, 'cm^3/(mol*s)'), n=4.34, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 225,
    label = "butane(1) + C2H3(41) <=> butR2(4) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2040, 'cm^3/(mol*s)'), n=3.1, Ea=(8.82, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 226,
    label = "butR2(4) + C2H5(44) <=> butane(1) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 227,
    label = "butane(1) + C2H5(44) <=> butR2(4) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00368, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 228,
    label = "butane(1) + O2(2) <=> butR2(4) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.176e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49.347, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 229,
    label = "butR2(4) <=> butR1(3)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.86e+09, 's^-1'), n=1.32, Ea=(40.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 230,
    label = "butane(1) + butR1(3) <=> butane(1) + butR2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00368, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 231,
    label = "O2(2) + butR1(3) <=> butROO1(5)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.089e+15, 'cm^3/(mol*s)'),
        n = -1.102,
        Ea = (3.244, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 232,
    label = "O2(2) + butR2(4) <=> butROO2(6)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 233,
    label = "butROO1(5) <=> C4H9O2(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.788e+07, 's^-1'), n=1.26, Ea=(18.17, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 234,
    label = "butROO2(6) <=> C4H9O2(8)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.034e+07, 's^-1'), n=1.35, Ea=(20.84, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 235,
    label = "O2(2) + C4H9O2(7) <=> C4H9O4(9)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 236,
    label = "O2(2) + C4H9O2(8) <=> C4H9O4(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.089e+15, 'cm^3/(mol*s)'),
        n = -1.102,
        Ea = (3.244, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 237,
    label = "C4H9O4(9) <=> C4H9O4(10)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.668e+06, 's^-1'), n=1.614, Ea=(29.669, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 238,
    label = "C4H9O4(9) <=> C4H9O4(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.97e+09, 's^-1'), n=1.01, Ea=(38.47, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 239,
    label = "C4H9O4(10) <=> C4H9O4(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+07, 's^-1'), n=1.1, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 240,
    label = "C4H8O3(11) + OH(23) <=> C4H9O4(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (39.542, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 241,
    label = "C4H9O4(9) <=> C4H9O4(13)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10980, 's^-1'), n=2.4, Ea=(19.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 242,
    label = "C4H9O4(13) <=> C4H9O4(10)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.71, 's^-1'), n=3.021, Ea=(25.23, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 243,
    label = "C4H9O4(13) <=> C4H9O4(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.566e+10, 's^-1'), n=0.55, Ea=(39.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 244,
    label = "C4H8O3(14) + OH(23) <=> C4H9O4(13)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (37.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 245,
    label = "C3H5O(17) + CH2O(32) <=> C4H7O2(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "CH3(31) + CH2CO(42) <=> C3H5O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14280, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (8.335, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 247,
    label = "butR2(4) + C2H3O(18) <=> butane(1) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 248,
    label = "butR1(3) + C2H3O(18) <=> butane(1) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 249,
    label = "C2H3O(18) + HO2(24) <=> O2(2) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.502, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 250,
    label = "butR1(3) + CH3CHO(49) <=> butane(1) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.037e-05, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 251,
    label = "butane(1) + C2H3O(18) <=> butR2(4) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009938, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 252,
    label = "C2H3O(18) + CH3CHO(49) <=> C4H7O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 253,
    label = "C2H3O(18) + CH2(S)(30) <=> C3H5O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.352e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 254,
    label = "O(20) + C2H3(41) <=> C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 255,
    label = "C2H3O(18) + O(20) <=> OH(23) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.837e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 256,
    label = "C2H3O(18) + H(22) <=> CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 257,
    label = "C2H3O(18) + HO2(24) <=> H2O2(25) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 258,
    label = "C2H3O(18) + H2O2(25) <=> HO2(24) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.46e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 259,
    label = "C2H3O(18) + CH(26) <=> CH2(28) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.046e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 260,
    label = "C2H3O(18) + CH2(28) <=> CH3(31) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.04e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 261,
    label = "CH(26) + CH3CHO(49) <=> C2H3O(18) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(300000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 262,
    label = "C2H3O(18) + HCO(29) <=> CH2O(32) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 263,
    label = "C2H3O(18) + CH3(31) <=> CH4(33) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 264,
    label = "CH2(28) + CH3CHO(49) <=> C2H3O(18) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.721e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 265,
    label = "C2H3O(18) + CH2O(32) <=> HCO(29) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18.36, 'cm^3/(mol*s)'), n=3.38, Ea=(9.04, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 266,
    label = "CH3(31) + CH3CHO(49) <=> C2H3O(18) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008865, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.85, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 267,
    label = "C2H3O(18) + CH2OH(35) <=> CH2O(32) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.946e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 268,
    label = "C2H3O(18) + CH2OH(35) <=> CH3OH(37) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 269,
    label = "C2H3O(18) + CH3O(36) <=> CH2O(32) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 270,
    label = "C2H3O(18) + CH3O(36) <=> CH3OH(37) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 271,
    label = "C2H3O(18) + CH3OH(37) <=> CH2OH(35) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 272,
    label = "CH3O(36) + CH3CHO(49) <=> C2H3O(18) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7902, 'cm^3/(mol*s)'),
        n = 3.82,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 273,
    label = "C2H3O(18) + C2H(38) <=> C2H2(39) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.297e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 274,
    label = "C2H(38) + CH3CHO(49) <=> C2H3O(18) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (360000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 275,
    label = "C2H3O(18) + HCCO(40) <=> CH2CO(42) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 276,
    label = "C2H3O(18) + HCCO(40) <=> CH2CO(42) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 277,
    label = "C2H3O(18) + C2H3(41) <=> C2H2(39) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 278,
    label = "C2H3O(18) + C2H3(41) <=> CH2CO(42) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 279,
    label = "HCCO(40) + CH3CHO(49) <=> C2H3O(18) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.006191, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (12.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 280,
    label = "C2H3(41) + CH3CHO(49) <=> C2H3O(18) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00054, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 281,
    label = "C2H3O(18) + C2H5(44) <=> C2H4(43) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 282,
    label = "C2H3O(18) + C2H5(44) <=> CH2CO(42) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 283,
    label = "C2H5(44) + CH3CHO(49) <=> C2H3O(18) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.037e-05, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 284,
    label = "OH(23) + CH3CHO(49) <=> C2H3O(18) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.551e+06, 'cm^3/(mol*s)'), n=2.2, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 285,
    label = "C2H3O(18) + HCCOH(48) <=> HCCO(40) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 286,
    label = "O2(2) + C2H3O(18) <=> HO2(24) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.908, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 287,
    label = "C2H3O(18) + C2H3O(18) <=> CH2CO(42) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 288,
    label = "C3H4O2(19) + CH3(31) <=> C4H7O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 289,
    label = "C2H3O(18) + HCO(29) <=> C3H4O2(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 290,
    label = "CO(27) + CH3CHO(49) <=> C3H4O2(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (274200, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (85.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 291,
    label = "C2H5O2(90) <=> O2(2) + C2H5(44)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(9.49e+21, 's^-1'), n=-2.41, Ea=(35.8, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.49e+21, 's^-1'), n=-2.41, Ea=(35.8, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 293,
    label = "C2H5O2(90) <=> HO2(24) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.68e+07, 's^-1'), n=1.69, Ea=(29.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 294,
    label = "C3H7(51) + CH3(31) <=> butane(1)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 295,
    label = "C3H7(51) + HO2(24) <=> O2(2) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.467, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 296,
    label = "C3H7(51) + CH2(S)(30) <=> butR1(3)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.302e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 297,
    label = "butR1(3) + C3H8(50) <=> butane(1) + C3H7(51)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00552, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 298,
    label = "butane(1) + C3H7(51) <=> butR2(4) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00368, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 299,
    label = "C3H7(51) + CH3CHO(49) <=> C2H3O(18) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.037e-05, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 300,
    label = "CH3(31) + C2H4(43) <=> C3H7(51)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41800, 'cm^3/(mol*s)'), n=2.41, Ea=(5.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 301,
    label = "CH2(S)(30) + C2H5(44) <=> C3H7(51)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.055e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 302,
    label = "C3H7(51) + H2(21) <=> H(22) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00384, 'cm^3/(mol*s)'), n=4.34, Ea=(9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 303,
    label = "C3H7(51) + H(22) <=> C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 304,
    label = "O(20) + C3H8(50) <=> C3H7(51) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5700, 'cm^3/(mol*s)'), n=3.05, Ea=(3.123, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 305,
    label = "C3H7(51) + H2O2(25) <=> HO2(24) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.597, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 306,
    label = "CH(26) + C3H8(50) <=> C3H7(51) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 307,
    label = "CH2(28) + C3H8(50) <=> C3H7(51) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.443e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 308,
    label = "C3H7(51) + CH2O(32) <=> HCO(29) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 309,
    label = "C3H7(51) + CH4(33) <=> CH3(31) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0864, 'cm^3/(mol*s)'),
        n = 4.14,
        Ea = (12.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 310,
    label = "C3H7(51) + CH2OH(35) <=> CH2O(32) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 311,
    label = "C3H7(51) + CH3O(36) <=> CH2O(32) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 312,
    label = "C3H7(51) + CH3OH(37) <=> CH2OH(35) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 313,
    label = "C3H7(51) + CH3OH(37) <=> CH3O(36) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 314,
    label = "C2H(38) + C3H8(50) <=> C3H7(51) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.612e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 315,
    label = "C3H7(51) + C2H3(41) <=> C2H2(39) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 316,
    label = "C3H7(51) + CH2CO(42) <=> HCCO(40) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0109, 'cm^3/(mol*s)'), n=4.34, Ea=(5.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 317,
    label = "C2H3(41) + C3H8(50) <=> C3H7(51) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00108, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 318,
    label = "C3H7(51) + C2H5(44) <=> C2H4(43) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 319,
    label = "C3H7(51) + C2H6(45) <=> C2H5(44) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00552, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 320,
    label = "C3H7(51) + H2O(46) <=> OH(23) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+06, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (20.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 321,
    label = "C3H7(51) + HCCOH(48) <=> HCCO(40) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 322,
    label = "C2H3O(18) + C3H7(51) <=> CH2CO(42) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 323,
    label = "butR2(4) + HO2(24) <=> S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 324,
    label = "S(149) + H(22) <=> butROO2(6) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 325,
    label = "butROO2(6) + H(22) <=> S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 326,
    label = "S(149) + O(20) <=> butROO2(6) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 327,
    label = "butROO2(6) + HO2(24) <=> O2(2) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 328,
    label = "butROO2(6) + H2O2(25) <=> S(149) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 329,
    label = "S(149) + CH(26) <=> butROO2(6) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 330,
    label = "S(149) + CH2(28) <=> butROO2(6) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 331,
    label = "butROO2(6) + CH2O(32) <=> S(149) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 332,
    label = "S(149) + CH3(31) <=> butROO2(6) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 333,
    label = "butROO2(6) + CH2OH(35) <=> S(149) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 334,
    label = "butROO2(6) + CH3O(36) <=> S(149) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 335,
    label = "S(149) + CH2OH(35) <=> butROO2(6) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 336,
    label = "S(149) + CH3O(36) <=> butROO2(6) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 337,
    label = "S(149) + C2H(38) <=> butROO2(6) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 338,
    label = "butROO2(6) + C2H3(41) <=> S(149) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 339,
    label = "S(149) + HCCO(40) <=> butROO2(6) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 340,
    label = "S(149) + C2H3(41) <=> butROO2(6) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 341,
    label = "butROO2(6) + C2H5(44) <=> S(149) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 342,
    label = "S(149) + C2H5(44) <=> butROO2(6) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 343,
    label = "S(149) + OH(23) <=> butROO2(6) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 344,
    label = "butROO2(6) + HCCOH(48) <=> S(149) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 345,
    label = "C2H3O(18) + S(149) <=> butROO2(6) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 346,
    label = "C3H7(51) + S(149) <=> butROO2(6) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 347,
    label = "butR2(4) + S(149) <=> butane(1) + butROO2(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 348,
    label = "butR1(3) + S(149) <=> butane(1) + butROO2(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 349,
    label = "S(149) + H(22) <=> C4H9O2(8) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3090, 'cm^3/(mol*s)'), n=3.24, Ea=(7.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 350,
    label = "C4H9O2(8) + H(22) <=> S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 351,
    label = "S(149) + O(20) <=> C4H9O2(8) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2850, 'cm^3/(mol*s)'), n=3.05, Ea=(3.123, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 352,
    label = "C4H9O2(8) + HO2(24) <=> O2(2) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.465, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 353,
    label = "C4H9O2(8) + H2O2(25) <=> S(149) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11.5, 'cm^3/(mol*s)'), n=2.94, Ea=(0.46, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 354,
    label = "S(149) + CH(26) <=> C4H9O2(8) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(300000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 355,
    label = "S(149) + CH2(28) <=> C4H9O2(8) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.721e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 356,
    label = "C4H9O2(8) + CH2O(32) <=> S(149) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 357,
    label = "S(149) + CH3(31) <=> C4H9O2(8) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.244e-05, 'cm^3/(mol*s)'),
        n = 4.99,
        Ea = (8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 358,
    label = "C4H9O2(8) + CH2OH(35) <=> S(149) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 359,
    label = "C4H9O2(8) + CH3O(36) <=> S(149) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 360,
    label = "C4H9O2(8) + CH3OH(37) <=> S(149) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 361,
    label = "S(149) + CH3O(36) <=> C4H9O2(8) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.581e+11, 'cm^3/(mol*s)'), n=0, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 362,
    label = "S(149) + C2H(38) <=> C4H9O2(8) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.806e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 363,
    label = "C4H9O2(8) + C2H3(41) <=> S(149) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 364,
    label = "S(149) + HCCO(40) <=> C4H9O2(8) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0495, 'cm^3/(mol*s)'), n=4.34, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 365,
    label = "S(149) + C2H3(41) <=> C4H9O2(8) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00054, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 366,
    label = "C4H9O2(8) + C2H5(44) <=> S(149) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 367,
    label = "C4H9O2(8) + C2H6(45) <=> S(149) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00552, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 368,
    label = "S(149) + OH(23) <=> C4H9O2(8) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.431e+09, 'cm^3/(mol*s)'),
        n = 1.152,
        Ea = (2.68, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 369,
    label = "C4H9O2(8) + HCCOH(48) <=> S(149) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 370,
    label = "C4H9O2(8) + CH3CHO(49) <=> C2H3O(18) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.037e-05, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 371,
    label = "C4H9O2(8) + C3H8(50) <=> C3H7(51) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00552, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 372,
    label = "butane(1) + C4H9O2(8) <=> butR2(4) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00368, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 373,
    label = "butane(1) + C4H9O2(8) <=> butR1(3) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00552, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 374,
    label = "butROO2(6) + C2H3O(18) <=> S(149) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 375,
    label = "C4H9O2(8) + C2H3O(18) <=> S(149) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 376,
    label = "C4H9O2(8) + S(149) <=> butROO2(6) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 377,
    label = "C3H6(144) + CH3(31) <=> butR2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(21000, 'cm^3/(mol*s)'), n=2.41, Ea=(5.32, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 378,
    label = "C3H6(144) + H(22) <=> C3H7(51)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.17e+08, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 379,
    label = "C3H7(51) + O(20) <=> C3H6(144) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 380,
    label = "C3H7(51) + H(22) <=> C3H6(144) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 381,
    label = "C3H7(51) + OH(23) <=> C3H6(144) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 382,
    label = "C3H7(51) + HO2(24) <=> C3H6(144) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 383,
    label = "C3H7(51) + CH(26) <=> C3H6(144) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 384,
    label = "C3H7(51) + CH2(28) <=> C3H6(144) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 385,
    label = "C3H7(51) + HCO(29) <=> C3H6(144) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 386,
    label = "C3H7(51) + CH3(31) <=> C3H6(144) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 387,
    label = "C3H7(51) + CH2OH(35) <=> C3H6(144) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 388,
    label = "C3H7(51) + CH3O(36) <=> C3H6(144) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 389,
    label = "C3H7(51) + C2H(38) <=> C3H6(144) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.206e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 390,
    label = "C3H7(51) + HCCO(40) <=> C3H6(144) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 391,
    label = "C3H7(51) + HCCO(40) <=> C3H6(144) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 392,
    label = "C3H7(51) + C2H3(41) <=> C3H6(144) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 393,
    label = "C3H7(51) + C2H5(44) <=> C3H6(144) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 394,
    label = "O2(2) + C3H7(51) <=> C3H6(144) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.666e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.85, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 395,
    label = "butR1(3) + C3H7(51) <=> butane(1) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 396,
    label = "butR2(4) + C3H7(51) <=> butane(1) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 397,
    label = "butROO2(6) + C3H7(51) <=> C3H6(144) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 398,
    label = "C4H9O2(8) + C3H7(51) <=> C3H6(144) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 399,
    label = "C2H3O(18) + C3H7(51) <=> C3H6(144) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 400,
    label = "C3H7(51) + C3H7(51) <=> C3H6(144) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 401,
    label = "CH2(S)(30) + C2H4(43) <=> C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.304e+12, 'cm^3/(mol*s)'),
        n = 0.007,
        Ea = (-1.045, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 402,
    label = "CH3(31) + C2H3(41) <=> C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 403,
    label = "CH3O2(75) <=> O2(2) + CH3(31)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.09e+14, 's^-1'), n=0.25, Ea=(33.3, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.09e+14, 's^-1'), n=0.25, Ea=(33.3, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 405,
    label = "CH3O2(75) + CH2(S)(30) <=> C2H5O2(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.672e+11, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 406,
    label = "O(20) + CH3O(36) <=> CH3O2(75)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 407,
    label = "HO2(24) + CH2(S)(30) <=> CH3O2(75)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.352e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 408,
    label = "butR2(4) + O(20) <=> C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 409,
    label = "C4H9O(147) + O(20) <=> butROO2(6)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 410,
    label = "C4H9O(147) + OH(23) <=> S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 411,
    label = "C2H5(44) + CH3CHO(49) <=> C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 412,
    label = "C3H7(95) + HO2(24) <=> O2(2) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.501, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 413,
    label = "butR1(3) + C3H8(50) <=> butane(1) + C3H7(95)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00184, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 414,
    label = "C3H7(95) + CH2(S)(30) <=> butR2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.411e+11, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 415,
    label = "butane(1) + C3H7(95) <=> butR2(4) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00346, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 416,
    label = "C3H7(95) + S(149) <=> butROO2(6) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 417,
    label = "C4H9O2(8) + C3H8(50) <=> C3H7(95) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00184, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 418,
    label = "C2H3O(18) + C3H8(50) <=> C3H7(95) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 419,
    label = "C3H7(51) <=> C3H7(95)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(718000, 's^-1'), n=2.05, Ea=(36.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 420,
    label = "C3H7(51) + C3H8(50) <=> C3H7(95) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00184, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 421,
    label = "C3H7(95) + H(22) <=> C3H6(144) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.332e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 422,
    label = "C3H6(144) + H(22) <=> C3H7(95)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e+09, 'cm^3/(mol*s)'),
        n = 1.553,
        Ea = (1.57, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 423,
    label = "O2(2) + C3H7(95) <=> C3H6(144) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.735e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.99, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 424,
    label = "C3H7(95) + CH(26) <=> C3H6(144) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.227e+10, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 425,
    label = "C3H7(95) + CH2(28) <=> C3H6(144) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.806e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 426,
    label = "C3H7(95) + HCO(29) <=> C3H6(144) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.086e+15, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 427,
    label = "C3H7(95) + CH3(31) <=> C3H6(144) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.314e+15, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 428,
    label = "C3H7(95) + CH2OH(35) <=> C3H6(144) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.734e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 429,
    label = "C3H7(95) + HCCO(40) <=> C3H6(144) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.12e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 430,
    label = "C3H7(95) + C2H3(41) <=> C3H6(144) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.12e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 431,
    label = "C3H7(95) + C2H5(44) <=> C3H6(144) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 432,
    label = "C2H3O(18) + C3H7(95) <=> C3H6(144) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.902e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 433,
    label = "C3H7(51) + C3H7(95) <=> C3H6(144) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.104e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 434,
    label = "C3H7(95) + C3H7(95) <=> C3H6(144) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.266e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 435,
    label = "butR2(4) + C3H7(95) <=> butane(1) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.266e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 436,
    label = "butR1(3) + C3H7(95) <=> butane(1) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 437,
    label = "C4H9O2(8) + C3H7(95) <=> C3H6(144) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 438,
    label = "C3H7(95) + O(20) <=> C3H6(144) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+09, 'cm^3/(mol*s)'), n=1.5, Ea=(-0.89, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 439,
    label = "H(22) + C3H8(50) <=> C3H7(95) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.678, 'cm^3/(mol*s)'), n=4.34, Ea=(3.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 440,
    label = "C3H7(95) + H(22) <=> C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 441,
    label = "C3H7(95) + OH(23) <=> C3H6(144) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.446e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 442,
    label = "O(20) + C3H8(50) <=> C3H7(95) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47800, 'cm^3/(mol*s)'), n=2.71, Ea=(2.11, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 443,
    label = "C3H7(95) + HO2(24) <=> C3H6(144) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 444,
    label = "C3H7(95) + H2O2(25) <=> HO2(24) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.141, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 445,
    label = "CH(26) + C3H8(50) <=> C3H7(95) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(200000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 446,
    label = "CH2(28) + C3H8(50) <=> C3H7(95) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(7.47, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 447,
    label = "C3H7(95) + CH2O(32) <=> HCO(29) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+11, 'cm^3/(mol*s)'), n=0, Ea=(6.96, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 448,
    label = "CH3(31) + C3H8(50) <=> C3H7(95) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.01606, 'cm^3/(mol*s)'), n=4.34, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 449,
    label = "C3H7(95) + CH2OH(35) <=> CH2O(32) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 450,
    label = "C3H7(95) + CH3O(36) <=> CH2O(32) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 451,
    label = "C3H7(95) + CH3O(36) <=> C3H6(144) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 452,
    label = "C3H7(95) + CH3OH(37) <=> CH2OH(35) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001752, 'cm^3/(mol*s)'),
        n = 4.416,
        Ea = (12.058, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 453,
    label = "CH3O(36) + C3H8(50) <=> C3H7(95) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 454,
    label = "C3H7(95) + C2H(38) <=> C3H6(144) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.166e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 455,
    label = "C2H(38) + C3H8(50) <=> C3H7(95) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 456,
    label = "C3H7(95) + HCCO(40) <=> C3H6(144) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 457,
    label = "C3H7(95) + C2H3(41) <=> C2H2(39) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 458,
    label = "HCCO(40) + C3H8(50) <=> C3H7(95) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0332, 'cm^3/(mol*s)'), n=4.34, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 459,
    label = "C2H3(41) + C3H8(50) <=> C3H7(95) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1020, 'cm^3/(mol*s)'), n=3.1, Ea=(8.82, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 460,
    label = "C3H7(95) + C2H5(44) <=> C2H4(43) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 461,
    label = "C2H5(44) + C3H8(50) <=> C3H7(95) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00184, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 462,
    label = "OH(23) + C3H8(50) <=> C3H7(95) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 463,
    label = "C3H7(95) + HCCOH(48) <=> HCCO(40) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 464,
    label = "butROO2(6) + C3H7(95) <=> C3H6(144) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 465,
    label = "C2H3O(18) + C3H7(95) <=> CH2CO(42) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 466,
    label = "H(22) + C4H8(96) <=> butR1(3)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.17e+08, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 467,
    label = "butR1(3) + O(20) <=> OH(23) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 468,
    label = "butR1(3) + H(22) <=> H2(21) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 469,
    label = "butR1(3) + OH(23) <=> H2O(46) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 470,
    label = "butR1(3) + HO2(24) <=> H2O2(25) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 471,
    label = "butR1(3) + CH(26) <=> CH2(28) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 472,
    label = "butR1(3) + CH2(28) <=> CH3(31) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 473,
    label = "butR1(3) + HCO(29) <=> CH2O(32) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 474,
    label = "butR1(3) + CH3(31) <=> CH4(33) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 475,
    label = "butR1(3) + CH2OH(35) <=> CH3OH(37) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 476,
    label = "butR1(3) + CH3O(36) <=> CH3OH(37) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 477,
    label = "butR1(3) + C2H(38) <=> C2H2(39) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.206e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 478,
    label = "butR1(3) + HCCO(40) <=> HCCOH(48) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 479,
    label = "butR1(3) + HCCO(40) <=> CH2CO(42) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 480,
    label = "butR1(3) + C2H3(41) <=> C2H4(43) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 481,
    label = "butR1(3) + C2H5(44) <=> C2H6(45) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 482,
    label = "O2(2) + butR1(3) <=> HO2(24) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.666e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.85, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 483,
    label = "butR1(3) + butR1(3) <=> butane(1) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 484,
    label = "H(22) + C4H8(96) <=> butR2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.48e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (0.51, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 485,
    label = "butR2(4) + O(20) <=> OH(23) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 486,
    label = "butR2(4) + H(22) <=> H2(21) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.166e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 487,
    label = "butR2(4) + OH(23) <=> H2O(46) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 488,
    label = "butR2(4) + HO2(24) <=> H2O2(25) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 489,
    label = "butR2(4) + CH(26) <=> CH2(28) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.137e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 490,
    label = "butR2(4) + CH2(28) <=> CH3(31) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 491,
    label = "butR2(4) + HCO(29) <=> CH2O(32) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 492,
    label = "butR2(4) + CH3(31) <=> CH4(33) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.57e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 493,
    label = "butR2(4) + CH2OH(35) <=> CH3OH(37) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 494,
    label = "butR2(4) + CH3O(36) <=> CH3OH(37) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 495,
    label = "butR2(4) + C2H(38) <=> C2H2(39) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.083e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 496,
    label = "butR2(4) + HCCO(40) <=> HCCOH(48) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 497,
    label = "butR2(4) + HCCO(40) <=> CH2CO(42) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 498,
    label = "butR2(4) + C2H3(41) <=> C2H4(43) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 499,
    label = "butR2(4) + C2H5(44) <=> C2H6(45) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 500,
    label = "O2(2) + butR2(4) <=> HO2(24) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.676e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.99, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 501,
    label = "butR1(3) + butR2(4) <=> butane(1) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.565e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 502,
    label = "butR2(4) + butR2(4) <=> butane(1) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 503,
    label = "butROO1(5) <=> HO2(24) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.58e+07, 's^-1'), n=1.46, Ea=(29.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 504,
    label = "butROO2(6) <=> HO2(24) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.937e+09, 's^-1'), n=1.17, Ea=(30.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 505,
    label = "butR1(3) + butROO2(6) <=> S(149) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 506,
    label = "butR2(4) + butROO2(6) <=> S(149) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 507,
    label = "butR1(3) + C4H9O2(8) <=> S(149) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 508,
    label = "butR2(4) + C4H9O2(8) <=> S(149) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 509,
    label = "butR1(3) + C2H3O(18) <=> CH3CHO(49) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 510,
    label = "butR2(4) + C2H3O(18) <=> CH3CHO(49) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 511,
    label = "butR1(3) + C3H7(51) <=> C3H8(50) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 512,
    label = "butR2(4) + C3H7(51) <=> C3H8(50) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 513,
    label = "C3H6(144) + CH2(S)(30) <=> C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.192e+14, 'cm^3/(mol*s)'),
        n = 0.324,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 514,
    label = "butR1(3) + C3H7(95) <=> C3H8(50) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 515,
    label = "butR2(4) + C3H7(95) <=> C3H8(50) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 516,
    label = "C2H3(41) + C2H5(44) <=> C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 517,
    label = "H(22) + CCOO(1350) <=> C2H5O2(90) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 518,
    label = "C2H5O2(90) + H(22) <=> CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 519,
    label = "O(20) + CCOO(1350) <=> C2H5O2(90) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 520,
    label = "C2H5O2(90) + HO2(24) <=> O2(2) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 521,
    label = "C2H5O2(90) + H2O2(25) <=> HO2(24) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 522,
    label = "CH(26) + CCOO(1350) <=> C2H5O2(90) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 523,
    label = "CH2(28) + CCOO(1350) <=> C2H5O2(90) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 524,
    label = "C2H5O2(90) + CH2O(32) <=> HCO(29) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 525,
    label = "CH3(31) + CCOO(1350) <=> C2H5O2(90) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 526,
    label = "C2H5O2(90) + CH2OH(35) <=> CH2O(32) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 527,
    label = "C2H5O2(90) + CH3O(36) <=> CH2O(32) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 528,
    label = "CH2OH(35) + CCOO(1350) <=> C2H5O2(90) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 529,
    label = "CH3O(36) + CCOO(1350) <=> C2H5O2(90) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 530,
    label = "C2H(38) + CCOO(1350) <=> C2H5O2(90) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 531,
    label = "C2H5O2(90) + C2H3(41) <=> C2H2(39) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 532,
    label = "HCCO(40) + CCOO(1350) <=> C2H5O2(90) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 533,
    label = "C2H3(41) + CCOO(1350) <=> C2H5O2(90) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 534,
    label = "C2H5O2(90) + C2H5(44) <=> C2H4(43) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 535,
    label = "C2H5(44) + CCOO(1350) <=> C2H5O2(90) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 536,
    label = "OH(23) + CCOO(1350) <=> C2H5O2(90) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 537,
    label = "C2H5O2(90) + HCCOH(48) <=> HCCO(40) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 538,
    label = "C2H3O(18) + CCOO(1350) <=> C2H5O2(90) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 539,
    label = "C3H7(95) + CCOO(1350) <=> C2H5O2(90) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 540,
    label = "C3H7(51) + CCOO(1350) <=> C2H5O2(90) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 541,
    label = "butR2(4) + CCOO(1350) <=> butane(1) + C2H5O2(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 542,
    label = "butR1(3) + CCOO(1350) <=> butane(1) + C2H5O2(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 543,
    label = "butR1(3) + C2H5O2(90) <=> C4H8(96) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 544,
    label = "butR2(4) + C2H5O2(90) <=> C4H8(96) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 545,
    label = "C2H3O(18) + C2H5O2(90) <=> CH2CO(42) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 546,
    label = "C3H7(51) + C2H5O2(90) <=> C3H6(144) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 547,
    label = "C4H9O2(8) + CCOO(1350) <=> C2H5O2(90) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 548,
    label = "butROO2(6) + CCOO(1350) <=> C2H5O2(90) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 549,
    label = "C2H5O2(90) + C3H7(95) <=> C3H6(144) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 550,
    label = "HO2(24) + C2H5(44) <=> CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 551,
    label = "O2(2) + C2H3O(18) <=> S(1139)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 552,
    label = "CH3O2(75) + CO(27) <=> S(1139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (274200, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (85.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 553,
    label = "S(1139) <=> HO2(24) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.203e+10, 's^-1'), n=0.622, Ea=(28.572, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 554,
    label = "C4H8(143) + H(22) <=> butR2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.37, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 555,
    label = "butR2(4) + O(20) <=> C4H8(143) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 556,
    label = "butR2(4) + H(22) <=> C4H8(143) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 557,
    label = "butR2(4) + OH(23) <=> C4H8(143) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 558,
    label = "butR2(4) + HO2(24) <=> C4H8(143) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 559,
    label = "butR2(4) + CH(26) <=> C4H8(143) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 560,
    label = "butR2(4) + CH2(28) <=> C4H8(143) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 561,
    label = "butR2(4) + HCO(29) <=> C4H8(143) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 562,
    label = "butR2(4) + CH3(31) <=> C4H8(143) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 563,
    label = "butR2(4) + CH2OH(35) <=> C4H8(143) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 564,
    label = "butR2(4) + CH3O(36) <=> C4H8(143) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 565,
    label = "butR2(4) + C2H(38) <=> C4H8(143) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.206e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 566,
    label = "butR2(4) + HCCO(40) <=> C4H8(143) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 567,
    label = "butR2(4) + HCCO(40) <=> C4H8(143) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 568,
    label = "butR2(4) + C2H3(41) <=> C4H8(143) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 569,
    label = "butR2(4) + C2H5(44) <=> C4H8(143) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 570,
    label = "O2(2) + butR2(4) <=> C4H8(143) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.666e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.85, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 571,
    label = "butR1(3) + butR2(4) <=> butane(1) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 572,
    label = "butR2(4) + butR2(4) <=> butane(1) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 573,
    label = "butROO2(6) <=> C4H8(143) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+09, 's^-1'), n=1.01, Ea=(29.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 574,
    label = "butR2(4) + butROO2(6) <=> C4H8(143) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 575,
    label = "butR2(4) + C4H9O2(8) <=> C4H8(143) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 576,
    label = "butR2(4) + C2H3O(18) <=> C4H8(143) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 577,
    label = "butR2(4) + C2H5O2(90) <=> C4H8(143) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 578,
    label = "butR2(4) + C3H7(51) <=> C4H8(143) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 579,
    label = "C3H6(144) + CH2(S)(30) <=> C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+11, 'cm^3/(mol*s)'),
        n = 0.465,
        Ea = (-1.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 580,
    label = "butR2(4) + C3H7(95) <=> C4H8(143) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 581,
    label = "butR2(4) + C2H5O(71) <=> butane(1) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 582,
    label = "butR1(3) + C2H5O(71) <=> butane(1) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 583,
    label = "C2H5O(71) + O(20) <=> C2H5O2(90)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 584,
    label = "C4H9O2(8) + C2H5O(71) <=> S(149) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 585,
    label = "C2H5O(71) + OH(23) <=> CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 586,
    label = "H(22) + CH3CHO(49) <=> C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.76e+06, 'cm^3/(mol*s)'),
        n = 1.99,
        Ea = (5.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 587,
    label = "CH3(31) + CH2O(32) <=> C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(216, 'cm^3/(mol*s)'), n=2.97, Ea=(3.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 588,
    label = "O(20) + C2H5(44) <=> C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 589,
    label = "CH2(S)(30) + CH3O(36) <=> C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.055e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 590,
    label = "C2H5O(71) + O(20) <=> OH(23) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 591,
    label = "C2H5O(71) + H(22) <=> H2(21) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 592,
    label = "C2H5O(71) + OH(23) <=> H2O(46) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 593,
    label = "C2H5O(71) + HO2(24) <=> H2O2(25) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 594,
    label = "C2H5O(71) + CH(26) <=> CH2(28) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 595,
    label = "C2H5O(71) + CH2(28) <=> CH3(31) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 596,
    label = "C2H5O(71) + HCO(29) <=> CH2O(32) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 597,
    label = "C2H5O(71) + CH3(31) <=> CH4(33) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 598,
    label = "C2H5O(71) + CH2OH(35) <=> CH3OH(37) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 599,
    label = "C2H5O(71) + CH3O(36) <=> CH3OH(37) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 600,
    label = "C2H5O(71) + C2H(38) <=> C2H2(39) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.206e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 601,
    label = "C2H5O(71) + HCCO(40) <=> HCCOH(48) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 602,
    label = "C2H5O(71) + HCCO(40) <=> CH2CO(42) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 603,
    label = "C2H5O(71) + C2H3(41) <=> C2H4(43) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 604,
    label = "C2H5O(71) + C2H5(44) <=> C2H6(45) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 605,
    label = "O2(2) + C2H5O(71) <=> HO2(24) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 606,
    label = "butROO2(6) + C2H5O(71) <=> S(149) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 607,
    label = "C2H3O(18) + C2H5O(71) <=> CH3CHO(49) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 608,
    label = "C2H5O(71) + C2H5O2(90) <=> CH3CHO(49) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 609,
    label = "C3H7(51) + C2H5O(71) <=> CH3CHO(49) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 610,
    label = "C2H5O(71) + C3H7(95) <=> CH3CHO(49) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 611,
    label = "H(22) + COO(1544) <=> CH3O2(75) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 612,
    label = "CH3O2(75) + H(22) <=> COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 613,
    label = "O(20) + COO(1544) <=> CH3O2(75) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 614,
    label = "CH3O2(75) + HO2(24) <=> O2(2) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 615,
    label = "CH3O2(75) + H2O2(25) <=> HO2(24) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 616,
    label = "CH(26) + COO(1544) <=> CH3O2(75) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 617,
    label = "CH2(28) + COO(1544) <=> CH3O2(75) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 618,
    label = "CH3O2(75) + CH2O(32) <=> HCO(29) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 619,
    label = "CH3(31) + COO(1544) <=> CH3O2(75) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 620,
    label = "CH3O2(75) + CH2OH(35) <=> CH2O(32) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 621,
    label = "CH3O2(75) + CH3O(36) <=> CH2O(32) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 622,
    label = "CH2OH(35) + COO(1544) <=> CH3O2(75) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 623,
    label = "CH3O(36) + COO(1544) <=> CH3O2(75) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 624,
    label = "C2H(38) + COO(1544) <=> CH3O2(75) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 625,
    label = "CH3O2(75) + C2H3(41) <=> C2H2(39) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 626,
    label = "HCCO(40) + COO(1544) <=> CH3O2(75) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 627,
    label = "C2H3(41) + COO(1544) <=> CH3O2(75) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 628,
    label = "CH3O2(75) + C2H5(44) <=> C2H4(43) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 629,
    label = "C2H5(44) + COO(1544) <=> CH3O2(75) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 630,
    label = "OH(23) + COO(1544) <=> CH3O2(75) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 631,
    label = "CH3O2(75) + HCCOH(48) <=> HCCO(40) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 632,
    label = "C2H3O(18) + COO(1544) <=> CH3O2(75) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 633,
    label = "C3H7(95) + COO(1544) <=> CH3O2(75) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 634,
    label = "C3H7(51) + COO(1544) <=> CH3O2(75) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 635,
    label = "butR2(4) + COO(1544) <=> butane(1) + CH3O2(75)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 636,
    label = "butR1(3) + COO(1544) <=> butane(1) + CH3O2(75)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 637,
    label = "butR1(3) + CH3O2(75) <=> C4H8(96) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 638,
    label = "butR2(4) + CH3O2(75) <=> C4H8(143) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 639,
    label = "butR2(4) + CH3O2(75) <=> C4H8(96) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 640,
    label = "C2H3O(18) + CH3O2(75) <=> CH2CO(42) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 641,
    label = "C3H7(51) + CH3O2(75) <=> C3H6(144) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 642,
    label = "C4H9O2(8) + COO(1544) <=> CH3O2(75) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 643,
    label = "CH3O2(75) + S(149) <=> butROO2(6) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 644,
    label = "CH3O2(75) + C3H7(95) <=> C3H6(144) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 645,
    label = "CH2(S)(30) + COO(1544) <=> CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.672e+11, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 646,
    label = "CH3O2(75) + CCOO(1350) <=> C2H5O2(90) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 647,
    label = "C2H5O(71) + CH3O2(75) <=> CH3CHO(49) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 648,
    label = "H2O2(25) + CH2(S)(30) <=> COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.703e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 649,
    label = "HO2(24) + CH3(31) <=> COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 650,
    label = "OH(23) + CH3O(36) <=> COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 651,
    label = "S(235) + CH2(S)(30) <=> butROO2(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.603e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 652,
    label = "C2H5O2(90) + CH2(S)(30) <=> S(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.115e+11, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 653,
    label = "S(235) <=> C3H6(144) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.874e+09, 's^-1'), n=1.17, Ea=(30.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 654,
    label = "O2(2) + C3H7(95) <=> S(235)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 655,
    label = "O2(2) + C3H5O(17) <=> S(1019)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 656,
    label = "C2H5O2(90) + CO(27) <=> S(1019)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3228, 'cm^3/(mol*s)'), n=3.29, Ea=(104.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 657,
    label = "H(22) + C3H5(1446) <=> C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 658,
    label = "C3H6(144) + O(20) <=> OH(23) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.502e+07, 'cm^3/(mol*s)'),
        n = 2.017,
        Ea = (3.981, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 659,
    label = "C3H6(144) + H(22) <=> H2(21) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3360, 'cm^3/(mol*s)'), n=3.14, Ea=(4.29, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 660,
    label = "C3H6(144) + OH(23) <=> H2O(46) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.045, 'cm^3/(mol*s)'),
        n = 3.684,
        Ea = (-1.28, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 661,
    label = "H2O2(25) + C3H5(1446) <=> C3H6(144) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0351, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 662,
    label = "C3H6(144) + CH(26) <=> CH2(28) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(300000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 663,
    label = "C3H6(144) + CH2(28) <=> CH3(31) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.721e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 664,
    label = "CH2O(32) + C3H5(1446) <=> C3H6(144) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0613, 'cm^3/(mol*s)'),
        n = 3.95,
        Ea = (12.22, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 665,
    label = "C3H6(144) + CH3(31) <=> CH4(33) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.072, 'cm^3/(mol*s)'), n=4.25, Ea=(7.53, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 666,
    label = "CH3O(36) + C3H5(1446) <=> C3H6(144) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 667,
    label = "CH2OH(35) + C3H5(1446) <=> C3H6(144) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 668,
    label = "C3H6(144) + CH2OH(35) <=> CH3OH(37) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 669,
    label = "C3H6(144) + CH3O(36) <=> CH3OH(37) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7902, 'cm^3/(mol*s)'),
        n = 3.82,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 670,
    label = "C3H6(144) + C2H(38) <=> C2H2(39) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (360000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 671,
    label = "C2H3(41) + C3H5(1446) <=> C3H6(144) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 672,
    label = "HCCOH(48) + C3H5(1446) <=> C3H6(144) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 673,
    label = "C3H6(144) + HCCO(40) <=> CH2CO(42) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00492, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (10.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 674,
    label = "C3H6(144) + C2H3(41) <=> C2H4(43) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00666, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 675,
    label = "C2H3O(18) + C3H5(1446) <=> C3H6(144) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 676,
    label = "C2H5(44) + C3H5(1446) <=> C3H6(144) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 677,
    label = "C3H6(144) + C2H5(44) <=> C2H6(45) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00087, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 678,
    label = "C2H5O(71) + C3H5(1446) <=> C3H6(144) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 679,
    label = "HO2(24) + C3H5(1446) <=> O2(2) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 680,
    label = "butR1(3) + C3H6(144) <=> butane(1) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00087, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 681,
    label = "butR2(4) + C3H6(144) <=> butane(1) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001008, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 682,
    label = "S(149) + C3H5(1446) <=> butROO2(6) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 683,
    label = "C4H9O2(8) + C3H6(144) <=> S(149) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00087, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 684,
    label = "C2H3O(18) + C3H6(144) <=> CH3CHO(49) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 685,
    label = "C3H5(1446) + CCOO(1350) <=> C2H5O2(90) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 686,
    label = "C3H7(51) + C3H6(144) <=> C3H8(50) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00087, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 687,
    label = "C3H7(51) + C3H5(1446) <=> C3H6(144) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 688,
    label = "C3H7(95) + C3H5(1446) <=> C3H6(144) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.374e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 689,
    label = "C3H5(1446) + COO(1544) <=> CH3O2(75) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 690,
    label = "C3H7(95) + C3H6(144) <=> C3H8(50) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001008, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 691,
    label = "CH3(31) + C3H5(1446) <=> C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 692,
    label = "butR1(3) + C3H5(1446) <=> C3H6(144) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 693,
    label = "butR2(4) + C3H5(1446) <=> C3H6(144) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 694,
    label = "butR2(4) + C3H5(1446) <=> C4H8(143) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 695,
    label = "O2(2) + C3H5(1446) <=> S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 696,
    label = "H(22) + C3H4(2124) <=> C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.84e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.82, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 697,
    label = "O(20) + C3H5(1446) <=> OH(23) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.684e+09, 'cm^3/(mol*s)'),
        n = 0.625,
        Ea = (-0.237, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 698,
    label = "H(22) + C3H5(1446) <=> H2(21) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 699,
    label = "OH(23) + C3H5(1446) <=> H2O(46) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 700,
    label = "HO2(24) + C3H5(1446) <=> H2O2(25) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 701,
    label = "CH(26) + C3H5(1446) <=> CH2(28) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 702,
    label = "CH2(28) + C3H5(1446) <=> CH3(31) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.356e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 703,
    label = "HCO(29) + C3H5(1446) <=> CH2O(32) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 704,
    label = "CH3(31) + C3H5(1446) <=> CH4(33) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 705,
    label = "CH2OH(35) + C3H5(1446) <=> CH3OH(37) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 706,
    label = "CH3O(36) + C3H5(1446) <=> CH3OH(37) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 707,
    label = "C2H(38) + C3H5(1446) <=> C2H2(39) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.109e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 708,
    label = "HCCO(40) + C3H5(1446) <=> HCCOH(48) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 709,
    label = "HCCO(40) + C3H5(1446) <=> CH2CO(42) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 710,
    label = "C2H3(41) + C3H5(1446) <=> C2H4(43) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 711,
    label = "C2H5(44) + C3H5(1446) <=> C2H6(45) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 712,
    label = "O2(2) + C3H5(1446) <=> HO2(24) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13.55, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 713,
    label = "butR1(3) + C3H5(1446) <=> butane(1) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 714,
    label = "butR2(4) + C3H5(1446) <=> butane(1) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 715,
    label = "butROO2(6) + C3H5(1446) <=> S(149) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 716,
    label = "C4H9O2(8) + C3H5(1446) <=> S(149) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 717,
    label = "C2H3O(18) + C3H5(1446) <=> CH3CHO(49) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 718,
    label = "C2H5O2(90) + C3H5(1446) <=> C3H4(2124) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 719,
    label = "C3H7(51) + C3H5(1446) <=> C3H8(50) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 720,
    label = "CH3O2(75) + C3H5(1446) <=> COO(1544) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 721,
    label = "C3H7(95) + C3H5(1446) <=> C3H8(50) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 722,
    label = "C3H5(1446) + C3H5(1446) <=> C3H6(144) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+10, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 723,
    label = "S(2185) <=> HO2(24) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.63e+09, 's^-1'), n=1.11, Ea=(42.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 724,
    label = "C4H7(1663) + H(22) <=> C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 725,
    label = "O(20) + C4H8(96) <=> C4H7(1663) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (83250, 'cm^3/(mol*s)'),
        n = 2.59,
        Ea = (1.495, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 726,
    label = "C4H7(1663) + H2(21) <=> H(22) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0458, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (22.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 727,
    label = "OH(23) + C4H8(96) <=> C4H7(1663) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(67, 'cm^3/(mol*s)'), n=3.475, Ea=(-2.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 728,
    label = "HO2(24) + C4H8(96) <=> C4H7(1663) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000508, 'cm^3/(mol*s)'),
        n = 4.59,
        Ea = (7.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 729,
    label = "CH(26) + C4H8(96) <=> C4H7(1663) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(200000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 730,
    label = "CH2(28) + C4H8(96) <=> C4H7(1663) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(7.47, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 731,
    label = "HCO(29) + C4H8(96) <=> C4H7(1663) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 732,
    label = "C4H7(1663) + CH4(33) <=> CH3(31) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0424, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (24.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 733,
    label = "C4H7(1663) + CH3O(36) <=> CH2O(32) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 734,
    label = "C4H7(1663) + CH2OH(35) <=> CH2O(32) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 735,
    label = "CH2OH(35) + C4H8(96) <=> C4H7(1663) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 736,
    label = "CH3O(36) + C4H8(96) <=> C4H7(1663) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 737,
    label = "C2H(38) + C4H8(96) <=> C4H7(1663) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 738,
    label = "C4H7(1663) + C2H3(41) <=> C2H2(39) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 739,
    label = "C4H7(1663) + HCCOH(48) <=> HCCO(40) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 740,
    label = "C4H7(1663) + CH2CO(42) <=> HCCO(40) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0338, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (20.996, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 741,
    label = "C2H3(41) + C4H8(96) <=> C4H7(1663) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01692, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 742,
    label = "C2H3O(18) + C4H7(1663) <=> CH2CO(42) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 743,
    label = "C4H7(1663) + C2H5(44) <=> C2H4(43) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 744,
    label = "C2H5(44) + C4H8(96) <=> C4H7(1663) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001806, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 745,
    label = "C2H5O(71) + C4H7(1663) <=> CH3CHO(49) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 746,
    label = "C4H7(1663) + HO2(24) <=> O2(2) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.645, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 747,
    label = "butR1(3) + C4H8(96) <=> butane(1) + C4H7(1663)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001806, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 748,
    label = "butane(1) + C4H7(1663) <=> butR2(4) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.02952, 'cm^3/(mol*s)'), n=4.34, Ea=(18, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 749,
    label = "butROO2(6) + C4H8(96) <=> C4H7(1663) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 750,
    label = "C4H9O2(8) + C4H8(96) <=> C4H7(1663) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001806, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 751,
    label = "C2H3O(18) + C4H8(96) <=> C4H7(1663) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 752,
    label = "C2H5O2(90) + C4H8(96) <=> C4H7(1663) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 753,
    label = "C3H7(51) + C4H8(96) <=> C4H7(1663) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001806, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 754,
    label = "C3H7(51) + C4H7(1663) <=> C3H6(144) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 755,
    label = "C4H7(1663) + C3H7(95) <=> C3H6(144) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.949e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 756,
    label = "CH3O2(75) + C4H8(96) <=> C4H7(1663) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 757,
    label = "C3H7(95) + C4H8(96) <=> C4H7(1663) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001706, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 758,
    label = "butR1(3) + C4H7(1663) <=> C4H8(96) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 759,
    label = "butR2(4) + C4H7(1663) <=> C4H8(96) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 760,
    label = "C4H7(1663) + H(22) <=> C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 761,
    label = "C4H8(143) + O(20) <=> C4H7(1663) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+07, 'cm^3/(mol*s)'),
        n = 2.017,
        Ea = (3.981, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 762,
    label = "C4H8(143) + H(22) <=> C4H7(1663) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6720, 'cm^3/(mol*s)'), n=3.14, Ea=(4.29, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 763,
    label = "C4H8(143) + OH(23) <=> C4H7(1663) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12.18, 'cm^3/(mol*s)'),
        n = 3.774,
        Ea = (-1.49, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 764,
    label = "C4H8(143) + HO2(24) <=> C4H7(1663) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00347, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 765,
    label = "C4H8(143) + CH(26) <=> C4H7(1663) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 766,
    label = "C4H8(143) + CH2(28) <=> C4H7(1663) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.443e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 767,
    label = "C4H7(1663) + CH2O(32) <=> C4H8(143) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0613, 'cm^3/(mol*s)'),
        n = 3.95,
        Ea = (12.22, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 768,
    label = "C4H8(143) + CH3(31) <=> C4H7(1663) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.144, 'cm^3/(mol*s)'), n=4.25, Ea=(7.53, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 769,
    label = "C4H7(1663) + CH3O(36) <=> C4H8(143) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 770,
    label = "C4H7(1663) + CH2OH(35) <=> C4H8(143) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 771,
    label = "C4H8(143) + CH2OH(35) <=> C4H7(1663) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008866, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 772,
    label = "C4H8(143) + CH3O(36) <=> C4H7(1663) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58, 'cm^3/(mol*s)'), n=3.82, Ea=(1.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 773,
    label = "C4H8(143) + C2H(38) <=> C4H7(1663) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (720000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 774,
    label = "C4H7(1663) + C2H3(41) <=> C4H8(143) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 775,
    label = "C4H7(1663) + HCCOH(48) <=> C4H8(143) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 776,
    label = "C4H8(143) + HCCO(40) <=> C4H7(1663) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00984, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (10.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 777,
    label = "C4H8(143) + C2H3(41) <=> C4H7(1663) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01332, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 778,
    label = "C2H3O(18) + C4H7(1663) <=> C4H8(143) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 779,
    label = "C4H7(1663) + C2H5(44) <=> C4H8(143) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 780,
    label = "C4H8(143) + C2H5(44) <=> C4H7(1663) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00174, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 781,
    label = "C2H5O(71) + C4H7(1663) <=> C4H8(143) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 782,
    label = "C4H7(1663) + HO2(24) <=> O2(2) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 783,
    label = "butR1(3) + C4H8(143) <=> butane(1) + C4H7(1663)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00174, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 784,
    label = "butR2(4) + C4H8(143) <=> butane(1) + C4H7(1663)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002016, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 785,
    label = "C4H7(1663) + S(149) <=> butROO2(6) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 786,
    label = "C4H9O2(8) + C4H8(143) <=> C4H7(1663) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00174, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 787,
    label = "C2H3O(18) + C4H8(143) <=> C4H7(1663) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008866, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 788,
    label = "C4H7(1663) + CCOO(1350) <=> C2H5O2(90) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 789,
    label = "C3H7(51) + C4H8(143) <=> C4H7(1663) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00174, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 790,
    label = "C3H7(51) + C4H7(1663) <=> C4H8(143) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 791,
    label = "C4H7(1663) + C3H7(95) <=> C4H8(143) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.374e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 792,
    label = "C4H7(1663) + COO(1544) <=> CH3O2(75) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 793,
    label = "C3H7(95) + C4H8(143) <=> C4H7(1663) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002016, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 794,
    label = "butR1(3) + C4H7(1663) <=> C4H8(143) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 795,
    label = "butR2(4) + C4H7(1663) <=> C4H8(143) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 796,
    label = "butR2(4) + C4H7(1663) <=> C4H8(143) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 797,
    label = "CH2(S)(30) + C3H5(1446) <=> C4H7(1663)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+11, 'cm^3/(mol*s)'),
        n = 0.465,
        Ea = (-1.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 798,
    label = "C4H8(96) + C3H5(1446) <=> C4H7(1663) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00904, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 799,
    label = "C4H8(143) + C3H5(1446) <=> C4H7(1663) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0087, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (13.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 800,
    label = "C4H7(1663) + C3H5(1446) <=> C4H8(96) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 801,
    label = "C4H7(1663) + C3H5(1446) <=> C4H8(143) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+10, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 802,
    label = "C4H7(1663) + C4H8(96) <=> C4H7(1663) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00904, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 803,
    label = "O2(2) + HCO(29) <=> CHO3(74)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 804,
    label = "HO2(24) + CO(27) <=> CHO3(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (59200, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 805,
    label = "C3H5(1446) <=> C3H5(2125)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 's^-1'), n=0.19, Ea=(26.377, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 806,
    label = "H(22) + C4H6(2483) <=> C4H7(1663)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.62e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (-0.47, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 807,
    label = "C4H7(1663) + O(20) <=> OH(23) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 808,
    label = "C4H7(1663) + H(22) <=> H2(21) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.166e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 809,
    label = "C4H7(1663) + OH(23) <=> H2O(46) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 810,
    label = "C4H7(1663) + HO2(24) <=> H2O2(25) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 811,
    label = "C4H7(1663) + CH(26) <=> CH2(28) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.137e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 812,
    label = "C4H7(1663) + CH2(28) <=> CH3(31) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 813,
    label = "C4H7(1663) + HCO(29) <=> CH2O(32) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 814,
    label = "C4H7(1663) + CH3(31) <=> CH4(33) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.57e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 815,
    label = "C4H7(1663) + CH2OH(35) <=> CH3OH(37) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 816,
    label = "C4H7(1663) + CH3O(36) <=> CH3OH(37) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 817,
    label = "C4H7(1663) + C2H(38) <=> C2H2(39) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.083e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 818,
    label = "C4H7(1663) + HCCO(40) <=> HCCOH(48) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 819,
    label = "C4H7(1663) + HCCO(40) <=> CH2CO(42) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 820,
    label = "C4H7(1663) + C2H3(41) <=> C2H4(43) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 821,
    label = "C4H7(1663) + C2H5(44) <=> C2H6(45) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 822,
    label = "O2(2) + C4H7(1663) <=> HO2(24) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.676e+13, 'cm^3/(mol*s)'), n=0, Ea=(22, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 823,
    label = "butR1(3) + C4H7(1663) <=> butane(1) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 824,
    label = "butR2(4) + C4H7(1663) <=> butane(1) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 825,
    label = "butROO2(6) + C4H7(1663) <=> S(149) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 826,
    label = "C4H9O2(8) + C4H7(1663) <=> S(149) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 827,
    label = "C2H3O(18) + C4H7(1663) <=> CH3CHO(49) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 828,
    label = "C4H7(1663) + C2H5O2(90) <=> C4H6(2483) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 829,
    label = "C3H7(51) + C4H7(1663) <=> C3H8(50) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 830,
    label = "C4H7(1663) + CH3O2(75) <=> COO(1544) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 831,
    label = "C4H7(1663) + C3H7(95) <=> C3H8(50) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 832,
    label = "C4H7(1663) + C3H5(1446) <=> C3H6(144) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 833,
    label = "C4H7(1663) + C4H7(1663) <=> C4H8(143) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 834,
    label = "C4H7(1663) + C4H7(1663) <=> C4H8(96) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 835,
    label = "C2H3(41) + C2H3(41) <=> C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 836,
    label = "CH2(S)(30) + S(2185) <=> S(2275)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.115e+11, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 837,
    label = "O2(2) + C4H7(1663) <=> S(2275)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 838,
    label = "S(2275) <=> HO2(24) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.476e+06, 's^-1'), n=1.829, Ea=(24.247, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 839,
    label = "CH2(S)(30) + S(2185) <=> S(2277)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+11, 'cm^3/(mol*s)'),
        n = 0.465,
        Ea = (-1.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 840,
    label = "O2(2) + C4H7(1663) <=> S(2277)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 841,
    label = "HO2(24) + C3H5(1446) <=> S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 842,
    label = "H(22) + S(2134) <=> H2(21) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 843,
    label = "H(22) + S(2185) <=> S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 844,
    label = "O(20) + S(2134) <=> OH(23) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 845,
    label = "HO2(24) + S(2185) <=> O2(2) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 846,
    label = "H2O2(25) + S(2185) <=> HO2(24) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 847,
    label = "CH(26) + S(2134) <=> CH2(28) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 848,
    label = "CH2(28) + S(2134) <=> CH3(31) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 849,
    label = "CH2O(32) + S(2185) <=> HCO(29) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 850,
    label = "CH3(31) + S(2134) <=> CH4(33) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 851,
    label = "CH2OH(35) + S(2185) <=> CH2O(32) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 852,
    label = "CH3O(36) + S(2185) <=> CH2O(32) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 853,
    label = "CH2OH(35) + S(2134) <=> CH3OH(37) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 854,
    label = "CH3O(36) + S(2134) <=> CH3OH(37) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 855,
    label = "C2H(38) + S(2134) <=> C2H2(39) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 856,
    label = "C2H3(41) + S(2185) <=> C2H2(39) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 857,
    label = "HCCO(40) + S(2134) <=> CH2CO(42) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 858,
    label = "C2H3(41) + S(2134) <=> C2H4(43) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 859,
    label = "C2H5(44) + S(2185) <=> C2H4(43) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 860,
    label = "C2H5(44) + S(2134) <=> C2H6(45) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 861,
    label = "OH(23) + S(2134) <=> H2O(46) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 862,
    label = "HCCOH(48) + S(2185) <=> HCCO(40) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 863,
    label = "C2H3O(18) + S(2134) <=> CH3CHO(49) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 864,
    label = "C3H7(95) + S(2134) <=> C3H8(50) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 865,
    label = "C3H7(51) + S(2134) <=> C3H8(50) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 866,
    label = "butR2(4) + S(2134) <=> butane(1) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 867,
    label = "butR1(3) + S(2134) <=> butane(1) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 868,
    label = "butR1(3) + S(2185) <=> C4H8(96) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 869,
    label = "butR2(4) + S(2185) <=> C4H8(143) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 870,
    label = "butR2(4) + S(2185) <=> C4H8(96) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 871,
    label = "C2H3O(18) + S(2185) <=> CH2CO(42) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 872,
    label = "C3H7(51) + S(2185) <=> C3H6(144) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 873,
    label = "C4H9O2(8) + S(2134) <=> S(149) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 874,
    label = "S(149) + S(2185) <=> butROO2(6) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 875,
    label = "C3H5(1446) + S(2134) <=> C3H6(144) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 876,
    label = "C3H7(95) + S(2185) <=> C3H6(144) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 877,
    label = "C4H8(96) + S(2185) <=> C4H7(1663) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 878,
    label = "S(2185) + CCOO(1350) <=> C2H5O2(90) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 879,
    label = "C4H7(1663) + S(2134) <=> C4H8(143) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 880,
    label = "C2H5O(71) + S(2185) <=> CH3CHO(49) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 881,
    label = "COO(1544) + S(2185) <=> CH3O2(75) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 882,
    label = "C3H5(1446) + S(2185) <=> C3H4(2124) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 883,
    label = "C4H7(1663) + S(2185) <=> S(2134) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 884,
    label = "H(22) + S(2644) <=> CHO3(74) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 885,
    label = "CHO3(74) + H(22) <=> S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 886,
    label = "O(20) + S(2644) <=> CHO3(74) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 887,
    label = "CHO3(74) + HO2(24) <=> O2(2) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 888,
    label = "CHO3(74) + H2O2(25) <=> HO2(24) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 889,
    label = "CH(26) + S(2644) <=> CHO3(74) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 890,
    label = "CH2(28) + S(2644) <=> CHO3(74) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 891,
    label = "CHO3(74) + CH2O(32) <=> HCO(29) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 892,
    label = "CH3(31) + S(2644) <=> CHO3(74) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 893,
    label = "CHO3(74) + CH2OH(35) <=> CH2O(32) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 894,
    label = "CHO3(74) + CH3O(36) <=> CH2O(32) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 895,
    label = "CHO3(74) + CH3OH(37) <=> CH2OH(35) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (938900, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (9.917, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 896,
    label = "CH3O(36) + S(2644) <=> CHO3(74) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 897,
    label = "C2H(38) + S(2644) <=> CHO3(74) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 898,
    label = "CHO3(74) + C2H3(41) <=> C2H2(39) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 899,
    label = "HCCO(40) + S(2644) <=> CHO3(74) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 900,
    label = "C2H3(41) + S(2644) <=> CHO3(74) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 901,
    label = "CHO3(74) + C2H5(44) <=> C2H4(43) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 902,
    label = "C2H5(44) + S(2644) <=> CHO3(74) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 903,
    label = "OH(23) + S(2644) <=> CHO3(74) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 904,
    label = "CHO3(74) + HCCOH(48) <=> HCCO(40) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 905,
    label = "C2H3O(18) + S(2644) <=> CHO3(74) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (0.746, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 906,
    label = "CHO3(74) + C3H8(50) <=> C3H7(95) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17.686, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 907,
    label = "C3H7(51) + S(2644) <=> CHO3(74) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 908,
    label = "butR2(4) + S(2644) <=> butane(1) + CHO3(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 909,
    label = "butR1(3) + S(2644) <=> butane(1) + CHO3(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 910,
    label = "butR1(3) + CHO3(74) <=> C4H8(96) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 911,
    label = "butR2(4) + CHO3(74) <=> C4H8(143) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 912,
    label = "butR2(4) + CHO3(74) <=> C4H8(96) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 913,
    label = "C2H3O(18) + CHO3(74) <=> CH2CO(42) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 914,
    label = "C3H7(51) + CHO3(74) <=> C3H6(144) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 915,
    label = "C4H9O2(8) + S(2644) <=> CHO3(74) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 916,
    label = "CHO3(74) + S(149) <=> butROO2(6) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 917,
    label = "CHO3(74) + C3H6(144) <=> C3H5(1446) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001735, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 918,
    label = "CHO3(74) + C3H7(95) <=> C3H6(144) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 919,
    label = "CHO3(74) + C4H8(96) <=> C4H7(1663) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 920,
    label = "CHO3(74) + CCOO(1350) <=> C2H5O2(90) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 921,
    label = "CHO3(74) + C4H8(143) <=> C4H7(1663) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00347, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 922,
    label = "C2H5O(71) + CHO3(74) <=> CH3CHO(49) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 923,
    label = "CHO3(74) + COO(1544) <=> CH3O2(75) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 924,
    label = "CHO3(74) + C3H5(1446) <=> S(2644) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 925,
    label = "C4H7(1663) + CHO3(74) <=> S(2644) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 926,
    label = "CHO3(74) + S(2134) <=> S(2644) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 927,
    label = "H2O2(25) + CO(27) <=> S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.254, 'cm^3/(mol*s)'), n=3.7, Ea=(53.36, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 928,
    label = "HO2(24) + HCO(29) <=> S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 929,
    label = "O2(2) + C3H4(2124) <=> S(2439)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2056, 'cm^3/(mol*s)'),
        n = 2.67,
        Ea = (14.261, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 930,
    label = "butR2(4) + CHO2(57) <=> butane(1) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 931,
    label = "butR1(3) + CHO2(57) <=> butane(1) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 932,
    label = "C4H9O2(8) + CHO2(57) <=> S(149) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 933,
    label = "CHO2(57) + C3H5(1446) <=> C3H6(144) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 934,
    label = "CHO2(57) + C4H7(1663) <=> CO2(34) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 935,
    label = "CHO2(57) + C4H7(1663) <=> C4H8(143) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 936,
    label = "CHO2(57) + O(20) <=> CHO3(74)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 937,
    label = "CHO2(57) + OH(23) <=> S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 938,
    label = "H(22) + CO2(34) <=> CHO2(57)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.134e+09, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 939,
    label = "O(20) + HCO(29) <=> CHO2(57)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 940,
    label = "CHO2(57) + O(20) <=> OH(23) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.837e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 941,
    label = "CHO2(57) + H(22) <=> H2(21) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.314e+11, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (0.023, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 942,
    label = "CHO2(57) + OH(23) <=> CO2(34) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 943,
    label = "CHO2(57) + HO2(24) <=> H2O2(25) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 944,
    label = "CHO2(57) + CH(26) <=> CH2(28) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.046e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 945,
    label = "CHO2(57) + CH2(28) <=> CH3(31) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.04e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 946,
    label = "CHO2(57) + HCO(29) <=> CH2O(32) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 947,
    label = "CHO2(57) + CH3(31) <=> CH4(33) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 948,
    label = "CHO2(57) + CH2OH(35) <=> CO2(34) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 949,
    label = "CHO2(57) + CH3O(36) <=> CO2(34) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 950,
    label = "CHO2(57) + C2H(38) <=> CO2(34) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.297e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 951,
    label = "CHO2(57) + HCCO(40) <=> CO2(34) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 952,
    label = "CHO2(57) + HCCO(40) <=> CO2(34) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 953,
    label = "CHO2(57) + C2H3(41) <=> CO2(34) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 954,
    label = "CHO2(57) + C2H5(44) <=> CO2(34) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 955,
    label = "O2(2) + CHO2(57) <=> HO2(24) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.908, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 956,
    label = "butROO2(6) + CHO2(57) <=> S(149) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 957,
    label = "C2H3O(18) + CHO2(57) <=> CO2(34) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 958,
    label = "CHO2(57) + C2H5O2(90) <=> CO2(34) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 959,
    label = "C3H7(51) + CHO2(57) <=> CO2(34) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 960,
    label = "CHO2(57) + CH3O2(75) <=> CO2(34) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 961,
    label = "CHO2(57) + C3H7(95) <=> CO2(34) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 962,
    label = "CHO2(57) + S(2185) <=> CO2(34) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 963,
    label = "CHO2(57) + CHO3(74) <=> CO2(34) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 964,
    label = "O(20) + C3H5(1446) <=> S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 965,
    label = "O(20) + S(2128) <=> S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 966,
    label = "OH(23) + S(2128) <=> S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 967,
    label = "CH2O(32) + C2H3(41) <=> S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5452, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (5.987, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 968,
    label = "H(22) + C4H5(2849) <=> C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 969,
    label = "O(20) + C4H6(2483) <=> OH(23) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.204e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 970,
    label = "H(22) + C4H6(2483) <=> H2(21) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.73, 'cm^3/(mol*s)'), n=4.34, Ea=(6.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 971,
    label = "OH(23) + C4H6(2483) <=> H2O(46) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+06, 'cm^3/(mol*s)'), n=2, Ea=(1.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 972,
    label = "H2O2(25) + C4H5(2849) <=> HO2(24) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 973,
    label = "CH(26) + C4H6(2483) <=> CH2(28) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(200000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 974,
    label = "CH2(28) + C4H6(2483) <=> CH3(31) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.248e+08, 'cm^3/(mol*s)'),
        n = 1.524,
        Ea = (5.498, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 975,
    label = "CH2O(32) + C4H5(2849) <=> HCO(29) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 976,
    label = "CH3(31) + C4H6(2483) <=> CH4(33) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01728, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 977,
    label = "CH3OH(37) + C4H5(2849) <=> CH2OH(35) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005592, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 978,
    label = "CH3O(36) + C4H6(2483) <=> CH3OH(37) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.156e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 979,
    label = "C2H(38) + C4H6(2483) <=> C2H2(39) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56460, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.678, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 980,
    label = "HCCOH(48) + C4H5(2849) <=> HCCO(40) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 981,
    label = "HCCO(40) + C4H6(2483) <=> CH2CO(42) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.053, 'cm^3/(mol*s)'), n=4.34, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 982,
    label = "C2H3(41) + C4H6(2483) <=> C2H4(43) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01864, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 983,
    label = "C2H5(44) + C4H6(2483) <=> C2H6(45) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00296, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 984,
    label = "HO2(24) + C4H5(2849) <=> O2(2) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.48, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 985,
    label = "butR1(3) + C4H6(2483) <=> butane(1) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00296, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 986,
    label = "butane(1) + C4H5(2849) <=> butR2(4) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.016, 'cm^3/(mol*s)'), n=4.34, Ea=(9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 987,
    label = "S(149) + C4H5(2849) <=> butROO2(6) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 988,
    label = "C4H9O2(8) + C4H6(2483) <=> S(149) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00296, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 989,
    label = "CH3CHO(49) + C4H5(2849) <=> C2H3O(18) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005589, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 990,
    label = "C4H5(2849) + CCOO(1350) <=> C2H5O2(90) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 991,
    label = "C3H7(51) + C4H6(2483) <=> C3H8(50) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00296, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 992,
    label = "COO(1544) + C4H5(2849) <=> CH3O2(75) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 993,
    label = "C3H8(50) + C4H5(2849) <=> C3H7(95) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.008, 'cm^3/(mol*s)'), n=4.34, Ea=(9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 994,
    label = "C3H6(144) + C4H5(2849) <=> C3H5(1446) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00309, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 995,
    label = "S(2134) + C4H5(2849) <=> S(2185) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 996,
    label = "C4H8(143) + C4H5(2849) <=> C4H7(1663) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00618, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 997,
    label = "C4H7(1663) + C4H6(2483) <=> C4H8(96) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0354, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (22.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 998,
    label = "S(2644) + C4H5(2849) <=> CHO3(74) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 999,
    label = "CH2OH(35) + C4H5(2849) <=> CH2O(32) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1000,
    label = "CH3O(36) + C4H5(2849) <=> CH2O(32) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1001,
    label = "C2H3(41) + C4H5(2849) <=> C2H2(39) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1002,
    label = "C2H5(44) + C4H5(2849) <=> C2H4(43) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1003,
    label = "butR1(3) + C4H5(2849) <=> C4H8(96) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1004,
    label = "butR2(4) + C4H5(2849) <=> C4H8(143) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1005,
    label = "butR2(4) + C4H5(2849) <=> C4H8(96) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1006,
    label = "C2H3O(18) + C4H5(2849) <=> CH2CO(42) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1007,
    label = "C3H7(51) + C4H5(2849) <=> C3H6(144) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1008,
    label = "C3H7(95) + C4H5(2849) <=> C3H6(144) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.876e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1009,
    label = "C2H5O(71) + C4H5(2849) <=> CH3CHO(49) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1010,
    label = "C3H5(1446) + C4H5(2849) <=> C3H4(2124) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.037e+10, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1011,
    label = "C4H7(1663) + C4H5(2849) <=> C4H6(2483) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1012,
    label = "CHO2(57) + C4H5(2849) <=> CO2(34) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1013,
    label = "O2(2) + C4H5(2849) <=> S(4050)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1014,
    label = "H(22) + S(3752) <=> S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+06, 'cm^3/(mol*s)'),
        n = 2.16,
        Ea = (4.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1015,
    label = "O(20) + S(2128) <=> OH(23) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1016,
    label = "H(22) + S(2128) <=> H2(21) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1017,
    label = "OH(23) + S(2128) <=> H2O(46) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1018,
    label = "HO2(24) + S(2128) <=> H2O2(25) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1019,
    label = "CH(26) + S(2128) <=> CH2(28) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1020,
    label = "CH2(28) + S(2128) <=> CH3(31) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1021,
    label = "HCO(29) + S(2128) <=> CH2O(32) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1022,
    label = "CH3(31) + S(2128) <=> CH4(33) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1023,
    label = "CH2OH(35) + S(2128) <=> CH3OH(37) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1024,
    label = "CH3O(36) + S(2128) <=> CH3OH(37) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1025,
    label = "C2H(38) + S(2128) <=> C2H2(39) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.206e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1026,
    label = "HCCO(40) + S(2128) <=> HCCOH(48) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1027,
    label = "HCCO(40) + S(2128) <=> CH2CO(42) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1028,
    label = "C2H3(41) + S(2128) <=> C2H4(43) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1029,
    label = "C2H5(44) + S(2128) <=> C2H6(45) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1030,
    label = "O2(2) + S(2128) <=> HO2(24) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1031,
    label = "butR1(3) + S(2128) <=> butane(1) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1032,
    label = "butR2(4) + S(2128) <=> butane(1) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1033,
    label = "butROO2(6) + S(2128) <=> S(149) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1034,
    label = "C4H9O2(8) + S(2128) <=> S(149) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1035,
    label = "C2H3O(18) + S(2128) <=> CH3CHO(49) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1036,
    label = "C2H5O2(90) + S(2128) <=> S(3752) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1037,
    label = "C3H7(51) + S(2128) <=> C3H8(50) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1038,
    label = "CH3O2(75) + S(2128) <=> S(3752) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1039,
    label = "C3H7(95) + S(2128) <=> C3H8(50) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1040,
    label = "C3H5(1446) + S(2128) <=> C3H6(144) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1041,
    label = "S(2128) + S(2185) <=> S(3752) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1042,
    label = "C4H7(1663) + S(2128) <=> C4H8(143) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1043,
    label = "C4H7(1663) + S(2128) <=> C4H8(96) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1044,
    label = "CHO3(74) + S(2128) <=> S(3752) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1045,
    label = "S(2128) + C4H5(2849) <=> S(3752) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1046,
    label = "CO(27) + C2H4(43) <=> S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (236800, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1047,
    label = "HCO(29) + C2H3(41) <=> S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1048,
    label = "O2(2) + C4H5(2849) <=> S(4051)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1049,
    label = "O(20) + C4H5(2849) <=> S(3929)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1050,
    label = "O(20) + S(3929) <=> S(4050)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1051,
    label = "C2H3(41) + CH2CO(42) <=> S(3929)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46270, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.843, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1052,
    label = "S(2439) <=> S(3467)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1053,
    label = "S(4993) <=> S(3467)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(15.642, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1054,
    label = "S(4993) <=> CH2O(32) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1055,
    label = "O2(2) + S(3929) <=> S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1056,
    label = "C3H6(144) + OH(23) <=> S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.312e+08, 'cm^3/(mol*s)'),
        n = 1.015,
        Ea = (-1.75, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1057,
    label = "O2(2) + C2H3(41) <=> C2H3O2(86)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1058,
    label = "C2H3O(18) + O(20) <=> C2H3O2(86)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1059,
    label = "S(4886) <=> S(5413)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.004e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1060,
    label = "CH3O2(75) + S(3929) <=> S(4928)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1061,
    label = "CH3(31) + S(4886) <=> S(4928)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1062,
    label = "S(3929) <=> S(4743)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 's^-1'), n=0.19, Ea=(20, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1063,
    label = "O2(2) + HCCO(40) <=> C2HO3(84)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1064,
    label = "S(4321) + H(22) <=> S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1065,
    label = "O(20) + S(3752) <=> S(4321) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1.79, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1066,
    label = "H(22) + S(3752) <=> S(4321) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1067,
    label = "OH(23) + S(3752) <=> S(4321) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(-1.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1068,
    label = "HO2(24) + S(3752) <=> S(4321) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1069,
    label = "CH(26) + S(3752) <=> S(4321) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1070,
    label = "CH2(28) + S(3752) <=> S(4321) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1071,
    label = "HCO(29) + S(3752) <=> S(4321) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1072,
    label = "CH3(31) + S(3752) <=> S(4321) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e-06, 'cm^3/(mol*s)'),
        n = 5.64,
        Ea = (2.46, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1073,
    label = "CH2OH(35) + S(3752) <=> S(4321) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1074,
    label = "CH3O(36) + S(3752) <=> S(4321) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1075,
    label = "C2H(38) + S(3752) <=> S(4321) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.489, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1076,
    label = "S(4321) + HCCOH(48) <=> HCCO(40) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1077,
    label = "HCCO(40) + S(3752) <=> S(4321) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1078,
    label = "C2H3(41) + S(3752) <=> S(4321) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1079,
    label = "C2H5(44) + S(3752) <=> S(4321) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1080,
    label = "S(4321) + HO2(24) <=> O2(2) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.669, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1081,
    label = "butR1(3) + S(3752) <=> butane(1) + S(4321)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1082,
    label = "butR2(4) + S(3752) <=> butane(1) + S(4321)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1083,
    label = "butROO2(6) + S(3752) <=> S(4321) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1084,
    label = "C4H9O2(8) + S(3752) <=> S(4321) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1085,
    label = "C2H3O(18) + S(3752) <=> S(4321) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1086,
    label = "C2H5O2(90) + S(3752) <=> S(4321) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1087,
    label = "C3H7(51) + S(3752) <=> S(4321) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1088,
    label = "CH3O2(75) + S(3752) <=> S(4321) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1089,
    label = "C3H7(95) + S(3752) <=> S(4321) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1090,
    label = "C3H5(1446) + S(3752) <=> S(4321) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1091,
    label = "S(3752) + S(2185) <=> S(4321) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1092,
    label = "C4H7(1663) + S(3752) <=> S(4321) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1093,
    label = "C4H7(1663) + S(3752) <=> S(4321) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1094,
    label = "CHO3(74) + S(3752) <=> S(4321) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1095,
    label = "S(3752) + C4H5(2849) <=> S(4321) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1096,
    label = "S(4321) + CH2OH(35) <=> CH2O(32) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1097,
    label = "S(4321) + CH3O(36) <=> CH2O(32) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1098,
    label = "S(4321) + C2H3(41) <=> C2H2(39) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1099,
    label = "S(4321) + C2H5(44) <=> C2H4(43) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1100,
    label = "butR1(3) + S(4321) <=> C4H8(96) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1101,
    label = "butR2(4) + S(4321) <=> C4H8(143) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1102,
    label = "butR2(4) + S(4321) <=> C4H8(96) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1103,
    label = "C2H3O(18) + S(4321) <=> CH2CO(42) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1104,
    label = "S(4321) + C3H7(51) <=> C3H6(144) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1105,
    label = "S(4321) + C3H7(95) <=> C3H6(144) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.086e+15, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1106,
    label = "S(4321) + C2H5O(71) <=> CH3CHO(49) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1107,
    label = "S(4321) + C3H5(1446) <=> S(3752) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1108,
    label = "S(4321) + C4H7(1663) <=> S(3752) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1109,
    label = "S(4321) + CHO2(57) <=> CO2(34) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1110,
    label = "S(4321) + S(2128) <=> S(3752) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1111,
    label = "O(20) + S(3929) <=> S(4745)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1112,
    label = "O(20) + S(4745) <=> S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1113,
    label = "CH3O(36) + S(4745) <=> S(4928)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1114,
    label = "S(4321) + CH2O(32) <=> S(4745)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5452, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (5.987, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1115,
    label = "O2(2) + S(4321) <=> S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1116,
    label = "O2(2) + S(4321) <=> S(6829)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1117,
    label = "S(4321) + HO2(24) <=> S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1118,
    label = "H(22) + S(6731) <=> H2(21) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1119,
    label = "H(22) + S(6828) <=> S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1120,
    label = "O(20) + S(6731) <=> OH(23) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1121,
    label = "HO2(24) + S(6828) <=> O2(2) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1122,
    label = "H2O2(25) + S(6828) <=> HO2(24) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1123,
    label = "CH(26) + S(6731) <=> CH2(28) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1124,
    label = "CH2(28) + S(6731) <=> CH3(31) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1125,
    label = "CH2O(32) + S(6828) <=> HCO(29) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1126,
    label = "CH3(31) + S(6731) <=> CH4(33) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1127,
    label = "CH2OH(35) + S(6828) <=> CH2O(32) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1128,
    label = "CH3O(36) + S(6828) <=> CH2O(32) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1129,
    label = "CH3OH(37) + S(6828) <=> CH2OH(35) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (938900, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (9.917, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1130,
    label = "CH3O(36) + S(6731) <=> CH3OH(37) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1131,
    label = "C2H(38) + S(6731) <=> C2H2(39) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1132,
    label = "C2H3(41) + S(6828) <=> C2H2(39) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1133,
    label = "HCCO(40) + S(6731) <=> CH2CO(42) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1134,
    label = "C2H3(41) + S(6731) <=> C2H4(43) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1135,
    label = "C2H5(44) + S(6828) <=> C2H4(43) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1136,
    label = "C2H5(44) + S(6731) <=> C2H6(45) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1137,
    label = "OH(23) + S(6731) <=> H2O(46) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1138,
    label = "HCCOH(48) + S(6828) <=> HCCO(40) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1139,
    label = "C2H3O(18) + S(6731) <=> CH3CHO(49) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (0.746, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1140,
    label = "C3H8(50) + S(6828) <=> C3H7(95) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17.686, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1141,
    label = "C3H7(51) + S(6731) <=> C3H8(50) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1142,
    label = "butR2(4) + S(6731) <=> butane(1) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1143,
    label = "butR1(3) + S(6731) <=> butane(1) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1144,
    label = "butR1(3) + S(6828) <=> C4H8(96) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1145,
    label = "butR2(4) + S(6828) <=> C4H8(143) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1146,
    label = "butR2(4) + S(6828) <=> C4H8(96) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1147,
    label = "C2H3O(18) + S(6828) <=> CH2CO(42) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1148,
    label = "C3H7(51) + S(6828) <=> C3H6(144) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1149,
    label = "C4H9O2(8) + S(6731) <=> S(149) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1150,
    label = "S(149) + S(6828) <=> butROO2(6) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1151,
    label = "C3H6(144) + S(6828) <=> C3H5(1446) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001735, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1152,
    label = "C3H7(95) + S(6828) <=> C3H6(144) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1153,
    label = "C4H8(96) + S(6828) <=> C4H7(1663) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1154,
    label = "CCOO(1350) + S(6828) <=> C2H5O2(90) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1155,
    label = "C4H8(143) + S(6828) <=> C4H7(1663) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00347, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1156,
    label = "C2H5O(71) + S(6828) <=> CH3CHO(49) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1157,
    label = "COO(1544) + S(6828) <=> CH3O2(75) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1158,
    label = "C3H5(1446) + S(6828) <=> C3H4(2124) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1159,
    label = "C4H7(1663) + S(6828) <=> C4H6(2483) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1160,
    label = "C4H5(2849) + S(6731) <=> C4H6(2483) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1161,
    label = "S(2134) + S(6828) <=> S(2185) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1162,
    label = "CHO3(74) + S(6731) <=> S(2644) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1163,
    label = "CHO2(57) + S(6828) <=> CO2(34) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1164,
    label = "S(2128) + S(6828) <=> S(3752) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1165,
    label = "S(3752) + S(6828) <=> S(4321) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1166,
    label = "H(22) + C3H3(2385) <=> C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1167,
    label = "O(20) + C3H4(2124) <=> OH(23) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.908e+09, 'cm^3/(mol*s)'),
        n = 1.305,
        Ea = (5.685, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1168,
    label = "H(22) + C3H4(2124) <=> H2(21) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.52, 'cm^3/(mol*s)'), n=4.34, Ea=(3.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1169,
    label = "OH(23) + C3H4(2124) <=> H2O(46) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1170,
    label = "HO2(24) + C3H4(2124) <=> H2O2(25) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.312, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1171,
    label = "CH(26) + C3H4(2124) <=> CH2(28) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1172,
    label = "CH2(28) + C3H4(2124) <=> CH3(31) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.496e+08, 'cm^3/(mol*s)'),
        n = 1.524,
        Ea = (5.411, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1173,
    label = "HCO(29) + C3H4(2124) <=> CH2O(32) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (112900, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (10.037, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1174,
    label = "CH3(31) + C3H4(2124) <=> CH4(33) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.1548, 'cm^3/(mol*s)'), n=4.34, Ea=(5.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1175,
    label = "CH3O(36) + C3H3(2385) <=> CH2O(32) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1176,
    label = "CH2OH(35) + C3H3(2385) <=> CH2O(32) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1177,
    label = "CHO2(57) + C3H3(2385) <=> CO2(34) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1178,
    label = "CH2OH(35) + C3H4(2124) <=> CH3OH(37) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06082, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.183, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1179,
    label = "CH3O(36) + C3H4(2124) <=> CH3OH(37) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (2.378, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1180,
    label = "C2H(38) + C3H4(2124) <=> C2H2(39) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (112900, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.533, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1181,
    label = "C2H3(41) + C3H3(2385) <=> C2H2(39) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1182,
    label = "HCCOH(48) + C3H3(2385) <=> HCCO(40) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1183,
    label = "HCCO(40) + C3H4(2124) <=> CH2CO(42) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1232, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1184,
    label = "C2H3(41) + C3H4(2124) <=> C2H4(43) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.1668, 'cm^3/(mol*s)'), n=4.34, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1185,
    label = "C2H3O(18) + C3H3(2385) <=> CH2CO(42) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1186,
    label = "C2H5(44) + C3H3(2385) <=> C2H4(43) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1187,
    label = "C2H5(44) + C3H4(2124) <=> C2H6(45) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0218, 'cm^3/(mol*s)'), n=4.34, Ea=(5.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1188,
    label = "C2H5O(71) + C3H3(2385) <=> CH3CHO(49) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1189,
    label = "HO2(24) + C3H3(2385) <=> O2(2) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.624, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1190,
    label = "butR1(3) + C3H4(2124) <=> butane(1) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0218, 'cm^3/(mol*s)'), n=4.34, Ea=(5.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1191,
    label = "butR2(4) + C3H4(2124) <=> butane(1) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02524, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (5.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1192,
    label = "butROO2(6) + C3H4(2124) <=> S(149) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.125, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1193,
    label = "C4H9O2(8) + C3H4(2124) <=> S(149) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0218, 'cm^3/(mol*s)'), n=4.34, Ea=(5.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1194,
    label = "C2H3O(18) + C3H4(2124) <=> CH3CHO(49) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06082, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.183, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1195,
    label = "C2H5O2(90) + C3H4(2124) <=> C3H3(2385) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.126, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1196,
    label = "C3H7(51) + C3H4(2124) <=> C3H8(50) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0218, 'cm^3/(mol*s)'), n=4.34, Ea=(5.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1197,
    label = "C3H7(51) + C3H3(2385) <=> C3H6(144) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1198,
    label = "C3H7(95) + C3H3(2385) <=> C3H6(144) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.12e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1199,
    label = "CH3O2(75) + C3H4(2124) <=> C3H3(2385) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.125, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1200,
    label = "C3H7(95) + C3H4(2124) <=> C3H8(50) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02524, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (5.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1201,
    label = "butR1(3) + C3H3(2385) <=> C4H8(96) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1202,
    label = "butR2(4) + C3H3(2385) <=> C4H8(96) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1203,
    label = "butR2(4) + C3H3(2385) <=> C4H8(143) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1204,
    label = "C3H5(1446) + C3H4(2124) <=> C3H6(144) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1088, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1205,
    label = "C3H4(2124) + S(2185) <=> C3H3(2385) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.125, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1206,
    label = "C3H3(2385) + C3H5(1446) <=> C3H4(2124) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1207,
    label = "C4H7(1663) + C3H4(2124) <=> C4H8(143) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1088, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1208,
    label = "C4H7(1663) + C3H4(2124) <=> C3H3(2385) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0676, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (15.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1209,
    label = "CHO3(74) + C3H4(2124) <=> C3H3(2385) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (4.086, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1210,
    label = "C4H7(1663) + C3H3(2385) <=> C3H4(2124) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1211,
    label = "C3H4(2124) + C4H5(2849) <=> C3H3(2385) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0772, 'cm^3/(mol*s)'), n=4.34, Ea=(8.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1212,
    label = "C3H3(2385) + S(2128) <=> S(3752) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1213,
    label = "C3H3(2385) + S(3752) <=> S(4321) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1214,
    label = "C3H4(2124) + S(6828) <=> C3H3(2385) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (4.086, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1215,
    label = "C3H6(144) + OH(23) <=> S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (-2.45, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1216,
    label = "C2H3O2(86) + CH3OH(37) <=> S(5703)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.16e-05, 'cm^3/(mol*s)'),
        n = 3.97,
        Ea = (78.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1217,
    label = "O2(2) + S(1450) <=> S(5703)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1218,
    label = "O2(2) + C3H3(2385) <=> S(8233)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1219,
    label = "O2(2) + C3H3(2385) <=> S(8234)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1220,
    label = "S(4321) + O(20) <=> S(6716)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1221,
    label = "O(20) + S(6716) <=> S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1222,
    label = "OH(23) + S(6716) <=> S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1223,
    label = "CO2(34) + C2H3(41) <=> S(6716)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (5.987, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1224,
    label = "S(4319) + H(22) <=> S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1225,
    label = "O(20) + S(3752) <=> S(4319) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1226,
    label = "H(22) + S(3752) <=> S(4319) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.3776, 'cm^3/(mol*s)'), n=4.34, Ea=(5.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1227,
    label = "OH(23) + S(3752) <=> S(4319) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(1.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1228,
    label = "S(4319) + H2O2(25) <=> HO2(24) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1229,
    label = "CH(26) + S(3752) <=> S(4319) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1230,
    label = "CH2(28) + S(3752) <=> S(4319) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.24e+07, 'cm^3/(mol*s)'),
        n = 1.524,
        Ea = (5.498, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1231,
    label = "S(4319) + CH2O(32) <=> HCO(29) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1232,
    label = "CH3(31) + S(3752) <=> S(4319) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008928, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1233,
    label = "S(4319) + CH3OH(37) <=> CH2OH(35) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005592, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1234,
    label = "CH3O(36) + S(3752) <=> S(4319) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1235,
    label = "C2H(38) + S(3752) <=> S(4319) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.678, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1236,
    label = "S(4319) + HCCOH(48) <=> HCCO(40) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1237,
    label = "HCCO(40) + S(3752) <=> S(4319) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.02741, 'cm^3/(mol*s)'), n=4.34, Ea=(18, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1238,
    label = "C2H3(41) + S(3752) <=> S(4319) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01302, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.405, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1239,
    label = "S(4319) + C2H6(45) <=> C2H5(44) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1240,
    label = "S(4319) + HO2(24) <=> O2(2) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.48, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1241,
    label = "butR1(3) + S(3752) <=> butane(1) + S(4319)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1242,
    label = "butane(1) + S(4319) <=> butR2(4) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00904, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (8.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1243,
    label = "S(4319) + S(149) <=> butROO2(6) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1244,
    label = "C4H9O2(8) + S(3752) <=> S(4319) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1245,
    label = "S(4319) + CH3CHO(49) <=> C2H3O(18) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005589, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1246,
    label = "S(4319) + CCOO(1350) <=> C2H5O2(90) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1247,
    label = "S(4319) + C3H8(50) <=> C3H7(51) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1248,
    label = "S(4319) + COO(1544) <=> CH3O2(75) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1249,
    label = "S(4319) + C3H8(50) <=> C3H7(95) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00452, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (8.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1250,
    label = "S(4319) + C3H6(144) <=> C3H5(1446) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005589, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1251,
    label = "S(4319) + S(2134) <=> S(3752) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1252,
    label = "S(4319) + C4H8(143) <=> C4H7(1663) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1253,
    label = "S(4319) + C4H8(96) <=> C4H7(1663) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.006127, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.867, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1254,
    label = "S(4319) + S(2644) <=> CHO3(74) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1255,
    label = "S(4319) + C4H6(2483) <=> S(3752) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01127, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (12.567, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1256,
    label = "S(4319) <=> S(4321)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.668e+06, 's^-1'), n=1.614, Ea=(29.669, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1257,
    label = "S(4319) + S(3752) <=> S(4321) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1258,
    label = "S(4319) + S(6731) <=> S(3752) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1259,
    label = "O(20) + C3H3(2385) <=> S(4319)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1260,
    label = "S(4319) + C3H4(2124) <=> C3H3(2385) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.09769, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (10.367, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1261,
    label = "S(4319) + O(20) <=> S(8234)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1262,
    label = "S(4319) + CH2OH(35) <=> CH2O(32) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1263,
    label = "S(4319) + CH3O(36) <=> CH2O(32) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1264,
    label = "S(4319) + C2H3(41) <=> C2H2(39) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1265,
    label = "S(4319) + C2H5(44) <=> C2H4(43) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1266,
    label = "butR1(3) + S(4319) <=> C4H8(96) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1267,
    label = "butR2(4) + S(4319) <=> C4H8(143) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1268,
    label = "butR2(4) + S(4319) <=> C4H8(96) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1269,
    label = "C2H3O(18) + S(4319) <=> CH2CO(42) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1270,
    label = "S(4319) + C3H7(51) <=> C3H6(144) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1271,
    label = "S(4319) + C3H7(95) <=> C3H6(144) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.876e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1272,
    label = "S(4319) + C2H5O(71) <=> CH3CHO(49) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1273,
    label = "S(4319) + C3H5(1446) <=> S(3752) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.037e+10, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1274,
    label = "S(4319) + C4H7(1663) <=> S(3752) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1275,
    label = "S(4319) + CHO2(57) <=> CO2(34) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1276,
    label = "S(4319) + S(2128) <=> S(3752) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1277,
    label = "O(20) + C4H8(96) <=> S(1667)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+08, 'cm^3/(mol*s)'),
        n = 1.58,
        Ea = (-2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1278,
    label = "CH3(31) + S(2128) <=> S(1667)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(21000, 'cm^3/(mol*s)'), n=2.41, Ea=(5.32, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1279,
    label = "S(1667) <=> S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1280,
    label = "C2H3O2(86) + CO(27) <=> S(5687)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (59200, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1281,
    label = "O2(2) + S(4319) <=> S(5687)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1282,
    label = "C2H3O2(86) <=> S(5678)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.004e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1283,
    label = "S(10031) <=> S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1284,
    label = "H(22) + S(9511) <=> S(4319)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.555e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1285,
    label = "S(4319) + O(20) <=> OH(23) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1286,
    label = "S(4319) + H(22) <=> H2(21) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.358e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1287,
    label = "S(4319) + OH(23) <=> H2O(46) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1288,
    label = "S(4319) + HO2(24) <=> H2O2(25) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1289,
    label = "S(4319) + CH(26) <=> CH2(28) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1290,
    label = "S(4319) + CH2(28) <=> CH3(31) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.498e+10, 'cm^3/(mol*s)'),
        n = 0.917,
        Ea = (-0.454, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1291,
    label = "S(4319) + HCO(29) <=> CH2O(32) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1292,
    label = "S(4319) + CH3(31) <=> CH4(33) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1293,
    label = "S(4319) + CH2OH(35) <=> CH3OH(37) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1294,
    label = "S(4319) + CH3O(36) <=> CH3OH(37) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1295,
    label = "S(4319) + C2H(38) <=> C2H2(39) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1296,
    label = "S(4319) + HCCO(40) <=> HCCOH(48) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1297,
    label = "S(4319) + HCCO(40) <=> CH2CO(42) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1298,
    label = "S(4319) + C2H3(41) <=> C2H4(43) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1299,
    label = "S(4319) + C2H5(44) <=> C2H6(45) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1300,
    label = "O2(2) + S(4319) <=> HO2(24) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1301,
    label = "butR1(3) + S(4319) <=> butane(1) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1302,
    label = "butR2(4) + S(4319) <=> butane(1) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1303,
    label = "butROO2(6) + S(4319) <=> S(149) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1304,
    label = "C4H9O2(8) + S(4319) <=> S(149) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1305,
    label = "C2H3O(18) + S(4319) <=> CH3CHO(49) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1306,
    label = "S(4319) + C2H5O2(90) <=> CCOO(1350) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1307,
    label = "S(4319) + C3H7(51) <=> C3H8(50) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1308,
    label = "S(4319) + CH3O2(75) <=> COO(1544) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1309,
    label = "S(4319) + C3H7(95) <=> C3H8(50) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1310,
    label = "S(4319) + C3H5(1446) <=> C3H6(144) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1311,
    label = "S(4319) + S(2185) <=> S(2134) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1312,
    label = "S(4319) + C4H7(1663) <=> C4H8(143) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1313,
    label = "S(4319) + C4H7(1663) <=> C4H8(96) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1314,
    label = "S(4319) + CHO3(74) <=> S(2644) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1315,
    label = "S(4319) + C4H5(2849) <=> C4H6(2483) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1316,
    label = "S(4319) + S(4321) <=> S(3752) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1317,
    label = "S(4319) + S(6828) <=> S(6731) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1318,
    label = "S(4319) + C3H3(2385) <=> C3H4(2124) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1319,
    label = "S(4319) + S(4319) <=> S(3752) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1320,
    label = "CO(27) + C2H2(39) <=> S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (118400, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1321,
    label = "HCO(29) + C2H(38) <=> S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1322,
    label = "HO2(24) + S(3929) <=> S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1323,
    label = "H(22) + S(4759) <=> H2(21) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1324,
    label = "H(22) + S(4886) <=> S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1325,
    label = "O(20) + S(4759) <=> OH(23) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1326,
    label = "HO2(24) + S(4886) <=> O2(2) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1327,
    label = "H2O2(25) + S(4886) <=> HO2(24) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1328,
    label = "CH(26) + S(4759) <=> CH2(28) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1329,
    label = "CH2(28) + S(4759) <=> CH3(31) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1330,
    label = "CH2O(32) + S(4886) <=> HCO(29) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1331,
    label = "CH3(31) + S(4759) <=> CH4(33) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1332,
    label = "CH2OH(35) + S(4886) <=> CH2O(32) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1333,
    label = "CH3O(36) + S(4886) <=> CH2O(32) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1334,
    label = "CH2OH(35) + S(4759) <=> CH3OH(37) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1335,
    label = "CH3O(36) + S(4759) <=> CH3OH(37) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1336,
    label = "C2H(38) + S(4759) <=> C2H2(39) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1337,
    label = "C2H3(41) + S(4886) <=> C2H2(39) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1338,
    label = "HCCO(40) + S(4759) <=> CH2CO(42) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1339,
    label = "C2H3(41) + S(4759) <=> C2H4(43) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1340,
    label = "C2H5(44) + S(4886) <=> C2H4(43) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1341,
    label = "C2H5(44) + S(4759) <=> C2H6(45) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1342,
    label = "OH(23) + S(4759) <=> H2O(46) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1343,
    label = "HCCOH(48) + S(4886) <=> HCCO(40) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1344,
    label = "C2H3O(18) + S(4759) <=> CH3CHO(49) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1345,
    label = "C3H7(95) + S(4759) <=> C3H8(50) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1346,
    label = "C3H7(51) + S(4759) <=> C3H8(50) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1347,
    label = "butR2(4) + S(4759) <=> butane(1) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1348,
    label = "butR1(3) + S(4759) <=> butane(1) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1349,
    label = "butR1(3) + S(4886) <=> C4H8(96) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1350,
    label = "butR2(4) + S(4886) <=> C4H8(143) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1351,
    label = "butR2(4) + S(4886) <=> C4H8(96) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1352,
    label = "C2H3O(18) + S(4886) <=> CH2CO(42) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1353,
    label = "C3H7(51) + S(4886) <=> C3H6(144) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1354,
    label = "C4H9O2(8) + S(4759) <=> S(149) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1355,
    label = "butROO2(6) + S(4759) <=> S(149) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1356,
    label = "C3H5(1446) + S(4759) <=> C3H6(144) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1357,
    label = "C3H7(95) + S(4886) <=> C3H6(144) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1358,
    label = "C4H8(96) + S(4886) <=> C4H7(1663) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1359,
    label = "CCOO(1350) + S(4886) <=> C2H5O2(90) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1360,
    label = "C4H7(1663) + S(4759) <=> C4H8(143) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1361,
    label = "C2H5O(71) + S(4886) <=> CH3CHO(49) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1362,
    label = "CH3O2(75) + S(4759) <=> COO(1544) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1363,
    label = "C3H5(1446) + S(4886) <=> C3H4(2124) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1364,
    label = "C3H4(2124) + S(4886) <=> C3H3(2385) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.126, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1365,
    label = "C4H7(1663) + S(4886) <=> C4H6(2483) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1366,
    label = "C4H5(2849) + S(4759) <=> C4H6(2483) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1367,
    label = "S(2185) + S(4759) <=> S(2134) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1368,
    label = "CHO3(74) + S(4759) <=> S(2644) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1369,
    label = "CHO2(57) + S(4886) <=> CO2(34) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1370,
    label = "S(2128) + S(4886) <=> S(3752) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1371,
    label = "S(4319) + S(4759) <=> S(3752) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1372,
    label = "S(3752) + S(4886) <=> S(4321) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1373,
    label = "CH2(S)(30) + S(4759) <=> S(4928)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.352e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1374,
    label = "OH(23) + S(4745) <=> S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.205e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1375,
    label = "S(4759) + S(6828) <=> S(4886) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1376,
    label = "S(4319) + S(4886) <=> S(4759) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1377,
    label = "C2H3O(18) + C2H5(44) <=> S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1378,
    label = "H(22) + S(1125) <=> C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1379,
    label = "C4H9O(147) + O(20) <=> OH(23) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2850, 'cm^3/(mol*s)'), n=3.05, Ea=(3.123, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1380,
    label = "C4H9O(147) + H(22) <=> H2(21) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3090, 'cm^3/(mol*s)'), n=3.24, Ea=(7.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1381,
    label = "C4H9O(147) + OH(23) <=> H2O(46) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.431e+09, 'cm^3/(mol*s)'),
        n = 1.152,
        Ea = (2.68, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1382,
    label = "C4H9O(147) + HO2(24) <=> H2O2(25) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20.435, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1383,
    label = "C4H9O(147) + CH(26) <=> CH2(28) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(300000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1384,
    label = "C4H9O(147) + CH2(28) <=> CH3(31) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.721e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1385,
    label = "CH2O(32) + S(1125) <=> C4H9O(147) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1386,
    label = "C4H9O(147) + CH3(31) <=> CH4(33) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.244e-05, 'cm^3/(mol*s)'),
        n = 4.99,
        Ea = (8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1387,
    label = "CH3O(36) + S(1125) <=> C4H9O(147) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1388,
    label = "CH2OH(35) + S(1125) <=> C4H9O(147) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1389,
    label = "CHO2(57) + S(1125) <=> C4H9O(147) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1390,
    label = "CH3OH(37) + S(1125) <=> C4H9O(147) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1391,
    label = "CH3OH(37) + S(1125) <=> C4H9O(147) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1392,
    label = "C4H9O(147) + C2H(38) <=> C2H2(39) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.806e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1393,
    label = "C2H3(41) + S(1125) <=> C4H9O(147) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1394,
    label = "HCCOH(48) + S(1125) <=> C4H9O(147) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1395,
    label = "C4H9O(147) + HCCO(40) <=> CH2CO(42) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0495, 'cm^3/(mol*s)'), n=4.34, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1396,
    label = "C4H9O(147) + C2H3(41) <=> C2H4(43) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00054, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1397,
    label = "C2H3O(18) + S(1125) <=> C4H9O(147) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1398,
    label = "C2H5(44) + S(1125) <=> C4H9O(147) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1399,
    label = "C2H6(45) + S(1125) <=> C4H9O(147) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00552, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1400,
    label = "C2H5O(71) + S(1125) <=> C4H9O(147) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1401,
    label = "O2(2) + C4H9O(147) <=> HO2(24) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (51.997, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1402,
    label = "butR1(3) + C4H9O(147) <=> butane(1) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00276, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1403,
    label = "butane(1) + S(1125) <=> butR2(4) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00368, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1404,
    label = "S(149) + S(1125) <=> butROO2(6) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1405,
    label = "S(149) + S(1125) <=> C4H9O2(8) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00276, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1406,
    label = "CH3CHO(49) + S(1125) <=> C2H3O(18) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.037e-05, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1407,
    label = "S(1125) + CCOO(1350) <=> C2H5O2(90) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1408,
    label = "C3H7(51) + C4H9O(147) <=> C3H8(50) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00276, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1409,
    label = "C3H7(51) + S(1125) <=> C3H6(144) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1410,
    label = "C3H7(95) + S(1125) <=> C3H6(144) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1411,
    label = "COO(1544) + S(1125) <=> CH3O2(75) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1412,
    label = "C3H8(50) + S(1125) <=> C3H7(95) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00184, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1413,
    label = "O(20) + C4H8(96) <=> S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.17e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (-1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1414,
    label = "butR1(3) + S(1125) <=> C4H9O(147) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1415,
    label = "butR2(4) + S(1125) <=> C4H9O(147) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1416,
    label = "butR2(4) + S(1125) <=> C4H8(143) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1417,
    label = "C3H6(144) + S(1125) <=> C4H9O(147) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00087, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1418,
    label = "S(2134) + S(1125) <=> C4H9O(147) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1419,
    label = "C3H5(1446) + S(1125) <=> C4H9O(147) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1420,
    label = "C4H8(143) + S(1125) <=> C4H7(1663) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00174, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1421,
    label = "C4H7(1663) + C4H9O(147) <=> C4H8(96) + S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.027, 'cm^3/(mol*s)'), n=4.34, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1422,
    label = "S(2644) + S(1125) <=> CHO3(74) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1423,
    label = "C4H7(1663) + S(1125) <=> C4H9O(147) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1424,
    label = "S(1125) + C4H6(2483) <=> C4H9O(147) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00296, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1425,
    label = "S(2128) + S(1125) <=> C4H9O(147) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1426,
    label = "S(1125) + S(4759) <=> C4H9O(147) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1427,
    label = "S(3752) + S(1125) <=> S(4321) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1428,
    label = "S(1125) + S(6731) <=> C4H9O(147) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1429,
    label = "C3H4(2124) + S(1125) <=> C4H9O(147) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0218, 'cm^3/(mol*s)'), n=4.34, Ea=(5.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1430,
    label = "S(3752) + S(1125) <=> S(4319) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1431,
    label = "S(1125) <=> S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1432,
    label = "S(4319) + S(1125) <=> C4H9O(147) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1433,
    label = "S(10058) <=> S(5687)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.668e+06, 's^-1'), n=1.614, Ea=(29.669, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1434,
    label = "HO2(24) + S(9511) <=> S(10058)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.459e+19, 'cm^3/(mol*s)'),
        n = -2.335,
        Ea = (3.17, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1435,
    label = "CH3O2(75) + S(9511) <=> S(10862)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.459e+19, 'cm^3/(mol*s)'),
        n = -2.335,
        Ea = (3.17, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1436,
    label = "CH2(S)(30) + S(10058) <=> S(10862)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.352e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1437,
    label = "H(22) + S(6711) <=> S(4321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.573e+12, 'cm^3/(mol*s)'),
        n = 0.298,
        Ea = (6.012, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1438,
    label = "S(4321) + O(20) <=> OH(23) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.837e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1439,
    label = "S(4321) + H(22) <=> H2(21) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.314e+11, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (0.023, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1440,
    label = "S(4321) + OH(23) <=> H2O(46) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1441,
    label = "S(4321) + HO2(24) <=> H2O2(25) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1442,
    label = "S(4321) + CH(26) <=> CH2(28) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.046e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1443,
    label = "S(4321) + CH2(28) <=> CH3(31) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.04e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1444,
    label = "S(4321) + HCO(29) <=> CH2O(32) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1445,
    label = "S(4321) + CH3(31) <=> CH4(33) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1446,
    label = "S(4321) + CH2OH(35) <=> CH3OH(37) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1447,
    label = "S(4321) + CH3O(36) <=> CH3OH(37) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1448,
    label = "S(4321) + C2H(38) <=> C2H2(39) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.297e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1449,
    label = "S(4321) + HCCO(40) <=> HCCOH(48) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (6.825, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1450,
    label = "S(4321) + HCCO(40) <=> CH2CO(42) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1451,
    label = "S(4321) + C2H3(41) <=> C2H4(43) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1452,
    label = "S(4321) + C2H5(44) <=> C2H6(45) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1453,
    label = "O2(2) + S(4321) <=> HO2(24) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (33.761, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1454,
    label = "butR1(3) + S(4321) <=> butane(1) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1455,
    label = "butR2(4) + S(4321) <=> butane(1) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1456,
    label = "butROO2(6) + S(4321) <=> S(149) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1457,
    label = "C4H9O2(8) + S(4321) <=> S(149) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1458,
    label = "C2H3O(18) + S(4321) <=> CH3CHO(49) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1459,
    label = "S(4321) + C2H5O2(90) <=> CCOO(1350) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1460,
    label = "S(4321) + C3H7(51) <=> C3H8(50) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1461,
    label = "S(4321) + CH3O2(75) <=> COO(1544) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1462,
    label = "S(4321) + C3H7(95) <=> C3H8(50) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1463,
    label = "S(4321) + C3H5(1446) <=> C3H6(144) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1464,
    label = "S(4321) + S(2185) <=> S(2134) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1465,
    label = "S(4321) + C4H7(1663) <=> C4H8(143) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1466,
    label = "S(4321) + C4H7(1663) <=> C4H8(96) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1467,
    label = "S(4321) + CHO3(74) <=> S(2644) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1468,
    label = "S(4321) + C4H5(2849) <=> C4H6(2483) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1469,
    label = "S(4321) + S(4886) <=> S(4759) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1470,
    label = "S(4321) + S(4321) <=> S(3752) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.214, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1471,
    label = "S(6828) <=> HO2(24) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.63e+09, 's^-1'), n=1.11, Ea=(58.272, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1472,
    label = "S(4321) + S(6828) <=> S(6731) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1473,
    label = "S(6829) <=> HO2(24) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.63e+09, 's^-1'), n=1.11, Ea=(42.841, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1474,
    label = "S(4321) + C3H3(2385) <=> C3H4(2124) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1475,
    label = "H(22) + S(6711) <=> S(4319)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.573e+12, 'cm^3/(mol*s)'),
        n = 0.298,
        Ea = (6.012, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1476,
    label = "S(4319) + O(20) <=> OH(23) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.837e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1477,
    label = "S(4319) + H(22) <=> H2(21) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.314e+11, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (0.023, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1478,
    label = "S(4319) + OH(23) <=> H2O(46) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1479,
    label = "S(4319) + HO2(24) <=> H2O2(25) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1480,
    label = "S(4319) + CH(26) <=> CH2(28) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.046e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1481,
    label = "S(4319) + CH2(28) <=> CH3(31) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.04e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1482,
    label = "S(4319) + HCO(29) <=> CH2O(32) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1483,
    label = "S(4319) + CH3(31) <=> CH4(33) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1484,
    label = "S(4319) + CH2OH(35) <=> CH3OH(37) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1485,
    label = "S(4319) + CH3O(36) <=> CH3OH(37) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1486,
    label = "S(4319) + C2H(38) <=> C2H2(39) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.297e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1487,
    label = "S(4319) + HCCO(40) <=> HCCOH(48) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1488,
    label = "S(4319) + HCCO(40) <=> CH2CO(42) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1489,
    label = "S(4319) + C2H3(41) <=> C2H4(43) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1490,
    label = "S(4319) + C2H5(44) <=> C2H6(45) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1491,
    label = "O2(2) + S(4319) <=> HO2(24) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17.046, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1492,
    label = "butR1(3) + S(4319) <=> butane(1) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1493,
    label = "butR2(4) + S(4319) <=> butane(1) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1494,
    label = "butROO2(6) + S(4319) <=> S(149) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1495,
    label = "C4H9O2(8) + S(4319) <=> S(149) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1496,
    label = "C2H3O(18) + S(4319) <=> CH3CHO(49) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1497,
    label = "S(4319) + C2H5O2(90) <=> CCOO(1350) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1498,
    label = "S(4319) + C3H7(51) <=> C3H8(50) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1499,
    label = "S(4319) + CH3O2(75) <=> COO(1544) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1500,
    label = "S(4319) + C3H7(95) <=> C3H8(50) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1501,
    label = "S(4319) + C3H5(1446) <=> C3H6(144) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1502,
    label = "S(4319) + S(2185) <=> S(2134) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1503,
    label = "S(4319) + C4H7(1663) <=> C4H8(143) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1504,
    label = "S(4319) + C4H7(1663) <=> C4H8(96) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1505,
    label = "S(4319) + CHO3(74) <=> S(2644) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1506,
    label = "S(4319) + C4H5(2849) <=> C4H6(2483) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1507,
    label = "S(4319) + S(4886) <=> S(4759) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1508,
    label = "S(4319) + S(4321) <=> S(3752) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1509,
    label = "S(4319) + S(6828) <=> S(6731) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1510,
    label = "S(4319) + C3H3(2385) <=> C3H4(2124) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1511,
    label = "S(4319) + S(4319) <=> S(3752) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1512,
    label = "S(5687) <=> HO2(24) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.203e+10, 's^-1'), n=0.622, Ea=(41.532, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1513,
    label = "S(4321) + S(1125) <=> C4H9O(147) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1514,
    label = "S(4319) + S(1125) <=> C4H9O(147) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1515,
    label = "butR2(4) + C2H3O(68) <=> butane(1) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1516,
    label = "butR1(3) + C2H3O(68) <=> butane(1) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1517,
    label = "C2H3O(68) + HO2(24) <=> O2(2) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.595, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1518,
    label = "butR1(3) + CH3CHO(49) <=> butane(1) + C2H3O(68)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1519,
    label = "butR2(4) + CH3CHO(49) <=> butane(1) + C2H3O(68)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1520,
    label = "C2H3O(68) + S(149) <=> butROO2(6) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0009569, 'cm^3/(mol*s)'),
        n = 4.45,
        Ea = (0.54, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1521,
    label = "C4H9O2(8) + CH3CHO(49) <=> C2H3O(68) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1522,
    label = "C2H3O(18) <=> C2H3O(68)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.668e+06, 's^-1'), n=1.614, Ea=(29.669, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1523,
    label = "C2H3O(18) + CH3CHO(49) <=> C2H3O(68) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1524,
    label = "C2H3O(68) + CCOO(1350) <=> C2H5O2(90) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0009569, 'cm^3/(mol*s)'),
        n = 4.45,
        Ea = (0.54, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1525,
    label = "C3H7(51) + CH3CHO(49) <=> C2H3O(68) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1526,
    label = "C4H9O2(8) + C2H3O(68) <=> S(149) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1527,
    label = "C2H3O(68) + C3H5(1446) <=> C3H6(144) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1528,
    label = "C2H3O(68) + COO(1544) <=> CH3O2(75) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1529,
    label = "C2H3O(68) + S(1125) <=> C4H9O(147) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1530,
    label = "C3H7(95) + CH3CHO(49) <=> C2H3O(68) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1531,
    label = "C2H3O(68) + C4H7(1663) <=> CH2CO(42) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1532,
    label = "C2H3O(68) + C4H7(1663) <=> C4H8(143) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1533,
    label = "C2H3O(68) + C3H6(144) <=> CH3CHO(49) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9060, 'cm^3/(mol*s)'), n=2.75, Ea=(17.53, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1534,
    label = "C2H3O(68) + S(2134) <=> CH3CHO(49) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1535,
    label = "C2H3O(68) + C3H3(2385) <=> CH2CO(42) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1536,
    label = "C2H3O(68) + C4H8(143) <=> C4H7(1663) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18120, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (17.53, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1537,
    label = "C2H3O(68) + C4H8(96) <=> C4H7(1663) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(16.24, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1538,
    label = "CHO3(74) + CH3CHO(49) <=> C2H3O(68) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1539,
    label = "CH3CHO(49) + C4H5(2849) <=> C2H3O(68) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1540,
    label = "C2H3O(68) + S(4759) <=> CH3CHO(49) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1541,
    label = "C2H3O(68) + S(3752) <=> S(4321) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1542,
    label = "CH3CHO(49) + S(6828) <=> C2H3O(68) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1543,
    label = "C2H3O(68) + C3H4(2124) <=> CH3CHO(49) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (112900, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (10.021, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1544,
    label = "S(4319) + CH3CHO(49) <=> C2H3O(68) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1545,
    label = "CH3CHO(49) + S(1125) <=> C2H3O(68) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1546,
    label = "H(22) + CH2CO(42) <=> C2H3O(68)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.067e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.969, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1547,
    label = "C2H3O(68) + O(20) <=> OH(23) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1548,
    label = "H(22) + CH3CHO(49) <=> C2H3O(68) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1549,
    label = "C2H3O(68) + H(22) <=> H2(21) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.166e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-0.297, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1550,
    label = "C2H3O(68) + H(22) <=> CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1551,
    label = "C2H3O(68) + OH(23) <=> CH2CO(42) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.794e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1552,
    label = "O(20) + CH3CHO(49) <=> C2H3O(68) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1.79, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1553,
    label = "C2H3O(68) + HO2(24) <=> H2O2(25) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1554,
    label = "C2H3O(68) + H2O2(25) <=> HO2(24) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.36e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1555,
    label = "C2H3O(68) + CH(26) <=> CH2(28) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.137e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1556,
    label = "C2H3O(68) + CH2(28) <=> CH3(31) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1557,
    label = "CH(26) + CH3CHO(49) <=> C2H3O(68) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1558,
    label = "C2H3O(68) + HCO(29) <=> CH2O(32) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1559,
    label = "C2H3O(68) + CH3(31) <=> CH4(33) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.878e+10, 'cm^3/(mol*s)'),
        n = 0.595,
        Ea = (-0.555, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1560,
    label = "CH2(28) + CH3CHO(49) <=> C2H3O(68) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1561,
    label = "C2H3O(68) + CH2O(32) <=> HCO(29) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1562,
    label = "CH3(31) + CH3CHO(49) <=> C2H3O(68) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e-06, 'cm^3/(mol*s)'),
        n = 5.64,
        Ea = (2.46, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1563,
    label = "C2H3O(68) + CH2OH(35) <=> CH2O(32) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1564,
    label = "C2H3O(68) + CH2OH(35) <=> CH3OH(37) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1565,
    label = "C2H3O(68) + CH3O(36) <=> CH2O(32) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1566,
    label = "C2H3O(68) + CH3O(36) <=> CH3OH(37) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1567,
    label = "CH2OH(35) + CH3CHO(49) <=> C2H3O(68) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1568,
    label = "CH3O(36) + CH3CHO(49) <=> C2H3O(68) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1569,
    label = "C2H3O(68) + C2H(38) <=> C2H2(39) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.083e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1570,
    label = "C2H(38) + CH3CHO(49) <=> C2H3O(68) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.562, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1571,
    label = "C2H3O(68) + HCCO(40) <=> CH2CO(42) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1572,
    label = "C2H3O(68) + HCCO(40) <=> CH2CO(42) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1573,
    label = "C2H3O(68) + C2H3(41) <=> C2H2(39) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1574,
    label = "C2H3O(68) + C2H3(41) <=> CH2CO(42) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1575,
    label = "HCCO(40) + CH3CHO(49) <=> C2H3O(68) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1576,
    label = "C2H3(41) + CH3CHO(49) <=> C2H3O(68) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.13e+10, 'cm^3/(mol*s)'), n=0, Ea=(3.68, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1577,
    label = "C2H3O(68) + C2H5(44) <=> C2H4(43) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1578,
    label = "C2H3O(68) + C2H5(44) <=> CH2CO(42) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1579,
    label = "C2H5(44) + CH3CHO(49) <=> C2H3O(68) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1580,
    label = "OH(23) + CH3CHO(49) <=> C2H3O(68) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(-1.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1581,
    label = "C2H3O(68) + HCCOH(48) <=> HCCO(40) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1582,
    label = "O2(2) + C2H3O(68) <=> HO2(24) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.676e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.99, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1583,
    label = "butR1(3) + C2H3O(68) <=> CH3CHO(49) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1584,
    label = "butR2(4) + C2H3O(68) <=> C4H8(143) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1585,
    label = "butR2(4) + C2H3O(68) <=> CH3CHO(49) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1586,
    label = "butROO2(6) + C2H3O(68) <=> S(149) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1587,
    label = "C2H3O(18) + C2H3O(68) <=> CH2CO(42) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1588,
    label = "C2H3O(68) + C2H5O2(90) <=> CH2CO(42) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1589,
    label = "C3H7(51) + C2H3O(68) <=> C3H6(144) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1590,
    label = "C3H7(51) + C2H3O(68) <=> CH2CO(42) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1591,
    label = "C2H3O(68) + CH3O2(75) <=> CH2CO(42) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1592,
    label = "C2H3O(68) + C3H7(95) <=> C3H6(144) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.086e+15, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1593,
    label = "C2H3O(68) + C3H7(95) <=> CH2CO(42) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1594,
    label = "C2H3O(68) + C2H5O(71) <=> CH3CHO(49) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1595,
    label = "C2H3O(68) + C3H5(1446) <=> CH3CHO(49) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1596,
    label = "C2H3O(68) + S(2185) <=> CH2CO(42) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1597,
    label = "C2H3O(68) + C4H7(1663) <=> CH3CHO(49) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1598,
    label = "C2H3O(68) + CHO3(74) <=> CH2CO(42) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1599,
    label = "CHO2(57) + C2H3O(68) <=> CO2(34) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1600,
    label = "C2H3O(68) + S(2128) <=> CH3CHO(49) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1601,
    label = "C2H3O(68) + C4H5(2849) <=> CH2CO(42) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1602,
    label = "C2H3O(68) + S(4886) <=> CH2CO(42) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1603,
    label = "S(4321) + C2H3O(68) <=> CH3CHO(49) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1604,
    label = "S(4321) + C2H3O(68) <=> CH2CO(42) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1605,
    label = "C2H3O(68) + S(6828) <=> CH2CO(42) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1606,
    label = "S(4319) + C2H3O(68) <=> CH3CHO(49) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1607,
    label = "S(4319) + C2H3O(68) <=> CH3CHO(49) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1608,
    label = "S(4319) + C2H3O(68) <=> CH2CO(42) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1609,
    label = "C2H3O(68) + C2H3O(68) <=> CH2CO(42) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1610,
    label = "HO2(24) + S(9511) <=> S(10707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.459e+19, 'cm^3/(mol*s)'),
        n = -2.335,
        Ea = (3.17, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1611,
    label = "CH3O2(75) + S(9511) <=> S(10863)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.459e+19, 'cm^3/(mol*s)'),
        n = -2.335,
        Ea = (3.17, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1612,
    label = "CH2(S)(30) + S(10707) <=> S(10863)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.352e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1613,
    label = "O(20) + S(9511) <=> S(10703)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1614,
    label = "OH(23) + S(10703) <=> S(10707)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1615,
    label = "CH3O(36) + S(10703) <=> S(10863)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1616,
    label = "O2(2) + C2H3O(68) <=> S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1617,
    label = "S(12113) <=> HO2(24) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+09, 's^-1'), n=1.2, Ea=(34.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1618,
    label = "S(10058) <=> OH(23) + S(11385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=0.18, Ea=(11.539, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1619,
    label = "S(10862) <=> CH3O(36) + S(11385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=0.18, Ea=(8.367, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1620,
    label = "S(10707) <=> OH(23) + S(11385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=0.18, Ea=(20.581, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1621,
    label = "S(10863) <=> CH3O(36) + S(11385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=0.18, Ea=(17.409, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1622,
    label = "S(10703) <=> S(11385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1623,
    label = "C3H6(144) + O(20) <=> S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+08, 'cm^3/(mol*s)'),
        n = 1.58,
        Ea = (-2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1624,
    label = "H(22) + S(1448) <=> H2(21) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.166e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1625,
    label = "H(22) + S(2128) <=> S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.48e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (0.51, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1626,
    label = "O2(2) + S(1448) <=> HO2(24) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.676e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.99, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1627,
    label = "CH(26) + S(1448) <=> CH2(28) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.137e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1628,
    label = "CH2(28) + S(1448) <=> CH3(31) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1629,
    label = "HCO(29) + S(1448) <=> CH2O(32) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1630,
    label = "CH3(31) + S(1448) <=> CH4(33) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.57e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1631,
    label = "CH2OH(35) + S(1448) <=> CH3OH(37) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1632,
    label = "HCCO(40) + S(1448) <=> CH2CO(42) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1633,
    label = "C2H3(41) + S(1448) <=> C2H4(43) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1634,
    label = "C2H5(44) + S(1448) <=> C2H6(45) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1635,
    label = "C2H3O(18) + S(1448) <=> CH3CHO(49) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1636,
    label = "C3H7(95) + S(1448) <=> C3H8(50) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1637,
    label = "C3H7(51) + S(1448) <=> C3H8(50) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1638,
    label = "butR2(4) + S(1448) <=> butane(1) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1639,
    label = "butR1(3) + S(1448) <=> butane(1) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1640,
    label = "C4H9O2(8) + S(1448) <=> S(149) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1641,
    label = "C3H5(1446) + S(1448) <=> C3H6(144) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1642,
    label = "S(1448) + S(1125) <=> C4H9O(147) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1643,
    label = "C4H7(1663) + S(1448) <=> C4H8(96) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1644,
    label = "C4H7(1663) + S(1448) <=> C4H8(143) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1645,
    label = "C3H3(2385) + S(1448) <=> C3H4(2124) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1646,
    label = "H(22) + S(1448) <=> S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1647,
    label = "O(20) + S(1450) <=> OH(23) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(4.69, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1648,
    label = "H2(21) + S(1448) <=> H(22) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.1264, 'cm^3/(mol*s)'), n=4, Ea=(4.91, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1649,
    label = "OH(23) + S(1450) <=> H2O(46) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17.3, 'cm^3/(mol*s)'), n=3.4, Ea=(-1.14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1650,
    label = "H2O2(25) + S(1448) <=> HO2(24) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.115, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1651,
    label = "CH2(28) + S(1448) <=> CH(26) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.501e+08, 'cm^3/(mol*s)'),
        n = 1.453,
        Ea = (2.382, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1652,
    label = "CH2(28) + S(1450) <=> CH3(31) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1653,
    label = "CH2O(32) + S(1448) <=> HCO(29) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(2.98, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1654,
    label = "CH4(33) + S(1448) <=> CH3(31) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00062, 'cm^3/(mol*s)'), n=5, Ea=(5.58, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1655,
    label = "CH3OH(37) + S(1448) <=> CH2OH(35) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (938900, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (9.809, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1656,
    label = "CH3O(36) + S(1450) <=> CH3OH(37) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1657,
    label = "C2H(38) + S(1450) <=> C2H2(39) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1658,
    label = "HCCOH(48) + S(1448) <=> HCCO(40) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1659,
    label = "HCCO(40) + S(1450) <=> CH2CO(42) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1660,
    label = "C2H3(41) + S(1450) <=> C2H4(43) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1661,
    label = "C2H6(45) + S(1448) <=> C2H5(44) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.162e+11, 'cm^3/(mol*s)'), n=0, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1662,
    label = "O2(2) + S(1450) <=> HO2(24) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(54.957, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1663,
    label = "butR1(3) + S(1450) <=> butane(1) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1664,
    label = "butane(1) + S(1448) <=> butR2(4) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1665,
    label = "S(149) + S(1448) <=> butROO2(6) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1666,
    label = "S(149) + S(1448) <=> C4H9O2(8) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.581e+11, 'cm^3/(mol*s)'), n=0, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1667,
    label = "CH3CHO(49) + S(1448) <=> C2H3O(18) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7902, 'cm^3/(mol*s)'),
        n = 3.82,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1668,
    label = "S(1448) + CCOO(1350) <=> C2H5O2(90) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1669,
    label = "C3H7(51) + S(1450) <=> C3H8(50) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1670,
    label = "COO(1544) + S(1448) <=> CH3O2(75) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1671,
    label = "C3H8(50) + S(1448) <=> C3H7(95) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1672,
    label = "C3H6(144) + S(1448) <=> C3H5(1446) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7902, 'cm^3/(mol*s)'),
        n = 3.82,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1673,
    label = "S(1448) + S(2134) <=> S(1450) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1674,
    label = "C4H8(143) + S(1448) <=> C4H7(1663) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58, 'cm^3/(mol*s)'), n=3.82, Ea=(1.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1675,
    label = "C4H8(96) + S(1448) <=> C4H7(1663) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1676,
    label = "S(2644) + S(1448) <=> CHO3(74) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1677,
    label = "S(1448) + C4H6(2483) <=> S(1450) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.156e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.219, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1678,
    label = "S(1448) + S(4759) <=> S(1450) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1679,
    label = "S(3752) + S(1448) <=> S(4321) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1680,
    label = "S(1448) + S(6731) <=> S(1450) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1681,
    label = "S(1448) + C3H4(2124) <=> C3H3(2385) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (2.367, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1682,
    label = "S(3752) + S(1448) <=> S(4319) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.219, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1683,
    label = "CH2(S)(30) + S(1448) <=> S(1667)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.055e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1684,
    label = "S(1450) + S(1125) <=> C4H9O(147) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1685,
    label = "CH3CHO(49) + S(1448) <=> C2H3O(68) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1686,
    label = "O(20) + S(1448) <=> OH(23) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1687,
    label = "OH(23) + S(1448) <=> H2O(46) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1688,
    label = "HO2(24) + S(1448) <=> H2O2(25) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1689,
    label = "CH2OH(35) + S(1448) <=> CH2O(32) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1690,
    label = "CH3O(36) + S(1448) <=> CH2O(32) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1691,
    label = "CH3O(36) + S(1448) <=> CH3OH(37) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1692,
    label = "C2H(38) + S(1448) <=> C2H2(39) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.083e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1693,
    label = "HCCO(40) + S(1448) <=> HCCOH(48) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1694,
    label = "C2H3(41) + S(1448) <=> C2H2(39) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1695,
    label = "C2H5(44) + S(1448) <=> C2H4(43) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1696,
    label = "butR1(3) + S(1448) <=> C4H8(96) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1697,
    label = "butR2(4) + S(1448) <=> C4H8(143) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1698,
    label = "butR2(4) + S(1448) <=> C4H8(96) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1699,
    label = "butROO2(6) + S(1448) <=> S(149) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1700,
    label = "C2H3O(18) + S(1448) <=> CH2CO(42) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1701,
    label = "C2H5O2(90) + S(1448) <=> S(2128) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1702,
    label = "C3H7(51) + S(1448) <=> C3H6(144) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1703,
    label = "CH3O2(75) + S(1448) <=> COO(1544) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1704,
    label = "C3H7(95) + S(1448) <=> C3H6(144) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1705,
    label = "C2H5O(71) + S(1448) <=> CH3CHO(49) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1706,
    label = "C3H5(1446) + S(1448) <=> S(1450) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1707,
    label = "S(1448) + S(2185) <=> S(2128) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1708,
    label = "C4H7(1663) + S(1448) <=> S(1450) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1709,
    label = "CHO3(74) + S(1448) <=> S(2644) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1710,
    label = "CHO2(57) + S(1448) <=> CO2(34) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1711,
    label = "S(1448) + S(2128) <=> S(3752) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1712,
    label = "S(1448) + C4H5(2849) <=> S(2128) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1713,
    label = "S(1448) + S(4886) <=> S(2128) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1714,
    label = "S(4321) + S(1448) <=> S(1450) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1715,
    label = "S(4321) + S(1448) <=> S(3752) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1716,
    label = "S(1448) + S(6828) <=> S(2128) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1717,
    label = "S(4319) + S(1448) <=> S(1450) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1718,
    label = "S(4319) + S(1448) <=> S(1450) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1719,
    label = "S(4319) + S(1448) <=> S(3752) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1720,
    label = "C2H3O(68) + S(1448) <=> CH2CO(42) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1721,
    label = "C2H3O(68) + S(1448) <=> CH3CHO(49) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1722,
    label = "S(1448) + S(1448) <=> S(1450) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1723,
    label = "C2H3O(68) + HO2(24) <=> S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1724,
    label = "H(22) + S(12093) <=> H2(21) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1725,
    label = "H(22) + S(12113) <=> S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1726,
    label = "O(20) + S(12093) <=> OH(23) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1727,
    label = "HO2(24) + S(12113) <=> O2(2) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1728,
    label = "H2O2(25) + S(12113) <=> HO2(24) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1729,
    label = "CH(26) + S(12093) <=> CH2(28) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1730,
    label = "CH2(28) + S(12093) <=> CH3(31) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1731,
    label = "CH2O(32) + S(12113) <=> HCO(29) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1732,
    label = "CH3(31) + S(12093) <=> CH4(33) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1733,
    label = "CH2OH(35) + S(12113) <=> CH2O(32) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1734,
    label = "CH3O(36) + S(12113) <=> CH2O(32) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1735,
    label = "CH3OH(37) + S(12113) <=> CH2OH(35) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (938900, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (9.917, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1736,
    label = "CH3O(36) + S(12093) <=> CH3OH(37) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1737,
    label = "C2H(38) + S(12093) <=> C2H2(39) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1738,
    label = "C2H3(41) + S(12113) <=> C2H2(39) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1739,
    label = "HCCO(40) + S(12093) <=> CH2CO(42) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1740,
    label = "C2H3(41) + S(12093) <=> C2H4(43) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1741,
    label = "C2H5(44) + S(12113) <=> C2H4(43) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1742,
    label = "C2H5(44) + S(12093) <=> C2H6(45) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1743,
    label = "OH(23) + S(12093) <=> H2O(46) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1744,
    label = "HCCOH(48) + S(12113) <=> HCCO(40) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1745,
    label = "C2H3O(18) + S(12093) <=> CH3CHO(49) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (0.746, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1746,
    label = "CH3CHO(49) + S(12113) <=> C2H3O(68) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1747,
    label = "C3H8(50) + S(12113) <=> C3H7(95) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17.686, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1748,
    label = "C3H7(51) + S(12093) <=> C3H8(50) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1749,
    label = "butR2(4) + S(12093) <=> butane(1) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5706, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (0.877, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1750,
    label = "butR1(3) + S(12093) <=> butane(1) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1751,
    label = "butR1(3) + S(12113) <=> C4H8(96) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1752,
    label = "butR2(4) + S(12113) <=> C4H8(143) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1753,
    label = "butR2(4) + S(12113) <=> C4H8(96) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1754,
    label = "C2H3O(18) + S(12113) <=> CH2CO(42) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1755,
    label = "C3H7(51) + S(12113) <=> C3H6(144) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1756,
    label = "C4H9O2(8) + S(12093) <=> S(149) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1757,
    label = "S(149) + S(12113) <=> butROO2(6) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1758,
    label = "C3H6(144) + S(12113) <=> C3H5(1446) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001735, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1759,
    label = "S(1125) + S(12093) <=> C4H9O(147) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1760,
    label = "C3H7(95) + S(12113) <=> C3H6(144) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1761,
    label = "C4H8(96) + S(12113) <=> C4H7(1663) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1762,
    label = "CCOO(1350) + S(12113) <=> C2H5O2(90) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1763,
    label = "C4H8(143) + S(12113) <=> C4H7(1663) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00347, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1764,
    label = "C2H5O(71) + S(12113) <=> CH3CHO(49) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1765,
    label = "COO(1544) + S(12113) <=> CH3O2(75) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1766,
    label = "C3H5(1446) + S(12113) <=> C3H4(2124) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1767,
    label = "C3H4(2124) + S(12113) <=> C3H3(2385) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (4.086, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1768,
    label = "C4H7(1663) + S(12113) <=> C4H6(2483) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1769,
    label = "C4H5(2849) + S(12093) <=> C4H6(2483) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1770,
    label = "S(2134) + S(12113) <=> S(2185) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1771,
    label = "CHO3(74) + S(12093) <=> S(2644) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1772,
    label = "CHO2(57) + S(12113) <=> CO2(34) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1773,
    label = "S(2128) + S(12113) <=> S(3752) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1774,
    label = "S(4319) + S(12093) <=> S(3752) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1775,
    label = "S(3752) + S(12113) <=> S(4321) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1776,
    label = "S(4321) + S(12113) <=> S(6711) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1777,
    label = "S(6731) + S(12113) <=> S(6828) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1778,
    label = "S(1448) + S(12093) <=> S(1450) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1779,
    label = "S(4319) + S(12113) <=> S(9511) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1780,
    label = "S(4319) + S(12113) <=> S(6711) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1781,
    label = "S(4759) + S(12113) <=> S(4886) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1782,
    label = "C2H3O(68) + S(12113) <=> CH2CO(42) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1783,
    label = "S(1448) + S(12113) <=> S(2128) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1784,
    label = "O(20) + S(9511) <=> S(10702)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1785,
    label = "OH(23) + S(10702) <=> S(10058)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1786,
    label = "CH3O(36) + S(10702) <=> S(10862)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1787,
    label = "S(10702) <=> S(11385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1788,
    label = "HCO(29) + HCCO(40) <=> S(10702)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5452, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (5.987, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1789,
    label = "CH2(S)(30) + S(10030) <=> S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.302e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1790,
    label = "S(1448) <=> S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1791,
    label = "CH2(S)(30) + CH3CHO(49) <=> S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.981e+14, 'cm^3/(mol*s)'),
        n = -0.467,
        Ea = (-0.022, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1792,
    label = "C2H3O(68) + O(20) <=> S(12091)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1793,
    label = "O(20) + S(12091) <=> S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1794,
    label = "OH(23) + S(12091) <=> S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1795,
    label = "CH3(31) + CO2(34) <=> S(12091)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (9.082, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1796,
    label = "S(5415) <=> S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.668e+06, 's^-1'), n=1.614, Ea=(29.669, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1797,
    label = "H(22) + S(5415) <=> S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1798,
    label = "O(20) + S(4759) <=> OH(23) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1799,
    label = "H(22) + S(4759) <=> H2(21) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.3776, 'cm^3/(mol*s)'), n=4.34, Ea=(5.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1800,
    label = "OH(23) + S(4759) <=> H2O(46) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(1.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1801,
    label = "H2O2(25) + S(5415) <=> HO2(24) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1802,
    label = "CH(26) + S(4759) <=> CH2(28) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1803,
    label = "CH2(28) + S(4759) <=> CH3(31) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.24e+07, 'cm^3/(mol*s)'),
        n = 1.524,
        Ea = (5.498, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1804,
    label = "CH2O(32) + S(5415) <=> HCO(29) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1805,
    label = "CH3(31) + S(4759) <=> CH4(33) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008928, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1806,
    label = "CH3OH(37) + S(5415) <=> CH2OH(35) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005592, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1807,
    label = "CH3O(36) + S(4759) <=> CH3OH(37) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1808,
    label = "C2H(38) + S(4759) <=> C2H2(39) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.678, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1809,
    label = "HCCOH(48) + S(5415) <=> HCCO(40) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1810,
    label = "HCCO(40) + S(4759) <=> CH2CO(42) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.02741, 'cm^3/(mol*s)'), n=4.34, Ea=(18, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1811,
    label = "C2H3(41) + S(4759) <=> C2H4(43) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01302, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.405, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1812,
    label = "C2H6(45) + S(5415) <=> C2H5(44) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1813,
    label = "HO2(24) + S(5415) <=> O2(2) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.48, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1814,
    label = "butR1(3) + S(4759) <=> butane(1) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1815,
    label = "butane(1) + S(5415) <=> butR2(4) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00904, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (8.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1816,
    label = "S(149) + S(5415) <=> butROO2(6) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1817,
    label = "C4H9O2(8) + S(4759) <=> S(149) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1818,
    label = "CH3CHO(49) + S(5415) <=> C2H3O(18) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005589, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1819,
    label = "CCOO(1350) + S(5415) <=> C2H5O2(90) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1820,
    label = "C3H8(50) + S(5415) <=> C3H7(51) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1821,
    label = "COO(1544) + S(5415) <=> CH3O2(75) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1822,
    label = "C3H8(50) + S(5415) <=> C3H7(95) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00452, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (8.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1823,
    label = "C3H6(144) + S(5415) <=> C3H5(1446) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005589, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1824,
    label = "S(2134) + S(5415) <=> S(2185) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1825,
    label = "C4H8(143) + S(5415) <=> C4H7(1663) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1826,
    label = "C4H8(96) + S(5415) <=> C4H7(1663) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.006127, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.867, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1827,
    label = "S(2644) + S(5415) <=> CHO3(74) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1828,
    label = "C4H6(2483) + S(5415) <=> C4H5(2849) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01127, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (12.567, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1829,
    label = "S(4759) + S(5415) <=> S(4759) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1830,
    label = "S(3752) + S(5415) <=> S(4321) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1831,
    label = "S(6731) + S(5415) <=> S(4759) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1832,
    label = "C3H4(2124) + S(5415) <=> C3H3(2385) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.09769, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (10.367, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1833,
    label = "S(4319) + S(4759) <=> S(3752) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005633, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (12.567, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1834,
    label = "S(1125) + S(4759) <=> C4H9O(147) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1835,
    label = "CH3CHO(49) + S(5415) <=> C2H3O(68) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1836,
    label = "S(5415) + S(12093) <=> S(4759) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1837,
    label = "S(1448) + S(4759) <=> S(1450) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.219, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1838,
    label = "CH2OH(35) + S(5415) <=> CH2O(32) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1839,
    label = "CH3O(36) + S(5415) <=> CH2O(32) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1840,
    label = "C2H3(41) + S(5415) <=> C2H2(39) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1841,
    label = "C2H5(44) + S(5415) <=> C2H4(43) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1842,
    label = "butR1(3) + S(5415) <=> C4H8(96) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1843,
    label = "butR2(4) + S(5415) <=> C4H8(143) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1844,
    label = "butR2(4) + S(5415) <=> C4H8(96) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1845,
    label = "C2H3O(18) + S(5415) <=> CH2CO(42) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1846,
    label = "C3H7(51) + S(5415) <=> C3H6(144) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1847,
    label = "C3H7(95) + S(5415) <=> C3H6(144) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.876e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1848,
    label = "C2H5O(71) + S(5415) <=> CH3CHO(49) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1849,
    label = "C3H5(1446) + S(5415) <=> C3H4(2124) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.037e+10, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1850,
    label = "C4H7(1663) + S(5415) <=> C4H6(2483) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1851,
    label = "CHO2(57) + S(5415) <=> CO2(34) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1852,
    label = "S(2128) + S(5415) <=> S(3752) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1853,
    label = "S(4321) + S(5415) <=> S(4759) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1854,
    label = "S(4319) + S(5415) <=> S(4759) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1855,
    label = "S(4319) + S(5415) <=> S(4759) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1856,
    label = "C2H3O(68) + S(5415) <=> CH2CO(42) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1857,
    label = "S(1448) + S(5415) <=> S(2128) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1858,
    label = "CH2(S)(30) + S(10606) <=> S(10031)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.055e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1859,
    label = "S(10606) <=> S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1860,
    label = "CH2(28) + CH3CHO(49) <=> S(10606)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1861,
    label = "O2(2) + S(5415) <=> S(15428)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1862,
    label = "HCO(29) + C3H6O(748) <=> C4H7O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1863,
    label = "H(22) + C3H6O(748) <=> C3H5O(17) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.629e+11, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (0.023, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1864,
    label = "C3H5O(17) + H(22) <=> C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1865,
    label = "O2(2) + C3H6O(748) <=> C3H5O(17) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.412e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.908, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1866,
    label = "CH(26) + C3H6O(748) <=> C3H5O(17) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1867,
    label = "CH2(28) + C3H6O(748) <=> C3H5O(17) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.079e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1868,
    label = "HCO(29) + C3H6O(748) <=> C3H5O(17) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1869,
    label = "CH3(31) + C3H6O(748) <=> C3H5O(17) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1870,
    label = "CH2OH(35) + C3H6O(748) <=> C3H5O(17) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1871,
    label = "HCCO(40) + C3H6O(748) <=> C3H5O(17) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1872,
    label = "C2H3(41) + C3H6O(748) <=> C3H5O(17) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1873,
    label = "C2H5(44) + C3H6O(748) <=> C3H5O(17) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1874,
    label = "C2H3O(18) + C3H6O(748) <=> C3H5O(17) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1875,
    label = "C3H7(95) + C3H6O(748) <=> C3H5O(17) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1876,
    label = "C3H7(51) + C3H6O(748) <=> C3H5O(17) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1877,
    label = "butR2(4) + C3H6O(748) <=> butane(1) + C3H5O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1878,
    label = "butR1(3) + C3H6O(748) <=> butane(1) + C3H5O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1879,
    label = "C2H3O(18) + CH3(31) <=> C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1880,
    label = "C4H9O2(8) + C3H6O(748) <=> C3H5O(17) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1881,
    label = "C3H6(144) + O(20) <=> C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.17e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (-1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1882,
    label = "C3H5(1446) + C3H6O(748) <=> C3H5O(17) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1883,
    label = "CH3(31) + C3H6O(748) <=> C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1884,
    label = "C3H6O(748) + S(1125) <=> C3H5O(17) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1885,
    label = "C4H7(1663) + C3H6O(748) <=> C3H5O(17) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1886,
    label = "C4H7(1663) + C3H6O(748) <=> C3H5O(17) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1887,
    label = "C3H3(2385) + C3H6O(748) <=> C3H5O(17) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1888,
    label = "H(22) + C3H6O(748) <=> S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1889,
    label = "O(20) + S(1449) <=> OH(23) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(4.69, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1890,
    label = "H2(21) + C3H6O(748) <=> H(22) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.1264, 'cm^3/(mol*s)'), n=4, Ea=(4.91, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1891,
    label = "OH(23) + S(1449) <=> H2O(46) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17.3, 'cm^3/(mol*s)'), n=3.4, Ea=(-1.14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1892,
    label = "H2O2(25) + C3H6O(748) <=> HO2(24) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.115, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1893,
    label = "CH2(28) + C3H6O(748) <=> CH(26) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.501e+08, 'cm^3/(mol*s)'),
        n = 1.453,
        Ea = (2.382, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1894,
    label = "CH2(28) + S(1449) <=> CH3(31) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1895,
    label = "CH2O(32) + C3H6O(748) <=> HCO(29) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(2.98, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1896,
    label = "CH4(33) + C3H6O(748) <=> CH3(31) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00062, 'cm^3/(mol*s)'), n=5, Ea=(5.58, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1897,
    label = "CH3OH(37) + C3H6O(748) <=> CH2OH(35) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (938900, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (9.809, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1898,
    label = "CH3O(36) + S(1449) <=> CH3OH(37) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1899,
    label = "C2H(38) + S(1449) <=> C2H2(39) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1900,
    label = "HCCOH(48) + C3H6O(748) <=> HCCO(40) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1901,
    label = "HCCO(40) + S(1449) <=> CH2CO(42) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1902,
    label = "C2H3(41) + S(1449) <=> C2H4(43) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1903,
    label = "C2H6(45) + C3H6O(748) <=> C2H5(44) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.162e+11, 'cm^3/(mol*s)'), n=0, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1904,
    label = "O2(2) + S(1449) <=> HO2(24) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(54.957, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1905,
    label = "butR1(3) + S(1449) <=> butane(1) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1906,
    label = "butane(1) + C3H6O(748) <=> butR2(4) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1907,
    label = "S(149) + C3H6O(748) <=> butROO2(6) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1908,
    label = "S(149) + C3H6O(748) <=> C4H9O2(8) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.581e+11, 'cm^3/(mol*s)'), n=0, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1909,
    label = "CH3CHO(49) + C3H6O(748) <=> C2H3O(18) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7902, 'cm^3/(mol*s)'),
        n = 3.82,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1910,
    label = "C3H6O(748) + CCOO(1350) <=> C2H5O2(90) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1911,
    label = "C3H7(51) + S(1449) <=> C3H8(50) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1912,
    label = "COO(1544) + C3H6O(748) <=> CH3O2(75) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1913,
    label = "C3H8(50) + C3H6O(748) <=> C3H7(95) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1914,
    label = "C3H6(144) + C3H6O(748) <=> C3H5(1446) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7902, 'cm^3/(mol*s)'),
        n = 3.82,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1915,
    label = "C3H6O(748) + S(2134) <=> S(1449) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1916,
    label = "C4H8(143) + C3H6O(748) <=> C4H7(1663) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58, 'cm^3/(mol*s)'), n=3.82, Ea=(1.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1917,
    label = "C4H8(96) + C3H6O(748) <=> C4H7(1663) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1918,
    label = "S(2644) + C3H6O(748) <=> CHO3(74) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1919,
    label = "C3H6O(748) + C4H6(2483) <=> S(1449) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.156e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.219, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1920,
    label = "C3H6O(748) + S(4759) <=> S(1449) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1921,
    label = "S(3752) + C3H6O(748) <=> S(4321) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1922,
    label = "C3H6O(748) + S(6731) <=> S(1449) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1923,
    label = "C3H4(2124) + C3H6O(748) <=> C3H3(2385) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (2.367, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1924,
    label = "S(3752) + C3H6O(748) <=> S(4319) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.219, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1925,
    label = "CH2(S)(30) + C3H6O(748) <=> S(1125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.302e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1926,
    label = "S(1449) + S(1125) <=> C4H9O(147) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1927,
    label = "CH3CHO(49) + C3H6O(748) <=> C2H3O(68) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1928,
    label = "C3H6O(748) + S(12093) <=> S(1449) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1929,
    label = "S(1448) + S(1449) <=> S(1450) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1930,
    label = "C3H6O(748) <=> S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1931,
    label = "C3H6O(748) + S(4759) <=> S(1449) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.219, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1932,
    label = "CH2(28) + CH3CHO(49) <=> C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.343e+07, 'cm^3/(mol*s)'),
        n = 1.603,
        Ea = (-1.375, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1933,
    label = "O(20) + C3H6O(748) <=> C3H5O(17) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1934,
    label = "OH(23) + C3H6O(748) <=> C3H5O(17) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1935,
    label = "HO2(24) + C3H6O(748) <=> C3H5O(17) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1936,
    label = "CH2OH(35) + C3H6O(748) <=> CH2O(32) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1937,
    label = "CH3O(36) + C3H6O(748) <=> CH2O(32) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1938,
    label = "CH3O(36) + C3H6O(748) <=> C3H5O(17) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1939,
    label = "C2H(38) + C3H6O(748) <=> C3H5O(17) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.659e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1940,
    label = "HCCO(40) + C3H6O(748) <=> C3H5O(17) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1941,
    label = "C2H3(41) + C3H6O(748) <=> C2H2(39) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1942,
    label = "C2H5(44) + C3H6O(748) <=> C2H4(43) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1943,
    label = "butR1(3) + C3H6O(748) <=> C4H8(96) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1944,
    label = "butR2(4) + C3H6O(748) <=> C4H8(143) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1945,
    label = "butR2(4) + C3H6O(748) <=> C4H8(96) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1946,
    label = "butROO2(6) + C3H6O(748) <=> C3H5O(17) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1947,
    label = "C2H3O(18) + C3H6O(748) <=> CH2CO(42) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1948,
    label = "C2H5O2(90) + C3H6O(748) <=> C3H5O(17) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1949,
    label = "C3H7(51) + C3H6O(748) <=> C3H6(144) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1950,
    label = "CH3O2(75) + C3H6O(748) <=> C3H5O(17) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1951,
    label = "C3H7(95) + C3H6O(748) <=> C3H6(144) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1952,
    label = "C2H5O(71) + C3H6O(748) <=> CH3CHO(49) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1953,
    label = "C3H5(1446) + C3H6O(748) <=> S(1449) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1954,
    label = "S(2185) + C3H6O(748) <=> C3H5O(17) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1955,
    label = "C4H7(1663) + C3H6O(748) <=> S(1449) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1956,
    label = "CHO3(74) + C3H6O(748) <=> C3H5O(17) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1957,
    label = "CHO2(57) + C3H6O(748) <=> CO2(34) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1958,
    label = "S(2128) + C3H6O(748) <=> S(3752) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1959,
    label = "C3H6O(748) + C4H5(2849) <=> C3H5O(17) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1960,
    label = "C3H6O(748) + S(4886) <=> C3H5O(17) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1961,
    label = "S(4321) + C3H6O(748) <=> S(1449) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1962,
    label = "S(4321) + C3H6O(748) <=> C3H5O(17) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1963,
    label = "C3H6O(748) + S(6828) <=> C3H5O(17) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1964,
    label = "S(4319) + C3H6O(748) <=> S(1449) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1965,
    label = "S(4319) + C3H6O(748) <=> S(1449) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1966,
    label = "S(4319) + C3H6O(748) <=> C3H5O(17) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1967,
    label = "C2H3O(68) + C3H6O(748) <=> CH2CO(42) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1968,
    label = "C2H3O(68) + C3H6O(748) <=> C3H5O(17) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1969,
    label = "C3H6O(748) + S(12113) <=> C3H5O(17) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1970,
    label = "S(1448) + C3H6O(748) <=> S(1449) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1971,
    label = "S(1448) + C3H6O(748) <=> C3H5O(17) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1972,
    label = "C3H6O(748) + S(5415) <=> C3H5O(17) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1973,
    label = "C3H6O(748) + C3H6O(748) <=> C3H5O(17) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1974,
    label = "H(22) + S(14812) <=> S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1975,
    label = "O(20) + S(10030) <=> OH(23) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (145000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.88, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1976,
    label = "H(22) + S(10030) <=> H2(21) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5220, 'cm^3/(mol*s)'), n=3.04, Ea=(2.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1977,
    label = "OH(23) + S(10030) <=> H2O(46) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3610, 'cm^3/(mol*s)'),
        n = 2.89,
        Ea = (-2.291, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1978,
    label = "H2O2(25) + S(14812) <=> HO2(24) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.97, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1979,
    label = "CH(26) + S(10030) <=> CH2(28) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(200000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1980,
    label = "CH2(28) + S(10030) <=> CH3(31) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(7.47, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1981,
    label = "CH2O(32) + S(14812) <=> HCO(29) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+11, 'cm^3/(mol*s)'), n=0, Ea=(6.96, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1982,
    label = "CH3(31) + S(10030) <=> CH4(33) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00248, 'cm^3/(mol*s)'),
        n = 4.44,
        Ea = (4.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1983,
    label = "CH3O(36) + S(14812) <=> CH2O(32) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1984,
    label = "CH2OH(35) + S(14812) <=> CH2O(32) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1985,
    label = "CHO2(57) + S(14812) <=> CO2(34) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1986,
    label = "CH2OH(35) + S(10030) <=> CH3OH(37) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1987,
    label = "CH3O(36) + S(10030) <=> CH3OH(37) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1988,
    label = "C2H(38) + S(10030) <=> C2H2(39) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1989,
    label = "C2H3(41) + S(14812) <=> C2H2(39) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1990,
    label = "HCCOH(48) + S(14812) <=> HCCO(40) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1991,
    label = "HCCO(40) + S(10030) <=> CH2CO(42) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009794, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.869, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1992,
    label = "C2H3(41) + S(10030) <=> C2H4(43) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.052, 'cm^3/(mol*s)'), n=3.9, Ea=(0.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1993,
    label = "C2H3O(68) + S(14812) <=> CH2CO(42) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1994,
    label = "C2H3O(18) + S(14812) <=> CH2CO(42) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1995,
    label = "C2H5(44) + S(14812) <=> C2H4(43) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1996,
    label = "C2H5(44) + S(10030) <=> C2H6(45) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1997,
    label = "C2H5O(71) + S(14812) <=> CH3CHO(49) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 1998,
    label = "HO2(24) + S(14812) <=> O2(2) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.529, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1999,
    label = "butR1(3) + S(10030) <=> butane(1) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2000,
    label = "butR2(4) + S(10030) <=> butane(1) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2001,
    label = "S(149) + S(14812) <=> butROO2(6) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2002,
    label = "C4H9O2(8) + S(10030) <=> S(149) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2003,
    label = "C3H6O(748) + S(14812) <=> C3H5O(17) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2004,
    label = "C2H3O(18) + S(10030) <=> CH3CHO(49) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2005,
    label = "CCOO(1350) + S(14812) <=> C2H5O2(90) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2006,
    label = "C3H7(51) + S(10030) <=> C3H8(50) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2007,
    label = "C3H7(51) + S(14812) <=> C3H6(144) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2008,
    label = "C3H7(95) + S(14812) <=> C3H6(144) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.949e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2009,
    label = "COO(1544) + S(14812) <=> CH3O2(75) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2010,
    label = "C3H7(95) + S(10030) <=> C3H8(50) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2011,
    label = "butR1(3) + S(14812) <=> C4H8(96) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2012,
    label = "butR2(4) + S(14812) <=> C4H8(96) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2013,
    label = "butR2(4) + S(14812) <=> C4H8(143) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2014,
    label = "C3H6(144) + S(14812) <=> C3H5(1446) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.172e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2015,
    label = "S(2134) + S(14812) <=> S(2185) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2016,
    label = "C3H5(1446) + S(14812) <=> C3H4(2124) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2017,
    label = "C4H8(143) + S(14812) <=> C4H7(1663) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.345e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2018,
    label = "C4H8(96) + S(14812) <=> C4H7(1663) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002162, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2019,
    label = "CHO3(74) + S(10030) <=> S(2644) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2020,
    label = "C4H7(1663) + S(14812) <=> C4H6(2483) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2021,
    label = "S(1448) + S(14812) <=> S(2128) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2022,
    label = "C4H5(2849) + S(10030) <=> C4H6(2483) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2023,
    label = "S(2128) + S(14812) <=> S(3752) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2024,
    label = "S(4759) + S(14812) <=> S(4886) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2025,
    label = "S(3752) + S(14812) <=> S(4321) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2026,
    label = "S(6828) + S(10030) <=> S(6731) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2027,
    label = "C3H4(2124) + S(14812) <=> C3H3(2385) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06264, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.353, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2028,
    label = "S(4319) + S(10030) <=> S(3752) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2029,
    label = "S(4319) + S(14812) <=> S(9511) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2030,
    label = "S(1125) + S(10030) <=> C4H9O(147) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2031,
    label = "S(4321) + S(14812) <=> S(6711) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2032,
    label = "S(4319) + S(14812) <=> S(6711) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2033,
    label = "CH3CHO(49) + S(14812) <=> C2H3O(68) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2034,
    label = "S(10030) + S(12113) <=> S(12093) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2035,
    label = "S(1448) + S(10030) <=> S(1450) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2036,
    label = "S(5415) + S(10030) <=> S(4759) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2037,
    label = "C3H6O(748) + S(10030) <=> S(1449) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2038,
    label = "H(22) + S(15301) <=> S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.555e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2039,
    label = "O(20) + S(5415) <=> OH(23) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2040,
    label = "H(22) + S(5415) <=> H2(21) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.358e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2041,
    label = "OH(23) + S(5415) <=> H2O(46) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2042,
    label = "HO2(24) + S(5415) <=> H2O2(25) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2043,
    label = "CH(26) + S(5415) <=> CH2(28) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2044,
    label = "CH2(28) + S(5415) <=> CH3(31) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.498e+10, 'cm^3/(mol*s)'),
        n = 0.917,
        Ea = (-0.454, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2045,
    label = "HCO(29) + S(5415) <=> CH2O(32) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2046,
    label = "CH3(31) + S(5415) <=> CH4(33) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2047,
    label = "CH2OH(35) + S(5415) <=> CH3OH(37) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2048,
    label = "CH3O(36) + S(5415) <=> CH3OH(37) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2049,
    label = "C2H(38) + S(5415) <=> C2H2(39) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2050,
    label = "HCCO(40) + S(5415) <=> HCCOH(48) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2051,
    label = "HCCO(40) + S(5415) <=> CH2CO(42) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2052,
    label = "C2H3(41) + S(5415) <=> C2H4(43) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2053,
    label = "C2H5(44) + S(5415) <=> C2H6(45) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2054,
    label = "O2(2) + S(5415) <=> HO2(24) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2055,
    label = "butR1(3) + S(5415) <=> butane(1) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2056,
    label = "butR2(4) + S(5415) <=> butane(1) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2057,
    label = "butROO2(6) + S(5415) <=> S(149) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2058,
    label = "C4H9O2(8) + S(5415) <=> S(149) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2059,
    label = "C2H3O(18) + S(5415) <=> CH3CHO(49) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2060,
    label = "C2H5O2(90) + S(5415) <=> CCOO(1350) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2061,
    label = "C3H7(51) + S(5415) <=> C3H8(50) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2062,
    label = "CH3O2(75) + S(5415) <=> COO(1544) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2063,
    label = "C3H7(95) + S(5415) <=> C3H8(50) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2064,
    label = "C3H5(1446) + S(5415) <=> C3H6(144) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2065,
    label = "S(2185) + S(5415) <=> S(2134) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2066,
    label = "C4H7(1663) + S(5415) <=> C4H8(143) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2067,
    label = "C4H7(1663) + S(5415) <=> C4H8(96) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2068,
    label = "CHO3(74) + S(5415) <=> S(2644) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2069,
    label = "C4H5(2849) + S(5415) <=> C4H6(2483) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2070,
    label = "S(4886) + S(5415) <=> S(4759) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2071,
    label = "S(4321) + S(5415) <=> S(3752) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2072,
    label = "S(6828) + S(5415) <=> S(6731) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2073,
    label = "C3H3(2385) + S(5415) <=> C3H4(2124) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2074,
    label = "S(4319) + S(5415) <=> S(3752) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2075,
    label = "S(1125) + S(5415) <=> C4H9O(147) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2076,
    label = "C2H3O(68) + S(5415) <=> CH3CHO(49) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2077,
    label = "S(5415) + S(12113) <=> S(12093) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2078,
    label = "S(1448) + S(5415) <=> S(1450) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2079,
    label = "S(5415) + S(5415) <=> S(4759) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2080,
    label = "C3H6O(748) + S(5415) <=> S(1449) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2081,
    label = "S(5415) + S(14812) <=> S(10030) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2082,
    label = "C2H3O(18) + CH2(S)(30) <=> S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+11, 'cm^3/(mol*s)'),
        n = 0.465,
        Ea = (-1.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2083,
    label = "H(22) + S(1054) <=> H2(21) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.166e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2084,
    label = "H(22) + S(3752) <=> S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(1.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2085,
    label = "O2(2) + S(1054) <=> HO2(24) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.676e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.99, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2086,
    label = "CH(26) + S(1054) <=> CH2(28) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.137e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2087,
    label = "CH2(28) + S(1054) <=> CH3(31) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2088,
    label = "HCO(29) + S(1054) <=> CH2O(32) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2089,
    label = "CH3(31) + S(1054) <=> CH4(33) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.57e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2090,
    label = "CH2OH(35) + S(1054) <=> CH3OH(37) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2091,
    label = "HCCO(40) + S(1054) <=> CH2CO(42) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2092,
    label = "C2H3(41) + S(1054) <=> C2H4(43) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2093,
    label = "C2H5(44) + S(1054) <=> C2H6(45) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2094,
    label = "C2H3O(18) + S(1054) <=> CH3CHO(49) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2095,
    label = "C3H7(95) + S(1054) <=> C3H8(50) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2096,
    label = "C3H7(51) + S(1054) <=> C3H8(50) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2097,
    label = "butR2(4) + S(1054) <=> butane(1) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.33e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2098,
    label = "butR1(3) + S(1054) <=> butane(1) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2099,
    label = "C4H9O2(8) + S(1054) <=> S(149) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2100,
    label = "C3H5(1446) + S(1054) <=> C3H6(144) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2101,
    label = "S(1054) + S(1125) <=> C4H9O(147) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2102,
    label = "C4H7(1663) + S(1054) <=> C4H8(96) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2103,
    label = "C4H7(1663) + S(1054) <=> C4H8(143) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2104,
    label = "C3H3(2385) + S(1054) <=> S(3752) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.56e+14, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2105,
    label = "H(22) + S(1054) <=> S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (7.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2106,
    label = "O(20) + S(1448) <=> OH(23) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.135e+10, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2107,
    label = "H(22) + S(1448) <=> H2(21) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.257e+11, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (0.023, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2108,
    label = "OH(23) + S(1448) <=> H2O(46) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2109,
    label = "HO2(24) + S(1448) <=> H2O2(25) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2110,
    label = "CH(26) + S(1448) <=> CH2(28) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.183e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2111,
    label = "CH2(28) + S(1448) <=> CH3(31) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.616e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2112,
    label = "HCO(29) + S(1448) <=> CH2O(32) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2113,
    label = "CH3(31) + S(1448) <=> CH4(33) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2114,
    label = "CH2OH(35) + S(1448) <=> CH3OH(37) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2115,
    label = "CH3O(36) + S(1448) <=> CH3OH(37) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2116,
    label = "C2H(38) + S(1448) <=> C2H2(39) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.319e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2117,
    label = "HCCO(40) + S(1448) <=> HCCOH(48) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2118,
    label = "HCCO(40) + S(1448) <=> CH2CO(42) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2119,
    label = "C2H3(41) + S(1448) <=> C2H4(43) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2120,
    label = "C2H5(44) + S(1448) <=> C2H6(45) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2121,
    label = "O2(2) + S(1448) <=> HO2(24) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.824e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.908, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2122,
    label = "butR1(3) + S(1448) <=> butane(1) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2123,
    label = "butR2(4) + S(1448) <=> butane(1) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2124,
    label = "butROO2(6) + S(1448) <=> S(149) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2125,
    label = "C4H9O2(8) + S(1448) <=> S(149) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2126,
    label = "C2H3O(18) + S(1448) <=> CH3CHO(49) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2127,
    label = "C2H5O2(90) + S(1448) <=> S(1054) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2128,
    label = "C3H7(51) + S(1448) <=> C3H8(50) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2129,
    label = "CH3O2(75) + S(1448) <=> COO(1544) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2130,
    label = "C3H7(95) + S(1448) <=> C3H8(50) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2131,
    label = "C3H5(1446) + S(1448) <=> C3H6(144) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2132,
    label = "S(1448) + S(2185) <=> S(1054) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2133,
    label = "C4H7(1663) + S(1448) <=> C4H8(143) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2134,
    label = "C4H7(1663) + S(1448) <=> C4H8(96) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2135,
    label = "CHO3(74) + S(1448) <=> S(2644) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2136,
    label = "S(1448) + C4H5(2849) <=> S(1054) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2137,
    label = "S(1448) + S(4886) <=> S(1054) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2138,
    label = "S(4321) + S(1448) <=> S(3752) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2139,
    label = "S(1448) + S(6828) <=> S(1054) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2140,
    label = "C3H3(2385) + S(1448) <=> C3H4(2124) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2141,
    label = "S(4319) + S(1448) <=> S(3752) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2142,
    label = "S(1448) + S(1125) <=> C4H9O(147) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2143,
    label = "C2H3O(68) + S(1448) <=> CH3CHO(49) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2144,
    label = "S(1448) + S(12113) <=> S(1054) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2145,
    label = "S(1448) + S(1448) <=> S(1450) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2146,
    label = "S(1054) + S(14812) <=> S(3752) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2147,
    label = "S(1448) + S(5415) <=> S(1054) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2148,
    label = "S(1448) + C3H6O(748) <=> S(1449) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2149,
    label = "S(1054) <=> S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 's^-1'), n=0.19, Ea=(26.314, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2150,
    label = "S(1448) + S(14812) <=> S(1054) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2151,
    label = "O(20) + S(1054) <=> OH(23) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2152,
    label = "OH(23) + S(1054) <=> H2O(46) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2153,
    label = "HO2(24) + S(1054) <=> H2O2(25) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2154,
    label = "CH3O(36) + S(1054) <=> CH3OH(37) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2155,
    label = "C2H(38) + S(1054) <=> C2H2(39) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.083e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2156,
    label = "HCCO(40) + S(1054) <=> HCCOH(48) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2157,
    label = "butROO2(6) + S(1054) <=> S(149) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2158,
    label = "C2H5O2(90) + S(1054) <=> S(3752) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2159,
    label = "CH3O2(75) + S(1054) <=> S(3752) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2160,
    label = "S(2185) + S(1054) <=> S(3752) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2161,
    label = "CHO3(74) + S(1054) <=> S(3752) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2162,
    label = "S(1054) + C4H5(2849) <=> S(3752) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2163,
    label = "S(1054) + S(4886) <=> S(3752) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2164,
    label = "S(4321) + S(1054) <=> S(3752) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2165,
    label = "S(1054) + S(6828) <=> S(3752) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2166,
    label = "S(4319) + S(1054) <=> S(3752) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2167,
    label = "C2H3O(68) + S(1054) <=> CH3CHO(49) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2168,
    label = "S(1054) + S(12113) <=> S(3752) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2169,
    label = "S(1448) + S(1054) <=> S(3752) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2170,
    label = "S(1054) + S(5415) <=> S(3752) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2171,
    label = "S(1054) + C3H6O(748) <=> S(3752) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2172,
    label = "CH3O2(75) + S(15301) <=> S(16274)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.459e+19, 'cm^3/(mol*s)'),
        n = -2.335,
        Ea = (3.17, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2173,
    label = "C2H5O2(90) + CO(27) <=> S(1352)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.532e+06, 'cm^3/(mol*s)'),
        n = 2.07,
        Ea = (82.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2174,
    label = "CH2(S)(30) + S(1139) <=> S(1352)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.115e+11, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2175,
    label = "S(1352) <=> HO2(24) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.476e+06, 's^-1'), n=1.829, Ea=(24.247, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2176,
    label = "O2(2) + S(1054) <=> S(1352)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2177,
    label = "CH3O2(75) + S(15301) <=> S(16275)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.459e+19, 'cm^3/(mol*s)'),
        n = -2.335,
        Ea = (3.17, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2178,
    label = "OH(23) + S(3752) <=> S(4325)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.312e+08, 'cm^3/(mol*s)'),
        n = 1.015,
        Ea = (-1.75, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2179,
    label = "S(4321) + H2O(46) <=> S(4325)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.446, 'cm^3/(mol*s)'),
        n = 3.131,
        Ea = (50.317, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2180,
    label = "OH(23) + S(3752) <=> S(4326)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.312e+08, 'cm^3/(mol*s)'),
        n = 1.015,
        Ea = (-1.75, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2181,
    label = "O(20) + S(15301) <=> S(16136)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2182,
    label = "CH3O(36) + S(16136) <=> S(16275)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2183,
    label = "S(16274) <=> CH3O(36) + S(16914)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=0.18, Ea=(8.367, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2184,
    label = "S(16275) <=> CH3O(36) + S(16914)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=0.18, Ea=(17.409, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2185,
    label = "S(16136) <=> S(16914)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2186,
    label = "H2O(46) + S(5687) <=> S(10135)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.145e+08, 'cm^3/(mol*s)'),
        n = 1.302,
        Ea = (62.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2187,
    label = "O2(2) + S(4326) <=> S(10135)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2188,
    label = "H(22) + S(1038) <=> C2H3O(18) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6.62, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2189,
    label = "C2H3O(18) + H(22) <=> S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2190,
    label = "O(20) + S(1038) <=> C2H3O(18) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2191,
    label = "C2H3O(18) + HO2(24) <=> O2(2) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2192,
    label = "HO2(24) + S(1038) <=> C2H3O(18) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2193,
    label = "CH(26) + S(1038) <=> C2H3O(18) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2194,
    label = "CH2(28) + S(1038) <=> C2H3O(18) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2195,
    label = "HCO(29) + S(1038) <=> C2H3O(18) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2196,
    label = "CH3(31) + S(1038) <=> C2H3O(18) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (6.62, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2197,
    label = "C2H3O(18) + CH2OH(35) <=> CH2O(32) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.061e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2198,
    label = "C2H3O(18) + CH3O(36) <=> CH2O(32) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2199,
    label = "CH2OH(35) + S(1038) <=> C2H3O(18) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2200,
    label = "CH3O(36) + S(1038) <=> C2H3O(18) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2201,
    label = "C2H(38) + S(1038) <=> C2H3O(18) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2202,
    label = "C2H3O(18) + C2H3(41) <=> C2H2(39) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2203,
    label = "HCCO(40) + S(1038) <=> C2H3O(18) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2204,
    label = "C2H3(41) + S(1038) <=> C2H3O(18) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2205,
    label = "C2H3O(18) + C2H5(44) <=> C2H4(43) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2206,
    label = "C2H5(44) + S(1038) <=> C2H3O(18) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2207,
    label = "OH(23) + S(1038) <=> C2H3O(18) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-0.25, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2208,
    label = "C2H3O(18) + HCCOH(48) <=> HCCO(40) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2209,
    label = "C2H3O(18) + S(1038) <=> C2H3O(18) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2210,
    label = "C2H3O(68) + S(1038) <=> C2H3O(18) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2211,
    label = "C3H7(95) + S(1038) <=> C2H3O(18) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2212,
    label = "C3H7(51) + S(1038) <=> C2H3O(18) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2213,
    label = "butR2(4) + S(1038) <=> butane(1) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2214,
    label = "butR1(3) + S(1038) <=> butane(1) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2215,
    label = "butR1(3) + C2H3O(18) <=> C4H8(96) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2216,
    label = "butR2(4) + C2H3O(18) <=> C4H8(143) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2217,
    label = "butR2(4) + C2H3O(18) <=> C4H8(96) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2218,
    label = "C2H3O(18) + C2H3O(18) <=> CH2CO(42) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2219,
    label = "C2H3O(18) + C3H7(51) <=> C3H6(144) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2220,
    label = "C4H9O2(8) + S(1038) <=> C2H3O(18) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2221,
    label = "butROO2(6) + S(1038) <=> C2H3O(18) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2222,
    label = "C3H5(1446) + S(1038) <=> C2H3O(18) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2223,
    label = "S(1038) + S(1125) <=> C2H3O(18) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2224,
    label = "C2H3O(18) + C3H7(95) <=> C3H6(144) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2225,
    label = "C2H3O(18) + C4H8(96) <=> C4H7(1663) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2226,
    label = "C2H5O2(90) + S(1038) <=> C2H3O(18) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2227,
    label = "C4H7(1663) + S(1038) <=> C2H3O(18) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2228,
    label = "C2H3O(18) + C2H5O(71) <=> CH3CHO(49) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2229,
    label = "CH3O2(75) + S(1038) <=> C2H3O(18) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2230,
    label = "C2H3O(18) + C3H5(1446) <=> C3H4(2124) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2231,
    label = "C2H3O(18) + C3H4(2124) <=> C3H3(2385) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.272, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2232,
    label = "C2H3O(18) + C4H7(1663) <=> S(1038) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2233,
    label = "S(1038) + C4H5(2849) <=> C2H3O(18) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2234,
    label = "S(2185) + S(1038) <=> C2H3O(18) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2235,
    label = "CHO3(74) + S(1038) <=> C2H3O(18) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2236,
    label = "C2H3O(18) + CHO2(57) <=> CO2(34) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2237,
    label = "C2H3O(18) + S(2128) <=> S(3752) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2238,
    label = "S(4319) + S(1038) <=> C2H3O(18) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2239,
    label = "C2H3O(18) + S(3752) <=> S(4321) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2240,
    label = "CH3(31) + S(1038) <=> S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2330, 'cm^3/(mol*s)'),
        n = 2.412,
        Ea = (7.374, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2241,
    label = "S(1038) + C3H6O(748) <=> C2H3O(18) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2242,
    label = "C2H3O(18) + S(4321) <=> S(1038) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2243,
    label = "S(1038) + S(6828) <=> C2H3O(18) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2244,
    label = "S(1448) + S(1038) <=> C2H3O(18) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2245,
    label = "C2H3O(18) + S(4319) <=> S(1038) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2246,
    label = "C2H3O(18) + S(4319) <=> S(1038) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2247,
    label = "S(1038) + S(5415) <=> C2H3O(18) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2248,
    label = "S(1038) + S(4886) <=> C2H3O(18) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2249,
    label = "C2H3O(18) + C2H3O(68) <=> CH2CO(42) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2250,
    label = "C2H3O(18) + S(1448) <=> S(2128) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2251,
    label = "C2H3O(18) + S(1448) <=> S(1038) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2252,
    label = "S(1038) + S(12113) <=> C2H3O(18) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2253,
    label = "S(1038) + S(14812) <=> C2H3O(18) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2254,
    label = "C2H3O(18) + S(5415) <=> S(1038) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2255,
    label = "C2H3O(18) + C3H6O(748) <=> C3H5O(17) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2256,
    label = "C2H3O(18) + S(1054) <=> S(3752) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2257,
    label = "HCO(29) + S(1038) <=> S(4325)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5452, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (5.987, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2258,
    label = "OH(23) + C2H3(41) <=> S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2259,
    label = "S(1038) <=> CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7040, 's^-1'), n=2.66, Ea=(48.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2260,
    label = "S(16136) <=> S(18396)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2261,
    label = "CH3O2(287) + C3H6(144) <=> C4H9O2(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2550, 'cm^3/(mol*s)'), n=2.562, Ea=(5.04, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2262,
    label = "C3H5O(17) + CH3O2(287) <=> C4H8O3(11)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2263,
    label = "CH3O2(75) <=> CH3O2(287)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.413e+09, 's^-1'), n=1.45, Ea=(42.27, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2264,
    label = "CH3O2(287) + CH3(31) <=> CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2265,
    label = "CH3O2(287) + H(22) <=> COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2266,
    label = "O(20) + COO(1544) <=> CH3O2(287) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.502e+07, 'cm^3/(mol*s)'),
        n = 2.017,
        Ea = (3.981, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2267,
    label = "H(22) + COO(1544) <=> CH3O2(287) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1353, 'cm^3/(mol*s)'), n=3.2, Ea=(3.49, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2268,
    label = "OH(23) + COO(1544) <=> CH3O2(287) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(24420, 'cm^3/(mol*s)'), n=2.8, Ea=(-0.42, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2269,
    label = "CH3O2(287) + H2O2(25) <=> HO2(24) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005918, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2270,
    label = "CH(26) + COO(1544) <=> CH3O2(287) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(300000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2271,
    label = "CH2(28) + COO(1544) <=> CH3O2(287) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.721e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2272,
    label = "CH3O2(287) + CH2O(32) <=> HCO(29) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18.36, 'cm^3/(mol*s)'), n=3.38, Ea=(9.04, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2273,
    label = "CH3(31) + COO(1544) <=> CH3O2(287) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000615, 'cm^3/(mol*s)'),
        n = 4.9,
        Ea = (6.72, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2274,
    label = "CH3O2(287) + CH3O(36) <=> CH2O(32) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2275,
    label = "CH3O2(287) + CH2OH(35) <=> CH2O(32) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2276,
    label = "CH3O2(287) + CHO2(57) <=> CO2(34) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2277,
    label = "CH3O2(287) + CH3OH(37) <=> CH2OH(35) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2278,
    label = "CH3O(36) + COO(1544) <=> CH3O2(287) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (938900, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (9.853, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2279,
    label = "C2H(38) + COO(1544) <=> CH3O2(287) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (360000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2280,
    label = "CH3O2(287) + C2H3(41) <=> C2H2(39) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2281,
    label = "CH3O2(287) + HCCOH(48) <=> HCCO(40) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2282,
    label = "HCCO(40) + COO(1544) <=> CH3O2(287) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01431, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.033, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2283,
    label = "C2H3(41) + COO(1544) <=> CH3O2(287) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00054, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2284,
    label = "CH3O2(287) + C2H3O(68) <=> CH2CO(42) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2285,
    label = "C2H3O(18) + CH3O2(287) <=> CH2CO(42) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2286,
    label = "CH3O2(287) + C2H5(44) <=> C2H4(43) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2287,
    label = "C2H5(44) + COO(1544) <=> CH3O2(287) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2288,
    label = "CH3O2(287) + C2H5O(71) <=> CH3CHO(49) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2289,
    label = "CH3O2(287) + HO2(24) <=> O2(2) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.49, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2290,
    label = "butR1(3) + COO(1544) <=> butane(1) + CH3O2(287)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2291,
    label = "butane(1) + CH3O2(287) <=> butR2(4) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120.8, 'cm^3/(mol*s)'),
        n = 2.95,
        Ea = (11.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2292,
    label = "CH3O2(287) + S(149) <=> butROO2(6) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2293,
    label = "C4H9O2(8) + COO(1544) <=> CH3O2(287) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2294,
    label = "CH3O2(287) + C3H6O(748) <=> C3H5O(17) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2295,
    label = "CH3O2(287) + CH3CHO(49) <=> C2H3O(18) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2296,
    label = "CH3O2(287) + S(1038) <=> C2H3O(18) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2297,
    label = "CH3O2(287) + CCOO(1350) <=> C2H5O2(90) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2298,
    label = "C3H7(51) + COO(1544) <=> CH3O2(287) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2299,
    label = "CH3O2(287) + C3H7(51) <=> C3H6(144) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2300,
    label = "CH3O2(287) + C3H7(95) <=> C3H6(144) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.734e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2301,
    label = "CH3O2(287) + COO(1544) <=> CH3O2(75) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2302,
    label = "CH3O2(287) + C3H8(50) <=> C3H7(95) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60.4, 'cm^3/(mol*s)'), n=2.95, Ea=(11.98, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2303,
    label = "butR1(3) + CH3O2(287) <=> C4H8(96) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2304,
    label = "butR2(4) + CH3O2(287) <=> C4H8(96) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2305,
    label = "butR2(4) + CH3O2(287) <=> C4H8(143) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2306,
    label = "CH3O2(287) + C3H6(144) <=> C3H5(1446) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2307,
    label = "CH3O2(287) + S(2134) <=> COO(1544) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2308,
    label = "CH3O2(287) + C3H5(1446) <=> COO(1544) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2309,
    label = "CH3O2(287) + C4H8(143) <=> C4H7(1663) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008866, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2310,
    label = "CH3O2(287) + C4H8(96) <=> C4H7(1663) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2311,
    label = "CH3O2(287) + S(2644) <=> CHO3(74) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2312,
    label = "CH3O2(287) + C4H7(1663) <=> COO(1544) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2313,
    label = "CH3O2(287) + C2H3(41) <=> S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2314,
    label = "CH3O2(287) + S(1448) <=> COO(1544) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2315,
    label = "COO(1544) + C4H5(2849) <=> CH3O2(287) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005592, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2316,
    label = "CH3O2(287) + S(1054) <=> S(3752) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2317,
    label = "CH3O2(287) + S(2128) <=> S(3752) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2318,
    label = "CH3O2(287) + S(4759) <=> COO(1544) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2319,
    label = "CH3O2(287) + S(3752) <=> S(4321) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2320,
    label = "CH3O2(287) + S(6731) <=> COO(1544) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2321,
    label = "CH3O2(287) + C3H4(2124) <=> C3H3(2385) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06082, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.183, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2322,
    label = "S(4319) + COO(1544) <=> CH3O2(287) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005592, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2323,
    label = "S(4319) + CH3O2(287) <=> COO(1544) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2324,
    label = "S(4321) + CH3O2(287) <=> S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2325,
    label = "COO(1544) + S(1125) <=> CH3O2(287) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2326,
    label = "S(4321) + CH3O2(287) <=> COO(1544) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2327,
    label = "S(4319) + CH3O2(287) <=> COO(1544) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2328,
    label = "CH3O2(287) + CH3CHO(49) <=> C2H3O(68) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2329,
    label = "CH3O2(287) + S(12093) <=> COO(1544) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2330,
    label = "COO(1544) + S(1448) <=> CH3O2(287) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (938900, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (9.852, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2331,
    label = "CH3O2(287) + S(6711) <=> S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (5.987, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2332,
    label = "COO(1544) + S(5415) <=> CH3O2(287) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005592, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2333,
    label = "COO(1544) + C3H6O(748) <=> CH3O2(287) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (938900, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (9.852, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2334,
    label = "CH3O2(287) + S(10030) <=> COO(1544) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2335,
    label = "CH3O2(287) + S(5415) <=> COO(1544) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2336,
    label = "CH3O2(287) + S(1448) <=> COO(1544) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2337,
    label = "OH(23) + CH2O(32) <=> CH3O2(287)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (33.191, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2338,
    label = "OH(23) + S(19508) <=> S(18396)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2339,
    label = "CO(27) + S(11385) <=> S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (59200, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2340,
    label = "H(22) + S(13512) <=> S(19508)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+07, 'cm^3/(mol*s)'),
        n = 2.16,
        Ea = (4.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2341,
    label = "O(20) + S(19508) <=> OH(23) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2342,
    label = "H(22) + S(19508) <=> H2(21) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2343,
    label = "OH(23) + S(19508) <=> H2O(46) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2344,
    label = "HO2(24) + S(19508) <=> H2O2(25) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2345,
    label = "CH(26) + S(19508) <=> CH2(28) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2346,
    label = "CH2(28) + S(19508) <=> CH3(31) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2347,
    label = "HCO(29) + S(19508) <=> CH2O(32) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2348,
    label = "CH3(31) + S(19508) <=> CH4(33) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2349,
    label = "CH2OH(35) + S(19508) <=> CH3OH(37) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2350,
    label = "CH3O(36) + S(19508) <=> CH3OH(37) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2351,
    label = "C2H(38) + S(19508) <=> C2H2(39) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.206e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2352,
    label = "HCCO(40) + S(19508) <=> HCCOH(48) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2353,
    label = "HCCO(40) + S(19508) <=> CH2CO(42) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2354,
    label = "C2H3(41) + S(19508) <=> C2H4(43) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2355,
    label = "C2H5(44) + S(19508) <=> C2H6(45) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2356,
    label = "O2(2) + S(19508) <=> HO2(24) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2357,
    label = "butR1(3) + S(19508) <=> butane(1) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2358,
    label = "butR2(4) + S(19508) <=> butane(1) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2359,
    label = "butROO2(6) + S(19508) <=> S(149) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2360,
    label = "C4H9O2(8) + S(19508) <=> S(149) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2361,
    label = "C2H3O(18) + S(19508) <=> CH3CHO(49) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2362,
    label = "C2H3O(18) + S(19508) <=> S(1038) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2363,
    label = "C2H5O2(90) + S(19508) <=> CCOO(1350) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2364,
    label = "C3H7(51) + S(19508) <=> C3H8(50) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2365,
    label = "CH3O2(75) + S(19508) <=> COO(1544) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2366,
    label = "C3H7(95) + S(19508) <=> C3H8(50) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2367,
    label = "C3H5(1446) + S(19508) <=> C3H6(144) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2368,
    label = "S(2185) + S(19508) <=> S(2134) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2369,
    label = "C4H7(1663) + S(19508) <=> C4H8(143) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2370,
    label = "C4H7(1663) + S(19508) <=> C4H8(96) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2371,
    label = "CHO3(74) + S(19508) <=> S(2644) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2372,
    label = "C4H5(2849) + S(19508) <=> C4H6(2483) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2373,
    label = "S(4886) + S(19508) <=> S(4759) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2374,
    label = "S(4321) + S(19508) <=> S(3752) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2375,
    label = "S(6828) + S(19508) <=> S(6731) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2376,
    label = "C3H3(2385) + S(19508) <=> C3H4(2124) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2377,
    label = "S(4319) + S(19508) <=> S(3752) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2378,
    label = "S(1125) + S(19508) <=> C4H9O(147) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2379,
    label = "C2H3O(68) + S(19508) <=> CH3CHO(49) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2380,
    label = "S(12113) + S(19508) <=> S(12093) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2381,
    label = "S(1448) + S(19508) <=> S(1450) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2382,
    label = "S(5415) + S(19508) <=> S(4759) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2383,
    label = "C3H6O(748) + S(19508) <=> S(1449) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2384,
    label = "S(14812) + S(19508) <=> S(10030) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2385,
    label = "CH3O2(287) + S(19508) <=> COO(1544) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2386,
    label = "CO(27) + S(10703) <=> S(12985)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (59200, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2387,
    label = "S(12985) <=> S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2388,
    label = "S(12985) <=> S(20269)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2389,
    label = "H(22) + S(10034) <=> S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2390,
    label = "O(20) + S(9960) <=> OH(23) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (145000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.88, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2391,
    label = "H(22) + S(9960) <=> H2(21) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5220, 'cm^3/(mol*s)'), n=3.04, Ea=(2.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2392,
    label = "OH(23) + S(9960) <=> H2O(46) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3610, 'cm^3/(mol*s)'),
        n = 2.89,
        Ea = (-2.291, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2393,
    label = "H2O2(25) + S(10034) <=> HO2(24) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.97, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2394,
    label = "CH(26) + S(9960) <=> CH2(28) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(200000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2395,
    label = "CH2(28) + S(9960) <=> CH3(31) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(7.47, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2396,
    label = "CH2O(32) + S(10034) <=> HCO(29) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+11, 'cm^3/(mol*s)'), n=0, Ea=(6.96, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2397,
    label = "CH3(31) + S(9960) <=> CH4(33) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00248, 'cm^3/(mol*s)'),
        n = 4.44,
        Ea = (4.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2398,
    label = "CH3O(36) + S(10034) <=> CH2O(32) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2399,
    label = "CH2OH(35) + S(10034) <=> CH2O(32) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2400,
    label = "CHO2(57) + S(10034) <=> CO2(34) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2401,
    label = "CH2OH(35) + S(9960) <=> CH3OH(37) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2402,
    label = "CH3O(36) + S(9960) <=> CH3OH(37) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2403,
    label = "C2H(38) + S(9960) <=> C2H2(39) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2404,
    label = "C2H3(41) + S(10034) <=> C2H2(39) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2405,
    label = "HCCOH(48) + S(10034) <=> HCCO(40) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2406,
    label = "HCCO(40) + S(9960) <=> CH2CO(42) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009794, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.869, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2407,
    label = "C2H3(41) + S(9960) <=> C2H4(43) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.052, 'cm^3/(mol*s)'), n=3.9, Ea=(0.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2408,
    label = "C2H3O(68) + S(10034) <=> CH2CO(42) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2409,
    label = "C2H3O(18) + S(10034) <=> CH2CO(42) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2410,
    label = "C2H5(44) + S(10034) <=> C2H4(43) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2411,
    label = "C2H5(44) + S(9960) <=> C2H6(45) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2412,
    label = "C2H5O(71) + S(10034) <=> CH3CHO(49) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2413,
    label = "HO2(24) + S(10034) <=> O2(2) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.529, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2414,
    label = "butR1(3) + S(9960) <=> butane(1) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2415,
    label = "butR2(4) + S(9960) <=> butane(1) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2416,
    label = "S(149) + S(10034) <=> butROO2(6) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2417,
    label = "C4H9O2(8) + S(9960) <=> S(149) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2418,
    label = "C3H6O(748) + S(10034) <=> C3H5O(17) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2419,
    label = "C2H3O(18) + S(9960) <=> CH3CHO(49) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2420,
    label = "S(1038) + S(10034) <=> C2H3O(18) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2421,
    label = "CCOO(1350) + S(10034) <=> C2H5O2(90) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2422,
    label = "C3H7(51) + S(9960) <=> C3H8(50) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2423,
    label = "C3H7(51) + S(10034) <=> C3H6(144) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2424,
    label = "C3H7(95) + S(10034) <=> C3H6(144) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.949e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2425,
    label = "COO(1544) + S(10034) <=> CH3O2(75) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2426,
    label = "C3H7(95) + S(9960) <=> C3H8(50) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2427,
    label = "butR1(3) + S(10034) <=> C4H8(96) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2428,
    label = "butR2(4) + S(10034) <=> C4H8(96) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2429,
    label = "butR2(4) + S(10034) <=> C4H8(143) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2430,
    label = "C3H6(144) + S(10034) <=> C3H5(1446) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.172e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2431,
    label = "S(2134) + S(10034) <=> S(2185) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2432,
    label = "C3H5(1446) + S(10034) <=> C3H4(2124) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2433,
    label = "C4H8(143) + S(10034) <=> C4H7(1663) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.345e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2434,
    label = "C4H8(96) + S(10034) <=> C4H7(1663) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002162, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2435,
    label = "CHO3(74) + S(9960) <=> S(2644) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2436,
    label = "C4H7(1663) + S(10034) <=> C4H6(2483) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2437,
    label = "S(1448) + S(10034) <=> S(2128) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2438,
    label = "C4H5(2849) + S(9960) <=> C4H6(2483) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2439,
    label = "S(1054) + S(10034) <=> S(3752) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2440,
    label = "S(2128) + S(10034) <=> S(3752) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2441,
    label = "S(4759) + S(10034) <=> S(4886) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2442,
    label = "S(3752) + S(10034) <=> S(4321) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2443,
    label = "S(6828) + S(9960) <=> S(6731) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2444,
    label = "C3H4(2124) + S(10034) <=> C3H3(2385) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06264, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.353, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2445,
    label = "S(4319) + S(9960) <=> S(3752) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2446,
    label = "S(4319) + S(10034) <=> S(9960) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2447,
    label = "S(1125) + S(9960) <=> C4H9O(147) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2448,
    label = "S(4321) + S(10034) <=> S(6711) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2449,
    label = "S(4319) + S(10034) <=> S(6711) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2450,
    label = "CH3CHO(49) + S(10034) <=> C2H3O(68) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2451,
    label = "S(9960) + S(12113) <=> S(10034) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2452,
    label = "S(1448) + S(9960) <=> S(1450) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2453,
    label = "S(5415) + S(9960) <=> S(4759) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2454,
    label = "C3H6O(748) + S(9960) <=> S(1449) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2455,
    label = "CH2(S)(30) + S(14812) <=> S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.302e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2456,
    label = "S(9960) + S(14812) <=> S(10030) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002162, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2457,
    label = "S(5415) + S(10034) <=> S(9960) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2458,
    label = "S(1448) + S(10034) <=> S(1054) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2459,
    label = "CH3O2(287) + S(9960) <=> COO(1544) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2460,
    label = "S(10034) + S(19508) <=> S(9960) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2461,
    label = "CH3(31) + S(3752) <=> S(4338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17720, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (3.057, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2462,
    label = "S(4338) + H(22) <=> S(1667)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (7.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2463,
    label = "S(1667) + O(20) <=> S(4338) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.135e+10, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2464,
    label = "S(1667) + H(22) <=> S(4338) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.257e+11, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (0.023, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2465,
    label = "S(1667) + OH(23) <=> S(4338) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2466,
    label = "S(1667) + HO2(24) <=> S(4338) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2467,
    label = "S(1667) + CH(26) <=> S(4338) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.183e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2468,
    label = "S(1667) + CH2(28) <=> S(4338) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.616e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2469,
    label = "S(1667) + HCO(29) <=> S(4338) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2470,
    label = "S(1667) + CH3(31) <=> S(4338) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2471,
    label = "S(1667) + CH2OH(35) <=> S(4338) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2472,
    label = "S(1667) + CH3O(36) <=> S(4338) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2473,
    label = "S(1667) + C2H(38) <=> S(4338) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.319e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2474,
    label = "S(1667) + HCCO(40) <=> S(4338) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2475,
    label = "S(1667) + HCCO(40) <=> S(4338) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2476,
    label = "S(1667) + C2H3(41) <=> S(4338) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2477,
    label = "S(1667) + C2H5(44) <=> S(4338) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2478,
    label = "O2(2) + S(1667) <=> S(4338) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.824e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.908, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2479,
    label = "butR1(3) + S(1667) <=> butane(1) + S(4338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2480,
    label = "butR2(4) + S(1667) <=> butane(1) + S(4338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2481,
    label = "butROO2(6) + S(1667) <=> S(4338) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2482,
    label = "C4H9O2(8) + S(1667) <=> S(4338) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2483,
    label = "C2H3O(18) + S(1667) <=> S(4338) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2484,
    label = "C2H3O(18) + S(1667) <=> S(4338) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2485,
    label = "S(1667) + C2H5O2(90) <=> S(4338) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2486,
    label = "C3H7(51) + S(1667) <=> S(4338) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2487,
    label = "S(1667) + CH3O2(75) <=> S(4338) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2488,
    label = "S(1667) + C3H7(95) <=> S(4338) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2489,
    label = "S(1667) + C3H5(1446) <=> S(4338) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2490,
    label = "S(1667) + S(2185) <=> S(4338) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2491,
    label = "C4H7(1663) + S(1667) <=> S(4338) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2492,
    label = "C4H7(1663) + S(1667) <=> S(4338) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2493,
    label = "S(1667) + CHO3(74) <=> S(4338) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2494,
    label = "S(1667) + C4H5(2849) <=> S(4338) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2495,
    label = "S(1667) + S(4886) <=> S(4338) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2496,
    label = "S(4321) + S(1667) <=> S(4338) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2497,
    label = "S(1667) + S(6828) <=> S(4338) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2498,
    label = "S(1667) + C3H3(2385) <=> S(4338) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2499,
    label = "S(4319) + S(1667) <=> S(4338) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2500,
    label = "S(1667) + S(1125) <=> S(4338) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2501,
    label = "C2H3O(68) + S(1667) <=> S(4338) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2502,
    label = "S(1667) + S(12113) <=> S(4338) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2503,
    label = "S(1667) + S(1448) <=> S(4338) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2504,
    label = "S(1667) + S(5415) <=> S(4338) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2505,
    label = "S(1667) + C3H6O(748) <=> S(4338) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2506,
    label = "S(1667) + S(14812) <=> S(4338) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2507,
    label = "CH2(S)(30) + S(1054) <=> S(4338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.055e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2508,
    label = "CH3O2(287) + S(1667) <=> S(4338) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2509,
    label = "S(4338) <=> S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 's^-1'), n=0.19, Ea=(26.314, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2510,
    label = "S(1667) + S(10034) <=> S(4338) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2511,
    label = "CH2(S)(30) + S(1352) <=> S(16944)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.302e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2512,
    label = "O2(2) + S(4338) <=> S(16944)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2513,
    label = "S(471) + H(22) <=> C4H8O3(11)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2514,
    label = "C4H8O3(11) + O(20) <=> S(471) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2515,
    label = "C4H8O3(11) + H(22) <=> S(471) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2516,
    label = "C4H8O3(11) + OH(23) <=> S(471) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2517,
    label = "S(471) + H2O2(25) <=> C4H8O3(11) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2518,
    label = "C4H8O3(11) + CH(26) <=> S(471) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2519,
    label = "C4H8O3(11) + CH2(28) <=> S(471) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2520,
    label = "S(471) + CH2O(32) <=> C4H8O3(11) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2521,
    label = "C4H8O3(11) + CH3(31) <=> S(471) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2522,
    label = "C4H8O3(11) + CH2OH(35) <=> S(471) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2523,
    label = "C4H8O3(11) + CH3O(36) <=> S(471) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2524,
    label = "C4H8O3(11) + C2H(38) <=> S(471) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2525,
    label = "S(471) + HCCOH(48) <=> C4H8O3(11) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2526,
    label = "C4H8O3(11) + HCCO(40) <=> S(471) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2527,
    label = "C4H8O3(11) + C2H3(41) <=> S(471) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2528,
    label = "C4H8O3(11) + C2H5(44) <=> S(471) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2529,
    label = "S(471) + HO2(24) <=> O2(2) + C4H8O3(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2530,
    label = "butR1(3) + C4H8O3(11) <=> butane(1) + S(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2531,
    label = "butR2(4) + C4H8O3(11) <=> butane(1) + S(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2532,
    label = "S(149) + S(471) <=> butROO2(6) + C4H8O3(11)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2533,
    label = "C4H9O2(8) + C4H8O3(11) <=> S(149) + S(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2534,
    label = "C4H7O2(16) + O(20) <=> S(471)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2535,
    label = "C4H8O3(11) + C2H3O(18) <=> S(471) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2536,
    label = "S(471) + S(1038) <=> C4H8O3(11) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2537,
    label = "S(471) + CCOO(1350) <=> C4H8O3(11) + C2H5O2(90)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2538,
    label = "C4H8O3(11) + C3H7(51) <=> S(471) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2539,
    label = "S(471) + COO(1544) <=> C4H8O3(11) + CH3O2(75)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2540,
    label = "C4H8O3(11) + C3H7(95) <=> S(471) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2541,
    label = "C4H8O3(11) + C3H5(1446) <=> C3H6(144) + S(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2542,
    label = "S(471) + S(2134) <=> C4H8O3(11) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2543,
    label = "C4H8O3(11) + C4H7(1663) <=> C4H8(143) + S(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2544,
    label = "S(471) + C4H8(96) <=> C4H8O3(11) + C4H7(1663)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2545,
    label = "C4H8O3(11) + CHO3(74) <=> S(471) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2546,
    label = "C4H8O3(11) + C4H5(2849) <=> S(471) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2547,
    label = "S(471) + S(4759) <=> C4H8O3(11) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2548,
    label = "S(471) + S(3752) <=> C4H8O3(11) + S(4321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2549,
    label = "C4H8O3(11) + S(6828) <=> S(471) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2550,
    label = "S(471) + C3H4(2124) <=> C4H8O3(11) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.125, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2551,
    label = "C4H8O3(11) + S(4319) <=> S(471) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2552,
    label = "C4H8O3(11) + S(1125) <=> C4H9O(147) + S(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2553,
    label = "C4H8O3(11) + C2H3O(68) <=> S(471) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0009569, 'cm^3/(mol*s)'),
        n = 4.45,
        Ea = (0.54, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2554,
    label = "C4H8O3(11) + S(12113) <=> S(471) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2555,
    label = "C4H8O3(11) + S(1448) <=> S(471) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2556,
    label = "C4H8O3(11) + S(5415) <=> S(471) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2557,
    label = "C4H8O3(11) + C3H6O(748) <=> S(471) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2558,
    label = "C4H8O3(11) + S(14812) <=> S(471) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2559,
    label = "C4H8O3(11) + CH3O2(287) <=> S(471) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2560,
    label = "C4H8O3(11) + S(10034) <=> S(471) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2561,
    label = "S(471) + CH2OH(35) <=> C4H8O3(11) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2562,
    label = "S(471) + CH3O(36) <=> C4H8O3(11) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2563,
    label = "S(471) + C2H3(41) <=> C4H8O3(11) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2564,
    label = "S(471) + C2H5(44) <=> C4H8O3(11) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2565,
    label = "butR1(3) + S(471) <=> C4H8O3(11) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2566,
    label = "butR2(4) + S(471) <=> C4H8O3(11) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2567,
    label = "butR2(4) + S(471) <=> C4H8O3(11) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2568,
    label = "C2H3O(18) + S(471) <=> C4H8O3(11) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2569,
    label = "C3H7(51) + S(471) <=> C4H8O3(11) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2570,
    label = "C3H7(95) + S(471) <=> C4H8O3(11) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2571,
    label = "C2H5O(71) + S(471) <=> C4H8O3(11) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2572,
    label = "S(471) + C3H5(1446) <=> C4H8O3(11) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2573,
    label = "C4H7(1663) + S(471) <=> C4H8O3(11) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2574,
    label = "CHO2(57) + S(471) <=> C4H8O3(11) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2575,
    label = "S(471) + S(2128) <=> C4H8O3(11) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2576,
    label = "S(4321) + S(471) <=> C4H8O3(11) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2577,
    label = "S(4319) + S(471) <=> C4H8O3(11) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2578,
    label = "S(4319) + S(471) <=> C4H8O3(11) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2579,
    label = "S(1667) + S(471) <=> C4H8O3(11) + S(4338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2580,
    label = "C2H3O(68) + S(471) <=> C4H8O3(11) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2581,
    label = "S(471) + S(1448) <=> C4H8O3(11) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2582,
    label = "S(471) + S(1448) <=> C4H8O3(11) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2583,
    label = "S(471) + S(5415) <=> C4H8O3(11) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2584,
    label = "S(471) + C3H6O(748) <=> C4H8O3(11) + C3H5O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2585,
    label = "S(471) + S(1054) <=> C4H8O3(11) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2586,
    label = "S(471) + S(19508) <=> C4H8O3(11) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2587,
    label = "S(471) <=> S(21159)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.004e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2588,
    label = "CH3(31) + S(21257) <=> S(21159)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(13.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2589,
    label = "S(21334) <=> S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2590,
    label = "C2H3O(68) + C2H4O(832) <=> C4H7O2(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+14, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2591,
    label = "H(22) + C2H4O(832) <=> C2H3O(18) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.257e+11, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (0.023, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2592,
    label = "C2H3O(18) + H(22) <=> C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2593,
    label = "O2(2) + C2H4O(832) <=> C2H3O(18) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.824e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.908, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2594,
    label = "CH(26) + C2H4O(832) <=> C2H3O(18) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.183e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2595,
    label = "CH2(28) + C2H4O(832) <=> C2H3O(18) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.616e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2596,
    label = "HCO(29) + C2H4O(832) <=> C2H3O(18) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2597,
    label = "CH3(31) + C2H4O(832) <=> C2H3O(18) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2598,
    label = "CH2OH(35) + C2H4O(832) <=> C2H3O(18) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2599,
    label = "HCCO(40) + C2H4O(832) <=> C2H3O(18) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2600,
    label = "C2H3(41) + C2H4O(832) <=> C2H3O(18) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2601,
    label = "C2H5(44) + C2H4O(832) <=> C2H3O(18) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2602,
    label = "C2H3O(18) + C2H4O(832) <=> C2H3O(18) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2603,
    label = "C3H7(95) + C2H4O(832) <=> C2H3O(18) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2604,
    label = "C3H7(51) + C2H4O(832) <=> C2H3O(18) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2605,
    label = "butR2(4) + C2H4O(832) <=> butane(1) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2606,
    label = "butR1(3) + C2H4O(832) <=> butane(1) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2607,
    label = "C4H9O2(8) + C2H4O(832) <=> C2H3O(18) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2608,
    label = "C3H5(1446) + C2H4O(832) <=> C2H3O(18) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2609,
    label = "C2H4O(832) + S(1125) <=> C2H3O(18) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2610,
    label = "C4H7(1663) + C2H4O(832) <=> C2H3O(18) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2611,
    label = "C4H7(1663) + C2H4O(832) <=> C2H3O(18) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2612,
    label = "H(22) + C2H4O(832) <=> C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2613,
    label = "C2H5O(71) + O(20) <=> OH(23) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2850, 'cm^3/(mol*s)'), n=3.05, Ea=(3.123, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2614,
    label = "C2H5O(71) + H(22) <=> H2(21) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3090, 'cm^3/(mol*s)'), n=3.24, Ea=(7.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2615,
    label = "C2H5O(71) + OH(23) <=> H2O(46) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.431e+09, 'cm^3/(mol*s)'),
        n = 1.152,
        Ea = (2.68, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2616,
    label = "C2H5O(71) + HO2(24) <=> H2O2(25) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20.435, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2617,
    label = "C2H5O(71) + CH(26) <=> CH2(28) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(300000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2618,
    label = "C2H5O(71) + CH2(28) <=> CH3(31) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.721e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2619,
    label = "CH2O(32) + C2H4O(832) <=> C2H5O(71) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2620,
    label = "C2H5O(71) + CH3(31) <=> CH4(33) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.244e-05, 'cm^3/(mol*s)'),
        n = 4.99,
        Ea = (8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2621,
    label = "CH3O(36) + C2H4O(832) <=> C2H5O(71) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2622,
    label = "CH2OH(35) + C2H4O(832) <=> C2H5O(71) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2623,
    label = "CHO2(57) + C2H4O(832) <=> C2H5O(71) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2624,
    label = "CH3OH(37) + C2H4O(832) <=> C2H5O(71) + CH2OH(35)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2625,
    label = "CH3OH(37) + C2H4O(832) <=> C2H5O(71) + CH3O(36)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2626,
    label = "C2H5O(71) + C2H(38) <=> C2H2(39) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.806e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2627,
    label = "C2H3(41) + C2H4O(832) <=> C2H5O(71) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2628,
    label = "HCCOH(48) + C2H4O(832) <=> C2H5O(71) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2629,
    label = "C2H5O(71) + HCCO(40) <=> CH2CO(42) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0495, 'cm^3/(mol*s)'), n=4.34, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2630,
    label = "C2H5O(71) + C2H3(41) <=> C2H4(43) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00054, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2631,
    label = "C2H3O(68) + C2H4O(832) <=> C2H5O(71) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2632,
    label = "C2H3O(18) + C2H4O(832) <=> C2H5O(71) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2633,
    label = "C2H5(44) + C2H4O(832) <=> C2H5O(71) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2634,
    label = "C2H6(45) + C2H4O(832) <=> C2H5O(71) + C2H5(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00552, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2635,
    label = "C2H5O(71) + C2H4O(832) <=> C2H5O(71) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2636,
    label = "O2(2) + C2H5O(71) <=> HO2(24) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (51.997, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2637,
    label = "butR1(3) + C2H5O(71) <=> butane(1) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00276, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2638,
    label = "butane(1) + C2H4O(832) <=> butR2(4) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00368, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2639,
    label = "S(149) + C2H4O(832) <=> butROO2(6) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2640,
    label = "S(149) + C2H4O(832) <=> C4H9O2(8) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00276, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2641,
    label = "C2H4O(832) + C3H6O(748) <=> C3H5O(17) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2642,
    label = "C2H4O(832) + C2H4O(832) <=> C2H3O(18) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2643,
    label = "CH3CHO(49) + C2H4O(832) <=> C2H3O(18) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.037e-05, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2644,
    label = "C2H4O(832) + S(1038) <=> C2H3O(18) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2645,
    label = "C2H4O(832) + CCOO(1350) <=> C2H5O(71) + C2H5O2(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2646,
    label = "C3H7(51) + C2H5O(71) <=> C3H8(50) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00276, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2647,
    label = "C3H7(51) + C2H4O(832) <=> C2H5O(71) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2648,
    label = "C3H7(95) + C2H4O(832) <=> C2H5O(71) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2649,
    label = "C2H4O(832) + COO(1544) <=> C2H5O(71) + CH3O2(75)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2650,
    label = "C3H8(50) + C2H4O(832) <=> C2H5O(71) + C3H7(95)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00184, 'cm^3/(mol*s)'), n=4.34, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2651,
    label = "butR1(3) + C2H4O(832) <=> C2H5O(71) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2652,
    label = "butR2(4) + C2H4O(832) <=> C2H5O(71) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2653,
    label = "butR2(4) + C2H4O(832) <=> C2H5O(71) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2654,
    label = "CH3O2(287) + C2H4O(832) <=> C2H3O(18) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2655,
    label = "C3H6(144) + C2H4O(832) <=> C2H5O(71) + C3H5(1446)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00087, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2656,
    label = "C2H4O(832) + S(2134) <=> C2H5O(71) + S(2185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2657,
    label = "C3H3(2385) + C2H4O(832) <=> C2H3O(18) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2658,
    label = "C3H5(1446) + C2H4O(832) <=> C2H5O(71) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2659,
    label = "C4H8(143) + C2H4O(832) <=> C2H5O(71) + C4H7(1663)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00174, 'cm^3/(mol*s)'), n=4.34, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2660,
    label = "C2H5O(71) + C4H7(1663) <=> C4H8(96) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.027, 'cm^3/(mol*s)'), n=4.34, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2661,
    label = "S(2644) + C2H4O(832) <=> C2H5O(71) + CHO3(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2662,
    label = "C4H7(1663) + C2H4O(832) <=> C2H5O(71) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2663,
    label = "C2H4O(832) + S(1448) <=> C2H5O(71) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2664,
    label = "C2H4O(832) + C4H6(2483) <=> C2H5O(71) + C4H5(2849)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00296, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2665,
    label = "C2H4O(832) + S(1054) <=> C2H5O(71) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=-0.35, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2666,
    label = "C2H4O(832) + S(2128) <=> C2H5O(71) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2667,
    label = "C2H4O(832) + S(4759) <=> C2H5O(71) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2668,
    label = "S(3752) + C2H4O(832) <=> S(4321) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2669,
    label = "C2H4O(832) + S(6731) <=> C2H5O(71) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2670,
    label = "C2H4O(832) + C3H4(2124) <=> C2H5O(71) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0218, 'cm^3/(mol*s)'), n=4.34, Ea=(5.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2671,
    label = "S(3752) + C2H4O(832) <=> S(4319) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2672,
    label = "C2H4O(832) + S(10034) <=> C2H3O(18) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2673,
    label = "S(4319) + C2H4O(832) <=> C2H5O(71) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2674,
    label = "C2H5O(71) + S(1125) <=> C4H9O(147) + C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00276, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2675,
    label = "S(4321) + C2H4O(832) <=> C2H5O(71) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2676,
    label = "S(4319) + C2H4O(832) <=> C2H5O(71) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2677,
    label = "CH3CHO(49) + C2H4O(832) <=> C2H3O(68) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2678,
    label = "C2H4O(832) + S(12093) <=> C2H5O(71) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7985, 'cm^3/(mol*s)'),
        n = 3.338,
        Ea = (1.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2679,
    label = "C2H4O(832) + S(1450) <=> C2H5O(71) + S(1448)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2680,
    label = "C2H4O(832) + S(14812) <=> C2H3O(18) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2681,
    label = "C2H4O(832) + S(4759) <=> C2H5O(71) + S(5415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2682,
    label = "CH2(S)(30) + C2H4O(832) <=> C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.703e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2683,
    label = "C2H4O(832) + S(1449) <=> C2H5O(71) + C3H6O(748)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(8.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2684,
    label = "C2H4O(832) + S(10030) <=> C2H5O(71) + S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2685,
    label = "C2H4O(832) + S(5415) <=> C2H5O(71) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2686,
    label = "C2H4O(832) + S(1448) <=> C2H5O(71) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2687,
    label = "C2H4O(832) + COO(1544) <=> CH3O2(287) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2688,
    label = "C2H4O(832) + S(19508) <=> C2H5O(71) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2689,
    label = "C2H4O(832) + S(9960) <=> C2H5O(71) + S(10034)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2690,
    label = "S(1667) + C2H4O(832) <=> S(4338) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2691,
    label = "C4H8O3(11) + C2H4O(832) <=> C2H5O(71) + S(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2692,
    label = "CO2(34) + C2H4O(832) <=> S(21334)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (9.531, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2693,
    label = "O(20) + C2H4(43) <=> C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.84e+07, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (-0.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2694,
    label = "CH2(28) + CH2O(32) <=> C2H4O(832)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.343e+07, 'cm^3/(mol*s)'),
        n = 1.603,
        Ea = (-1.375, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2695,
    label = "O(20) + C2H4O(832) <=> C2H3O(18) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.135e+10, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2696,
    label = "OH(23) + C2H4O(832) <=> C2H3O(18) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2697,
    label = "HO2(24) + C2H4O(832) <=> C2H3O(18) + H2O2(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2698,
    label = "CH3O(36) + C2H4O(832) <=> C2H3O(18) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2699,
    label = "C2H(38) + C2H4O(832) <=> C2H3O(18) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.319e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2700,
    label = "HCCO(40) + C2H4O(832) <=> C2H3O(18) + HCCOH(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2701,
    label = "butROO2(6) + C2H4O(832) <=> C2H3O(18) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2702,
    label = "C2H3O(18) + C2H4O(832) <=> C2H3O(18) + S(1038)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2703,
    label = "C2H5O2(90) + C2H4O(832) <=> C2H3O(18) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2704,
    label = "CH3O2(75) + C2H4O(832) <=> C2H3O(18) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2705,
    label = "C2H4O(832) + S(2185) <=> C2H3O(18) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2706,
    label = "CHO3(74) + C2H4O(832) <=> C2H3O(18) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2707,
    label = "C2H4O(832) + C4H5(2849) <=> C2H3O(18) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2708,
    label = "C2H4O(832) + S(4886) <=> C2H3O(18) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2709,
    label = "S(4321) + C2H4O(832) <=> C2H3O(18) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2710,
    label = "C2H4O(832) + S(6828) <=> C2H3O(18) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2711,
    label = "S(4319) + C2H4O(832) <=> C2H3O(18) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2712,
    label = "C2H3O(68) + C2H4O(832) <=> C2H3O(18) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2713,
    label = "C2H4O(832) + S(12113) <=> C2H3O(18) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2714,
    label = "C2H4O(832) + S(1448) <=> C2H3O(18) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2715,
    label = "C2H4O(832) + S(5415) <=> C2H3O(18) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2716,
    label = "C2H4O(832) + C3H6O(748) <=> C2H3O(18) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2717,
    label = "S(471) + C2H4O(832) <=> C4H8O3(11) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2718,
    label = "CH2(S)(30) + S(14811) <=> S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.023e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2719,
    label = "C2H4O(832) <=> S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2720,
    label = "CH2(S)(30) + CH2O(32) <=> S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.981e+14, 'cm^3/(mol*s)'),
        n = -0.467,
        Ea = (-0.022, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2721,
    label = "S(22205) <=> S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2722,
    label = "CH2(28) + CH2O(32) <=> S(22205)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2723,
    label = "C2H3O(18) <=> S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 's^-1'), n=0.19, Ea=(25.026, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2724,
    label = "C2H5(44) + S(1035) <=> S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.79e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2725,
    label = "CH3(31) + S(1035) <=> S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.8e+14, 'cm^3/(mol*s)'), n=-0.68, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2726,
    label = "CH2(S)(30) + S(1035) <=> S(14812)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.703e+10, 'cm^3/(mol*s)'),
        n = 0.699,
        Ea = (-1.584, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2727,
    label = "H(22) + S(1035) <=> S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2728,
    label = "O(20) + S(14811) <=> OH(23) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (290000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.88, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2729,
    label = "H(22) + S(14811) <=> H2(21) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10440, 'cm^3/(mol*s)'), n=3.04, Ea=(2.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2730,
    label = "OH(23) + S(14811) <=> H2O(46) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7220, 'cm^3/(mol*s)'),
        n = 2.89,
        Ea = (-2.291, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2731,
    label = "H2O2(25) + S(1035) <=> HO2(24) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.97, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2732,
    label = "CH(26) + S(14811) <=> CH2(28) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2733,
    label = "CH2(28) + S(14811) <=> CH3(31) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02, 'cm^3/(mol*s)'), n=3.46, Ea=(7.47, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2734,
    label = "CH2O(32) + S(1035) <=> HCO(29) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+11, 'cm^3/(mol*s)'), n=0, Ea=(6.96, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2735,
    label = "CH3(31) + S(14811) <=> CH4(33) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00496, 'cm^3/(mol*s)'),
        n = 4.44,
        Ea = (4.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2736,
    label = "CH3O(36) + S(1035) <=> CH2O(32) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2737,
    label = "CH2OH(35) + S(1035) <=> CH2O(32) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2738,
    label = "CHO2(57) + S(1035) <=> CO2(34) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2739,
    label = "CH2OH(35) + S(14811) <=> CH3OH(37) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009938, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2740,
    label = "CH3O(36) + S(14811) <=> CH3OH(37) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.757e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2741,
    label = "C2H(38) + S(14811) <=> C2H2(39) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2742,
    label = "C2H3(41) + S(1035) <=> C2H2(39) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2743,
    label = "HCCOH(48) + S(1035) <=> HCCO(40) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2744,
    label = "HCCO(40) + S(14811) <=> CH2CO(42) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01959, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.869, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2745,
    label = "C2H3(41) + S(14811) <=> C2H4(43) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.104, 'cm^3/(mol*s)'), n=3.9, Ea=(0.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2746,
    label = "C2H3O(68) + S(1035) <=> CH2CO(42) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2747,
    label = "C2H3O(18) + S(1035) <=> CH2CO(42) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2748,
    label = "C2H5(44) + S(1035) <=> C2H4(43) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2749,
    label = "C2H5(44) + S(14811) <=> C2H6(45) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e-05, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2750,
    label = "C2H5O(71) + S(1035) <=> CH3CHO(49) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2751,
    label = "HO2(24) + S(1035) <=> O2(2) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.529, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2752,
    label = "butR1(3) + S(14811) <=> butane(1) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e-05, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2753,
    label = "butR2(4) + S(14811) <=> butane(1) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2754,
    label = "S(149) + S(1035) <=> butROO2(6) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2755,
    label = "C4H9O2(8) + S(14811) <=> S(149) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e-05, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2756,
    label = "S(1035) + C3H6O(748) <=> C3H5O(17) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2757,
    label = "C2H4O(832) + S(1035) <=> C2H3O(18) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2758,
    label = "C2H3O(18) + S(14811) <=> CH3CHO(49) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009938, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2759,
    label = "S(1035) + S(1038) <=> C2H3O(18) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2760,
    label = "S(1035) + CCOO(1350) <=> C2H5O2(90) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2761,
    label = "C3H7(51) + S(14811) <=> C3H8(50) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e-05, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2762,
    label = "C3H7(51) + S(1035) <=> C3H6(144) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2763,
    label = "C3H7(95) + S(1035) <=> C3H6(144) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.949e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2764,
    label = "COO(1544) + S(1035) <=> CH3O2(75) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2765,
    label = "C3H7(95) + S(14811) <=> C3H8(50) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2766,
    label = "butR1(3) + S(1035) <=> C4H8(96) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2767,
    label = "butR2(4) + S(1035) <=> C4H8(96) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2768,
    label = "butR2(4) + S(1035) <=> C4H8(143) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2769,
    label = "C3H6(144) + S(1035) <=> C3H5(1446) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.172e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2770,
    label = "S(1035) + S(2134) <=> S(2185) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2771,
    label = "C3H5(1446) + S(1035) <=> C3H4(2124) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2772,
    label = "C4H8(143) + S(1035) <=> C4H7(1663) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.345e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2773,
    label = "C4H8(96) + S(1035) <=> C4H7(1663) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002162, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2774,
    label = "CHO3(74) + S(14811) <=> S(2644) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.757e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2775,
    label = "C4H7(1663) + S(1035) <=> C4H6(2483) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2776,
    label = "S(1448) + S(1035) <=> S(2128) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2777,
    label = "C4H5(2849) + S(14811) <=> S(1035) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01165, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2778,
    label = "S(1035) + S(1054) <=> S(3752) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2779,
    label = "S(2128) + S(1035) <=> S(3752) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2780,
    label = "S(1035) + S(4759) <=> S(4886) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2781,
    label = "S(3752) + S(1035) <=> S(4321) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2782,
    label = "S(6828) + S(14811) <=> S(1035) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.757e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2783,
    label = "C3H4(2124) + S(1035) <=> C3H3(2385) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06264, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.353, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2784,
    label = "S(4319) + S(14811) <=> S(3752) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01165, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2785,
    label = "S(4319) + S(1035) <=> S(9511) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2786,
    label = "S(1125) + S(14811) <=> C4H9O(147) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e-05, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2787,
    label = "S(4321) + S(1035) <=> S(6711) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2788,
    label = "S(4319) + S(1035) <=> S(6711) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2789,
    label = "CH3CHO(49) + S(1035) <=> C2H3O(68) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2790,
    label = "S(12113) + S(14811) <=> S(1035) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.757e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2791,
    label = "S(1448) + S(14811) <=> S(1450) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.757e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2792,
    label = "S(5415) + S(14811) <=> S(1035) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01165, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2793,
    label = "C3H6O(748) + S(14811) <=> S(1449) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.757e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2794,
    label = "S(14811) + S(14812) <=> S(1035) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004324, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2795,
    label = "S(1035) + S(5415) <=> S(15301) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2796,
    label = "S(1448) + S(1035) <=> S(1054) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2797,
    label = "CH3O2(287) + S(14811) <=> COO(1544) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009938, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2798,
    label = "S(1035) + S(19508) <=> S(13512) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2799,
    label = "S(1035) + S(9960) <=> S(10034) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002162, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2800,
    label = "S(1667) + S(1035) <=> S(4338) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2801,
    label = "C4H8O3(11) + S(1035) <=> S(471) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2802,
    label = "C2H4O(832) + S(14811) <=> C2H5O(71) + S(1035)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e-05, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2803,
    label = "H(22) + S(654) <=> C4H8O3(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2804,
    label = "C4H8O3(14) + O(20) <=> OH(23) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2805,
    label = "C4H8O3(14) + H(22) <=> H2(21) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248800, 'cm^3/(mol*s)'),
        n = 2.388,
        Ea = (5.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2806,
    label = "C4H8O3(14) + OH(23) <=> H2O(46) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29210, 'cm^3/(mol*s)'),
        n = 2.467,
        Ea = (-0.722, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2807,
    label = "H2O2(25) + S(654) <=> C4H8O3(14) + HO2(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.184, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2808,
    label = "C4H8O3(14) + CH(26) <=> CH2(28) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2809,
    label = "C4H8O3(14) + CH2(28) <=> CH3(31) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2810,
    label = "CH2O(32) + S(654) <=> C4H8O3(14) + HCO(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41200, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2811,
    label = "C4H8O3(14) + CH3(31) <=> CH4(33) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (627.7, 'cm^3/(mol*s)'),
        n = 2.813,
        Ea = (5.777, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2812,
    label = "C4H8O3(14) + CH2OH(35) <=> CH3OH(37) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2813,
    label = "C4H8O3(14) + CH3O(36) <=> CH3OH(37) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2814,
    label = "C4H8O3(14) + C2H(38) <=> C2H2(39) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2815,
    label = "HCCOH(48) + S(654) <=> C4H8O3(14) + HCCO(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2816,
    label = "C4H8O3(14) + HCCO(40) <=> CH2CO(42) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.731, 'cm^3/(mol*s)'),
        n = 3.337,
        Ea = (1.117, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2817,
    label = "C4H8O3(14) + C2H3(41) <=> C2H4(43) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1, 'cm^3/(mol*s)'), n=3.52, Ea=(-7.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2818,
    label = "C4H8O3(14) + C2H5(44) <=> C2H6(45) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2819,
    label = "HO2(24) + S(654) <=> O2(2) + C4H8O3(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2820,
    label = "butR1(3) + C4H8O3(14) <=> butane(1) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2821,
    label = "butR2(4) + C4H8O3(14) <=> butane(1) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2822,
    label = "butROO2(6) + C4H8O3(14) <=> S(149) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2823,
    label = "C4H9O2(8) + C4H8O3(14) <=> S(149) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2824,
    label = "C4H7O2(15) + O(20) <=> S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2825,
    label = "C4H8O3(14) + C2H3O(18) <=> CH3CHO(49) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2826,
    label = "S(654) + S(1038) <=> C4H8O3(14) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2827,
    label = "C4H8O3(14) + C2H5O2(90) <=> S(654) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2828,
    label = "C4H8O3(14) + C3H7(51) <=> C3H8(50) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2829,
    label = "C4H8O3(14) + CH3O2(75) <=> S(654) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2830,
    label = "C4H8O3(14) + C3H7(95) <=> C3H8(50) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2831,
    label = "S(235) + CO(27) <=> S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (548400, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (85.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2832,
    label = "C4H8O3(14) + C3H5(1446) <=> C3H6(144) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2833,
    label = "C4H8O3(14) + S(2185) <=> S(654) + S(2134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2834,
    label = "C4H8O3(14) + C4H7(1663) <=> C4H8(143) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2835,
    label = "C4H8(96) + S(654) <=> C4H8O3(14) + C4H7(1663)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)'),
        n = 4.313,
        Ea = (8.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2836,
    label = "C4H8O3(14) + CHO3(74) <=> S(654) + S(2644)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2837,
    label = "C4H8O3(14) + C4H5(2849) <=> S(654) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2838,
    label = "C4H8O3(14) + S(4886) <=> S(654) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2839,
    label = "S(3752) + S(654) <=> C4H8O3(14) + S(4321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2840,
    label = "C4H8O3(14) + S(6828) <=> S(654) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2841,
    label = "S(654) + C3H4(2124) <=> C4H8O3(14) + C3H3(2385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.312e+07, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (7.126, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2842,
    label = "C4H8O3(14) + S(4319) <=> S(3752) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2843,
    label = "C4H8O3(14) + S(1125) <=> C4H9O(147) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2844,
    label = "C4H8O3(14) + C2H3O(68) <=> CH3CHO(49) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0009569, 'cm^3/(mol*s)'),
        n = 4.45,
        Ea = (0.54, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2845,
    label = "C4H8O3(14) + S(12113) <=> S(654) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2846,
    label = "C4H8O3(14) + S(1448) <=> S(654) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2847,
    label = "C4H8O3(14) + S(5415) <=> S(654) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2848,
    label = "C4H8O3(14) + C3H6O(748) <=> S(654) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.557, 'cm^3/(mol*s)'),
        n = 3.467,
        Ea = (7.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2849,
    label = "C4H8O3(14) + S(14812) <=> S(654) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2850,
    label = "C4H8O3(14) + CH3O2(287) <=> S(654) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2851,
    label = "C4H8O3(14) + S(10034) <=> S(654) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2852,
    label = "C4H8O3(14) + S(471) <=> C4H8O3(11) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.092, 'cm^3/(mol*s)'), n=3.96, Ea=(6.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2853,
    label = "C4H8O3(14) + C2H4O(832) <=> C2H5O(71) + S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2854,
    label = "C4H8O3(14) + S(1035) <=> S(654) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2855,
    label = "CH2OH(35) + S(654) <=> C4H8O3(14) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2856,
    label = "CH3O(36) + S(654) <=> C4H8O3(14) + CH2O(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2857,
    label = "C2H3(41) + S(654) <=> C4H8O3(14) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2858,
    label = "C2H5(44) + S(654) <=> C4H8O3(14) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2859,
    label = "butR1(3) + S(654) <=> C4H8O3(14) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2860,
    label = "butR2(4) + S(654) <=> C4H8O3(14) + C4H8(143)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2861,
    label = "butR2(4) + S(654) <=> C4H8O3(14) + C4H8(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2862,
    label = "C2H3O(18) + S(654) <=> C4H8O3(14) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2863,
    label = "C3H7(51) + S(654) <=> C4H8O3(14) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2864,
    label = "C3H7(95) + S(654) <=> C4H8O3(14) + C3H6(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.111e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2865,
    label = "C2H5O(71) + S(654) <=> C4H8O3(14) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2866,
    label = "C3H5(1446) + S(654) <=> C4H8O3(14) + C3H4(2124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2867,
    label = "C4H7(1663) + S(654) <=> C4H8O3(14) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2868,
    label = "CHO2(57) + S(654) <=> C4H8O3(14) + CO2(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2869,
    label = "S(654) + S(2128) <=> C4H8O3(14) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2870,
    label = "S(4321) + S(654) <=> C4H8O3(14) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2871,
    label = "S(4319) + S(654) <=> C4H8O3(14) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2872,
    label = "S(4319) + S(654) <=> C4H8O3(14) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2873,
    label = "S(1667) + S(654) <=> C4H8O3(14) + S(4338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2874,
    label = "C2H3O(68) + S(654) <=> C4H8O3(14) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2875,
    label = "S(654) + S(1448) <=> C4H8O3(14) + S(2128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2876,
    label = "S(654) + S(1448) <=> C4H8O3(14) + S(1054)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2877,
    label = "S(654) + S(5415) <=> C4H8O3(14) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2878,
    label = "S(654) + C3H6O(748) <=> C4H8O3(14) + C3H5O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2879,
    label = "S(654) + S(1054) <=> C4H8O3(14) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.056e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2880,
    label = "S(654) + S(19508) <=> C4H8O3(14) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2881,
    label = "S(654) + C2H4O(832) <=> C4H8O3(14) + C2H3O(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2882,
    label = "HO2(24) + C4H7O(649) <=> C4H8O3(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2883,
    label = "O(20) + C4H7O(649) <=> C4H7O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2884,
    label = "C3H6(144) + HCO(29) <=> C4H7O(649)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5452, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (5.987, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2885,
    label = "C3H7(95) + CO(27) <=> C4H7O(649)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (355200, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2886,
    label = "S(4338) <=> C4H7O(649)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+10, 's^-1'), n=0.75, Ea=(45.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2887,
    label = "O2(2) + C4H7O(649) <=> S(654)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2888,
    label = "S(654) <=> S(22762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.004e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2889,
    label = "CHO3(74) + C3H6(144) <=> S(2736)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10.6, 'cm^3/(mol*s)'), n=3.29, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2890,
    label = "S(2736) <=> CHO2(57) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 's^-1'), n=0, Ea=(7.074, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2891,
    label = "CHO2(57) + C3H6O(748) <=> S(2736)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2892,
    label = "S(2736) <=> S(22762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.004e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2893,
    label = "H(22) + S(20101) <=> S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2894,
    label = "O(20) + S(13512) <=> OH(23) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(1.79, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2895,
    label = "H(22) + S(13512) <=> H2(21) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(4.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2896,
    label = "OH(23) + S(13512) <=> H2O(46) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(-1.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2897,
    label = "HO2(24) + S(13512) <=> H2O2(25) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2898,
    label = "CH(26) + S(13512) <=> CH2(28) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(200000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2899,
    label = "CH2(28) + S(13512) <=> CH3(31) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.04e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2900,
    label = "HCO(29) + S(13512) <=> CH2O(32) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2901,
    label = "CH3(31) + S(13512) <=> CH4(33) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e-06, 'cm^3/(mol*s)'),
        n = 5.64,
        Ea = (2.46, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2902,
    label = "CH2OH(35) + S(13512) <=> CH3OH(37) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2903,
    label = "CH3O(36) + S(13512) <=> CH3OH(37) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2904,
    label = "C2H(38) + S(13512) <=> C2H2(39) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56460, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.489, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2905,
    label = "HCCOH(48) + S(20101) <=> HCCO(40) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (26.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2906,
    label = "HCCO(40) + S(13512) <=> CH2CO(42) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2907,
    label = "C2H3(41) + S(13512) <=> C2H4(43) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2908,
    label = "C2H5(44) + S(13512) <=> C2H6(45) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2909,
    label = "HO2(24) + S(20101) <=> O2(2) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.669, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2910,
    label = "butR1(3) + S(13512) <=> butane(1) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2911,
    label = "butR2(4) + S(13512) <=> butane(1) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3391, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2912,
    label = "butROO2(6) + S(13512) <=> S(149) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2913,
    label = "C4H9O2(8) + S(13512) <=> S(149) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2914,
    label = "C2H3O(18) + S(13512) <=> CH3CHO(49) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2915,
    label = "C2H3O(18) + S(13512) <=> S(1038) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2916,
    label = "C2H5O2(90) + S(13512) <=> CCOO(1350) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2917,
    label = "C3H7(51) + S(13512) <=> C3H8(50) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2918,
    label = "CH3O2(75) + S(13512) <=> COO(1544) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2919,
    label = "C3H7(95) + S(13512) <=> C3H8(50) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3391, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2920,
    label = "C3H5(1446) + S(13512) <=> C3H6(144) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2921,
    label = "S(2185) + S(13512) <=> S(2134) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2922,
    label = "C4H7(1663) + S(13512) <=> C4H8(143) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2923,
    label = "C4H7(1663) + S(13512) <=> C4H8(96) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3391, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2924,
    label = "CHO3(74) + S(13512) <=> S(2644) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2925,
    label = "C4H5(2849) + S(13512) <=> C4H6(2483) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2926,
    label = "S(4886) + S(13512) <=> S(4759) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2927,
    label = "S(3752) + S(20101) <=> S(4321) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2928,
    label = "S(6828) + S(13512) <=> S(6731) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2929,
    label = "C3H3(2385) + S(13512) <=> C3H4(2124) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2930,
    label = "S(4319) + S(13512) <=> S(3752) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2931,
    label = "S(1125) + S(13512) <=> C4H9O(147) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2932,
    label = "C2H3O(68) + S(13512) <=> CH3CHO(49) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2933,
    label = "S(12113) + S(13512) <=> S(12093) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2934,
    label = "S(1448) + S(13512) <=> S(1450) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2935,
    label = "S(5415) + S(13512) <=> S(4759) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2936,
    label = "C3H6O(748) + S(13512) <=> S(1449) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2937,
    label = "S(13512) + S(14812) <=> S(10030) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3391, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2938,
    label = "CH3O2(287) + S(13512) <=> COO(1544) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2939,
    label = "S(10034) + S(13512) <=> S(9960) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3391, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2940,
    label = "S(471) + S(13512) <=> C4H8O3(11) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2941,
    label = "C2H4O(832) + S(13512) <=> C2H5O(71) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2942,
    label = "S(1035) + S(13512) <=> S(14811) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3391, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2943,
    label = "S(654) + S(13512) <=> C4H8O3(14) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2944,
    label = "CH2OH(35) + S(20101) <=> CH2O(32) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2945,
    label = "CH3O(36) + S(20101) <=> CH2O(32) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2946,
    label = "C2H3(41) + S(20101) <=> C2H2(39) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2947,
    label = "C2H5(44) + S(20101) <=> C2H4(43) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2948,
    label = "butR1(3) + S(20101) <=> C4H8(96) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2949,
    label = "butR2(4) + S(20101) <=> C4H8(143) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2950,
    label = "butR2(4) + S(20101) <=> C4H8(96) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2951,
    label = "C2H3O(18) + S(20101) <=> CH2CO(42) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2952,
    label = "C3H7(51) + S(20101) <=> C3H6(144) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2953,
    label = "C3H7(95) + S(20101) <=> C3H6(144) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.086e+15, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2954,
    label = "C2H5O(71) + S(20101) <=> CH3CHO(49) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2955,
    label = "C3H5(1446) + S(20101) <=> C3H4(2124) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2956,
    label = "C4H7(1663) + S(20101) <=> C4H6(2483) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2957,
    label = "CHO2(57) + S(20101) <=> CO2(34) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2958,
    label = "S(2128) + S(20101) <=> S(3752) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2959,
    label = "S(4321) + S(20101) <=> S(6711) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.214, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2960,
    label = "S(4319) + S(20101) <=> S(9511) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2961,
    label = "S(4319) + S(20101) <=> S(6711) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2962,
    label = "S(1667) + S(20101) <=> S(4338) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2963,
    label = "C2H3O(68) + S(20101) <=> CH2CO(42) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2964,
    label = "S(1448) + S(20101) <=> S(2128) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2965,
    label = "S(1448) + S(20101) <=> S(1054) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2966,
    label = "S(5415) + S(20101) <=> S(13512) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2967,
    label = "C3H6O(748) + S(20101) <=> C3H5O(17) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2968,
    label = "S(1054) + S(20101) <=> S(3752) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2969,
    label = "S(20101) + S(19508) <=> S(13512) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2970,
    label = "C2H4O(832) + S(20101) <=> C2H3O(18) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2971,
    label = "O2(2) + S(20101) <=> S(23419)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2972,
    label = "O2(2) + S(20101) <=> S(23420)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2973,
    label = "S(20101) <=> S(23200)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2974,
    label = "C3H5O(17) + CH2O(32) <=> S(941)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2975,
    label = "C2H3O(68) + S(22205) <=> S(941)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2976,
    label = "S(20113) <=> HO2(24) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.813e+10, 's^-1'), n=0.493, Ea=(13.702, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2977,
    label = "S(13511) <=> HO2(24) + S(11385)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.813e+10, 's^-1'), n=0.493, Ea=(13.702, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2978,
    label = "CO(27) + S(13511) <=> S(20113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (59200, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2979,
    label = "C2H3O(18) + CH2O(32) <=> S(1061)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2980,
    label = "HCO(29) + S(22205) <=> S(1061)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2981,
    label = "H(22) + C3H6O(912) <=> C3H5O(17) + H2(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.748, 'cm^3/(mol*s)'), n=4.34, Ea=(2.75, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2982,
    label = "C3H5O(17) + H(22) <=> C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2983,
    label = "O(20) + C3H6O(912) <=> C3H5O(17) + OH(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+07, 'cm^3/(mol*s)'),
        n = 2.017,
        Ea = (3.981, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2984,
    label = "C3H5O(17) + HO2(24) <=> O2(2) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.541, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2985,
    label = "C3H5O(17) + H2O2(25) <=> HO2(24) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.46e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2986,
    label = "CH(26) + C3H6O(912) <=> C3H5O(17) + CH2(28)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2987,
    label = "CH2(28) + C3H6O(912) <=> C3H5O(17) + CH3(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.443e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (6.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2988,
    label = "C3H5O(17) + CH2O(32) <=> HCO(29) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18.36, 'cm^3/(mol*s)'), n=3.38, Ea=(9.04, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2989,
    label = "CH3(31) + C3H6O(912) <=> C3H5O(17) + CH4(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01773, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.85, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2990,
    label = "C3H5O(17) + CH2OH(35) <=> CH2O(32) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.946e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2991,
    label = "C3H5O(17) + CH3O(36) <=> CH2O(32) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2992,
    label = "CH2OH(35) + C3H6O(912) <=> C3H5O(17) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008866, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2993,
    label = "CH3O(36) + C3H6O(912) <=> C3H5O(17) + CH3OH(37)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58, 'cm^3/(mol*s)'), n=3.82, Ea=(1.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2994,
    label = "C2H(38) + C3H6O(912) <=> C3H5O(17) + C2H2(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (720000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2995,
    label = "C3H5O(17) + C2H3(41) <=> C2H2(39) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2996,
    label = "HCCO(40) + C3H6O(912) <=> C3H5O(17) + CH2CO(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01238, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (12.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2997,
    label = "C2H3(41) + C3H6O(912) <=> C3H5O(17) + C2H4(43)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00108, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2998,
    label = "C3H5O(17) + C2H5(44) <=> C2H4(43) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2999,
    label = "C2H5(44) + C3H6O(912) <=> C3H5O(17) + C2H6(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001007, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3000,
    label = "OH(23) + C3H6O(912) <=> C3H5O(17) + H2O(46)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(132.6, 'cm^3/(mol*s)'), n=3.29, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3001,
    label = "C3H5O(17) + HCCOH(48) <=> HCCO(40) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3002,
    label = "C2H3O(18) + C3H6O(912) <=> C3H5O(17) + CH3CHO(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008866, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3003,
    label = "C3H5O(17) + CH3CHO(49) <=> C2H3O(68) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3004,
    label = "C3H7(95) + C3H6O(912) <=> C3H5O(17) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003505, 'cm^3/(mol*s)'),
        n = 4.416,
        Ea = (12.058, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3005,
    label = "C3H7(51) + C3H6O(912) <=> C3H5O(17) + C3H8(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001007, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3006,
    label = "butR2(4) + C3H6O(912) <=> butane(1) + C3H5O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003505, 'cm^3/(mol*s)'),
        n = 4.416,
        Ea = (12.058, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3007,
    label = "butR1(3) + C3H6O(912) <=> butane(1) + C3H5O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001007, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3008,
    label = "butR1(3) + C3H5O(17) <=> C4H8(96) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3009,
    label = "butR2(4) + C3H5O(17) <=> C4H8(143) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3010,
    label = "butR2(4) + C3H5O(17) <=> C4H8(96) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3011,
    label = "C4H8O3(11) + C3H5O(17) <=> S(471) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3012,
    label = "C4H8O3(14) + C3H5O(17) <=> S(654) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3013,
    label = "C3H5O(17) + C2H3O(18) <=> CH2CO(42) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3014,
    label = "C3H5O(17) + C3H7(51) <=> C3H6(144) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3015,
    label = "C4H9O2(8) + C3H6O(912) <=> C3H5O(17) + S(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001007, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3016,
    label = "C3H5O(17) + S(149) <=> butROO2(6) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3017,
    label = "C3H5O(17) + C3H6(144) <=> C3H5(1446) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004433, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3018,
    label = "C3H6O(912) + S(1125) <=> C3H5O(17) + C4H9O(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001007, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3019,
    label = "C3H5O(17) + C3H7(95) <=> C3H6(144) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.902e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3020,
    label = "C3H5O(17) + C4H8(96) <=> C4H7(1663) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3021,
    label = "C3H5O(17) + CCOO(1350) <=> C2H5O2(90) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3022,
    label = "C3H5O(17) + C4H8(143) <=> C4H7(1663) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008866, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3023,
    label = "C3H5O(17) + C2H5O(71) <=> CH3CHO(49) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3024,
    label = "C2H4O(832) + C3H6O(912) <=> C3H5O(17) + C2H5O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001007, 'cm^3/(mol*s)'),
        n = 4.82,
        Ea = (4.225, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3025,
    label = "CH3O2(287) + C3H6O(912) <=> C3H5O(17) + COO(1544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008866, 'cm^3/(mol*s)'),
        n = 4.368,
        Ea = (13.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3026,
    label = "C3H5O(17) + COO(1544) <=> CH3O2(75) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3027,
    label = "C3H5O(17) + C3H5(1446) <=> C3H4(2124) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3028,
    label = "C3H5O(17) + C3H4(2124) <=> C3H3(2385) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06082, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.183, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3029,
    label = "C3H5O(17) + C4H7(1663) <=> C3H6O(912) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3030,
    label = "C3H6O(912) + C4H5(2849) <=> C3H5O(17) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3031,
    label = "C3H5O(17) + S(2134) <=> S(2185) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3032,
    label = "C3H5O(17) + S(2644) <=> CHO3(74) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (4.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3033,
    label = "C3H5O(17) + CHO2(57) <=> CO2(34) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3034,
    label = "C3H5O(17) + S(2128) <=> S(3752) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3035,
    label = "S(4319) + C3H6O(912) <=> C3H5O(17) + S(3752)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3036,
    label = "C3H5O(17) + S(3752) <=> S(4321) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3037,
    label = "C3H6O(748) + C3H6O(912) <=> C3H5O(17) + S(1449)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58, 'cm^3/(mol*s)'), n=3.82, Ea=(1.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3038,
    label = "C3H5O(17) + S(4321) <=> C3H6O(912) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3039,
    label = "C3H5O(17) + S(6731) <=> C3H6O(912) + S(6828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (4.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3040,
    label = "S(1448) + C3H6O(912) <=> C3H5O(17) + S(1450)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58, 'cm^3/(mol*s)'), n=3.82, Ea=(1.63, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3041,
    label = "C3H5O(17) + S(4319) <=> C3H6O(912) + S(9511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3042,
    label = "C3H5O(17) + S(4319) <=> C3H6O(912) + S(6711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3043,
    label = "C3H5O(17) + S(1667) <=> S(4338) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3044,
    label = "C3H6O(912) + S(10034) <=> C3H5O(17) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.345e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3045,
    label = "C3H6O(912) + S(5415) <=> C3H5O(17) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3046,
    label = "C3H5O(17) + S(4759) <=> C3H6O(912) + S(4886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3047,
    label = "C2H3O(68) + CH3(31) <=> C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3048,
    label = "C3H5O(17) + C2H3O(68) <=> CH2CO(42) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3049,
    label = "C3H5O(17) + S(1448) <=> S(2128) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3050,
    label = "C3H5O(17) + S(1448) <=> S(1054) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3051,
    label = "C3H5O(17) + S(12093) <=> C3H6O(912) + S(12113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (4.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3052,
    label = "C3H6O(912) + S(14812) <=> C3H5O(17) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.345e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3053,
    label = "C3H5O(17) + S(5415) <=> C3H6O(912) + S(15301)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3054,
    label = "C3H5O(17) + C3H6O(748) <=> C3H5O(17) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3055,
    label = "C3H5O(17) + S(1054) <=> S(3752) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3056,
    label = "C3H5O(17) + S(1038) <=> C2H3O(18) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002959, 'cm^3/(mol*s)'),
        n = 4.241,
        Ea = (5.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3057,
    label = "C3H5O(17) + S(19508) <=> C3H6O(912) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3058,
    label = "C3H5O(17) + S(13512) <=> C3H6O(912) + S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3059,
    label = "C3H5O(17) + C2H4O(832) <=> C2H3O(18) + C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3060,
    label = "S(1035) + C3H6O(912) <=> C3H5O(17) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.345e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3061,
    label = "CO(27) + C2H6(45) <=> C3H6O(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6456, 'cm^3/(mol*s)'), n=3.29, Ea=(104.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3062,
    label = "S(4321) + CH2O(32) <=> S(6749)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3063,
    label = "H(22) + S(23208) <=> S(20101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.268e+09, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (8.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3064,
    label = "O(20) + S(20101) <=> OH(23) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.837e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3065,
    label = "H(22) + S(20101) <=> H2(21) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.314e+11, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (0.023, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3066,
    label = "OH(23) + S(20101) <=> H2O(46) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3067,
    label = "HO2(24) + S(20101) <=> H2O2(25) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3068,
    label = "CH(26) + S(20101) <=> CH2(28) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.046e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3069,
    label = "CH2(28) + S(20101) <=> CH3(31) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.04e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3070,
    label = "HCO(29) + S(20101) <=> CH2O(32) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3071,
    label = "CH3(31) + S(20101) <=> CH4(33) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3072,
    label = "CH2OH(35) + S(20101) <=> CH3OH(37) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3073,
    label = "CH3O(36) + S(20101) <=> CH3OH(37) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3074,
    label = "C2H(38) + S(20101) <=> C2H2(39) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.297e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3075,
    label = "HCCO(40) + S(20101) <=> HCCOH(48) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.159, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3076,
    label = "HCCO(40) + S(20101) <=> CH2CO(42) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3077,
    label = "C2H3(41) + S(20101) <=> C2H4(43) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3078,
    label = "C2H5(44) + S(20101) <=> C2H6(45) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3079,
    label = "O2(2) + S(20101) <=> HO2(24) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26.883, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3080,
    label = "butR1(3) + S(20101) <=> butane(1) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3081,
    label = "butR2(4) + S(20101) <=> butane(1) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3082,
    label = "butROO2(6) + S(20101) <=> S(149) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3083,
    label = "C4H9O2(8) + S(20101) <=> S(149) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3084,
    label = "C3H5O(17) + S(20101) <=> C3H6O(912) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3085,
    label = "C2H3O(18) + S(20101) <=> CH3CHO(49) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3086,
    label = "C2H3O(18) + S(20101) <=> S(1038) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3087,
    label = "C2H5O2(90) + S(20101) <=> CCOO(1350) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3088,
    label = "C3H7(51) + S(20101) <=> C3H8(50) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3089,
    label = "CH3O2(75) + S(20101) <=> COO(1544) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3090,
    label = "C3H7(95) + S(20101) <=> C3H8(50) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3091,
    label = "C3H5(1446) + S(20101) <=> C3H6(144) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3092,
    label = "S(2185) + S(20101) <=> S(2134) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3093,
    label = "C4H7(1663) + S(20101) <=> C4H8(143) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3094,
    label = "C4H7(1663) + S(20101) <=> C4H8(96) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3095,
    label = "CHO3(74) + S(20101) <=> S(2644) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3096,
    label = "C4H5(2849) + S(20101) <=> C4H6(2483) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3097,
    label = "S(4886) + S(20101) <=> S(4759) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3098,
    label = "S(4321) + S(20101) <=> S(3752) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3099,
    label = "S(6828) + S(20101) <=> S(6731) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3100,
    label = "C3H3(2385) + S(20101) <=> C3H4(2124) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3101,
    label = "S(4319) + S(20101) <=> S(3752) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3102,
    label = "S(1125) + S(20101) <=> C4H9O(147) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3103,
    label = "C2H3O(68) + S(20101) <=> CH3CHO(49) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3104,
    label = "S(12113) + S(20101) <=> S(12093) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3105,
    label = "S(1448) + S(20101) <=> S(1450) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3106,
    label = "S(5415) + S(20101) <=> S(4759) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3107,
    label = "C3H6O(748) + S(20101) <=> S(1449) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3108,
    label = "S(14812) + S(20101) <=> S(10030) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3109,
    label = "CH3O2(287) + S(20101) <=> COO(1544) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3110,
    label = "S(10034) + S(20101) <=> S(9960) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3111,
    label = "S(471) + S(20101) <=> C4H8O3(11) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3112,
    label = "C2H4O(832) + S(20101) <=> C2H5O(71) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3113,
    label = "S(1035) + S(20101) <=> S(14811) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3114,
    label = "S(654) + S(20101) <=> C4H8O3(14) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.852e+09, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3115,
    label = "S(20101) + S(20101) <=> S(13512) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3116,
    label = "S(23420) <=> HO2(24) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.203e+10, 's^-1'), n=0.622, Ea=(31.533, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3117,
    label = "S(25384) <=> S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3118,
    label = "S(23208) <=> S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3271, 's^-1'), n=2.877, Ea=(34.079, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3119,
    label = "S(25384) <=> S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3120,
    label = "S(25753) <=> S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3121,
    label = "H(22) + S(25762) <=> H2(21) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3122,
    label = "H(22) + S(25386) <=> S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (773400, 'cm^3/(mol*s)'),
        n = 2.941,
        Ea = (8.52, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3123,
    label = "O2(2) + S(25762) <=> HO2(24) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.288e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3124,
    label = "CH(26) + S(25762) <=> CH2(28) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.046e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3125,
    label = "CH2(28) + S(25762) <=> CH3(31) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3126,
    label = "HCO(29) + S(25762) <=> CH2O(32) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3127,
    label = "CH3(31) + S(25762) <=> CH4(33) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.49e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3128,
    label = "CH2OH(35) + S(25762) <=> CH3OH(37) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3129,
    label = "HCCO(40) + S(25762) <=> CH2CO(42) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3130,
    label = "C2H3(41) + S(25762) <=> C2H4(43) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3131,
    label = "C2H5(44) + S(25762) <=> C2H6(45) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3132,
    label = "C2H3O(18) + S(25762) <=> CH3CHO(49) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.946e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3133,
    label = "C3H7(95) + S(25762) <=> C3H8(50) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3134,
    label = "C3H7(51) + S(25762) <=> C3H8(50) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3135,
    label = "butR2(4) + S(25762) <=> butane(1) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3136,
    label = "butR1(3) + S(25762) <=> butane(1) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3137,
    label = "C4H9O2(8) + S(25762) <=> S(149) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3138,
    label = "C3H5(1446) + S(25762) <=> C3H6(144) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3139,
    label = "S(1125) + S(25762) <=> C4H9O(147) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3140,
    label = "C4H7(1663) + S(25762) <=> C4H8(96) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3141,
    label = "C4H7(1663) + S(25762) <=> C4H8(143) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3142,
    label = "C2H4O(832) + S(25762) <=> C2H5O(71) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3143,
    label = "CH3O2(287) + S(25762) <=> COO(1544) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3144,
    label = "C3H3(2385) + S(25762) <=> C3H4(2124) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3145,
    label = "S(10034) + S(25762) <=> S(9960) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3146,
    label = "S(14812) + S(25762) <=> S(10030) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3147,
    label = "S(1035) + S(25762) <=> S(14811) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3148,
    label = "C3H5O(17) + S(25762) <=> C3H6O(912) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.946e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3149,
    label = "O(20) + S(25762) <=> OH(23) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.04e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3150,
    label = "OH(23) + S(25762) <=> H2O(46) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3151,
    label = "HO2(24) + S(25762) <=> H2O2(25) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3152,
    label = "CH3O(36) + S(25762) <=> CH3OH(37) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3153,
    label = "C2H(38) + S(25762) <=> C2H2(39) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.61e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3154,
    label = "HCCO(40) + S(25762) <=> HCCOH(48) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.061e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3155,
    label = "butROO2(6) + S(25762) <=> S(149) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3156,
    label = "C2H3O(18) + S(25762) <=> S(1038) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.061e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3157,
    label = "C2H5O2(90) + S(25762) <=> CCOO(1350) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3158,
    label = "CH3O2(75) + S(25762) <=> COO(1544) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3159,
    label = "S(2185) + S(25762) <=> S(2134) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3160,
    label = "CHO3(74) + S(25762) <=> S(2644) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3161,
    label = "C4H5(2849) + S(25762) <=> C4H6(2483) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3162,
    label = "S(4886) + S(25762) <=> S(4759) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3163,
    label = "S(4321) + S(25762) <=> S(3752) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3164,
    label = "S(6828) + S(25762) <=> S(6731) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3165,
    label = "S(4319) + S(25762) <=> S(3752) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3166,
    label = "C2H3O(68) + S(25762) <=> CH3CHO(49) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3167,
    label = "S(12113) + S(25762) <=> S(12093) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3168,
    label = "S(1448) + S(25762) <=> S(1450) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3169,
    label = "S(5415) + S(25762) <=> S(4759) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3170,
    label = "C3H6O(748) + S(25762) <=> S(1449) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3171,
    label = "S(471) + S(25762) <=> C4H8O3(11) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3172,
    label = "S(654) + S(25762) <=> C4H8O3(14) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3173,
    label = "S(20101) + S(25762) <=> S(13512) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3174,
    label = "H(22) + S(26110) <=> H2(21) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3175,
    label = "H(22) + S(25762) <=> S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3176,
    label = "O(20) + S(26110) <=> OH(23) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1.79, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3177,
    label = "HO2(24) + S(25762) <=> O2(2) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.831, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3178,
    label = "HO2(24) + S(26110) <=> H2O2(25) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3179,
    label = "CH(26) + S(26110) <=> CH2(28) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3180,
    label = "CH2(28) + S(26110) <=> CH3(31) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3181,
    label = "HCO(29) + S(26110) <=> CH2O(32) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3182,
    label = "CH3(31) + S(26110) <=> CH4(33) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e-06, 'cm^3/(mol*s)'),
        n = 5.64,
        Ea = (2.46, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3183,
    label = "CH2OH(35) + S(25762) <=> CH2O(32) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3184,
    label = "CH3O(36) + S(25762) <=> CH2O(32) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3185,
    label = "CH2OH(35) + S(26110) <=> CH3OH(37) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3186,
    label = "CH3O(36) + S(26110) <=> CH3OH(37) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3187,
    label = "C2H(38) + S(26110) <=> C2H2(39) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.326, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3188,
    label = "C2H3(41) + S(25762) <=> C2H2(39) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3189,
    label = "HCCO(40) + S(26110) <=> CH2CO(42) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3190,
    label = "C2H3(41) + S(26110) <=> C2H4(43) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3191,
    label = "C2H5(44) + S(25762) <=> C2H4(43) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3192,
    label = "C2H5(44) + S(26110) <=> C2H6(45) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3193,
    label = "OH(23) + S(26110) <=> H2O(46) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(-1.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3194,
    label = "HCCO(40) + S(26110) <=> HCCOH(48) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3195,
    label = "C2H3O(18) + S(26110) <=> CH3CHO(49) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3196,
    label = "C2H3O(68) + S(26110) <=> CH3CHO(49) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3197,
    label = "C3H7(95) + S(26110) <=> C3H8(50) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3198,
    label = "C3H7(51) + S(26110) <=> C3H8(50) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3199,
    label = "butR2(4) + S(26110) <=> butane(1) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3200,
    label = "butR1(3) + S(26110) <=> butane(1) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3201,
    label = "butR1(3) + S(25762) <=> C4H8(96) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3202,
    label = "butR2(4) + S(25762) <=> C4H8(143) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3203,
    label = "butR2(4) + S(25762) <=> C4H8(96) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3204,
    label = "S(471) + S(26110) <=> C4H8O3(11) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3205,
    label = "S(654) + S(26110) <=> C4H8O3(14) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3206,
    label = "C2H3O(18) + S(25762) <=> CH2CO(42) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3207,
    label = "C3H7(51) + S(25762) <=> C3H6(144) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3208,
    label = "C4H9O2(8) + S(26110) <=> S(149) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3209,
    label = "butROO2(6) + S(26110) <=> S(149) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3210,
    label = "C3H5(1446) + S(26110) <=> C3H6(144) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3211,
    label = "S(1125) + S(26110) <=> C4H9O(147) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3212,
    label = "C3H7(95) + S(25762) <=> C3H6(144) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.086e+15, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3213,
    label = "C4H7(1663) + S(26110) <=> C4H8(96) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3214,
    label = "C2H5O2(90) + S(26110) <=> CCOO(1350) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3215,
    label = "C4H7(1663) + S(26110) <=> C4H8(143) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3216,
    label = "C2H5O(71) + S(25762) <=> CH3CHO(49) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3217,
    label = "C2H4O(832) + S(26110) <=> C2H5O(71) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3218,
    label = "CH3O2(287) + S(26110) <=> COO(1544) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3219,
    label = "CH3O2(75) + S(26110) <=> COO(1544) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3220,
    label = "C3H5(1446) + S(25762) <=> C3H4(2124) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3221,
    label = "C3H3(2385) + S(26110) <=> C3H4(2124) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3222,
    label = "C4H7(1663) + S(25762) <=> C4H6(2483) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3223,
    label = "C4H5(2849) + S(26110) <=> C4H6(2483) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3224,
    label = "S(2185) + S(26110) <=> S(2134) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3225,
    label = "CHO3(74) + S(26110) <=> S(2644) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3226,
    label = "CHO2(57) + S(25762) <=> CO2(34) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3227,
    label = "S(2128) + S(25762) <=> S(3752) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3228,
    label = "S(4319) + S(26110) <=> S(3752) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3229,
    label = "S(4321) + S(26110) <=> S(3752) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3230,
    label = "C3H6O(748) + S(26110) <=> S(1449) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3231,
    label = "S(4321) + S(25762) <=> S(6711) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.176, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3232,
    label = "S(6828) + S(26110) <=> S(6731) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3233,
    label = "S(1448) + S(26110) <=> S(1450) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3234,
    label = "S(4319) + S(25762) <=> S(9511) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3235,
    label = "S(4319) + S(25762) <=> S(6711) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3236,
    label = "S(1667) + S(25762) <=> S(4338) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3237,
    label = "S(10034) + S(26110) <=> S(9960) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3238,
    label = "S(5415) + S(26110) <=> S(4759) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3239,
    label = "S(4886) + S(26110) <=> S(4759) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3240,
    label = "C2H3O(68) + S(25762) <=> CH2CO(42) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3241,
    label = "S(1448) + S(25762) <=> S(2128) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3242,
    label = "S(1448) + S(25762) <=> S(1054) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3243,
    label = "S(12113) + S(26110) <=> S(12093) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3244,
    label = "S(14812) + S(26110) <=> S(10030) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3245,
    label = "S(5415) + S(25762) <=> S(15301) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3246,
    label = "C3H6O(748) + S(25762) <=> C3H5O(17) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3247,
    label = "S(1054) + S(25762) <=> S(3752) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.43e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3248,
    label = "C2H3O(18) + S(26110) <=> S(1038) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3249,
    label = "S(19508) + S(25762) <=> S(13512) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3250,
    label = "S(20101) + S(26110) <=> S(13512) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3251,
    label = "C2H4O(832) + S(25762) <=> C2H3O(18) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3252,
    label = "S(1035) + S(26110) <=> S(14811) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3253,
    label = "S(20101) + S(25762) <=> S(23208) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.298, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3254,
    label = "C3H5O(17) + S(26110) <=> C3H6O(912) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3255,
    label = "S(25762) + S(25762) <=> S(26110) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3256,
    label = "S(20255) <=> S(12985)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(37990, 's^-1'), n=2.515, Ea=(48.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3257,
    label = "S(20255) <=> S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3258,
    label = "S(20412) <=> S(20269)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(37990, 's^-1'), n=2.515, Ea=(48.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3259,
    label = "S(20255) <=> S(20412)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3260,
    label = "S(26490) <=> S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1636, 's^-1'), n=2.877, Ea=(34.079, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3261,
    label = "S(27441) <=> CH2CO(42) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3262,
    label = "H(22) + S(27338) <=> H2(21) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3263,
    label = "H(22) + S(26490) <=> S(27338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.391e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (3.113, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3264,
    label = "O2(2) + S(27338) <=> HO2(24) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13.55, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3265,
    label = "CH(26) + S(27338) <=> CH2(28) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3266,
    label = "CH2(28) + S(27338) <=> CH3(31) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.356e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3267,
    label = "HCO(29) + S(27338) <=> CH2O(32) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3268,
    label = "CH3(31) + S(27338) <=> CH4(33) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3269,
    label = "CH2OH(35) + S(27338) <=> CH3OH(37) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3270,
    label = "HCCO(40) + S(27338) <=> CH2CO(42) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3271,
    label = "C2H3(41) + S(27338) <=> C2H4(43) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3272,
    label = "C2H5(44) + S(27338) <=> C2H6(45) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3273,
    label = "C2H3O(18) + S(27338) <=> CH3CHO(49) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3274,
    label = "C3H7(95) + S(27338) <=> C3H8(50) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3275,
    label = "C3H7(51) + S(27338) <=> C3H8(50) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3276,
    label = "butR2(4) + S(27338) <=> butane(1) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3277,
    label = "butR1(3) + S(27338) <=> butane(1) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3278,
    label = "C4H9O2(8) + S(27338) <=> S(149) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3279,
    label = "C3H5(1446) + S(27338) <=> C3H6(144) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+10, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3280,
    label = "S(1125) + S(27338) <=> C4H9O(147) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3281,
    label = "C4H7(1663) + S(27338) <=> C4H8(96) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3282,
    label = "C4H7(1663) + S(27338) <=> C4H8(143) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+10, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3283,
    label = "C2H4O(832) + S(27338) <=> C2H5O(71) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3284,
    label = "CH3O2(287) + S(27338) <=> COO(1544) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3285,
    label = "C3H3(2385) + S(27338) <=> C3H4(2124) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3286,
    label = "S(10034) + S(27338) <=> S(9960) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3287,
    label = "S(14812) + S(27338) <=> S(10030) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3288,
    label = "S(1035) + S(27338) <=> S(14811) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3289,
    label = "C3H5O(17) + S(27338) <=> C3H6O(912) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.851e+11, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3290,
    label = "O(20) + S(27338) <=> OH(23) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.684e+09, 'cm^3/(mol*s)'),
        n = 0.625,
        Ea = (-0.237, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3291,
    label = "OH(23) + S(27338) <=> H2O(46) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3292,
    label = "HO2(24) + S(27338) <=> H2O2(25) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3293,
    label = "CH3O(36) + S(27338) <=> CH3OH(37) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3294,
    label = "C2H(38) + S(27338) <=> C2H2(39) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.109e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3295,
    label = "HCCO(40) + S(27338) <=> HCCOH(48) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3296,
    label = "butROO2(6) + S(27338) <=> S(149) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3297,
    label = "C2H3O(18) + S(27338) <=> S(1038) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3298,
    label = "C2H5O2(90) + S(27338) <=> CCOO(1350) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3299,
    label = "CH3O2(75) + S(27338) <=> COO(1544) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3300,
    label = "S(2185) + S(27338) <=> S(2134) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3301,
    label = "CHO3(74) + S(27338) <=> S(2644) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3302,
    label = "C4H5(2849) + S(27338) <=> C4H6(2483) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.037e+10, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3303,
    label = "S(4886) + S(27338) <=> S(4759) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3304,
    label = "S(4321) + S(27338) <=> S(3752) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3305,
    label = "S(6828) + S(27338) <=> S(6731) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3306,
    label = "S(4319) + S(27338) <=> S(3752) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.037e+10, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3307,
    label = "C2H3O(68) + S(27338) <=> CH3CHO(49) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3308,
    label = "S(12113) + S(27338) <=> S(12093) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3309,
    label = "S(1448) + S(27338) <=> S(1450) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3310,
    label = "S(5415) + S(27338) <=> S(4759) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.037e+10, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3311,
    label = "C3H6O(748) + S(27338) <=> S(1449) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3312,
    label = "S(471) + S(27338) <=> C4H8O3(11) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3313,
    label = "S(654) + S(27338) <=> C4H8O3(14) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.618e+09, 'cm^3/(mol*s)'),
        n = 0.502,
        Ea = (0.076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3314,
    label = "S(20101) + S(27338) <=> S(13512) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3315,
    label = "S(27338) + S(25762) <=> S(26490) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.254e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3316,
    label = "S(26490) <=> S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(37990, 's^-1'), n=2.515, Ea=(48.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3317,
    label = "H(22) + S(27328) <=> S(27338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (386700, 'cm^3/(mol*s)'),
        n = 2.941,
        Ea = (8.52, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3318,
    label = "O(20) + S(27338) <=> OH(23) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.04e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3319,
    label = "H(22) + S(27338) <=> H2(21) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3320,
    label = "OH(23) + S(27338) <=> H2O(46) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3321,
    label = "HO2(24) + S(27338) <=> H2O2(25) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3322,
    label = "CH(26) + S(27338) <=> CH2(28) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.046e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3323,
    label = "CH2(28) + S(27338) <=> CH3(31) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3324,
    label = "HCO(29) + S(27338) <=> CH2O(32) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3325,
    label = "CH3(31) + S(27338) <=> CH4(33) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.49e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3326,
    label = "CH2OH(35) + S(27338) <=> CH3OH(37) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3327,
    label = "CH3O(36) + S(27338) <=> CH3OH(37) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3328,
    label = "C2H(38) + S(27338) <=> C2H2(39) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.61e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3329,
    label = "HCCO(40) + S(27338) <=> HCCOH(48) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.061e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3330,
    label = "HCCO(40) + S(27338) <=> CH2CO(42) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3331,
    label = "C2H3(41) + S(27338) <=> C2H4(43) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3332,
    label = "C2H5(44) + S(27338) <=> C2H6(45) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3333,
    label = "O2(2) + S(27338) <=> HO2(24) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.288e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3334,
    label = "butR1(3) + S(27338) <=> butane(1) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3335,
    label = "butR2(4) + S(27338) <=> butane(1) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3336,
    label = "butROO2(6) + S(27338) <=> S(149) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3337,
    label = "C4H9O2(8) + S(27338) <=> S(149) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3338,
    label = "C3H5O(17) + S(27338) <=> C3H6O(912) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.946e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3339,
    label = "C2H3O(18) + S(27338) <=> CH3CHO(49) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.946e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3340,
    label = "C2H3O(18) + S(27338) <=> S(1038) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.061e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3341,
    label = "C2H5O2(90) + S(27338) <=> CCOO(1350) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3342,
    label = "C3H7(51) + S(27338) <=> C3H8(50) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3343,
    label = "CH3O2(75) + S(27338) <=> COO(1544) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3344,
    label = "C3H7(95) + S(27338) <=> C3H8(50) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3345,
    label = "C3H5(1446) + S(27338) <=> C3H6(144) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3346,
    label = "S(2185) + S(27338) <=> S(2134) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3347,
    label = "C4H7(1663) + S(27338) <=> C4H8(143) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3348,
    label = "C4H7(1663) + S(27338) <=> C4H8(96) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3349,
    label = "CHO3(74) + S(27338) <=> S(2644) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3350,
    label = "C4H5(2849) + S(27338) <=> C4H6(2483) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3351,
    label = "S(4886) + S(27338) <=> S(4759) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3352,
    label = "S(4321) + S(27338) <=> S(3752) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3353,
    label = "S(6828) + S(27338) <=> S(6731) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3354,
    label = "C3H3(2385) + S(27338) <=> C3H4(2124) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3355,
    label = "S(4319) + S(27338) <=> S(3752) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3356,
    label = "S(1125) + S(27338) <=> C4H9O(147) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3357,
    label = "C2H3O(68) + S(27338) <=> CH3CHO(49) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3358,
    label = "S(12113) + S(27338) <=> S(12093) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3359,
    label = "S(1448) + S(27338) <=> S(1450) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3360,
    label = "S(5415) + S(27338) <=> S(4759) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3361,
    label = "C3H6O(748) + S(27338) <=> S(1449) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3362,
    label = "S(14812) + S(27338) <=> S(10030) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3363,
    label = "CH3O2(287) + S(27338) <=> COO(1544) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3364,
    label = "S(10034) + S(27338) <=> S(9960) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3365,
    label = "S(471) + S(27338) <=> C4H8O3(11) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3366,
    label = "C2H4O(832) + S(27338) <=> C2H5O(71) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3367,
    label = "S(1035) + S(27338) <=> S(14811) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3368,
    label = "S(654) + S(27338) <=> C4H8O3(14) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3369,
    label = "S(20101) + S(27338) <=> S(13512) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3370,
    label = "S(27338) + S(25762) <=> S(27328) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3371,
    label = "S(27338) <=> S(27668)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3372,
    label = "S(25762) <=> S(26093)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3373,
    label = "S(25762) <=> S(26099)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3374,
    label = "S(28788) <=> S(26099)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3375,
    label = "O2(2) + S(28788) <=> S(29153)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3376,
    label = "H(22) + S(29001) <=> H2(21) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.3776, 'cm^3/(mol*s)'), n=4.34, Ea=(5.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3377,
    label = "H(22) + S(28788) <=> S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3378,
    label = "O(20) + S(29001) <=> OH(23) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3379,
    label = "HO2(24) + S(28788) <=> O2(2) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.48, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3380,
    label = "H2O2(25) + S(28788) <=> HO2(24) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3381,
    label = "CH(26) + S(29001) <=> CH2(28) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3382,
    label = "CH2(28) + S(29001) <=> CH3(31) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.24e+07, 'cm^3/(mol*s)'),
        n = 1.524,
        Ea = (5.498, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3383,
    label = "CH2O(32) + S(28788) <=> HCO(29) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3384,
    label = "CH3(31) + S(29001) <=> CH4(33) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.008928, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3385,
    label = "CH2OH(35) + S(28788) <=> CH2O(32) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3386,
    label = "CH3O(36) + S(28788) <=> CH2O(32) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3387,
    label = "CH3OH(37) + S(28788) <=> CH2OH(35) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005592, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3388,
    label = "CH3O(36) + S(29001) <=> CH3OH(37) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3389,
    label = "C2H(38) + S(29001) <=> C2H2(39) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.678, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3390,
    label = "C2H3(41) + S(28788) <=> C2H2(39) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3391,
    label = "HCCO(40) + S(29001) <=> CH2CO(42) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.02741, 'cm^3/(mol*s)'), n=4.34, Ea=(18, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3392,
    label = "C2H3(41) + S(29001) <=> C2H4(43) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01302, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.405, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3393,
    label = "C2H5(44) + S(28788) <=> C2H4(43) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3394,
    label = "C2H6(45) + S(28788) <=> C2H5(44) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3395,
    label = "OH(23) + S(29001) <=> H2O(46) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(1.45, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3396,
    label = "HCCOH(48) + S(28788) <=> HCCO(40) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3397,
    label = "CH3CHO(49) + S(28788) <=> C2H3O(18) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005589, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3398,
    label = "CH3CHO(49) + S(28788) <=> C2H3O(68) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3399,
    label = "C3H8(50) + S(28788) <=> C3H7(95) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00452, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (8.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3400,
    label = "C3H8(50) + S(28788) <=> C3H7(51) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3401,
    label = "butane(1) + S(28788) <=> butR2(4) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00904, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (8.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3402,
    label = "butR1(3) + S(29001) <=> butane(1) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3403,
    label = "butR1(3) + S(28788) <=> C4H8(96) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3404,
    label = "butR2(4) + S(28788) <=> C4H8(143) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3405,
    label = "butR2(4) + S(28788) <=> C4H8(96) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3406,
    label = "C4H8O3(11) + S(28788) <=> S(471) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3407,
    label = "C4H8O3(14) + S(28788) <=> S(654) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3408,
    label = "C2H3O(18) + S(28788) <=> CH2CO(42) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3409,
    label = "C3H7(51) + S(28788) <=> C3H6(144) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3410,
    label = "C4H9O2(8) + S(29001) <=> S(149) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3411,
    label = "S(149) + S(28788) <=> butROO2(6) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3412,
    label = "C3H6(144) + S(28788) <=> C3H5(1446) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005589, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3413,
    label = "S(1125) + S(29001) <=> C4H9O(147) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3414,
    label = "C3H7(95) + S(28788) <=> C3H6(144) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.876e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3415,
    label = "C4H8(96) + S(28788) <=> C4H7(1663) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.006127, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.867, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3416,
    label = "CCOO(1350) + S(28788) <=> C2H5O2(90) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3417,
    label = "C4H8(143) + S(28788) <=> C4H7(1663) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3418,
    label = "C2H5O(71) + S(28788) <=> CH3CHO(49) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3419,
    label = "C2H4O(832) + S(29001) <=> C2H5O(71) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004577, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (14.819, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3420,
    label = "COO(1544) + S(28788) <=> CH3O2(287) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005592, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3421,
    label = "COO(1544) + S(28788) <=> CH3O2(75) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3422,
    label = "C3H5(1446) + S(28788) <=> C3H4(2124) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.037e+10, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3423,
    label = "C3H4(2124) + S(28788) <=> C3H3(2385) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.09769, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (10.367, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3424,
    label = "C4H7(1663) + S(28788) <=> C4H6(2483) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3425,
    label = "C4H6(2483) + S(28788) <=> C4H5(2849) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01127, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (12.567, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3426,
    label = "S(2134) + S(28788) <=> S(2185) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3427,
    label = "S(2644) + S(28788) <=> CHO3(74) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3428,
    label = "CHO2(57) + S(28788) <=> CO2(34) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3429,
    label = "S(2128) + S(28788) <=> S(3752) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3430,
    label = "S(4319) + S(29001) <=> S(3752) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005633, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (12.567, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3431,
    label = "S(3752) + S(28788) <=> S(4321) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3432,
    label = "C3H6O(748) + S(29001) <=> S(1449) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.219, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3433,
    label = "S(4321) + S(28788) <=> S(6711) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3434,
    label = "S(6731) + S(28788) <=> S(6828) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3435,
    label = "S(1448) + S(29001) <=> S(1450) + S(28788)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.78e+06, 'cm^3/(mol*s)'),
        n = 1.845,
        Ea = (6.219, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3436,
    label = "S(4319) + S(28788) <=> S(9511) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3437,
    label = "S(4319) + S(28788) <=> S(6711) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3438,
    label = "S(1667) + S(28788) <=> S(4338) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3439,
    label = "S(9960) + S(28788) <=> S(10034) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3440,
    label = "S(4759) + S(28788) <=> S(5415) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005633, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (12.567, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3441,
    label = "S(4759) + S(28788) <=> S(4886) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3442,
    label = "C2H3O(68) + S(28788) <=> CH2CO(42) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3443,
    label = "S(1448) + S(28788) <=> S(2128) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3444,
    label = "S(1448) + S(28788) <=> S(1054) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3445,
    label = "S(12093) + S(28788) <=> S(12113) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3446,
    label = "S(10030) + S(28788) <=> S(14812) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3447,
    label = "S(5415) + S(28788) <=> S(15301) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.378e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (-0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3448,
    label = "C3H6O(748) + S(28788) <=> C3H5O(17) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3449,
    label = "S(1054) + S(28788) <=> S(3752) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.938e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3450,
    label = "S(1038) + S(28788) <=> C2H3O(18) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3451,
    label = "S(19508) + S(28788) <=> S(13512) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3452,
    label = "S(13512) + S(28788) <=> S(20101) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5420, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3453,
    label = "C2H4O(832) + S(28788) <=> C2H3O(18) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.584e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3454,
    label = "S(14811) + S(28788) <=> S(1035) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01165, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3455,
    label = "S(20101) + S(28788) <=> S(23208) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3456,
    label = "C3H6O(912) + S(28788) <=> C3H5O(17) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01118, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3457,
    label = "S(25762) + S(28788) <=> S(25386) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3458,
    label = "S(26110) + S(28788) <=> S(29001) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2710, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3459,
    label = "S(27338) + S(28788) <=> S(26490) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.037e+10, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3460,
    label = "S(27338) + S(28788) <=> S(27328) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3461,
    label = "S(20255) <=> S(26824)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.668e+06, 's^-1'), n=1.614, Ea=(29.669, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3462,
    label = "S(26824) <=> S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.773e+12, 's^-1'), n=0.019, Ea=(1.585, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3463,
    label = "S(27338) <=> S(27674)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(37990, 's^-1'), n=2.515, Ea=(48.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3464,
    label = "H(22) + S(27674) <=> H2(21) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3465,
    label = "H(22) + S(27328) <=> S(27674)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.798e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.277, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3466,
    label = "O2(2) + S(27674) <=> HO2(24) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3467,
    label = "CH(26) + S(27674) <=> CH2(28) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3468,
    label = "CH2(28) + S(27674) <=> CH3(31) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3469,
    label = "HCO(29) + S(27674) <=> CH2O(32) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3470,
    label = "CH3(31) + S(27674) <=> CH4(33) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3471,
    label = "CH2OH(35) + S(27674) <=> CH3OH(37) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3472,
    label = "HCCO(40) + S(27674) <=> CH2CO(42) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3473,
    label = "C2H3(41) + S(27674) <=> C2H4(43) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3474,
    label = "C2H5(44) + S(27674) <=> C2H6(45) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3475,
    label = "C2H3O(18) + S(27674) <=> CH3CHO(49) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3476,
    label = "C3H7(95) + S(27674) <=> C3H8(50) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3477,
    label = "C3H7(51) + S(27674) <=> C3H8(50) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3478,
    label = "butR2(4) + S(27674) <=> butane(1) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3479,
    label = "butR1(3) + S(27674) <=> butane(1) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3480,
    label = "C4H9O2(8) + S(27674) <=> S(149) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3481,
    label = "C3H5(1446) + S(27674) <=> C3H6(144) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3482,
    label = "S(1125) + S(27674) <=> C4H9O(147) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3483,
    label = "C4H7(1663) + S(27674) <=> C4H8(96) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3484,
    label = "C4H7(1663) + S(27674) <=> C4H8(143) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3485,
    label = "C2H4O(832) + S(27674) <=> C2H5O(71) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3486,
    label = "CH3O2(287) + S(27674) <=> COO(1544) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3487,
    label = "C3H3(2385) + S(27674) <=> C3H4(2124) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3488,
    label = "S(10034) + S(27674) <=> S(9960) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3489,
    label = "S(14812) + S(27674) <=> S(10030) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3490,
    label = "S(1035) + S(27674) <=> S(14811) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3491,
    label = "C3H5O(17) + S(27674) <=> C3H6O(912) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3492,
    label = "O(20) + S(27674) <=> OH(23) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3493,
    label = "OH(23) + S(27674) <=> H2O(46) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3494,
    label = "HO2(24) + S(27674) <=> H2O2(25) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3495,
    label = "CH3O(36) + S(27674) <=> CH3OH(37) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3496,
    label = "C2H(38) + S(27674) <=> C2H2(39) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.206e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3497,
    label = "HCCO(40) + S(27674) <=> HCCOH(48) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3498,
    label = "butROO2(6) + S(27674) <=> S(149) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3499,
    label = "C2H3O(18) + S(27674) <=> S(1038) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3500,
    label = "C2H5O2(90) + S(27674) <=> CCOO(1350) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3501,
    label = "CH3O2(75) + S(27674) <=> COO(1544) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3502,
    label = "S(2185) + S(27674) <=> S(2134) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3503,
    label = "CHO3(74) + S(27674) <=> S(2644) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3504,
    label = "C4H5(2849) + S(27674) <=> C4H6(2483) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3505,
    label = "S(4886) + S(27674) <=> S(4759) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3506,
    label = "S(4321) + S(27674) <=> S(3752) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3507,
    label = "S(6828) + S(27674) <=> S(6731) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3508,
    label = "S(4319) + S(27674) <=> S(3752) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3509,
    label = "C2H3O(68) + S(27674) <=> CH3CHO(49) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3510,
    label = "S(12113) + S(27674) <=> S(12093) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3511,
    label = "S(1448) + S(27674) <=> S(1450) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3512,
    label = "S(5415) + S(27674) <=> S(4759) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3513,
    label = "C3H6O(748) + S(27674) <=> S(1449) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3514,
    label = "S(471) + S(27674) <=> C4H8O3(11) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3515,
    label = "S(654) + S(27674) <=> C4H8O3(14) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3516,
    label = "S(20101) + S(27674) <=> S(13512) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3517,
    label = "S(27674) + S(25762) <=> S(27328) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3518,
    label = "S(27674) + S(28788) <=> S(27328) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3519,
    label = "S(28126) <=> HO2(24) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.241e+11, 's^-1'), n=0.622, Ea=(38.732, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3520,
    label = "O2(2) + S(27674) <=> S(28126)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.672e+13, 'cm^3/(mol*s)'),
        n = -0.085,
        Ea = (-0.567, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3521,
    label = "S(28126) <=> S(30197)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3522,
    label = "S(30234) <=> S(30197)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3523,
    label = "H(22) + S(21335) <=> S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3524,
    label = "O(20) + S(21257) <=> OH(23) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (145000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.88, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3525,
    label = "H(22) + S(21257) <=> H2(21) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5220, 'cm^3/(mol*s)'), n=3.04, Ea=(2.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3526,
    label = "OH(23) + S(21257) <=> H2O(46) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3610, 'cm^3/(mol*s)'),
        n = 2.89,
        Ea = (-2.291, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3527,
    label = "H2O2(25) + S(21335) <=> HO2(24) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.97, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3528,
    label = "CH(26) + S(21257) <=> CH2(28) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(200000, 'cm^3/(mol*s)'), n=0, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3529,
    label = "CH2(28) + S(21257) <=> CH3(31) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(7.47, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3530,
    label = "CH2O(32) + S(21335) <=> HCO(29) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+11, 'cm^3/(mol*s)'), n=0, Ea=(6.96, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3531,
    label = "CH3(31) + S(21257) <=> CH4(33) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00248, 'cm^3/(mol*s)'),
        n = 4.44,
        Ea = (4.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3532,
    label = "CH3O(36) + S(21335) <=> CH2O(32) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3533,
    label = "CH2OH(35) + S(21335) <=> CH2O(32) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3534,
    label = "CHO2(57) + S(21335) <=> CO2(34) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3535,
    label = "CH3OH(37) + S(21335) <=> CH2OH(35) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001752, 'cm^3/(mol*s)'),
        n = 4.416,
        Ea = (12.058, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3536,
    label = "CH3O(36) + S(21257) <=> CH3OH(37) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3537,
    label = "C2H(38) + S(21257) <=> C2H2(39) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3538,
    label = "C2H3(41) + S(21335) <=> C2H2(39) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3539,
    label = "HCCOH(48) + S(21335) <=> HCCO(40) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3540,
    label = "HCCO(40) + S(21257) <=> CH2CO(42) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009794, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.869, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3541,
    label = "C2H3(41) + S(21257) <=> C2H4(43) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.052, 'cm^3/(mol*s)'), n=3.9, Ea=(0.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3542,
    label = "C2H3O(68) + S(21335) <=> CH2CO(42) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3543,
    label = "C2H3O(18) + S(21335) <=> CH2CO(42) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3544,
    label = "C2H5(44) + S(21335) <=> C2H4(43) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3545,
    label = "C2H5(44) + S(21257) <=> C2H6(45) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3546,
    label = "C2H5O(71) + S(21335) <=> CH3CHO(49) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3547,
    label = "HO2(24) + S(21335) <=> O2(2) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28230, 'cm^3/(mol*s)'),
        n = 2.483,
        Ea = (9.515, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3548,
    label = "butR1(3) + S(21257) <=> butane(1) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3549,
    label = "butR2(4) + S(21257) <=> butane(1) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3550,
    label = "S(149) + S(21335) <=> butROO2(6) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3551,
    label = "C4H9O2(8) + S(21257) <=> S(149) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3552,
    label = "C3H6O(748) + S(21335) <=> C3H5O(17) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3553,
    label = "C3H6O(912) + S(21335) <=> C3H5O(17) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.345e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3554,
    label = "C2H4O(832) + S(21335) <=> C2H3O(18) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3555,
    label = "C2H3O(18) + S(21257) <=> CH3CHO(49) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3556,
    label = "S(1038) + S(21335) <=> C2H3O(18) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00679, 'cm^3/(mol*s)'),
        n = 4.018,
        Ea = (2.617, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3557,
    label = "CCOO(1350) + S(21335) <=> C2H5O2(90) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3558,
    label = "C3H7(51) + S(21257) <=> C3H8(50) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3559,
    label = "C3H7(51) + S(21335) <=> C3H6(144) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3560,
    label = "C3H7(95) + S(21335) <=> C3H6(144) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.949e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3561,
    label = "COO(1544) + S(21335) <=> CH3O2(75) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3562,
    label = "C3H7(95) + S(21257) <=> C3H8(50) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3563,
    label = "butR1(3) + S(21335) <=> C4H8(96) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3564,
    label = "butR2(4) + S(21335) <=> C4H8(96) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3565,
    label = "butR2(4) + S(21335) <=> C4H8(143) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3566,
    label = "C3H6(144) + S(21335) <=> C3H5(1446) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.172e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3567,
    label = "S(2134) + S(21335) <=> S(2185) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3568,
    label = "C3H5(1446) + S(21335) <=> C3H4(2124) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3569,
    label = "C4H8(143) + S(21335) <=> C4H7(1663) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.345e-05, 'cm^3/(mol*s)'),
        n = 5.02,
        Ea = (3.65, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3570,
    label = "C4H8(96) + S(21335) <=> C4H7(1663) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002162, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3571,
    label = "CHO3(74) + S(21257) <=> S(2644) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3572,
    label = "C4H7(1663) + S(21335) <=> C4H6(2483) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3573,
    label = "S(1448) + S(21335) <=> S(2128) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3574,
    label = "C4H5(2849) + S(21257) <=> C4H6(2483) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3575,
    label = "S(1054) + S(21335) <=> S(3752) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.744e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3576,
    label = "S(2128) + S(21335) <=> S(3752) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3577,
    label = "S(4759) + S(21335) <=> S(4886) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3578,
    label = "S(3752) + S(21335) <=> S(4321) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3579,
    label = "S(6828) + S(21257) <=> S(6731) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3580,
    label = "C3H4(2124) + S(21335) <=> C3H3(2385) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06264, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.353, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3581,
    label = "S(4319) + S(21257) <=> S(3752) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3582,
    label = "S(4319) + S(21335) <=> S(9511) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3583,
    label = "S(1125) + S(21257) <=> C4H9O(147) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3584,
    label = "S(4321) + S(21335) <=> S(6711) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3585,
    label = "S(4319) + S(21335) <=> S(6711) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3586,
    label = "CH3CHO(49) + S(21335) <=> C2H3O(68) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3587,
    label = "S(12113) + S(21257) <=> S(12093) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3588,
    label = "S(1448) + S(21257) <=> S(1450) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3589,
    label = "S(5415) + S(21257) <=> S(4759) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3590,
    label = "C3H6O(748) + S(21257) <=> S(1449) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.379e+08, 'cm^3/(mol*s)'),
        n = 1.078,
        Ea = (10.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3591,
    label = "S(10030) + S(21335) <=> S(14812) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002162, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3592,
    label = "S(5415) + S(21335) <=> S(15301) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.932e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3593,
    label = "S(1448) + S(21335) <=> S(1054) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3594,
    label = "CH3O2(287) + S(21257) <=> COO(1544) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004969, 'cm^3/(mol*s)'),
        n = 4.304,
        Ea = (8.942, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3595,
    label = "S(19508) + S(21335) <=> S(13512) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3596,
    label = "S(9960) + S(21335) <=> S(10034) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002162, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3597,
    label = "S(1667) + S(21335) <=> S(4338) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.938e+12, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3598,
    label = "C4H8O3(11) + S(21335) <=> S(471) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3599,
    label = "C2H4O(832) + S(21257) <=> C2H5O(71) + S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3600,
    label = "S(14811) + S(21335) <=> S(1035) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004324, 'cm^3/(mol*s)'),
        n = 4.354,
        Ea = (9.271, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3601,
    label = "C4H8O3(14) + S(21335) <=> S(654) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.485, 'cm^3/(mol*s)'), n=3.39, Ea=(1.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3602,
    label = "S(13512) + S(21335) <=> S(20101) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3391, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3603,
    label = "S(20101) + S(21335) <=> S(21257) + S(23208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.344e+11, 'cm^3/(mol*s)'),
        n = 0.079,
        Ea = (1.316, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3604,
    label = "S(21335) + S(25762) <=> S(21257) + S(25386)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3605,
    label = "S(21335) + S(26110) <=> S(21257) + S(25762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1696, 'cm^3/(mol*s)'), n=2.52, Ea=(5.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3606,
    label = "S(21335) + S(27338) <=> S(21257) + S(26490)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3607,
    label = "S(21335) + S(27674) <=> S(21257) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3608,
    label = "S(21335) + S(27338) <=> S(21257) + S(27328)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3609,
    label = "S(21257) + S(28788) <=> S(21335) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005826, 'cm^3/(mol*s)'),
        n = 4.305,
        Ea = (1.115, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3610,
    label = "CO2(34) + S(21335) <=> S(30234)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.93e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (14.527, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3611,
    label = "C2H3O(18) + CO2(34) <=> S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.371,
        Ea = (11.201, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3612,
    label = "CO(27) + S(12091) <=> S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (274200, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (85.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3613,
    label = "H(22) + S(1066) <=> S(21334)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.76e+06, 'cm^3/(mol*s)'),
        n = 1.99,
        Ea = (5.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3614,
    label = "O(20) + S(21334) <=> OH(23) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.675e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3615,
    label = "H(22) + S(21334) <=> H2(21) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.24e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3616,
    label = "OH(23) + S(21334) <=> H2O(46) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3617,
    label = "HO2(24) + S(21334) <=> H2O2(25) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3618,
    label = "CH(26) + S(21334) <=> CH2(28) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.092e+09, 'cm^3/(mol*s)'),
        n = 1.075,
        Ea = (0.019, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3619,
    label = "CH2(28) + S(21334) <=> CH3(31) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3620,
    label = "HCO(29) + S(21334) <=> CH2O(32) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3621,
    label = "CH3(31) + S(21334) <=> CH4(33) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3622,
    label = "CH2OH(35) + S(21334) <=> CH3OH(37) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3623,
    label = "CH3O(36) + S(21334) <=> CH3OH(37) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3624,
    label = "C2H(38) + S(21334) <=> C2H2(39) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.206e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3625,
    label = "HCCO(40) + S(21334) <=> HCCOH(48) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3626,
    label = "HCCO(40) + S(21334) <=> CH2CO(42) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3627,
    label = "C2H3(41) + S(21334) <=> C2H4(43) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3628,
    label = "C2H5(44) + S(21334) <=> C2H6(45) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3629,
    label = "O2(2) + S(21334) <=> HO2(24) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3630,
    label = "butR1(3) + S(21334) <=> butane(1) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3631,
    label = "butR2(4) + S(21334) <=> butane(1) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3632,
    label = "butROO2(6) + S(21334) <=> S(149) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3633,
    label = "C4H9O2(8) + S(21334) <=> S(149) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3634,
    label = "C3H5O(17) + S(21334) <=> C3H6O(912) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3635,
    label = "C2H3O(18) + S(21334) <=> CH3CHO(49) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3636,
    label = "C2H3O(18) + S(21334) <=> S(1038) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3637,
    label = "C2H5O2(90) + S(21334) <=> S(1066) + CCOO(1350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3638,
    label = "C3H7(51) + S(21334) <=> C3H8(50) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3639,
    label = "CH3O2(75) + S(21334) <=> COO(1544) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3640,
    label = "C3H7(95) + S(21334) <=> C3H8(50) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3641,
    label = "C3H5(1446) + S(21334) <=> C3H6(144) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3642,
    label = "S(2185) + S(21334) <=> S(2134) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3643,
    label = "C4H7(1663) + S(21334) <=> C4H8(143) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3644,
    label = "C4H7(1663) + S(21334) <=> C4H8(96) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3645,
    label = "CHO3(74) + S(21334) <=> S(2644) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3646,
    label = "C4H5(2849) + S(21334) <=> S(1066) + C4H6(2483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3647,
    label = "S(4886) + S(21334) <=> S(1066) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3648,
    label = "S(4321) + S(21334) <=> S(3752) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3649,
    label = "S(6828) + S(21334) <=> S(1066) + S(6731)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3650,
    label = "C3H3(2385) + S(21334) <=> C3H4(2124) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.42e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3651,
    label = "S(4319) + S(21334) <=> S(3752) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3652,
    label = "S(1125) + S(21334) <=> C4H9O(147) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3653,
    label = "C2H3O(68) + S(21334) <=> CH3CHO(49) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3654,
    label = "S(12113) + S(21334) <=> S(1066) + S(12093)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3655,
    label = "S(1448) + S(21334) <=> S(1450) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3656,
    label = "S(5415) + S(21334) <=> S(1066) + S(4759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3657,
    label = "C3H6O(748) + S(21334) <=> S(1449) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3658,
    label = "S(14812) + S(21334) <=> S(1066) + S(10030)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3659,
    label = "CH3O2(287) + S(21334) <=> COO(1544) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3660,
    label = "S(10034) + S(21334) <=> S(1066) + S(9960)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3661,
    label = "S(471) + S(21334) <=> C4H8O3(11) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3662,
    label = "C2H4O(832) + S(21334) <=> C2H5O(71) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3663,
    label = "S(1035) + S(21334) <=> S(1066) + S(14811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3664,
    label = "S(654) + S(21334) <=> C4H8O3(14) + S(1066)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+10, 'cm^3/(mol*s)'),
        n = 1.004,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3665,
    label = "S(20101) + S(21334) <=> S(1066) + S(13512)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3666,
    label = "S(21334) + S(25762) <=> S(1066) + S(26110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.62e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3667,
    label = "S(21334) + S(28788) <=> S(1066) + S(29001)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.292e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3668,
    label = "S(1066) <=> S(21335)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 's^-1'), n=0.19, Ea=(52.549, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3669,
    label = "S(21334) + S(21335) <=> S(1066) + S(21257)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(26300, 'cm^3/(mol*s)'), n=2, Ea=(0.57, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3670,
    label = "S(27668) <=> S(28473)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(37990, 's^-1'), n=2.515, Ea=(48.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3671,
    label = "S(27674) <=> S(28473)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3672,
    label = "S(27674) <=> S(30009)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.007e+10, 's^-1'), n=0.18, Ea=(19.934, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3673,
    label = "CH2O(32) + S(3929) <=> S(4780)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.465e+13, 'cm^3/(mol*s)'),
        n = -0.659,
        Ea = (5.172, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3674,
    label = "S(4321) + S(22205) <=> S(4780)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3675,
    label = "O(20) + O(20) <=> O2(2)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.2e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 15.4, '[H][H]': 2.4, '[Ar]': 0.83},
    ),
)

entry(
    index = 3676,
    label = "O(20) + H(22) <=> OH(23)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3677,
    label = "O2(2) + H(22) <=> HO2(24)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.8e+18, 'cm^6/(mol^2*s)'),
            n = -0.86,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 1.5, 'CC': 1.5, 'O': 0, '[O][O]': 0, 'N#N': 0, '[Ar]': 0},
    ),
)

entry(
    index = 3678,
    label = "H(22) + H(22) <=> H2(21)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 0, 'CC': 3, 'O': 0, '[H][H]': 0, '[Ar]': 0.63},
    ),
)

entry(
    index = 3679,
    label = "H(22) + OH(23) <=> H2O(46)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.2e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 0.73, 'O': 3.65, '[Ar]': 0.38},
    ),
)

entry(
    index = 3680,
    label = "HCO(29) <=> H(22) + CO(27)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.87e+17, 'cm^3/(mol*s)'), n=-1, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 0},
    ),
)

entry(
    index = 3681,
    label = "O(20) + CO(27) <=> CO2(34)",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.8e+10, 'cm^3/(mol*s)'), n=0, Ea=(2.385, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6.02e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.5, 'CC': 3, 'O': 6, '[H][H]': 2, '[O][O]': 6, '[Ar]': 0.5},
    ),
)

entry(
    index = 3682,
    label = "H(22) + CH2(28) <=> CH3(31)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.04e+26, 'cm^6/(mol^2*s)'),
            n = -2.76,
            Ea = (1.6, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.562,
        T3 = (91, 'K'),
        T1 = (5840, 'K'),
        T2 = (8550, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3683,
    label = "H(22) + CH3(31) <=> CH4(33)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.39e+16, 'cm^3/(mol*s)'),
            n = -0.534,
            Ea = (0.536, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.62e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2.44, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2940, 'K'),
        T2 = (6960, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3684,
    label = "H(22) + HCO(29) <=> CH2O(32)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-0.26, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.47e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (0.425, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2760, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3685,
    label = "H(22) + CH2O(32) <=> CH2OH(35)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (3.6, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (6.53, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1290, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 3686,
    label = "H(22) + CH2O(32) <=> CH3O(36)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (2.6, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (5.56, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.758,
        T3 = (94, 'K'),
        T1 = (1560, 'K'),
        T2 = (4200, 'K'),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 3687,
    label = "H(22) + CH2OH(35) <=> CH3OH(37)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.055e+12, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (0.086, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.36e+31, 'cm^6/(mol^2*s)'),
            n = -4.65,
            Ea = (5.08, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 3688,
    label = "H(22) + CH3O(36) <=> CH3OH(37)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.43e+12, 'cm^3/(mol*s)'),
            n = 0.515,
            Ea = (0.05, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (14.08, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 3689,
    label = "H(22) + C2H(38) <=> C2H2(39)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1.9, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6464,
        T3 = (132, 'K'),
        T1 = (1320, 'K'),
        T2 = (5570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3690,
    label = "H(22) + C2H2(39) <=> C2H3(41)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2.4, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.8e+40, 'cm^6/(mol^2*s)'),
            n = -7.27,
            Ea = (7.22, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7507,
        T3 = (98.5, 'K'),
        T1 = (1300, 'K'),
        T2 = (4170, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3691,
    label = "H(22) + C2H3(41) <=> C2H4(43)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.08e+12, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (0.28, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3.32, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (208, 'K'),
        T1 = (2660, 'K'),
        T2 = (6100, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3692,
    label = "H(22) + C2H4(43) <=> C2H5(44)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (1.82, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6e+41, 'cm^6/(mol^2*s)'),
            n = -7.62,
            Ea = (6.97, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9753,
        T3 = (210, 'K'),
        T1 = (984, 'K'),
        T2 = (4370, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3693,
    label = "H(22) + C2H5(44) <=> C2H6(45)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1.58, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6.685, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2220, 'K'),
        T2 = (6880, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3694,
    label = "H2(21) + CO(27) <=> CH2O(32)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79.6, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84.35, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3695,
    label = "OH(23) + OH(23) <=> H2O2(25)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.4e+13, 'cm^3/(mol*s)'), n=-0.37, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.3e+18, 'cm^6/(mol^2*s)'),
            n = -0.9,
            Ea = (-1.7, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7346,
        T3 = (94, 'K'),
        T1 = (1760, 'K'),
        T2 = (5180, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3696,
    label = "OH(23) + CH3(31) <=> CH3OH(37)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.79e+18, 'cm^3/(mol*s)'),
            n = -1.43,
            Ea = (1.33, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4e+36, 'cm^6/(mol^2*s)'),
            n = -5.92,
            Ea = (3.14, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.412,
        T3 = (195, 'K'),
        T1 = (5900, 'K'),
        T2 = (6390, 'K'),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 3697,
    label = "CH(26) + CO(27) <=> HCCO(40)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+28, 'cm^6/(mol^2*s)'),
            n = -3.74,
            Ea = (1.936, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5757,
        T3 = (237, 'K'),
        T1 = (1650, 'K'),
        T2 = (5070, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3698,
    label = "CO(27) + CH2(28) <=> CH2CO(42)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.1e+11, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (4.51, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7.095, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1230, 'K'),
        T2 = (5180, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3699,
    label = "CH2(S)(30) + H2O(46) <=> CH3OH(37)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.82e+17, 'cm^3/(mol*s)'),
            n = -1.16,
            Ea = (1.145, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.88e+38, 'cm^6/(mol^2*s)'),
            n = -6.36,
            Ea = (5.04, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6027,
        T3 = (208, 'K'),
        T1 = (3920, 'K'),
        T2 = (10200, 'K'),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 3700,
    label = "CH3(31) + CH3(31) <=> C2H6(45)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.77e+16, 'cm^3/(mol*s)'),
            n = -1.18,
            Ea = (0.654, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.4e+41, 'cm^6/(mol^2*s)'),
            n = -7.03,
            Ea = (2.762, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.619,
        T3 = (73.2, 'K'),
        T1 = (1180, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3701,
    label = "C2H4(43) <=> H2(21) + C2H2(39)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(86.77, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.58e+51, 'cm^3/(mol*s)'),
            n = -9.3,
            Ea = (97.8, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7345,
        T3 = (180, 'K'),
        T1 = (1040, 'K'),
        T2 = (5420, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3702,
    label = "H2(21) + CH(26) <=> CH3(31)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.97e+12, 'cm^3/(mol*s)'),
            n = 0.43,
            Ea = (-0.37, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.82e+25, 'cm^6/(mol^2*s)'),
            n = -2.8,
            Ea = (0.59, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.578,
        T3 = (122, 'K'),
        T1 = (2540, 'K'),
        T2 = (9360, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3703,
    label = "H(22) + CH2CO(42) <=> C2H3O(18)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.865e+11, 'cm^3/(mol*s)'),
            n = 0.422,
            Ea = (-1.755, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.012e+42, 'cm^6/(mol^2*s)'),
            n = -7.63,
            Ea = (3.854, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.465,
        T3 = (201, 'K'),
        T1 = (1770, 'K'),
        T2 = (5330, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 3704,
    label = "CH3(31) + C2H5(44) <=> C3H8(50)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.43e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.71e+74, 'cm^6/(mol^2*s)'),
            n = -16.82,
            Ea = (13.065, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1527,
        T3 = (291, 'K'),
        T1 = (2740, 'K'),
        T2 = (7750, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

