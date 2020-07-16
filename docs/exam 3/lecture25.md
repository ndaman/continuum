## AE333
## Mechanics of Materials
Lecture 25 - Strain Transformation<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

5 Apr, 2019

----

## schedule

- 5 Apr - Deflection of Beams
- 8 Apr - Deflection of Beams, HW8 Due
- 10 Apr - Deflection of Beams
- 12 Apr - Deflection of Beams


----
## outline

<!-- vim-markdown-toc GFM -->

* plane strain
* principal strains and mohr’s circle
* strain rosettes
* material property relationships
* deflection of beams and shafts

<!-- vim-markdown-toc -->

---
# plane strain

----
## plane strain

-   Under plane stress we assume no out-of-plane stresses are present
-   This is typically a good assumption for very thin materials
-   Under plane strain we assume no out-of-plane strains are present
-   Typically a good assumption for very thick materials

----
## sign convention

-   Normal strains, *ϵ*<sub>*x*</sub> and *ϵ*<sub>*y*</sub>, are considered positive when they cause elongation, and negative when they cause contraction
-   Shear strains, *γ*<sub>*xy*</sub> are positive if the interior angle becomes smaller than 90<sup>∘</sup>, and negative if the angles becomes larger than 90<sup>∘</sup>

----
## general equations

-   We derive the general strain transformation equations by comparing infinitesimal elements before and after deformation
-   To find *γ*<sub>*x*<sup>′</sup>*y*<sup>′</sup></sub> we compare the angle between *dx* and *dy* before and after deformation

----
## general equations

-   The equations are nearly exactly the same as the stress transformation equations
-   Pay attention to the difference, strain transformation equations are NOT on the equation sheet
$$\\begin{aligned}
  \\epsilon\_{x^\\prime} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} + \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\cos 2 \\theta + \\frac{\\gamma\_{xy}}{2} \\sin 2\\theta \\\\
  \\frac{\\gamma\_{x^\\prime y^\\prime}}{2} &= -\\left( \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\right)\\sin 2 \\theta + \\frac{\\gamma\_{xy}}{2} \\cos 2\\theta
\\end{aligned}$$

-   As with *σ*<sub>*y*<sup>′</sup></sub>, we find *ϵ*<sub>*y*<sup>′</sup></sub> by letting *θ*<sub>*y*</sub> = *θ*<sub>*x*</sub> + 90<sup>∘</sup>

----
## engineering strain

-   Side note: there is another definition of shear strain known as tensorial shear strain, where *γ*<sub>*xy*</sub> = 2*ϵ*<sub>*xy*</sub>
-   Under tensorial strain, the transformation equations are exactly the same (as in this case both stress and strain are tensors)
-   *γ*<sub>*xy*</sub> is known as engineering strain, you will need to pay attention to which strain convention is used when extracting data from finite elements or other sources

---
# principal strains and mohr’s circle

----
## principal strains

-   As you might imagine, since the transformation equations are nearly identical so are the principal strain equations
$$\\begin{aligned}
  \\tan 2\\theta\_p &= \\frac{\\gamma\_{xy}}{\\epsilon\_x-\\epsilon\_y}\\\\
  \\epsilon\_{1,2} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} \\pm \\sqrt{ \\left( \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\right)^2 + \\left(\\frac{\\gamma\_{xy}}{2}\\right)^2}
\\end{aligned}$$

----
## mohr’s circle

-   Mohr’s circle can also be used in exactly the same way for strain as it is for stress
-   The only difference is that the vertical axis is tensor strain, or *γ*<sub>*xy*</sub>/2

----
## example 10.4

<div class="left">
![](..\images\example-10-4.jpg) 
</div>

<div class="right">
The state of plane strain at a point has components of `$\epsilon_x = 250 \mu \epsilon$`, `$\epsilon_y = -150 \mu \epsilon$`, and `$\gamma_{xy} = 120 \mu \epsilon$`. Determine the principal strains and the direction they act.
</div>

---
# strain rosettes

----
## rosettes

-   Normal strain is fairly easy to measure using a strain gage
-   Shear strain is more difficult to measure directly, so instead a “rossette” of normal strain gages is used
-   We can use the strain transformation equations to determine *τ*<sub>*xy*</sub>

