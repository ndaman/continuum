## AE333
## Mechanics of Materials
Lecture 18 - Transverse Shear<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

20 Mar, 2019

----

## schedule

- 20 Mar - Transverse Shear
- 22 Mar - Transverse Shear
- 25 Mar - Combined Loading, HW6 Due

----
## outline
<!-- TOC START min:1 max:1 link:false update:true -->
- shear in straight members
- the shear formula
- group problems
- shear flow in built-up members

<!-- TOC END -->


---
# shear in straight members

----
## shear

-   We have discussed the internal stresses caused by the internal moment *M*
-   There are also internal shear stresses caused by the internal shear force *V*
-   We can illustrate the effect of internal shear stress by considering three boards, either resting on top of on another or bonded

----
## shear

![A comparison of three boards stacked on top of each other and loaded with pin supports at both ends. The top shows how the boards look if they are stacked with no bond, while the bottom shows the boards bonded together.](images\bonded-boards.png) <!-- .element width="60%" -->

---
# the shear formula

----
## shear formula

-   Internal shear causes a more complicated deformation state, so we will use an indirect method to find the shear stress-strain distribution
-   We will consider equilibrium along a section of a beam, then we will consider another section

----
## equilibrium

![A free body diagram of an arbitrary beam.](images\beam-fbd.png)

----
## equilibrium

![A section of some arbitrary cut of an arbitrary beam cross-section showing the shear acting on a sub-section of this element.](images\fbd-newsection.jpg) <!-- .element width="50%" -->

----
## equilibrium

-   There must be a shear force along the bottom to equilibrate the different stresses on either side of the section
-   If we assume that this shear is constant through the thickness, we obtain the following from equilibrium
`$$\sum F_x = 0 = \int_{A^\prime} \sigma^\prime dA^\prime - \int_{A^\prime} \sigma dA^\prime - \tau (t dx)$$`

----
## equilibrium
$$\\tiny{\\begin{aligned}
  0 &= \\int\_{A^\\prime} \\left( \\frac{M + dM}{I} \\right) y dA^\\prime - \\int\_{A^\\prime} \\left( \\frac{M}{I} \\right)y dA^\\prime - \\tau(t dx) \\\\
  \\left( \\frac{M}{I} \\right) \\int\_{A^\\prime} y dA^\\prime &= \\tau (t dx)\\\\
  \\tau &= \\frac{1}{It} \\left( \\frac{dM}{dx} \\right)\\int\_{A^\\prime} y dA^\\prime
\\end{aligned}}$$

----
## shear formula

-   In this formula, recall that $V = \\frac{dM}{dx}$
-   We also call *Q* the moment of the area `$A^\prime$` which is equal to `$\int_{a^\prime} y dA^\prime$`
-   We can also write *Q* in terms of the centroid
$$Q = \\bar{y}^\\prime A^\\prime$$

----
## shear formula

-   Simplified, the shear formula is
$$\\tau = \\frac{VQ}{It}$$
-   *Q* poses the greatest difficulty in calculations, so we will consider a few examples

----
## Q

-   *Q* represents the moment of the cross-sectional area above (or below) the point at which the shear stress is being calculated
-   We apply the formula to that area

----
## Q

![Some beam cross-sections to illustrate the calculation of Q](images\Q.jpg) <!-- .element width="35%" -->

----
## shear formula limitations

-   A major assumption made is that the shear stress was constant through the thickness, essentially we have found the average shear
-   This is more accurate the more slender a beam is (small *b* and large *h*)
-   The formula is also not accurate for cross sections that change or have boundaries that are not right angles

----
## procedure

-   First we find the internal shear, *V*
-   Find *I*, the moment of inertia (of the entire section) about the neutral axis
-   Find *t* from an imaginary cross-section at the point of interest
-   Calculate *Q* from either the area above or below the point of interest
-   $\tau$ acts in the same direction as *V* (and must be equilibrated on other faces)

----
## example 7.1

![A simply supported beam 8 meters long has a uniformly distributed load of 6.5 kN/m applied on the rightmost 4 meters. The beam has a t-shaped cross section with the top 150 mm wide and 30 mm tall and the bottom 150 mm tall and 30 mm wide.](images\example-7-1.jpg) <!-- .element width="35%" -->

Determine the maximum stress needed by a glue to hold the boards together.

----
## example 7.3

![An I-beam is shown with a width of 300 mm and height of 240 mm, a web 15 mm thick, and flanges 20 mm thick. There is a shear force of 80 kN applied.](images\example-7-3.jpg) <!-- .element width="50%" -->

Plot the shear stress distribution through the beam.

---
# group problems

----
## group one

![](images\group-7-1.jpg) <!-- .element width="30%" -->

Find Q and t that would be used to find the shear stress at A.

----
## group two

![](images\group-7-2.jpg) <!-- .element width="30%" -->

Find Q and t that would be used to find the shear stress at A.

----
## group three

![](images\group-7-3.jpg) <!-- .element width="30%" -->

Find Q and t that would be used to find the shear stress at A.

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
