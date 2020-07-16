
# AE333
## Mechanics of Materials
Lecture 9 - Axial Load, Torsion<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

February 15, 2019

----

## schedule

- 15 Feb - Axial Load, Torsion
- 18 Feb - Torsion, HW3 Due
- 20 Feb - Torsion
- 22 Feb - Bending

----
## outline
- superposition
- statically indeterminate
- force method
- thermal stress
- torsion

---
# superposition

----
## superposition

-   Some problems are too complicated to solve all at once
-   Instead, we break them up into two simpler problems
-   Each "sub-problem" must still satisfy equilibrium
-   Problem must be linear and the deformation should be small enough that it does not cause moment-equilibrium isssues

---
# statically indeterminate

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
## example 4.7

<div class="left">
![A 0.8 m long rigid horizontal bar is supported by hanging from 3 vertical rods. Rod AB supports the left end, rod CD supports the middle and rod EF supports the right end. A 15 kN load is applied 0.2 m from the left end.](images\example-4-7.jpg)
</div>
<div class="right">
Assuming the bottom bar is rigid, find the force developed in each bar.
AB and EF have cross-sectional areas of 50 mm<sup>2</sup> while CD has a cross-sectional area of 30 mm<sup>2</sup>.
</div>

---
# force method

----
## force method

-   One way to solve statically indeterminate problems is using the principle of superposition
-   We choose one redundant support and remove it
-   We then add it back as a force separately (without the other forces in the problem)

----
## force method

![An illustration of the force method, we have the same statically indeterminate problem as before, a 5 m long, vertically-oriented bar is fixed at both ends, with a 500 N downward load applied 2 m from the top. We set this equivalent to a a bar with the same load, but no support on the bottom end. We then add a force which will provide enough displacement to cancel out the displacement introduced by removing the load.](images\force-method.png)

----
## force method

-   We connect the two problems by requiring that the displacement in both frames adds to 0 to meet the support requirements
-   This is referred to as the equation of compatibility

----
## procedure

-   Choose one support as redundant, write the equation of compatibility
-   Express the external load and redundant displacements in terms of load-displacement relationship
-   Draw free body diagrams and use the equations of equilibrium to solve

----
## example 4.9

![A 1200 mm long horizontal rod is fixed at its left end and has a fixed support 0.2 mm away from its right end. A 20 kN load is applied to the right 400 mm away from its left end.](images\example-4-9.jpg)

The steel rod shown has a diamater of 10 mm. Determine the reactions at A and B'.

---
# thermal stress

----
## thermal stress

-   A change in temperature cases a material to either expand or contract
-   For most materials this is linear and can be described using the coefficient of linear expansion
`$$\delta_T = \alpha \Delta T L$$`

----
## thermal stress

-   When a body is free to expand, the deformation can be readily calculated using
-   If it is not free to expand, however, thermal stresses develop
-   We can use the force method described previously to find the thermal stresses developed

----
## example 4.12

<div class="left">
![An aluminum tube used as a sleeve for a steel bolt. The tube is 150 mm long.](images\example-4-12.jpg)
</div>
<div class="right">
An aluminum tube with cross-section of 600 mm<sup>2</sup> is used as a sleeve for a steel bolt with cross-sectional area of 400 mm<sup>2</sup>. When T=15 degrees Celsius there is negligible force and a snug fit, find the force in the bolt and sleeve when T=80 degrees Celsius.
</div>

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

-   For a linearly elastic material, Hooke’s Law in shear will hold (`$\tau = G \gamma$`)
-   This means that, like shear strain, shear stress will vary linearly along the radius

----
## torsion formula

-   We can find the total force on an element, *dA* by multiplying the shear stress by the area
`$$ dF = \tau dA$$`
-   The torque (`$dT = \rho dF$`) produced by this force is then
`$$dT = \rho(\tau dA)$$`

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
## example 5.1

<div class="left">
![On left is a solid 100 mm radius tube, while on the right is a hollow tube with outter radius of 100 mm and inner radius of 75 mm. Element A is on the surface of the solid tube on the left, element B is on the outter surface of the hollow tube on the right and Element C is on the inner surface of the hollow tube on the right.](images\example-5-1.png)
</div>
<div class="right">
The allowable shear stress is 75 MPa. Determine the maximum torque that can be applied to each of the cross-sections shown and find the stress acting on a small element at A, B and C.
</div>
