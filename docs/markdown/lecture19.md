## AE333
## Mechanics of Materials
Lecture 19 - Transverse Shear<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

22 Mar, 2019

----

## schedule

- 22 Mar - Transverse Shear
- 25 Mar - Combined Loading, HW6 Due
- 27 Mar - Combined Loading
- 29 Mar - Combined Loading

----
## outline
<!-- TOC START min:1 max:1 link:false update:true -->
- shear flow in built-up members
- thin-walled pressure vessels

<!-- TOC END -->

---
# shear flow in built-up members

----
## built-up members

-   Often in practice, structural members are "built-up"
-   This refers to parts that are comprised of several other parts to have greater strength in certain areas
-   We need to analyze the shear between these members to choose appropriate adhesives or fasteners

----
## equilibrium

![](images\built-up-equilibrium.jpg)

----
## equilibrium

-   From equilibrium we see that
$$dF = \\frac{dM}{I} \\int\_{A^\\prime} y dA^\\prime$$
-   We recall that this integral represents *Q*, we can also define the shear flow as *q*=*dF*/*dx* and recall that *dM*/*dx*=*V* to find
$$q = \\frac{VQ}{I}$$

----
## fastener spacing

-   We can use shear flow to determine fastener spacing
-   Say a fastener can support a shear force of *F*<sub>0</sub> before failure
-   The shear flow (force/distance) times the spacing (distance) will give the shear force per fastener
    *F*=*qs*

----
## multiple fasteners

![](images\shear-flow-multiple.jpg)

----
## multiple fasteners

-   When multiple arms are connecting the same area (as shown in the previous slide)
-   The shear flow "seen" by each fastener is *q*/*n* where *n* is the number of fastners per area

----
## example 7.4

![](images\example-7-4.jpg) <!-- .element width="30%" -->

Determine the shear flow at B and B' that must be resisted by glue to bond the boards together.

----
## example 7.5

<div class="left">
  ![](images\example-7-5.jpg)
</div>

<div class="right">
  If each nail can support a maximum shear force of 30 lb, determine the maximum spacing of the nails at B and at C so that the beam can support the force of 80 lb.
</div>

----
## example 7.6

![](images\example-7-6.jpg) <!-- .element width="50%" -->

Nails with a shear strength of 40 lb are used in a beam that can be constructed as shown in Case I or Case II. If the nails are spaced at 9 in determine the largest vertical shear that can be supported.

---
# thin-walled pressure vessels

----
## thin-walled pressure vessels

-   If the radius to wall thickness ratio is 10 or more, we can treet a pressure vessule as "thin-walled"
-   Cylindrical pressure vessels will have two primary sources of stress, and serve as an introduction to more general states of combined loading

----
## cylindrical vessels

![](images\cylinder-slice.jpg) <!-- .element width="30%" -->

----
## cylindrical vessels

-   From equilibrium of a section of a cylindrical vessel, we see that
$$\\begin{aligned}
  \\sum F\_x &= 0\\\\
  &= 2(\\sigma\_1 t dy) - p (2r) dy\\\\
  \\sigma\_1 &= \\frac{pr}{t}
\\end{aligned}$$

----
## cylindrical vessels

![](images\cylinder-end.jpg) <!-- .element width="50%" -->

----
## cylindrical vessels

-   Considering another section we can find the longitudinal stress
$$\\begin{aligned}
  \\sum F\_y &= 0\\\\
  &= \\sigma\_2 (2\\pi rt) - p (\\pi r^2)\\\\
  \\sigma\_2 &= \\frac{pr}{2t}
\\end{aligned}$$

----
## spherical vessels

-   We can find the stress in spherical vessels using an identical section to the longitudinal section for a cylindrical vessel, and we find that
    $$\\sigma = \\frac{pr}{2t}$$
-   Which is valid everywhere in a cylindrical vessel

----
## example 8.1

-   A cylindrical pressure vessel has an inner diameter of 4 ft. and a thickness of 1/2 in.
-   Determine the maximum internal pressure it can sustain if the maximum stress it can support is 20 ksi.
-   What is the maximum internal pressure a spherical pressure vessel could sustain under identical conditions?
