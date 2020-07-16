<span>schedule</span>

-   3 Dec - Buckling, Final Review

-   5 Dec - Final Review

-   12 Dec - 9:00 - 10:50 Final Exam

<span>outline</span>

buckling
========

<span>stability</span>

-   In enineering problems, stability and instability relate how an object behaves when it experiences some random perturbation

-   A stable aircraft has aerodynamic features that tend to keep it flying level, small bumps of wind that would cause it to rotate will eventually get pushed back to level

-   Some aircraft are designed to be unstable (can have a tighter turn radius), but they need to be actively controlled, as a small perturbation will cause them to spiral out of control

<span>buckling</span>

-   For long and slender structures, stability comes into play in the form of buckling

-   A structure that is subject to buckling is generally referred to as a column

-   Buckling is usually a very sudden and drastic failure, so we need to design columns to avoid buckling

<span>critical load</span>

-   The critical load is the maximum load a column can hold before buckling

-   We can model the critical load by considering the column as a rigid truss with a spring force acting to maintain stability

-   When the loading force overcomes the spring force, buckling occurs

<span>critical load</span>

<img src="../figures/buckling-truss" alt="image" style="width:40.0%" />

<span>critical load</span>

-   The balance of forces will be
    *F* = *k**Δ* = *P*tan*θ*

-   For small *θ*, we can further say that *Δ* = *θ*(*L*/2) and tan*θ* = *θ*

<span>critical load</span>

-   We find that, for stability, we need
    $$P &lt; \\frac{kL}{4}$$

ideal pin-supported column
==========================

<span>ideal column</span>

-   Our previous analysis treated a column as a two-member truss with a spring, but we can be more precise

-   An ideal column is made of homogeneous linear elastic material and is perfectly straight before loading

-   The load is assumed to be applied through the centroid of the cross section

<span>euler-bernoulli</span>

-   We can treat the column as a beam and use the familiar relationship
    $$EI \\frac{d^2v}{dx^2} = M$$

<span>euler-bernoulli</span>

<img src="../figures/column-fbd" alt="image" style="width:40.0%" />

<span>solution</span>

-   We see by equilibrium that *M* = −*P**v*, which gives the differential equation
    $$\\begin{aligned}
                EI \\frac{d^2v}{dx^2} &= -Pv \\\\
                \\frac{d^2v}{dx^2} + \\frac{P}{EI}v &= 0
            \\end{aligned}$$

-   Which has the solution
    $$v = C\_1 \\sin \\left( \\sqrt{\\frac{P}{EI}}x \\right) + C\_2 \\cos \\left( \\sqrt{\\frac{P}{EI}}x \\right)$$

<span>boundary conditions</span>

-   We know that for *v* = 0 at *x* = 0, *C*<sub>2</sub> = 0

-   We also know that *v* = 0 at *x* = *L* which gives
    $$C\_1 \\sin \\left( \\sqrt{\\frac{P}{EI}}L \\right) = 0$$

-   *C*<sub>1</sub> = 0 would give the trivial solution, or we can say that
    $$\\sqrt{\\frac{P}{EI}}L = n \\pi$$

<span>critical load</span>

-   The smallest value where this occurs is when *n* = 1 and gives the critical load of
    $$P\_{cr} = \\frac{\\pi^2 EI}{L^2}$$

-   This is sometimes called the “Euler Load”

-   We can increase *P*<sub>*c**r*</sub> by decreasing *L*, increasing *E*, or increasing *I*

<span>radius of gyration</span>

-   Sometimes we desire to find the critical stress instead of the critical load

-   We re-formulate the equation with *I* = *A**r*<sup>2</sup> (where *r* is the radius of gyration)

-   This gives
    $$\\sigma\_{cr} = \\frac{\\pi^2 E}{(L/r)^2}$$

-   L/r is often called the slenderness ratio

<span>example 13.1</span>

<img src="../figures/example-13-1" alt="Find the largest axial load the A992 steal member shown can support before it buckles or yields, use \sigma_y=\US{50}{ksi}." style="width:40.0%" />
