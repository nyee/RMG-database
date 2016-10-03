#!/usr/bin/env python
# encoding: utf-8

name = 'iButanol_peroxy'
shortDesc = u'Peroxy chemistry for isobutanol'
longDesc = ''

entry(
    index = 1,
    label = 'Ap01 + OH <=> Ap10',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.807e+02, 'cm^3/(mol*s)'),
        n = 3.053,
        Ea = (22.492, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = 'Ap02 + H <=> Ap13',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.066e+05, 'cm^3/(mol*s)'),
        n = 2.559,
        Ea = (6.908, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = 'Ap03 + OH <=> Ap12',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.039e+01, 'cm^3/(mol*s)'),
        n = 3.233,
        Ea = (33.314, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = 'Ap05_a + Ap05_b <=> Ap13',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.663e+01, 'cm^3/(mol*s)'),
        n = 2.627,
        Ea = (9.333, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = 'Ap06 + CH3 <=> Ap12',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.145e+02, 'cm^3/(mol*s)'),
        n = 2.495,
        Ea = (6.841, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = 'Ap07 + HO2 <=> Ap13',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.710e-04, 'cm^3/(mol*s)'),
        n = 4.216,
        Ea = (15.096, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)
#use two irreversible reactions to handle submerged TS
entry(
    index = 7,
    label = 'Ap11 => Ap07 + HO2',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.74952e+11, 's^-1'),
        n = 0.258677,
        Ea = (11.598, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reversible = False,
    duplicate = True,
)

entry(
    index = 8,
    label = 'Ap07 + HO2 => Ap11',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24825e+15, 'cm^3/(mol*s)'),
        n = -3.92085,
        Ea = (5.113, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reversible = False,
    duplicate = True,
)

entry(
    index = 9,
    label = 'Ap09 + HO2 <=> Ap11',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.068e-02, 'cm^3/(mol*s)'),
        n = 3.724,
        Ea = (6.052, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = 'Ap09 + HO2 <=> Ap10',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.854e-02, 'cm^3/(mol*s)'),
        n = 4.029,
        Ea = (1.261, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = 'Ap10 <=> Ap11',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.873e-04, 's^-1'),
        n = 4.222,
        Ea = (10.634, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = 'Ap10 <=> Ap13',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.402e-07, 's^-1'),
        n = 5.146,
        Ea = (23.407, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 13,
    label = 'Ap11 <=> Ap12',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.756e+03, 's^-1'),
        n = 2.326,
        Ea = (20.469, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 14,
    label = 'Ap12 <=> Ap13',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.950e+01, 's^-1'),
        n = 2.800,
        Ea = (13.864, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 15,
    label = 'Ap01 + OH <=> Bp6',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.699e+03, 'cm^3/(mol*s)'),
        n = 2.618,
        Ea = (25.635, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 16,
    label = 'Bp7 <=> Bp9',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.632e-12, 's^-1'),
        n = 6.922,
        Ea = (24.001, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 17,
    label = 'Bp6 <=> Bp11 + H2O',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.248e+08, 's^-1'),
        n = 1.059,
        Ea = (7.914, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 18,
    label = 'Bp2 + OH <=> Bp9',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.117e+03, 'cm^3/(mol*s)'),
        n = 2.738,
        Ea = (26.445, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 19,
    label = 'Bp3 + HO2 <=> Bp9',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.254e-06, 'cm^3/(mol*s)'),
        n = 4.866,
        Ea = (4.213, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = 'Bp3 + HO2 <=> Bp7',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.176e-06, 'cm^3/(mol*s)'),
        n = 4.765,
        Ea = (0.880, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = 'Ap09 + HO2 <=> Bp7',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.119e-01, 'cm^3/(mol*s)'),
        n = 3.916,
        Ea = (8.708, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 22,
    label = 'Ap09 + HO2 <=> Bp6',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.459e+00, 'cm^3/(mol*s)'),
        n = 3.140,
        Ea = (1.462, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = 'Bp6 <=> Bp7',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.276e-03, 's^-1'),
        n = 4.176,
        Ea = (9.947, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)
#changed to f12-vtz with no scaling, since with scaling does not converge
entry(
    index = 24,
    label = 'Bp7 <=> Bp8',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.040e+12, 's^-1'),
        n = -0.441,
        Ea = (2.193e+01, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 25,
    label = 'Bp8 <=> acetone + OH + CH2O',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.859e+10, 's^-1'),
        n = 0.909,
        Ea = (3.772, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 26,
    label = 'Gp08 <=> Gp01 + H2O',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.283e+15, 's^-1'),
        n = -1.207,
        Ea = (10.028, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = 'Ap03 + OH <=> Gp08',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.055e+04, 'cm^3/(mol*s)'),
        n = 2.443,
        Ea = (38.116, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 28,
    label = 'Gp03 + OH <=> Gp10',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.587e-02, 'cm^3/(mol*s)'),
        n = 4.118,
        Ea = (33.183, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 29,
    label = 'Bp2 + OH <=> Gp11',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.475e+04, 'cm^3/(mol*s)'),
        n = 2.330,
        Ea = (28.047, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 30,
    label = 'Bp3 + HO2 <=> Gp09',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.291e-03, 'cm^3/(mol*s)'),
        n = 3.703,
        Ea = (11.001, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 31,
    label = 'Bp3 + HO2 <=> Gp11',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.809e+01, 'cm^3/(mol*s)'),
        n = 3.028,
        Ea = (5.919, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 32,
    label = 'Gp09 <=> Gp08',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.011e+02, 's^-1'),
        n = 2.622,
        Ea = (14.188, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 33,
    label = 'Gp09 <=> Gp10',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.602e+04, 's^-1'),
        n = 2.057,
        Ea = (20.011, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 34,
    label = 'Gp09 <=> Gp11',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.942e-06, 's^-1'),
        n = 4.976,
        Ea = (18.644, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 36,
    label = 'Gp09 <=> Gp14',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.170e+07, 's^-1'),
        n = 0.821,
        Ea = (21.373, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = 'Gp08 <=> Gp15 + OH + CH2O',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.212e+15, 's^-1'),
        n = -0.574,
        Ea = (25.818, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

