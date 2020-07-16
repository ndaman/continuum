<span>schedule</span>

-   22 Oct - Mohr’s Circle

-   24 Oct - Strain Transformation, HW7 Due

-   26 Oct - Strain Transformation

-   29 Oct - Deflection of Beams and Shafts

<span>outline</span>

plane stress transformation
===========================

<span>plane stress</span>

-   In general, the state of stress at a point is characterized by six stress components

-   In practice, this is rare, as most stresses and forces act in the same plane

-   This case is referred to as plane stress

<span>transformation</span>

<img src="../figures/transformation" alt="image" style="width:80.0%" />

<span>procedure</span>

-   If the state of stress (*σ*<sub>*x*</sub>, *σ*<sub>*y*</sub>, *τ*<sub>*x**y*</sub>) is known for a known axis system *x* and *y*, we can find the stress relative to some rotated coordinate system

-   We do this by considering a section of the element perpendicular to the *x*<sup>′</sup> axis

-   Sum of forces in *x* and *y* will give *σ*<sub>*x*<sup>′</sup></sub> and *τ*<sub>*x*<sup>′</sup>*y*<sup>′</sup></sub>

-   A second section is needed to find *σ*<sub>*y*<sup>′</sup></sub>, perpendicular to the *y*<sup>′</sup> axis

<span>procedure</span>

<img src="../figures/transformation-2" alt="image" style="width:80.0%" />

<span>example 9.1</span>

<img src="../figures/example-9-1" alt="Represent the state of stress shown on the fuselage section on an element rotated 30^\circ clockwise from the position shown." style="width:80.0%" />

general equations
=================

<span>general equations</span>

-   We can follow the methodology from the previous section to develop equations for some arbitrary rotation and a completely general state of stress

-   We use some trig identities to simplify the formulae
    $$\\begin{aligned}
                \\sigma\_{x^\\prime} &= \\frac{\\sigma\_x+\\sigma\_y}{2} + \\frac{\\sigma\_x-\\sigma\_y}{2} \\cos 2\\theta + \\tau\_{xy} \\sin 2\\theta \\\\
                \\tau\_{x^\\prime y^\\prime} &= - \\frac{\\sigma\_x-\\sigma\_y}{2}\\sin 2\\theta + \\tau\_{xy} \\cos 2\\theta
            \\end{aligned}$$

-   To find *σ*<sub>*y*<sup>′</sup></sub> we can simply add 90<sup>∘</sup> to *θ*

<span>procedure</span>

-   The procedure in general is mostly “plug and chug”

-   The only thing we need to be cautious about is sign convention: stresses are positive in tension, shear is positive with arrows pointing to the 1st and 3rd quadrants, *θ* is measured counter-clockwise from the *x*-axis

<span>example 9.2</span>

<img src="../figures/example-9-2" alt="Determine the stress at this point on an element rotated 30^\circ clockwise from the position shown." style="width:50.0%" />

principal stresses
==================

<span>principal stresses</span>

-   Since the local stresses only change with the rotation angle, we might like to find the angle with gives the maximum stress

-   This is known as the principal direction, and the stresses are known as principal stresses

-   We can find this direction by differentiating the equation for *σ*<sub>*x*<sup>′</sup></sub>

<span>principal stress</span>

-   We find the angle as
    $$\\tan 2\\theta\_p = \\frac{2 \\tau\_{xy}}{\\sigma\_x-\\sigma\_y}$$

-   The principal stresses are then
    $$\\sigma\_{1,2} = \\frac{\\sigma\_x+\\sigma\_y}{2} \\pm \\sqrt {\\left( \\frac{\\sigma\_x-\\sigma\_y}{2}\\right)^2 + \\tau\_{xy}^2}$$

<span>maximum shear stress</span>

-   Similarly, we might want to find the direction of maximum shear stress
    $$\\tan 2\\theta\_s = \\frac{\\sigma\_y-\\sigma\_x}{2 \\tau\_{xy}}$$

-   And the maximum shear stress is
    $$\\tau\_{max} = \\sqrt{\\left( \\frac{\\sigma\_x-\\sigma\_y}{2} \\right)^2 + \\tau\_{xy}^2}$$

<span>example 9.3</span>

<img src="../figures/example-9-3" alt="Find the principal stress for the stress state shown" style="width:50.0%" />

<span>example 9.5</span>

-   When torsional loading *T* is applied to a circular bar it produces a state of pure shear stress.

-   Find the maximum in-plane shear stress and the associated average normal stress

-   Find the principal stresses


