# AE333
## Mechanics of Materials
Lecture 5 - Strain, Mechanical Properties<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

February 4, 2019

----

## schedule

- 4 Feb - Strain, Mechanical Properties
- 6 Feb - Mechanical Properties, Exam 1 Review, HW2 Due
- 8 Feb - Exam 1
- 11 Feb - Exam 1 Return, Axial Load

----
## outline

- strain
- stress-strain
- strain energy
- poisson's ratio
- shear stress-strain

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


---
# stress-strain

----
## stress-strain

-   Most engineering materials can be characterized by their stress-strain diagram
-   Comes from a tensile or compressive test, where a load is applied (gives stress) and the strain is measured (via an extensometer or strain gauge)
-   *Engineering stress* is plotted on the y-axis vs. *engineering strain* on the x-axis

----
## stress-strain

![A stress-strain diagram for a typical metal. From left to right, the stress increases linearly until reaching the proportional limit, or yield stress, at which point the stress does not increase very much with increasing strain. When the strain reaches the strain hardening region, the stress begins to increase again with increasing strain until the material fails.](images\stress-strain.jpg)<!-- .element width="70%"-->

----
## elastic behavior

-   Most of the time, the linear region is the one we are most interested in
-   In this region, the material is elastic, meaning when the load is removed the material will return to its original state

----
## elastic behavior

-   Because the stress-strain curve is a straight line, we can relate stress and strain with a single constant
-   This constant is known as the *modulus of elasticity* or *Young's modulus*
`$$ \sigma=E \epsilon $$`

----
## plastic behavior

-   Yielding occurs when stress increases beyond the *yield stress* or *elastic limit*, this is when plastic deformation occurs, meaning the material will not go back to its original shape
-   Strain hardening is common in many metals, and means as more stress is applied the material becomes more stiff

----
## plastic behavior

-   Necking occurs when the material begins to have a noticeable "neck" due to being stretched very thin and lower forces are required to deform the material

----
## true stress-strain

-   True stress and strain use the actual material cross-section (instead of the original cross-section) to calculate stress and strain
-   In the elastic region the difference is negligible, so in many cases we just stick with engineering strain, even if we know it is *wrong*

----
## ductile materials

-   Ductile materials can undergo large strains before failure
-   One way to report how ductile a material is is known as percent elongation
-   Steel, brass, molybdenum, and zinc exhibit similar ductile stress-strain characteristics
-   Aluminum is often considered ductile, but it’s stress-strain behavior is a bit different

----
## brittle materials

-   Materials that exhibit little or no yielding before failure are called *brittle*
-   Cast iron, concrete, and glass are common brittle materials
-   Brittle materials fail easily in tension, but are very strong in compression

----
## strain hardening

![A stress-strain diagram showing how strain hardening works. A material is loaded beyond its elastic limit, and then unloaded. If it is loaded again, it will not yield until it reaches the final stress to which it had been previously loaded (but it will not have as much toughness).](images\strain-hardening.jpg) <!-- .element width="40%"-->

---
# strain energy

----
## strain energy

-   Work in physics is defined as force times distance
-   As a force is applied to a material, the energy from the work done by the load is stored in the material and called strain energy
-   In engineering, we often use the strain energy density, or the amount of strain energy per unit volume of material
$$u = \\frac{1}{2} \\sigma \\epsilon$$

----
## toughness

-   Graphically, the area under the stress strain curve represents the strain energy density
-   We call the entire region (usually for a ductile material) the *toughness*
-   Some hardened steels have a high failure strength, but are not very ductile, this gives them a lower toughness

----
## example 3.3

<div class="left">
![A bar is under a 10 kilonewton tensile load. One section of the bar is 600 mm long with a 20 mm diameter, while the other section is 400 mm long with a 15 mm diameter. The stress-strain diagram below shows that for a stress of 56.59 MPa there will be a strain of .045](images\example-3-3.png)
</div>

<div class="right">
The aluminum rod shown has a circular cross-section. Determine the elongation of the rod when load is applied using the given stress-strain diagram.
</div>

---
# poisson's ratio

----
## poisson's ratio

-   When a material is stretched in one direction, it tends to contract in the transverse direction
-   The ratio of transverse to axial strain is called *Poisson's ratio*
$$\\nu = - \\frac{\\epsilon\_{transverse}}{\\epsilon\_{axial}}$$

---
# shear stress-strain

----
## shear stress-strain

-   It can be experimentally difficult to obtain a state of pure shear, but a common method for many materials is to place a thin tube in torsion
-   For most engineering materials, the shear stress-strain behavior is linear in the elastic region, but has a different constant relating stress to strain, known as the *Shear Modulus*
$$\tau=G \gamma $$

----
## elastic constants

-   For most materials, *E*, *G* and `$\nu$` are related by the following expression
$$G = \\frac{E}{2(1+\\nu)}$$

----
## example 3.5

<div class="left">
![A block 4 inches deep, 3 inches wide, and 2 inches tall is loaded in shear (in the 3 inch direction). The stress-strain diagram shows that at the elastic limit of 52 ksi there is a strain of 0.008.](images\example-3-5.png)
</div>
<div class="right">
Determine G for the specimen shown. Also find the maximum distance d, that the top could be displaced horizontally while remaining elastic. What force V is required to cause this displacement?
</div>
