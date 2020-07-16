# AE333
## Mechanics of Materials
Lecture 4 - Strain<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

February 1, 2019

----

## schedule

- 1 Feb - Allowable stress, Strain
- 4 Feb - Strain, Mechanical Properties
- 6 Feb - Mechanical Properties, Exam 1 Review, HW2 Due
- 8 Feb - Exam 1

----
## outline

- allowable stress
- limit state
- strain

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
  -   Weight is considered a *dead load* and can usually be determined
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
The 400 kg uniform bar, $AB$ is supported by a steel rod $AC$ and a roller at $B$. If it supports a live distributed loading, determine the required diameter of the rod. Use $\sigma_{fail}=345 \text{ MPa}$ with $\phi=0.9$, $\gamma_D=1.2$, and $\gamma_L=1.6$
</div>

---
# strain

----
## deformation

-   When forces are applied to a body, it will change its shape and size
-   We call these changes *deformation*
-   Sometimes they are barely noticeable (steel), other times they are very significant (rubber)

----
## strain

-   Strain is a more precise measurement of the deformation of a body
-   Normal strain is given as the change in length divided by the original length
$$\\epsilon = \\frac{L-L\_0}{L\_0}$$
-   We can consider the average normal strain (over an entire body) or the local strain (take an infinitely small portion and calculate the strain there)

----
## units

-   Since we divide length by length, strain is unitless
-   However it is customary to use *in/in* or for stiff specimens to use the phrase *microstrain* as a unit
-   Strain can also sometimes be represented as a percent

----
## shear strain

-   Normal strain causes a line segement to expand or contract
-   Deformation can also cause two lines to change their relative angle
-   The change in angle between two originally perpeindicular line segments is called shear strain
$$\\gamma = \\frac{\\pi}{2} - \\theta$$

----
## shear strain

![Three stages are shown, the first is a rectangular block at rest, with a fixed support on the ground. The second shows the block after it deforms with a horizontal force acting along the top to the right. The third showns the block after it deforms with a force acting along the top to the left. The first case causes a decrease in angle between the legs of the rectangle, the difference between 90 degrees and the new angle is called gamma, the engineering shear strain. When the angle becomes larger than 90 degrees, as in the third block, the engineernig shear strain is negative.](images\shear-strain.jpg)

----
## cartesian components

-   If we consider a very small cube/prism with sides of $\Delta x$, $\Delta y$, and $\Delta z$, normal strains will change the side lengths to
$$(1+\epsilon_x)\Delta x (1 + \epsilon_y)\Delta y (1 + \epsilon_z)\Delta z$$
-   And the shear strains will change the shape
$$\\frac{\\pi}{2}-\\gamma\_{xy} \\qquad \\frac{\\pi}{2}-\\gamma\_{yz} \\qquad \\frac{\\pi}{2}-\\gamma\_{xz}$$

----
## small strain

-   Most engineering analysis is based on the assumption of small strains
-   This is valid for many materials (wood, metal), but not for rubbers and some other polymers
-   When strains are small, we assume that the change in angle, `$\Delta \theta$` is very small
-   `$\sin \Delta \theta \approx \Delta \theta$`, `$\cos\Delta \theta \approx 1$`, `$\tan\Delta \theta\approx \Delta \theta$`

----
## example 2.1

![Two supports, B and C are spaced six meters apart horizontally. A cable is hanging from each support and joined by a ring at point A, which is horizontally between points B and C but 4 meters below them. The ring is pulled to A prime which is 20 mm below A and 10 mm to the left](images\example-2-1.jpg)<!-- .element width="45%" -->

Find the normal strains in the two wires if A moves to `$A^\prime$`

----
## example 2.3

<div class="left">
![A 150 mm square block is constrained along the top, left, and bottom faces, but pushed 2 mm to the left on its right face. AC is the diagonal line going from the top left to the bottom right. E is the center point of the block (where the two diagonals intersect after deformation).](images\example-2-3.jpg)
</div>
<div class="right">
The plate is fixed along AB and held in horizontal guides along AD and BC. If the right side is displaced 2 mm find the average normal strain along AC and the shear strain at E relative to the x and y axes.
</div>
