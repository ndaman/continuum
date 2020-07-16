<span>schedule</span>

-   24 Oct - Mohr’s Circle, Strain Transformation, HW7 Due

-   26 Oct - Strain Transformation

-   29 Oct - Deflection of Beams and Shafts

-   31 Oct - Deflection of Beams and Shafts, HW8 Due

<span>outline</span>

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

mohr’s circle
=============

<span>mohr’s circle</span>

-   We can visualize plane stress transformation using a technique known as Mohr’s circle

-   If we re-write the stress transformation equations we find
    $$\\begin{aligned}
                \\hspace\*{-2cm}
                \\sigma\_{x^\\prime} - \\left( \\frac{\\sigma\_x + \\sigma\_y}{2} \\right) &= \\left( \\frac{\\sigma\_x - \\sigma\_y}{2} \\right) \\cos 2 \\theta + \\tau\_{xy} \\sin 2\\theta \\\\
                \\tau\_{x^\\prime y^\\prime} &= -\\left( \\frac{\\sigma\_x - \\sigma\_y}{2} \\right) \\sin 2\\theta + \\tau\_{xy} \\cos 2\\theta
            \\end{aligned}$$

<span>mohr’s circle</span>

-   If we square each equation and add them together, we find
    $$\\label{eq:mohr}
                \\hspace\*{-2cm}
                \\left\[\\sigma\_{x^\\prime} - \\left( \\frac{\\sigma\_x + \\sigma\_y}{2} \\right) \\right\]^2 + \\tau\_{x^\\prime y^\\prime}^2 = \\left( \\frac{\\sigma\_x - \\sigma\_y}{2} \\right)^2+\\tau\_{xy}^2$$

<span>mohr’s circle</span>

-   Since *σ*<sub>*x*</sub>, *σ*<sub>*y*</sub> and *τ*<sub>*x**y*</sub> are known constants, we can write a more compact form by letting
    $$\\begin{aligned}
                (\\sigma\_{x^\\prime}-\\sigma\_{avg})^2 + \\tau\_{x^\\prime y^\\prime}^2 &= R^2\\\\
                \\sigma\_{avg} &= \\frac{\\sigma\_x+\\sigma\_y}{2}\\\\
                R &= \\sqrt{ \\left( \\frac{\\sigma\_x - \\sigma\_y}{2} \\right)^2 + \\tau\_{xy}^2}
            \\end{aligned}$$

<span>mohr’s circle</span>

-   Re-written in this way, we can see that  \[eq:mohr\] is the equation of a circle on the *σ*, *τ* axis

-   The center of the circle is at *τ* = 0 and *σ* = *σ*<sub>*a**v**g*</sub>

-   The radius of the circle is $\\sqrt{ \\left( \\frac{\\sigma\_x - \\sigma\_y}{2} \\right)^2 + \\tau\_{xy}^2}$

-   Each point on the circle represents *σ*<sub>*x*<sup>′</sup></sub>, *τ*<sub>*x*<sup>′</sup>*y*<sup>′</sup></sub>

<span>mohr’s circle</span>

<img src="../figures/mohr" alt="image" style="width:60.0%" />

<span>visual construction of Mohr’s circle</span>

-   By convention, positive *τ* points down, use this convention to plot the center of the circle and a reference point at (*σ*<sub>*x*</sub>, *τ*<sub>*x**y*</sub>) where the *x*<sup>′</sup> axis is coincident with the *x* axis

-   Use these two points to sketch the circle

<span>principal stress</span>

-   The principal stresses, *σ*<sub>1</sub> and *σ*<sub>2</sub> are the coordinates where Mohr’s circle intersects the *σ* axis

-   The angles *θ*<sub>*p*1</sub> and *θ*<sub>*p*2</sub> can be found by calculating the angle between the reference line and the *σ* axis (note that this angle is equal to 2*θ*<sub>*p*</sub>)

-   Note that the direction from the the reference point to the *σ* axis will be the same as the direction from the *x* axis to the principal axis

<span>maximum shear stress</span>

-   The top and bottom of the circle represent the maximum shear stress

-   The angles *θ*<sub>*s*1</sub> and *θ*<sub>*s*2</sub> can be found in a similar method to that described for the principal stress

<span>stress on arbitrary plane</span>

-   To find the stress at some arbitrary plane some known angle *θ* away from our reference plane, we find the angle 2*θ* away from the reference line on Mohr’s circle

-   We can use trigonometry to find the value of the coordinates at that point

-   We must draw our angle in the same direction as the desired rotation

<span>example 9.9</span>

<img src="../figures/example-9-9" alt="Represent the state of stress shown on an element rotated 30^\circ counterclockwise from the position shown." style="width:50.0%" />
