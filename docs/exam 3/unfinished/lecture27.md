<span>schedule</span>

-   31 Oct - Deflection of Beams and Shafts, HW8 Due

-   2 Nov - Deflection of Beams and Shafts

-   5 Nov - SPTE, Deflection of Beams and Shafts

-   7 Nov - Deflection of Beams and Shafts, HW9 Due

-   9 Nov - Stress Concentration

<span>outline</span>

strain rosettes
===============

<span>rosettes</span>

-   Normal strain is fairly easy to measure using a strain gage

-   Shear strain is more difficult to measure directly, so instead a “rossette” of normal strain gages is used

-   We can use the strain transformation equations to determine *τ*<sub>*x**y*</sub>

<span>rosettes</span>

-   Usually, we have *θ*<sub>*a*</sub> = 0, *θ*<sub>*b*</sub> = 90 and *θ*<sub>*c*</sub> = 45 OR *θ*<sub>*a*</sub> = 0, *θ*<sub>*b*</sub> = 60 and *θ*<sub>*c*</sub> = 120
    $$\\begin{aligned}
                \\epsilon\_{a} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} + \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\cos 2 \\theta\_a + \\frac{\\gamma\_{xy}}{2} \\sin 2\\theta\_a \\\\
                \\epsilon\_{b} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} + \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\cos 2 \\theta\_b + \\frac{\\gamma\_{xy}}{2} \\sin 2\\theta\_b \\\\
                \\epsilon\_{c} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} + \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\cos 2 \\theta\_c + \\frac{\\gamma\_{xy}}{2} \\sin 2\\theta\_c
            \\end{aligned}$$

<span>example 10.8</span>

<img src="../figures/example-10-8" alt="The readings from the rosette shown are \epsilon_a=60\mu\epsilon, \epsilon_b=135\mu\epsilon and \epsilon_c=264\mu\epsilon. Find the in-plane principal strains and their directions." style="width:60.0%" />

material property relationships
===============================

<span>generalized hooke’s law</span>

-   We have previously used Hooke’s Law in 2D, in 3D we have
    $$\\begin{aligned}
                \\epsilon\_x &= \\frac{1}{E}\[\\sigma\_x - \\nu(\\sigma\_y + \\sigma\_z)\]\\\\
                \\epsilon\_y &= \\frac{1}{E}\[\\sigma\_y - \\nu(\\sigma\_x + \\sigma\_z)\]\\\\
                \\epsilon\_z &= \\frac{1}{E}\[\\sigma\_z - \\nu(\\sigma\_x + \\sigma\_y)\]
            \\end{aligned}$$

<span>generalized hooke’s law</span>

-   And in shear
    $$\\begin{aligned}
                \\gamma\_{xy} &= \\frac{1}{G} \\tau\_{xy}\\\\
                \\gamma\_{yz} &= \\frac{1}{G} \\tau\_{yz}\\\\
                \\gamma\_{xz} &= \\frac{1}{G} \\tau\_{xz}
            \\end{aligned}$$

<span>dilatation</span>

-   When a material deforms it often changes volume

-   The change in volume per unit volume is called “volumetric strain” or dilatation
    $$e = \\frac{\\partial V}{d V} = \\epsilon\_x + \\epsilon\_y + \\epsilon\_z = \\frac{1-2\\nu}{E}(\\sigma\_x+\\sigma\_y+\\sigma\_z)$$

<span>hydrostatic pressure</span>

-   One way of characterizing volumetric response is to apply hydrostatic pressure (equal compression on all sides with no shear)

-   Under this case, we have
    $$\\frac{p}{e} = -\\frac{E}{3(1-2\\nu)}$$

-   We call the term on the right (with no negative sign) the bulk modulus, *k*

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
