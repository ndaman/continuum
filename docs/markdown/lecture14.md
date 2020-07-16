
## AE333
## Mechanics of Materials
Lecture 14 - Bending<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

February 27, 2019

----

## schedule

- 27 Feb - Bending
- 1 Mar - Bending
- 4 Mar - Transverse Shear, HW 5 Due
- 6 Mar - Exam 2 Review

----
## outline
<!-- TOC START min:1 max:1 link:false update:true -->
- shear and moment diagrams
- graphical method
- bending deformation
- flexure formula

<!-- TOC END -->


----
## shear-moment diagrams

- Drawing shear-moment diagrams is a very important skill
- Learning MasteringEngineering's drawing system is not as important (in my opinion)
- If you are more comfortable doing your shear-moment diagrams by hand, you may turn them into me in class on Monday and I will grade them by hand


---
# shear and moment diagrams

----
## shear and moment diagrams

-   The general approach to shear and moment diagrams is to first find the support reactions
-   Next we section the beam and instead of finding the internal force and moment at a single point, we find it as a function of *x*
-   Many beams will require piecewise sectioning
-   We then draw this as a shear and moment diagram

----
## sign convention

![A cantilever beam with some arbitrary loads and a section marked](images\beam-internal.jpg) <!-- .element width="60%" -->

![A free body diagram of the above beam with internal loads shown where the section cut was made.](images\beam-internal-cut.jpg) <!-- .element width="60%" -->

----
## example beam

![A simply supported beam with a distruted load acting over one portion and a concentrated load later. This beam is to illustrate the method of setting up multiple coordinate systems for different sections.](images\piece-wise-beam.jpg) <!-- .element width="60%" -->

----
## example beam

![A shear diagram for the above beam](images\shear-diagram.jpg) <!-- .element width="60%" -->

----
## example beam

![A moment diagram for the above beam](images\moment-diagram.jpg) <!-- .element width="60%" -->

---
# graphical method

----
## relation between load, shear, moment

-   When there are several forces, supports, or loading conditions applied to a beam, the piecewise method can be cumbersome
-   In this section we will examine the differential relationships between distributed load, shear, and bending moments

----
## distributed load

![Internal loading shown on a differential element sectioned from a beam.](images\distributed-load.jpg) <!-- .element width="40%" -->

----
## distributed load

-   Consider a beam subjected to only distributed loading
-   If we section this beam in the middle (to remove both supports) we can relate *V* to the loading function *w*(*x*)
-   Considering the sum of forces in *y*:
$$\\begin{aligned}
  V + w(x)\\Delta x - (V + \\Delta V) &= 0\\\\
  \\Delta V &= w(x) \\Delta x
\\end{aligned}$$

----
## distributed load

-   If we divide by $\Delta x$ and let $\Delta x \to 0$ we find
$$\\frac{dV}{dx} = w(x)$$
-   Thus the slope of the shear diagram is equal to the distributed load function

----
## moment diagram

-   If we consider the sum of moments about *O* on the same section we find
$$\\begin{aligned}
  (M + \\Delta M) - (w(x)\\Delta x)k \\Delta x - V\\Delta x - M &= 0\\\\
  \\Delta M &= V \\Delta x + k w(x) \\Delta x ^2
\\end{aligned}$$
-   Dividing by $\Delta x$ and letting $\Delta x \to 0$ gives
$$\\frac{dM}{dx} = V$$

----
## concentrated forces

-   If we consider a concentrated force (instead of a distributed load) we find
$$\Delta V = F $$
-   This means that concentrated loads will cause the shear diagram to "jump" by the amount of the concentrated force (causing a discontinuity on our graph)

----
## couple moments

-   If our section includes a couple moment, we find (from the moment equation) that
$$\Delta M = M_0 $$
-   Thus the moment diagram will have a jump discontinuity

----
## example 7.9

![A beam is 6 meters long with pin supports at the left end, A, and at B, 4 meters to the right of A. From B to the right end of the beam is a uniform distributed load of 4 kN/m.](images\example-7-9.jpg)

----
## example 7.10

![A beam is 12 feet long with pin supports at both ends and a linearly increasing distributed load, beginning with 0 at the left end and rising to 120 lb/ft at the right end.](images\example-7-10.jpg) <!-- .element width="60%" -->

