#!/usr/bin/env python
# encoding: utf-8

name = 'iButanol_peroxy'
shortDesc = u'Peroxy chemistry for isobutanol'
longDesc = ''

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
    index = 1993,
    label = "iBuOH + O2 <=> C4H9Oi1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (51870, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)
