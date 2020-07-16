# AE333
## Mechanics of Materials
Lecture 3 - Average Stress<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

January 28, 2019

----

## schedule

- 28 Jan - Average stress, Intro HW Due
- 30 Jan - Assessment Test
- 1 Feb - Allowable stress, Strain
- 4 Feb - Strain, Mechanical Properties

----

## office hours

- Office hours will be Fridays from 11:00 - 12:00
- Send me an e-mail if you have a question and can't make it then
- My office is in WH 200D (inside the main AE offices in Wallace Hall)

----

## outline

  - assessment test
  - stress review
  - average normal stress
  - average shear stress

---

#  assessment test

----
## assessment test

  -   5 (multi-part) problems
  -   Integration of basic functions (polynomials, not trig)
  -   Moment with respect to an axis
  -   Vector addition, particle equilibrium
  -   Distributed loads
  -   Moments of inertia


---
# review

----
## example 1.8

<div class="left">
![A block 200 mm long has a leg resting against the floor at its right end, point C, and is supported by a vertical hanging rod at its left end (points A and B). A 3 kilonewton force pointing down is applied at some distance, x, from the left end.](images\example-1-8.jpg)
</div>

<div class="right">
Determine the position, x, of the load so that the average compressive stress at C is equal to the average tensile stress in the rod AB. The rod has an area of `$400\si{mm}^2$` and the contact at $C$ has an area of `$650\si{mm}^2$`.
</div>

---

# average shear stress

----

## shear stress

-   If we consider a section from a bridge-like structure we can
    demonstrate one way shear stress can be formed in a material
-   As a reminder, shear stress is formed by forces acting in the plane
    of a section cut

----

## shear stress

![A block bridging across two other blocks is loaded over the gap it is bridging. This loading creates a shear stress directly above the blocks it is bridging, which is further illustrated with some free body diagrams.](images\shear-stress.jpg)<!-- .element width="30%" -->

----

## shear stress equilibrium

-   If we consider equilibrium of an element subjected to shear on one
    face, we will find that there must be shear forces on other faces to
    remain in equilibrium
-   In the following example, we will consider the sum of forces in the
    y-direction and the sum of moments about the x-axis
-   We can convert between stresses and forces by recalling that
    `$\sigma = F/A$`, or `$F = \sigma A$`

----

## shear stress equilibrium

![A block section is loaded horizontally along its top edge. For the block to remain in equilibrium, it is shown that equal and opposite shear stresses must develop along the other 3 faces.](images\shear-equilibrium.jpg)<!-- .element width="90%" -->

----

## example 1-9

![A 6 meter long beam is shown with a pin support at the left end, a downward vertical load of 30 kilonewtons 2 meters from the left end and a rope support at a 3-4-5 triangle on the right edge (3 in the horizontal direction, 4 vertically). At the left end, the pin is in double shear, while the rope is attached with a single-shear bolt.](images\example-1-9.jpg)<!-- .element width="50%" -->

Determine the average shear stress in the 20-mm diameter pin at `$A$` and the 30-mm diameter pin at `$B$`.

----

## example 1-11

<div class="left">
![A wooden block is shown with one leg at a 3-4-5 angle and a 600 pound compressive load acting in the direction of that leg.](images\example-1-11.jpg)
</div>
<div class="right">
Determine the average compressive stress along the smooth contact of `$AB$` and `$BC$` and the average shear stress along the horizontal plane `$DB$`.
</div>

---
# allowable stress design

----

## allowable stress

  -   Most of the time, we design structures so the stress is less than
      some limit
  -   By setting a conservative allowable stress, we account for some
      manufacturing tolerances, unintended loads, and variability in
      mechanical properties

----

## factor of safety

  -   The factor of safety is the failure load divided by the allowable
      load
`$$FS = \frac{F_{fail}}{F_{allow}}$$`

  -   Since load and stress are linearly proportional, we could also
      define the factor of safety in terms of stress and it would be
      identical

----

## factor of safety

  -   Typical values for the factor of safety will vary based on
      application

  -   Aircraft and space vehicles might have a factor close to 1 to
      minimize weight

  -   Nuclear power plants might have a factor close to 3 since weight is
      not as important and failure would be catastrophic

----

## simple connections

  -   We can rearrange the equations `$\sigma=N/A$` and `$\tau=V/A$` to size
      components based on some allowable stress
`$$\begin{aligned}
  A &= \frac{N}{\sigma_{allow}}\\
  A &= \frac{V}{\tau_{allow}}
\end{aligned}$$`

----

## bearing stress

  ![A column under compressive loading, bearing stress is the stress developed under the column under this load.](images\bearing-stress.jpg)<!-- .element width="40%" -->

----

## embedded shear stress

![A rod embedded in concrete is under tension pulling it out. The shear stress on the outer edge of the rod inside the concrete is known as embedded shear stress.](images\embedded-shear.jpg)<!-- .element width="30%" -->

----

## lap joint shear

![Two plates are attached together and pulled in opposite directions. The shear stress between the two where they are attached is called lap shear.](images\lap-shear.jpg)<!-- .element width="50%" -->

---
# limit state design

----

## limit state design

  -   Allowable stress design accounts for uncertainty in the applied
      loading and the material properties in one factor of safety
  -   Limit state design separates these two into load and resistance
      factors

----

## load factors

  -   The load factor combines uncertainty in various types of load
  -   For example, a building can have loading from a few different
      sources, such as its own weight, people in the building, and snow on
      top of the building
  -   Weight is considered a “dead load” and can usually be determined
      more precisely than moving things like people

----

## load factors

  -   In this simple example, we consider a load factor, `$\gamma_D=1.2$`
      for the dead load, `$\gamma_L=1.6$` and `$\gamma_S=0.5$`
`$$R = 1.2D + 1.6L + 0.5S$$`

  -   These load factors combine the concept of a safety factor with the
      probability that loads will occur

----

## resistance factors

  -   Resistance factors, `$\phi$` are used to express the probability a
      material will fail at its limit load

  -   If we are very confident in the failure stress of a material (i.e.
      steel has little variability), we might use `$\phi=0.9$`

  -   If we are not as confident, (using a new material, or an organic
      material like wood with higher variability), we might use `$\phi=0.7$`

----

## design criteria

  -   If we call the nominal load `$P$`, then we can combine load and
      resistance factors using `$$\phi P \ge R$$`

----

## example 1-12

<div class="left">
![An l-shaped bracket has an 8 inch vertical leg and a 5 inch horizontal leg. A single shear pinned connector holds the point of the leg, A, in place while a double shear pinned connector holds the base of the L at point C in position. There is 3 kilopound load 3 inches to the right of C acting downward and a 5 kilopound load 2 inches to the right of that acting down and to the right in the direction of a 3-4-5 triangle (3 down, 4 to the right).](images\example-1-12.jpg)
</div>
<div class="right">
Determine to the nearest 1/4" the diameters of steel pins at $A$ and $C$ if the factor of safety in shear is 1.5 and the failure shear stress is 12 ksi.
</div>

----

## example 1-15

<div class="left">
![A 2 meter long beam is supported at the left end with a steel rod connecting vertically. It is subjected to a uniform load of 3 kilonewtons per meter, and a roller support at the right end.](images\example-1-15.png)
</div>
<div class="right">
The 400 kg uniform bar, $AB$ is supported by a steel rod $AC$ and a roller at $B$. If it supports a live distributed loading, determine the required diameter of the rod. Use $\sigma_{fail}=345 \si{MPa}$ with $\phi=0.9$, $\gamma_D=1.2$, and $\gamma_L=1.6$
</div>
