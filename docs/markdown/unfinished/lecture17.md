<span>schedule</span>

-   3 Oct - Transverse Shear, HW5 Due

-   5 Oct - Transverse Shear

-   8 Oct - Exam 2 Review, HW6 Due

-   10 Oct - Exam 2

-   12 Oct - Combined Loading

<span>outline</span>

the shear formula
=================

<span>shear formula</span>

-   Internal shear causes a more complicated deformation state, so we will use an indirect method to find the shear stress-strain distribution

-   We will consider equilibrium along a section of a beam, then we will consider another section

<span>equilibrium</span>

<img src="../figures/beam-fbd" alt="image" style="width:90.0%" />

<span>equilibrium</span>

<img src="../figures/fbd-newsection" alt="image" style="width:50.0%" />

<span>equilibrium</span>

-   There must be a shear force along the bottom to equilibrate the different stresses on either side of the section

-   If we assume that this shear is constant through the thickness, we obtain the following from equilibrium
    ∑*F*<sub>*x*</sub> = 0 = ∫<sub>*A*<sup>′</sup></sub>*σ*<sup>′</sup>*d**A*<sup>′</sup> − ∫<sub>*A*<sup>′</sup></sub>*σ**d**A*<sup>′</sup> − *τ*(*t**d**x*)=0

<span>equilibrium</span>
$$\\begin{aligned}
        0 &= \\int\_{A^\\prime} \\left( \\frac{M + dM}{I} \\right) y dA^\\prime - \\int\_{A^\\prime} \\left( \\frac{M}{I} \\right)y dA^\\prime - \\tau(t dx) \\\\
        \\left( \\frac{M}{I} \\right) \\int\_{A^\\prime} y dA^\\prime &= \\tau (t dx)\\\\
        \\tau &= \\frac{1}{It} \\left( \\frac{dM}{dx} \\right)\\int\_{A^\\prime} y dA^\\prime
    \\end{aligned}$$

<span>shear formula</span>

-   In this formula, recall that $V = \\frac{dM}{dx}$

-   We also call *Q* the moment of the area *A*<sup>′</sup> which is equal to ∫<sub>*A*<sup>′</sup></sub>*y**d**A*<sup>′</sup>

-   We can also write *Q* in terms of the centroid
    $$\\label{eq:Q}
                Q = \\bar{y}^\\prime A^\\prime$$

<span>shear formula</span>

-   Simplified, the shear formula is
    $$\\tau = \\frac{VQ}{It}$$

-   *Q* poses the greatest difficulty in calculations, so we will consider a few examples

<span>Q</span>

-   *Q* represents the moment of the cross-sectional area above (or below) the point at which the shear stress is being calculated

-   We apply  \[eq:Q\] to that area

<span>Q</span>

<img src="../figures/Q" alt="Examples of Q." style="width:40.0%" />

<span>shear formula limitations</span>

-   A major assumption made is that the shear stress was constant through the thickness, essentially we have found the average shear

-   This is more accurate the more slender a beam is (small *b* and large *h*)

-   The formula is also not accurate for cross sections that change or have boundaries that are not right angles

<span>procedure</span>

-   First we find the internal shear, *V*

-   Find *I*, the moment of inertia (of the entire section) about the neutral axis

-   Find *t* from an imaginary cross-section at the point of interest

-   Calculate *Q* from either the area above or below the point of interest

-   *τ* acts in the same direction as *V* (and must be equilibrated on other faces)

<span>example 7.1</span>

<img src="../figures/example-7-1" alt="Determine the maximum stress needed by a glue to hold the boards together." style="width:50.0%" />

<span>example 7.3</span>

<img src="../figures/example-7-3" alt="If V=\SI{80}{kN}, plot the shear-stress distribution." style="width:70.0%" />

group problems
==============

<span>group one</span>

<img src="../figures/group-7-1" alt="Find Q and t that would be used to find the shear stress at A." style="width:40.0%" />

<span>group two</span>

<img src="../figures/group-7-2" alt="Find Q and t that would be used to find the shear stress at A." style="width:40.0%" />

<span>group three</span>

<img src="../figures/group-7-3" alt="Find Q and t that would be used to find the shear stress at A." style="width:60.0%" />
