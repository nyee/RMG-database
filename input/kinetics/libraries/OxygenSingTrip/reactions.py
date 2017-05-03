#!/usr/bin/env python
# encoding: utf-8

name = "OxygenSingTrip"
shortDesc = u"reactions of singlet and triplet oxygen"
longDesc = u"""
Reactions of singlet and triplet oxygen. added based on the new adjacency list representation in 2014 by Connie
"""
entry(
    index = 1,
    label = "O2S => O2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(0.00023, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "O2S => O2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.05, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'[O][O]': 5.43, 'O=C=O': 4.29},
    ),
)

entry(
    index = 3,
    label = "O2S <=> O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3e+06, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C1=CC=CC=C1': 1.067, 'O': 1.783, '[H][H]': 1, '[O][O]': 0.34, 'N#N': 0.028, '[C]=O': 14, '[Ar]': 0.00166},
    ),
)

