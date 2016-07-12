# Coordinates for s1_3_3_ane (angstroms):
#   C    0.0000    0.0000    0.0000
#   C    1.2830    0.6844    0.2417
#   C    0.0412    1.4322    0.5095
#   C    2.5464    0.3977    0.9450
#   C    2.5443    0.9076   -0.4877
#   H   -0.3115   -0.7661    0.6959
#   H   -0.3141   -0.1549   -1.0225
#   H   -0.2457    2.2133   -0.1802
#   H   -0.2435    1.6021    1.5382
#   H    2.8215   -0.6353    1.1042
#   H    2.8711    1.0823    1.7157
#   H    2.8183    0.2080   -1.2646
#   H    2.8677    1.9256   -0.6531
conformer(
    label = 's1_3_3_ane',
    E0 = (155.58, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(68.0626, 'amu')),
        NonlinearRotor(
            inertia = ([47.1981, 119.823, 119.827], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([290.635, 296.38, 296.429, 618.812, 785.405, 785.405, 842.785, 903.901, 903.908, 935.608, 998.988, 1018.22, 1044.68, 1064.98, 1064.99, 1094.11, 1158.05, 1167.69, 1180.5, 1180.52, 1429.3, 1451.83, 1451.83, 1486.31, 1601.97, 3109.71, 3109.72, 3112.42, 3112.93, 3190.35, 3191.74, 3202.47, 3202.47], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

# Thermodynamics for s1_3_3_ane:
#   Enthalpy of formation (298 K)   =    40.872 kcal/mol
#   Entropy of formation (298 K)    =    69.989 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      21.091      40.914      70.130      19.875
#            400      28.077      43.376      77.165      12.510
#            500      34.241      46.501      84.113       4.445
#            600      39.311      50.187      90.819      -4.304
#            800      47.244      58.883     103.273     -23.735
#           1000      53.044      68.943     114.472     -45.529
#           1500      61.457      97.847     137.797    -108.848
#           2000      65.611     129.707     156.100    -182.492
#           2400      67.908     156.430     168.274    -247.426
#    =========== =========== =========== =========== ===========
thermo(
    label = 's1_3_3_ane',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.11911, -0.0101141, 0.000177109, -2.80334e-07, 1.42933e-10, 18712.3, 9.09401],
                Tmin = (10, 'K'),
                Tmax = (608.931, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.88589, 0.0519808, -3.16426e-05, 9.29168e-09, -1.05137e-12, 19023.7, 31.638],
                Tmin = (608.931, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (155.577, 'kJ/mol'),
    ),
)

