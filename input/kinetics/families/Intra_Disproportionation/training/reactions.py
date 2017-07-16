#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "C10H10 <=> C10H10-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.949e+11, 's^-1'), n=0.486, Ea=(5.464, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3H3_C7H7_Matsugi""",
    longDesc = 
u"""
Taken from entry: W8 <=> W10
""",
)

