#!/usr/bin/env python
# encoding: utf-8

name = "phenol_pyr"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "PHENOXY <=> bridgedPhenoxy",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.68e+11, 's^-1'), n=0.57, Ea=(49.53, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "bridgedPhenoxy <=> cpdylCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+12, 's^-1'), n=0.14, Ea=(8.11, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "cpdylCO <=> CPDYL + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.36e+12, 's^-1'), n=0.43, Ea=(4.43, 'kcal/mol'), T0=(1, 'K')),
)

