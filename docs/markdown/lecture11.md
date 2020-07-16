
## AE333
## Mechanics of Materials
Lecture 11 - Torsion<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

February 20, 2019

----

## schedule

- 20 Feb - Torsion
- 22 Feb - Torsion
- 25 Feb - Bending, HW4 Due
- 27 Feb - Bending

----
## outline
<!-- TOC START min:1 max:1 link:false update:true -->
- torsion
- power transmission
- group problems

<!-- TOC END -->

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
-   In Freedom Units, power is expressed in Horsepower 1 hp = 550 ft lb / sec

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

---
# group problems

----
## group one

<div class="left">
![A 40 mm radius solid shaft. Point A is on the outer surface, Point B is 30 mm away from the center.](images\group5-1.jpg)
</div>

<div class="right">
The solid circular shaft is subjected to a an internal torque of 5 kN.m. Determine the shear stress at A and B and represent each state of stress on a volume element.  
</div>

----
## group two

<div class="left">
  ![A hollow circular shaft with outter radius of 60 mm and inner radius of 40 mm. Point A is on the inner surface, Point B is on the outter surface.](images\group5-2.jpg)
</div>

<div class="right">
The hollow circular shaft is subjected to a an internal torque of 10 kN.m. Determine the shear stress at A and B and represent each state of stress on a volume element.  
</div>

----
## group three

<div class="left">
![There is a fixed support at C, an applied torque of 4 kN.m at B (in the middle) and an applied torque of 2 kN.m at A (at the free end).](images\group5-3.jpg)
</div>

<div class="right">
The circular shaft is hollow from A to B and solid from B to C. Determine the shear stress at A and B. The outer diameter is 80 mm and the wall thickness is 10 mm.
</div>

----
## group four

<div class="left">
![A shaft supports to pulleys, one with a 150 mm radius and tension of 6 kN at one end and 2 kN at the other other. The other pulley has a 100 mm radius and tensions of 10 kN and 4 kN.](images\group-5-4.png)
</div>

<div class="right">
Determine the maximum shear stress in the 40 mm diameter shaft.
</div>
