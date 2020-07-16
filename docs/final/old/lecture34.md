<span>schedule</span>

-   28 Nov - Exam 3 Return, Stress Concentrations

-   30 Nov - Stress Concentrations, Buckling

-   3 Dec - Buckling, Final Review

-   5 Dec - Final Review

<span>outline</span>

exam
====

<span>exam stats</span>

-   Pre-curve average: 56.3%

-   Post-curve average: 71%

-   Curve formula: curved score = 0.75original score + 28.75

stress concentration factors
============================

<span>stress concentration</span>

-   Our textbook splits the idea of concentration factors across multiple chapters

-   4.7, 5.8, 6.9

-   The basic idea of a stress concentration factor is that some geometry causes the maximum stress to be greater than the ’nominal’ stress

<span>stress concentration</span>

-   Stress concentrations occur when there is a sudden change in cross-sectional area

-   Features such as holes and fillets will have a stress concentration factor
    $$K = \\frac{\\sigma\_{max}}{\\sigma\_{avg}}$$

<span>stress concentration</span>

-   The exact value of the stress concentration factor can be derived for simple shapes, but in practice it is usually looked up on a chart or figure

-   The value of *K* depends on the ratio of the radius and depth of the feature relative to the total object depth

<span>fillets</span>

<img src="../figures/stress-concentration-fillet" alt="image" style="width:70.0%" />

<span>holes</span>

<img src="../figures/stress-concentration-hole" alt="image" style="width:70.0%" />

<span>example</span>

<img src="../figures/stress-concentration-example" alt="If \sigma_{allow}=\si{120}{MPa}, find the maximum axial force, P." style="width:80.0%" />

<span>stress concentration in torsion</span>

-   We can also have stress concentration in torsion

-   For circular shafts, this is usually around a filleted shaft as shown in the next slide

-   The maximum shear can be found with
    $$\\tau\_{max} = K \\frac{Tc}{J}$$

<span>fillet</span>

<img src="../figures/stress-concentration-torsion" alt="image" style="width:70.0%" />

<span>example 5.14</span>

<img src="../figures/example-5-14" alt="Determine the maximum stress in the shaft due to the applied torques. The shoulder fillet has a radius of r=\si{6}{mm}" style="width:70.0%" />

<span>beams</span>

-   We can also have a stress concentration in a beam

-   The maximum stress can be found with
    $$\\sigma\_{max} = K \\frac{Mc}{I}$$

<span>fillet</span>

<img src="../figures/beam-fillet" alt="image" style="width:70.0%" />

<span>notch</span>

<img src="../figures/beam-notch" alt="image" style="width:70.0%" />

<span>example 6.20</span>

<img src="../figures/example-6-20" alt="Determine the maximum normal stress for a steel bar with a shoulder fillet as shown." style="width:70.0%" />
