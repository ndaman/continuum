## AE333
## Mechanics of Materials
Lecture 17 - Exam Review<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

6 Mar, 2019

----

## schedule

- 6 Mar - Exam Review
- 8 Mar - Exam 2
- 11-15 Mar - Spring Break

----
## outline

---
# exam

----
## exam format

- Similar format to last exam
- Five questions
- Covers Axial Load, Torsion, and Bending
- Past exams included Transverse Shear, which will not be on this exam

---
# topics

----
## axial load

-   Saint Venant's Principle
-   Elastic Deformation
-   Superposition
-   Statically Indeterminate
-   Force Method
-   Thermal Stress

----
## torsion

-   Torsional deformation
-   Torsion formula
-   Power transmission
-   Angle of twist
-   Statically indeterminate torsion
-   Thin-walled tubes

----
## bending

-   Shear and moment diagrams
-   Bending deformation
-   Flexure formula

---
# axial load

----
## axially loaded member

-   We can use Hooke's Law to find the deformation of a general body under axial loading (below the elastic limit)

![If we consider some homogeneous body with an applied load, we can look at a small section of this body with an applied load of N(x) which is initially dx wide, but under load stretches an additional d delta.](images\axial-load.jpg)

----
## axially loaded member

-   For some differential element, we can consider the internal forces and stresses
$$\\sigma = \\frac{N(x)}{A(x)} = E(x) \\epsilon(x) = E(x) \\left(\\frac{d\\delta}{dx}\\right)$$
-   We can solve this for $d \delta$ to find
$$d \\delta = \\frac{N(x) dx}{A(x)E(x)}$$
-   We integrate this over the length of the bar to find the total displacement

----
## sign convention

-   In general, we consider a force or stress to be positive if it causes tension and elongation
-   It is negative if it causes compression and contraction

----
## statically indeterminate

-   There are many problems that are at least slightly over-constrained
-   While this is common engineering practice, it creates too many variables for statics analysis
-   These problems are called "statically indeterminate"

----
## statically indeterminate

-   One extra equation we can use is called "compatibility" or the "kinematic condition"
-   We know that at the displacement must be equal on both sides of any arbitrary section we make in a member
-   We can separate a member into two parts, then use compatibility to relate the two unknown forces

----
## statically indeterminate

![A 5 m long, vertically-oriented bar is fixed at both ends, with a 500 N downward load applied 2 m from the top.](images\statically-indeterminate.jpg) <!-- .element width="25%" -->

----
## thermal stress

-   A change in temperature cases a material to either expand or contract
-   For most materials this is linear and can be described using the coefficient of linear expansion
$$\delta T = \alpha \Delta T L$$

----
## thermal stress

-   When a body is free to expand, the deformation can be readily calculated
-   If it is not free to expand, however, thermal stresses develop
-   We can use the force method described previously to find the thermal stresses developed

---
# torsion

----
## torsion

-   Torque is a moment that tends to twist a member about its axis
-   For small deformation problems, we assume that the length and radius do not change signicantly under torsion
-   The primary deformation we are concerned with in torsion is the angle of twist, denoted with $\phi$

----
## shear

![A thin disk under applied torsion. The shear strain varies linearly with radial distance from the center.](images\torsion-disk.jpg)<!-- .element width="40%" -->

----
## torsion formula

-   For a linearly elastic material, Hooke's Law in shear will hold ($\tau = G \gamma$)
-   This means that, like shear strain, shear stress will vary linearly along the radius

----
## torsion formula

-   We can find the total force on an element, *dA* by multiplying the shear stress by the area
`$$dF = \tau dA$$`
-   The torque ($dT = \rho dF$) produced by this force is then
$$dT = \rho (\tau dA)$$

----
## torsion formula

-   Integrating over the whole cross-section gives
$$T = \\int\_A \\rho (\\tau dA) = \\frac{\\tau\_{max}}{c} \\int\_A \\rho^2 dA$$
-   The integral `$\int_A \rho^2 dA$` is also called the Polar Moment of Inertia, *J*, so we can write
$$\\tau\_{max} = \\frac{Tc}{J}$$

