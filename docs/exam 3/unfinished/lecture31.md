<span>schedule</span>

-   9 Nov - Superposition

-   12 Nov - Statically indeterminate beams and shafts

-   14 Nov - Statically indeterminate beams and shafts, HW10 Due

-   16 Nov - Exam 3 Review

-   19 Nov - Exam 3

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

superposition
=============

<span>superposition</span>

-   The differential equation *E**I**d*<sup>4</sup>*v*/*d**x*<sup>4</sup> = *w*(*x*) satisfies the requirements for superposition

-   *w*(*x*) is linearly related to *v*(*x*)

-   Load does not significantly change the shape of the beam

<span>superposition</span>

-   This means we can superpose multiple deflection solutions from simpler cases

-   Appendix C in the text has many solutions that can be superposed

<span>example 12.13</span>

<img src="../figures/example-12-13" alt="Use superposition to find the displacement at C and the slope at A" style="width:70.0%" />

<span>example 12.15</span>

<img src="../figures/example-12-15" alt="Use superposition to find the displacement at C" style="width:70.0%" />

<span>example 12.16</span>

<img src="../figures/example-12-16" alt="The steel bar is supported by springs with k=\US{15}{kip/ft} originally unstretched. For the force shown, determine the displacement at C. Take E_{st}=\US{29}{Msi} and I=\US{12}{in^4}." style="width:70.0%" />
