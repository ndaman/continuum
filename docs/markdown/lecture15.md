
## AE333
## Mechanics of Materials
Lecture 15 - Bending<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

1 Mar, 2019

----

## schedule

- 1 Mar - Bending
- 4 Mar - Transverse Shear, HW 5 Due
- 6 Mar - Exam 2 Review
- 8 Mar - Exam 2

----
## outline
<!-- TOC START min:1 max:1 link:false update:true -->
- bending deformation
- flexure formula
- moment of inertia
- group problems

<!-- TOC END -->

----
## shear-moment diagrams

- Drawing shear-moment diagrams is a very important skill
- Learning MasteringEngineering's drawing system is not as important (in my opinion)
- If you are more comfortable doing your shear-moment diagrams by hand, you may turn them into me in class on Monday and I will grade them by hand

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

---
# moment of inertia

----
## moment of inertia

-   We know that `$I = \int_A y^2 dA$`
-   For common shapes, this integral has been pre-calculated (about the centroid of the shape)
-   For compound shapes, we use the parallel axis theorem to combine inertias from multiple areas

----
## parallel axis theorem

-   The parallel axis theorem is used to find the moment about any axis parallel to an axis passing through the centroid
-   If we consider an axis parallel to the *x*-axis, separated by some *dy* we have
`$$I_X = \int_A (y + dy)^2 dA$$`
-   Which gives
`$$I_x = \int_A y^2 dA + 2dy \int_A ydA + dy^2 \int_A dA$$`

----
## parallel axis theorem

-   The first integral is the moment of inertia about the original *x*-axis, which we will call $\\bar{I}\_x$
-   The second integral is zero since the *x*-axis passes through the centroid
-   This gives the parallel axis theorem
$$I\_x = \\bar{I}\_x + A dy^2$$

----
## parallel axis theorem

-   Similarly for the *y*-axis and polar moment of inertia we find
$$I\_y = \\bar{I}\_y + A dx^2$$
$$J\_O = \\bar{J}\_C + A d^2$$

---
# group problems

----
## group one

<div class="left">
![A hollow rectangular tube 0.4m tall and 0.2m wide on the outside and 0.2 m tall and 0.1 wide on the inside.](images\group-6-1.jpg)  
</div>

<div class="right">
  Determine the moment of inertia about the neutral axis
</div>

----
## group two

<div class="left">
![An upside-down t-section is 0.2m wide at the base, which is 0.1 m tall, the web is 0.1 m wide and 0.3 m tall.](images\group-6-2.jpg)  
</div>

<div class="right">
  Find the neutral axis and determine the moment of inertia about the neutral axis
</div>

----
## group three

![A beam is supported by pins at the right end and a point some distance away from the left end. A vertical load is applied at the left end, point B as it at the bottom side of the beam between the load and the first pin support, point A is between the two pin supports.](images\group-6-3.jpg)

Show how the bending stress acts on a differential volume at point A and B.