---
# bending deformation

----
## bending deformation

-   If we drew a grid on a specimen in bending, we would find that vertical lines tend to stay straight (but rotate)
-   Horizontal lines will become curved
-   If bending lifts the ends up (like a smile), then the top face will be in compression (and expand), while the bottom face will be in tension (and contract)

----
## bending deformation

![An example beam drawn in 3D with a grid drawn on it while it bends.](images\beam-deformation.jpg) <!-- .element width="60%" -->

----
## neutral axis

-   Since the bottom is in tension and the top is in compression, there must be somewhere in between that is under no stress
-   We call that the neutral axis, and assume it does not change in length
-   We also assume that planar sections remain planar (no warping)
-   Finally, Poisson's effects are neglected (cross-sections keep the same size and shape)

----
## strain

-   We will now consider an infinitesimal beam element before and after deformation
-   $\Delta x$ is located on the neutral axis and thus does not change in length after deformation
-   Some other line segment, $\Delta s$ is located *y* away from the neutral axis and changes its length to $\Delta s ^\prime$ after deformation

----
## strain

![A small beam section before and after deformation](images\beam-element.jpg) <!-- .element width="40%" -->

----
## strain

-   We can now define strain at the line segment $\Delta s$ as
$$\\epsilon = \\lim\_{\\Delta s \\to 0} \\frac{\\Delta s^\\prime - \\Delta s}{\\Delta s}$$

----
## strain

-   If we define $\rho$ as the radius of curvature after deformation, thus $\Delta x = \Delta s = \rho \Delta \theta $
-   The radius of curvature at $\Delta s$ is $\rho - y$, thus we can write
$$\\epsilon = \\lim\_{\\Delta \\theta \\to 0} \\frac{(\\rho-y)\\Delta \\theta - \\rho \\Delta \\theta}{\\rho \\Delta \\theta}$$
-   Which gives
$$\\epsilon = -\\frac{y}{\\rho}$$

---
# flexure formula

----
## hooke's law

-   If the beam is a linear material that follows Hooke's Law, the stress must be linearly proportional to the strain
-   Thus the stress will vary linearly through the beam, just like the strain does

----
## neutral axis

-   We have already hypothesized that a neutral axis must exist, we will now find its location
-   To be in equilibrium, the resultant force(s) produced by the stress must sum to zero, which means
$$\\begin{aligned}
  \\sum F\_x &= 0 = \\int\_A dF = \\int\_A \\sigma dA\\\\
  &= \\int\_A -\\left( \\frac{y}{c} \\right) \\sigma\_{max} dA\\\\
  &= -\\frac{\\sigma\_{max}}{c} \\int\_A y dA
\\end{aligned}$$

----
## neutral axis

-   Since $\sigma_{max}$ and *c* are both non-zero constants, we know that
$$ \int_A y dA = 0$$
-   Which can only be satisfied at the horizontal centroidal axis, so the neutral axis is the centroidal axis

----
## bending moment

-   The internal bending moment must be equal to the total moment produced by the stress distribution
$$\\begin{aligned}
  M &= \\int\_A y dF = \\int\_A y (\\sigma dA) \\\\
  &= \\int\_A y \\left( \\frac{y}{c} \\sigma\_{max} \\right) dA \\\\
  &= \\frac{\\sigma\_{max}}{c} \\int\_A y^2 dA
\\end{aligned}$$

----
## bending moment

-   We recognize that `$\int_A y^2 dA = I$`, and we re-arrange to write
$$\\sigma\_{max} = \\frac{Mc}{I}$$

----
## procedure

-   Find the internal moment at the point of interest, or draw a moment diagram to find the maximum point (if needed)
-   Determine the moment of inertia for the beam section
-   Find the neutral axis and/or the distance from the neutral axis to the point of interest
-   Use the flexure formula to find the stress

----
## example 6.12

<div class="left">
    ![A 6 meter long beam is pinned at both ends and subjected to a uniformly distruted load of 5 kN/m. ](images\example-6-12.png)
</div>

<div class="right">
  Find the maximum bending stress and draw the stress distribution through the thickness at that point.
</div>
