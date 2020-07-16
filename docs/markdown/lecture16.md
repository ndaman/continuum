## AE333
## Mechanics of Materials
Lecture 16 - Bending<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

4 Mar, 2019

----

## schedule

- 4 Mar - Transverse Shear
- 6 Mar - Exam Review
- 8 Mar - Exam 2
- 11-15 Mar - Spring Break

----
## outline
<!-- TOC START min:1 max:1 link:false update:true -->
- compound centroids
- shear in straight members
- the shear formula

<!-- TOC END -->


---
# compound centroids

----
## composite bodies

-   Often we have to deal with bodies that are not described by a continuous function, but are made of different materials or different shapes

-   We can use the same logic previously, but with a finite sum instead of an integral
$$\\begin{aligned}
  \\bar{x} \\sum W &= \\sum \\tilde{x} W\\\\
  \\bar{y} \\sum W &= \\sum \\tilde{y} W\\\\
  \\bar{z} \\sum W &= \\sum \\tilde{z} W
\\end{aligned}$$

----
## analysis procedure

-   Use a sketch to divide the body into sub-bodies
-   If a body has a hole, it may be easier to treat that volume as whole and then subtract the hole
-   Take note of any symmetry (an object symmetric about any axis will have a centroid along that axis)

---
# shear in straight members

----
## shear

-   We have discussed the internal stresses caused by the internal moment *M*
-   There are also internal shear stresses caused by the internal shear force *V*
-   We can illustrate the effect of internal shear stress by considering three boards, either resting on top of on another or bonded

----
## shear

![A comparison of three boards stacked on top of each other and loaded with pin supports at both ends. The top shows how the boards look if they are stacked with no bond, while the bottom shows the boards bonded together.](images\bonded-boards.png) <!-- .element width="60%" -->

---
# the shear formula

----
## shear formula

-   Internal shear causes a more complicated deformation state, so we will use an indirect method to find the shear stress-strain distribution
-   We will consider equilibrium along a section of a beam, then we will consider another section

----
## equilibrium

![A free body diagram of an arbitrary beam.](images\beam-fbd.png)

----
## equilibrium

![A section of some arbitrary cut of an arbitrary beam cross-section showing the shear acting on a sub-section of this element.](images\fbd-newsection.jpg) <!-- .element width="50%" -->

----
## equilibrium

-   There must be a shear force along the bottom to equilibrate the different stresses on either side of the section
-   If we assume that this shear is constant through the thickness, we obtain the following from equilibrium
`$$\sum F_x = 0 = \int_{A^\prime} \sigma^\prime dA^\prime - \int_{A^\prime} \sigma dA^\prime - \tau (t dx)$$`

----
## equilibrium
$$\\tiny{\\begin{aligned}
  0 &= \\int\_{A^\\prime} \\left( \\frac{M + dM}{I} \\right) y dA^\\prime - \\int\_{A^\\prime} \\left( \\frac{M}{I} \\right)y dA^\\prime - \\tau(t dx) \\\\
  \\left( \\frac{M}{I} \\right) \\int\_{A^\\prime} y dA^\\prime &= \\tau (t dx)\\\\
  \\tau &= \\frac{1}{It} \\left( \\frac{dM}{dx} \\right)\\int\_{A^\\prime} y dA^\\prime
\\end{aligned}}$$

----
## shear formula

-   In this formula, recall that $V = \\frac{dM}{dx}$
-   We also call *Q* the moment of the area `$A^\prime$` which is equal to `$\int_{a^\prime} y dA^\prime$`
-   We can also write *Q* in terms of the centroid
$$Q = \\bar{y}^\\prime A^\\prime$$

----
## shear formula

-   Simplified, the shear formula is
$$\\tau = \\frac{VQ}{It}$$
-   *Q* poses the greatest difficulty in calculations, so we will consider a few examples

----
## Q

-   *Q* represents the moment of the cross-sectional area above (or below) the point at which the shear stress is being calculated
-   We apply the formula to that area

----
## Q

![Some beam cross-sections to illustrate the calculation of Q](images\Q.jpg) <!-- .element width="35%" -->

----
## shear formula limitations

-   A major assumption made is that the shear stress was constant through the thickness, essentially we have found the average shear
-   This is more accurate the more slender a beam is (small *b* and large *h*)
-   The formula is also not accurate for cross sections that change or have boundaries that are not right angles

----
## procedure

-   First we find the internal shear, *V*
-   Find *I*, the moment of inertia (of the entire section) about the neutral axis
-   Find *t* from an imaginary cross-section at the point of interest
-   Calculate *Q* from either the area above or below the point of interest
-   $\tau$ acts in the same direction as *V* (and must be equilibrated on other faces)

----
## example 7.1

![A simply supported beam 8 meters long has a uniformly distributed load of 6.5 kN/m applied on the rightmost 4 meters. The beam has a t-shaped cross section with the top 150 mm wide and 30 mm tall and the bottom 150 mm tall and 30 mm wide.](images\example-7-1.jpg) <!-- .element width="35%" -->

Determine the maximum stress needed by a glue to hold the boards together.

----
## example 7.3

![An I-beam is shown with a width of 300 mm and height of 240 mm, a web 15 mm thick, and flanges 20 mm thick. There is a shear force of 80 kN applied.](images\example-7-3.jpg) <!-- .element width="50%" -->

Plot the shear stress distribution through the beam.
