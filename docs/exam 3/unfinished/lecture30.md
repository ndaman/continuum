<span>schedule</span>

-   7 Nov - Deflection of Beams and Shafts, HW9 Due

-   9 Nov - Deflection of Beams and Shafts

-   12 Nov - Deflection of Beams and Shafts

-   14 Nov - Deflection of Beams and Shafts, HW10 Due

<span>outline</span>

discontinuity functions
=======================

<span>discontinuity functions</span>

-   Direct integration can be very cumbersome if multiple loads or boundary conditions are applied

-   Instead of using a piecewise function, we can use discontinuity functions

<span>Macaulay functions</span>

-   Macaulay functions can be used to describe various loading conditions, the general definition is
    $$\\langle x-a\\rangle^n = \\begin{cases}
                    0 & \\text{for } x &lt; a\\\\
                    (x-a)^n & \\text{for } x \\ge a
            \\end{cases}$$

-   Macaulay functions integrate like usual polynomials

<span>singularity functions</span>

-   Singularity functions are used for concentrated forces and can be written
    $$w = P\\langle x-a\\rangle^{-1} = \\begin{cases}
                    0 & \\text{for } x\\ne a\\\\
                    P & \\text{for } x=a
            \\end{cases}$$

-   When *n* = −1, −2, singularity functions integrate such that ∫⟨*x* − *a*⟩<sup>*n*</sup>*d**x* = ⟨*x* − *a*⟩<sup>*n* + 1</sup>

<span>discontinuity functions</span>

<img src="../figures/discontinuity" alt="image" style="width:90.0%" />

<span>example 12.5</span>

<img src="../figures/example-12-5" alt="image" style="width:80.0%" />

group problems
==============

<span>group one</span>

<img src="../figures/group-12-1" alt="Find the maximum deflection using either direct integration or discontinuity functions." style="width:70.0%" />

<span>group two</span>

<img src="../figures/group-12-2" alt="Find the maximum deflection using either direct integration or discontinuity functions." style="width:70.0%" />

<span>group three</span>

<img src="../figures/group-12-3" alt="Find the maximum deflection using either direct integration or discontinuity functions." style="width:70.0%" />
