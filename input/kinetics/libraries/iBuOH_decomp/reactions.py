#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "iBuOH <=> iC4H8 + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.0132, 0.1316, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.16e+94, 's^-1'), n=-23.93, Ea=(112313, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.83e+89, 's^-1'), n=-22.19, Ea=(112653, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.97e+82, 's^-1'), n=-19.93, Ea=(111845, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.57e+71, 's^-1'), n=-16.66, Ea=(107734, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.13e+51, 's^-1'), n=-10.82, Ea=(96480, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.24e+27, 's^-1'), n=-4, Ea=(80732, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.0132, 0.1316, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(6.74e+41, 's^-1'), n=-9.46, Ea=(74714.8, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.72e+38, 's^-1'), n=-8.4, Ea=(74113, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.73e+31, 's^-1'), n=-6.17, Ea=(72051.7, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.18e+24, 's^-1'), n=-3.95, Ea=(69694.5, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.1e+16, 's^-1'), n=-1.46, Ea=(66679.9, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.83e+09, 's^-1'), n=0.61, Ea=(63570, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
    longDesc = 
u"""
/ Replacing with SJK calculations (two PLOG fit, makes the system stiff)
""",
)

entry(
    index = 3,
    label = "iBuOH <=> CH3 + C3H7O-N2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.0132, 0.1316, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(3.86e+123, 's^-1'), n=-32, Ea=(138678, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.93e+112, 's^-1'), n=-28.32, Ea=(136273, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.13e+104, 's^-1'), n=-25.73, Ea=(136287, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.15e+98, 's^-1'), n=-23.67, Ea=(136787, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.95e+24, 's^-1'), n=-2.35, Ea=(90619.7, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.4e+63, 's^-1'), n=-13.26, Ea=(120315, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.0132, 0.1316, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.33e+76, 's^-1'), n=-18.54, Ea=(107647, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.47e+70, 's^-1'), n=-16.65, Ea=(106177, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.83e+65, 's^-1'), n=-15.18, Ea=(105115, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.67e+56, 's^-1'), n=-12.32, Ea=(102257, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(-1.01e+61, 's^-1'), n=-11.88, Ea=(132857, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.71e+38, 's^-1'), n=-6.52, Ea=(95614.2, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 5,
    label = "iBuOH <=> C3H7-2 + CH2OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.0132, 0.1316, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(9.35e+139, 's^-1'), n=-30.73, Ea=(133785, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.73e+109, 's^-1'), n=-27.23, Ea=(131350, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.08e+102, 's^-1'), n=-24.97, Ea=(131632, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.09e+96, 's^-1'), n=-22.81, Ea=(131400, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.37e+83, 's^-1'), n=-18.96, Ea=(127037, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.72e+64, 's^-1'), n=-13.56, Ea=(116921, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.0132, 0.1316, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(3.48e+71, 's^-1'), n=-17.07, Ea=(101522, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.36e+66, 's^-1'), n=-15.58, Ea=(100253, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.01e+62, 's^-1'), n=-13.96, Ea=(98924.6, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.42e+53, 's^-1'), n=-11.35, Ea=(96267.5, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.42e+43, 's^-1'), n=-8.27, Ea=(92804.1, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.22e+35, 's^-1'), n=-5.71, Ea=(89722.1, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

