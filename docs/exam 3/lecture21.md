## AE333
## Mechanics of Materials
Lecture 21 - Combined loading<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

27 Mar, 2019

----

## schedule

- 25 Mar - Combined Loading, HW6 Due
- 27 Mar - Stress Transformation 
- 29 Mar - Stress Transformation 
- 1 Apr - Stress Transformation, HW7 Due


----
## outline

<!-- vim-markdown-toc GFM -->

* combined loading
* group problems
* plane stress transformation

<!-- vim-markdown-toc -->

---
# combined loading

----
## combined loading

-   We can use the principle of superposition to treat various loading conditions separately and then add them together to find the total stress

----
## procedure

-   Section the member at the point of interest, internal force components should be drawn acting through the centroid of the section
-   Moment components should be calculated about the centroidal axis

----
## stress components

-   Normal stress: *σ* = *N*/*A*
-   Shear: *τ* = Q*/*It
-   Bending: *σ* = y*/*I
-   Torsion: *τ* = ρ*/*J
-   Pressure Vessels: *σ*<sub>1</sub> = r*/*t*, *σ*<sub>2</sub> =*r*/2*t

----
## example 8.2

![](../images/example-8-2.jpg) <!-- .element width="30%" -->

Neglect the weight of the member and find the stress at B and C.

----
## example 8.4

![](../images/example-8-4.jpg) 

Determine the stress at C and D.

----
## example 8.5

![](../images/example-8-5.jpg) <!-- .element width="30%" -->

The rod shown has a radius of 0.75 in. Find the stress at A.

---
# group problems

----
## group one

![](../images/group-8-1.jpg) <!-- .element width="40%" -->

Find the stress at the corners A and B for the column shown.

----
## group two

![](../images/group-8-2.jpg) <!-- .element width="30%" -->

Find the stress at point A for the cantilever beam shown.

----
## group three

![](../images/group-8-3.jpg) <!-- .element width="30%" -->

Find the load P that will cause a maximum normal stress of &sigma;=30 ksi along the section a-a.

---
# plane stress transformation

----
## plane stress

-   In general, the state of stress at a point is characterized by six stress components
-   In practice, this is rare, as most stresses and forces act in the same plane
-   This case is referred to as plane stress

----
## transformation

![](../images/transformation.png)

----
## procedure

-   If the state of stress (*σ*<sub>*x*</sub>, *σ*<sub>*y*</sub>, *τ*<sub>*xy*</sub>) is known for a known axis system *x* and *y*, we can find the stress relative to some rotated coordinate system
-   We do this by considering a section of the element perpendicular to the *x*<sup>′</sup> axis
-   Sum of forces in *x* and *y* will give *σ*<sub>*x*<sup>′</sup></sub> and *τ*<sub>*x*<sup>′</sup>*y*<sup>′</sup></sub>
-   A second section is needed to find *σ*<sub>*y*<sup>′</sup></sub>, perpendicular to the *y*<sup>′</sup> axis

----
## procedure

![](../images/transformation-2.png)

----
## example 9.1

![](../images/example-9-1.jpg) <!-- .element width="50%" -->

Represent the state of stress shown on the fuselage section on an element rotated 30&deg; clockwise from the position shown.
