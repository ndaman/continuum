<span>schedule</span>

-   26 Oct - Strain Transformation

-   29 Oct - Deflection of Beams and Shafts

-   31 Oct - Deflection of Beams and Shafts, HW8 Due

-   2 Nov - Deflection of Beams and Shafts

<span>outline</span>

review
======

<span>review</span>

-   What are principal stresses?

-   How do we draw Mohr’s circle?

-   How do we use Mohrn’s circle?

absolute maximum shear
======================

<span>absolute maximum shear</span>

-   We already know how to find the maximum in-plane shear, but sometimes the maximum shear stress can occur in another plane

-   We can do this (without treating it as a fully 3D problem) by treating each plane as its own plane stress problem

<span>mohr’s circle</span>

<img src="../figures/max-shear" alt="image" style="width:50.0%" />

<span>mohr’s circle</span>

<img src="../figures/mohr-absolute" alt="image" style="width:60.0%" />

<span>absolute max shear</span>

-   The maximum absolute shear will depend on whether *σ*<sub>1</sub> and *σ*<sub>2</sub> are in the same or opposite directions
    $$\\begin{aligned}
                \\tau\_{abs,max} &= \\frac{\\sigma\_1}{2} & \\qquad \\text{same direction} \\\\
                \\tau\_{abs,max} &= \\frac{\\sigma\_1-\\sigma\_2}{2} & \\qquad \\text{opposite directions}
            \\end{aligned}$$

-   Which of the three mohr’s circles the maximum occurs in will determine which plane the shear acts in

plane strain
============

<span>plane strain</span>

-   Under plane stress we assume no out-of-plane stresses are present

-   This is typically a good assumption for very thin materials

-   Under plane strain we assume no out-of-plane strains are present

-   Typically a good assumption for very thick materials

<span>sign convention</span>

-   Normal strains, *ϵ*<sub>*x*</sub> and *ϵ*<sub>*y*</sub>, are considered positive when they cause elongation, and negative when they cause contraction

-   Shear strains, *γ*<sub>*x**y*</sub> are positive if the interior angle becomes smaller than 90<sup>∘</sup>, and negative if the angles becomes larger than 90<sup>∘</sup>

<span>general equations</span>

-   We derive the general strain transformation equations by comparing infinitesimal elements before and after deformation

-   To find *γ*<sub>*x*<sup>′</sup>*y*<sup>′</sup></sub> we compare the angle between *d**x* and *d**y* before and after deformation

<span>general equations</span>

-   The equations are nearly exactly the same as the stress transformation equations

-   Pay attention to the difference, strain transformation equations are NOT on the equation sheet
    $$\\begin{aligned}
                \\epsilon\_{x^\\prime} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} + \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\cos 2 \\theta + \\frac{\\gamma\_{xy}}{2} \\sin 2\\theta \\\\
                \\frac{\\gamma\_{x^\\prime y^\\prime}}{2} &= -\\left( \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\right)\\sin 2 \\theta + \\frac{\\gamma\_{xy}}{2} \\cos 2\\theta
            \\end{aligned}$$

-   As with *σ*<sub>*y*<sup>′</sup></sub>, we find *ϵ*<sub>*y*<sup>′</sup></sub> by letting *θ*<sub>*y*</sub> = *θ*<sub>*x*</sub> + 90<sup>∘</sup>

<span>engineering strain</span>

-   Side note: there is another definition of shear strain known as tensorial shear strain, where *γ*<sub>*x**y*</sub> = 2*ϵ*<sub>*x**y*</sub>

-   Under tensorial strain, the transformation equations are exactly the same (as in this case both stress and strain are tensors)

-   *γ*<sub>*x**y*</sub> is known as engineering strain, you will need to pay attention to which strain convention is used when extracting data from finite elements or other sources

principal strains and mohr’s circle
===================================

<span>principal strains</span>

-   As you might imagine, since the transformation equations are nearly identical so are the principal strain equations
    $$\\begin{aligned}
                \\tan 2\\theta\_p &= \\frac{\\gamma\_{xy}}{\\epsilon\_x-\\epsilon\_y}\\\\
                \\epsilon\_{1,2} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} \\pm \\sqrt{ \\left( \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\right)^2 + \\left(\\frac{\\gamma\_{xy}}{2}\\right)^2}
            \\end{aligned}$$

<span>mohr’s circle</span>

-   Mohr’s circle can also be used in exactly the same way for strain as it is for stress

-   The only difference is that the vertical axis is tensor strain, or *γ*<sub>*x**y*</sub>/2

<span>example 10.4</span>

<img src="../figures/example-10-4" alt="The state of plane strain at a point has components of \epsilon_x = 250 \mu \epsilon, \epsilon_y = -150 \mu \epsilon, and \gamma_{xy} = 120 \mu \epsilon. Determine the principal strains and the direction they act." style="width:50.0%" />
