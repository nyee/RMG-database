#!/usr/bin/env python
# encoding: utf-8

name = "publishedIBuOH_peroxyRemoved"
shortDesc = u""
longDesc = u"""

"""
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