----
## polar moment of inertia

-   We know that `$J=\int_A \rho^2 dA$`, so we can compute this for some common shapes
-   For a solid circular cross-section, we have
$$J = \\int\_0^c \\rho^2 (2\\pi \\rho d\\rho) = \\frac{\\pi}{2}c^4$$
-   For a circular tube we have
$$J = \\int\_{c\_1}^{c\_2} \\rho^2 (2\\pi \\rho d\\rho) = \\frac{\\pi}{2}(c\_2^4-c\_1^4)$$

----
## power transmission

-   Shafts and tubes are often connected to belts and drives, and the torque, speed, and power are all related
-   Power is the rate of work done, for rotation problems, $P = T \omega$
-   We are often given the frequency *f* instead of the angular velocity, $\omega$, in this case $P = 2\pi f T$

----
## power units

-   In SI Units, power is expressed in Watts 1 W = 1 N m / sec
-   In Freedom Units, power is expressed in Horsepower 1 hp = 550 ft lb / sec

-----
## shaft design

-   We often know the power and frequency of a drive, and need to design a shaft such that the shear stress is acceptable
-   We can easily find the torque as $T=P/2\pi f$, we can use this combined with the torsion equation
$$\\tau\_{max} = \\frac{Tc}{J}$$
to find the appropriate shaft diameter.
-   For solid shafts we can solve for *c* uniquely, but not for hollow shafts


----
## angle of twist

-   While in axial problems we examined the total deformation for the general case, in torsion we will examine the total angle of twist in general
-   Using the method of sections, we can consider a differential disk which has some internal torque as a function of *x*, *T*(*x*).
-   On this section, the shear strain will be related to the angle of twist by the thickness of the section (*dx*) and the radial distance ($\rho$).

----
## angle of twist

![A section of an arbitrary cone is shown to depict how we can find the incremental change in angle from one end of the section to the next.](images\generaltorsion.png)


----
## angle of twist

-   $\gamma$ and $d\phi$ are related by
$$d\\phi = \\gamma \\frac{dx}{\\rho}$$
-   We also know that $\gamma = \tau/G$ and $\tau = T(x) \rho / J(x)$ substituting both this gives
$$d\\phi = \\frac{T(x)}{J(x)G(x)}dx$$

----
## multiple torques

-   If a shaft is subjected to multiple torques, or if there is a discontinuous change in shape or material we can sum the change in angle over various segments
$$\\phi = \\sum \\frac{TL}{JG}$$

----
## sign convention

-   When we section a shaft and consider the internal torque, it is important to be consistent with our signs
-   Both torque and angle of twist should follow the same convention
-   The convention is to use the right hand rule with the thumb pointing normal to the cut, and the fingers curling in the positive direction

----
## shear flow

-   Thin-walled tubes of non-circular cross-sections are commonly found in aerospace and other applications
-   We can analyze these using a technique called shear flow
-   Because the walls of the tube are thin, we assume that the shear stress is uniformly distributed through the wall thickness

----
## shear flow

-   If we consider an arbitrary segment of a tube with varying thickness, we find from equilibrium that the product of the average shear stress and the thickness must be the same at every location on the cross-section
$$q = \tau_{avg} t$$
-   *q* is called the shear flow

----
## average shear stress

-   We can relate the average shear stress to the torque by considering the torque produced about some point within the tubes boundary
`$$T = \oint h \tau_{avg} t ds$$`
-   Where *h* is the distance from the reference point, *ds* is the differential arc length and *t* is the tube thickness.

----
## average shear stress

-   We notice that `$\tau_{avg}t$` is equal to the shear flow, *q*, which must be constant
-   We can also simplify the integral by relating a similar area integral to the arc length integral
$$dA_m = 1/2 h ds$$
-   Thus
$$T = \oint h\tau_{avg} t ds = 2 q \int dA_m = 2 q A_m$$

----
## angle of twist

- The angle of twist for a thin-walled tube is given by
`$$ \phi = \frac{TL}{4A_m^2 G} \oint \frac{ds}{t} $$`

---
# bending

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
