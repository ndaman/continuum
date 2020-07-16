<span>schedule</span>

-   2 Nov - Deflection of Beams and Shafts

-   5 Nov - SPTE, Deflection of Beams and Shafts

-   7 Nov - Deflection of Beams and Shafts, HW9 Due

-   9 Nov - Stress Concentration

<span>outline</span>

deflection of beams and shafts
==============================

<span>elastic curve</span>

-   Before finding the exact displacement, it is useful to sketch the approximate deformed shape of a beam

-   For difficult beams, it is useful to draw the moment curve first

-   Positive internal moment tends to bend the beam concave up, while negative moment tends to bend the beam concave down

<span>elastic curve</span>

<img src="../figures/elastic-curve" alt="image" style="width:60.0%" />

<span>elastic curve</span>

<img src="../figures/elastic-curve2" alt="image" style="width:60.0%" />

<span>moment-curvature</span>

-   In Chapter 6 we compared the strain in a segment of a beam to the radius of curvature and found
    $$\\frac{1}{\\rho} = -\\frac{\\epsilon}{y}$$

-   Since Hooke’s Law applies, *ϵ* = *σ*/*E* = −*M**y*/*E**I*, substituting gives
    $$\\frac{1}{\\rho} = \\frac{M}{EI}$$

<span>sign convention</span>

<img src="../figures/curvature" alt="\rho is positive when the center of the arc is above the beam, negative when it is below." style="width:80.0%" />

slope and displacement
======================

<span>curvature</span>

-   When talking about displacement in beams, we use the coordinates *v* and *x*, where *v* is the vertical displacement and *x* is the horizontal position

-   In this notation, curvature is formally related to displacement according to
    $$\\label{eq:beam-formal}
                \\frac{1}{\\rho} = \\frac{d^2v/dx^2}{\[1+(dv/dx)^2\]^{3/2}} = \\frac{M}{EI}$$

<span>curvature</span>

-   Equation  \[eq:beam-formal\] is difficult to solve in general, but for cases of small displacement, (*d**v*/*d**x*)<sup>2</sup> will be negligible compared to 1, which then simplifies to
    $$\\frac{d^2v}{dx^2} = \\frac{M}{EI}$$

<span>flexural rigidity</span>

-   In general, *M*, is a function of *x*, but *E**I* (known as the flexural rigidity) is a constant along the length of the beam

-   In this case, we can say
    $$\\begin{aligned}
                EI\\frac{d^2v}{dx^2} &= M(x) \\\\
                EI\\frac{d^3v}{dx^3} &= V(x) \\\\
                EI\\frac{d^4v}{dx^4} &= w(x)
            \\end{aligned}$$

<span>boundary conditions</span>

-   If a support restricts displacement, but not rotation, we will have a boundary condition of *v* = 0 at that point

-   Supports that restrict rotation give a boundary condition that *θ* = 0

<span>continuity conditions</span>

-   If we have a piecewise function for *M*(*x*), not all integration constants can be found from the boundary conditions

-   Instead, we must also use continuity conditions to ensure that the slope and displacement are continuous at every point

-   In other words, for two sets of functions, *θ*<sub>1</sub>(*x*) and *v*<sub>1</sub>(*x*), *θ*<sub>2</sub>(*x*), and *v*<sub>2</sub>(*x*), *θ*<sub>1</sub>(*a*)=*θ*<sub>2</sub>(*a*) and *v*<sub>1</sub>(*a*)=*v*<sub>2</sub>(*a*)

<span>slope</span>

-   For small displacements, we have
    *θ* ≈ tan*θ* = *d**v*/*d**x*

<span>example 12.1</span>

<img src="../figures/example-12-1" alt="Determine the maximum deflection if EI is constant." style="width:70.0%" />

<span>example 12.4</span>

<img src="../figures/example-12-4" alt="Determine the displacement at C, EI is constant." style="width:70.0%" />

discontinuity functions
=======================

<span>discontinuity functions</span>

-   Direct integration can be very cumbersome if multiple loads or boundary conditions are applied

-   Instead of using a piecewise function, we can use discontinuity functions

<span>Macaulay functions</span>

-   Macaulay functions can be used to describe various loading conditions, the general definition is
    $$\\langle x-a\\rangle^n = \\begin{cases}
                    0 & \\text{for} x &lt; a\\\\
                    (x-a)^2 & \\text{for} x \\ge a
            \\end{cases}$$

<span>singularity functions</span>

-   Singularity functions are used for concentrated forces and can be written
    $$w = P\\langle x-a\\rangle^{-1} = \\begin{cases}
                    0 & \\text{for} x\\ne a\\\\
                    P & \\text{for} x=a
            \\end{cases}$$

<span>discontinuity functions</span>

<img src="../figures/discontinuity" alt="image" style="width:80.0%" />

<span>example 12.5</span>

<img src="../figures/example-12-5" alt="image" style="width:80.0%" />