----
## rosettes

-   Usually, we have *θ*<sub>*a*</sub> = 0, *θ*<sub>*b*</sub> = 90 and *θ*<sub>*c*</sub> = 45 OR *θ*<sub>*a*</sub> = 0, *θ*<sub>*b*</sub> = 60 and *θ*<sub>*c*</sub> = 120

$$\\begin{aligned}
  \\epsilon\_{a} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} + \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\cos 2 \\theta\_a + \\frac{\\gamma\_{xy}}{2} \\sin 2\\theta\_a \\\\
  \\epsilon\_{b} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} + \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\cos 2 \\theta\_b + \\frac{\\gamma\_{xy}}{2} \\sin 2\\theta\_b \\\\
  \\epsilon\_{c} &= \\frac{\\epsilon\_x+\\epsilon\_y}{2} + \\frac{\\epsilon\_x-\\epsilon\_y}{2}\\cos 2 \\theta\_c + \\frac{\\gamma\_{xy}}{2} \\sin 2\\theta\_c
\\end{aligned}$$

----
## example 10.8

<div class="left">
![](..\images\example-10-8.jpg)
</div>

<div class="right">
The readings from the rosette shown are `$\epsilon_a=60\mu\epsilon$`, `$\epsilon_b=135\mu\epsilon$` and `$\epsilon_c=264\mu\epsilon$`. Find the in-plane principal strains and their directions.
</div>

---
# material property relationships

----
## generalized hooke’s law

-   We have previously used Hooke’s Law in 2D, in 3D we have

$$\\begin{aligned}
  \\epsilon\_x &= \\frac{1}{E}\[\\sigma\_x - \\nu(\\sigma\_y + \\sigma\_z)\]\\\\
  \\epsilon\_y &= \\frac{1}{E}\[\\sigma\_y - \\nu(\\sigma\_x + \\sigma\_z)\]\\\\
  \\epsilon\_z &= \\frac{1}{E}\[\\sigma\_z - \\nu(\\sigma\_x + \\sigma\_y)\]
\\end{aligned}$$

----
## generalized hooke’s law

-   And in shear

$$\\begin{aligned}
  \\gamma\_{xy} &= \\frac{1}{G} \\tau\_{xy}\\\\
  \\gamma\_{yz} &= \\frac{1}{G} \\tau\_{yz}\\\\
  \\gamma\_{xz} &= \\frac{1}{G} \\tau\_{xz}
\\end{aligned}$$

----
## dilatation

-   When a material deforms it often changes volume
-   The change in volume per unit volume is called “volumetric strain” or dilatation

$$e = \\frac{\\partial V}{d V} = \\epsilon\_x + \\epsilon\_y + \\epsilon\_z = \\frac{1-2\\nu}{E}(\\sigma\_x+\\sigma\_y+\\sigma\_z)$$

----
## hydrostatic pressure

-   One way of characterizing volumetric response is to apply hydrostatic pressure (equal compression on all sides with no shear)
-   Under this case, we have

$$\\frac{p}{e} = -\\frac{E}{3(1-2\\nu)}$$

-   We call the term on the right (with no negative sign) the bulk modulus, *k*


---
# deflection of beams and shafts

----
## elastic curve

-   Before finding the exact displacement, it is useful to sketch the approximate deformed shape of a beam
-   For difficult beams, it is useful to draw the moment curve first
-   Positive internal moment tends to bend the beam concave up, while negative moment tends to bend the beam concave down

----
## elastic curve

![](..\images\elastic-curve.jpg) <!-- .element width="40%" -->

----
## elastic curve

![](..\images\elastic-curve2.jpg) <!-- .element width="40%" -->

----
## moment-curvature

-   In Chapter 6 we compared the strain in a segement of a beam to the radius of curvature and found

$$\\frac{1}{\\rho} = -\\frac{\\epsilon}{y}$$

-   Since Hooke’s Law applies, *ϵ* = *σ*/*E* = −*My*/*EI*, substituting gives

$$\\frac{1}{\\rho} = \\frac{M}{EI}$$

----
## sign convention

![](..\images\curvature.jpg)

`$\rho$` is positive when the center of the arc is above the beam, negative when it is below.
