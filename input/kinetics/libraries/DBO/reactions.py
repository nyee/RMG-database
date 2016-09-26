#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "R2 <=> R2a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348e+12, 's^-1'), n=0.323, Ea=(32.163, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "R2 <=> R2c",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.497e+12, 's^-1'), n=0.261, Ea=(26.67, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "R4 <=> R4a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+11, 's^-1'), n=0.5, Ea=(25.798, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "R4 <=> R4b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.181e+13, 's^-1'), n=0.071, Ea=(19.363, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "R6 <=> R6a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+11, 's^-1'), n=0.5, Ea=(25.798, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "R6 <=> R6b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.181e+13, 's^-1'), n=0.071, Ea=(19.363, 'kcal/mol'), T0=(1, 'K')),
)

