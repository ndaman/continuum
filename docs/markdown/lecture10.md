
## AE333
## Mechanics of Materials
Lecture 10 - Torsion<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

February 18, 2019

----

## schedule

- 18 Feb - Torsion, HW3 Due
- 20 Feb - Torsion
- 22 Feb - Bending
- 25 Feb - Bending, HW4 Due

----
## outline
<!-- TOC depthFrom:1 depthTo:1 withLinks:0 updateOnSave:1 orderedList:0 -->

- force method
- thermal stress
- torsion
- power transmission

<!-- /TOC -->

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

-   A change in temperature causes a material to either expand or contract
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

-   For a linearly elastic material, Hooke's Law in shear will hold (`$\tau = G \gamma$`)
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

---
# power transmission

----
## power transmission

-   Shafts and tubes are often connected to belts and drives, and the torque, speed, and power are all related
-   Power is the rate of work done, for rotation problems, $P = T \omega$
-   We are often given the frequency *f* instead of the angular velocity, $\omega$, in this case $P = 2\pi f T$

----
## power units

-   In SI Units, power is expressed in Watts 1 W = 1 N m / sec
-   In Freedom Units, power is expressed in Horsepower 1 hp = 555 ft lb / sec

----
## shaft design

-   We often know the power and frequency of a drive, and need to design a shaft such that the shear stress is acceptable
-   We can easily find the torque as $T=P/2\pi f$, we can use this combined with the torsion equation
$$\\tau\_{max} = \\frac{Tc}{J}$$
to find the appropriate shaft diameter.
-   For solid shafts we can solve for *c* uniquely, but not for hollow shafts

----
## example 5.4

<div class="left">
![A rotating shaft connected to a motor](images\example-5-4.jpg)
</div>

<div class="right">
The steel shaft shown is connected to a 5 hp motor that rotates at $\omega=175$ rpm. If `$\tau_{allow}=14.5$` ksi, determine the required shaft diameter.
</div>
