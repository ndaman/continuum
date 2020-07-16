## AE333
## Mechanics of Materials
Lecture 36 - Buckling<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

3 May, 2019

----

## schedule

- 3 May - Buckling
- 6 May - Final Review, HW11 Due
- 8 May - Final Review
- 15 May 1:00 - 2:50 - Final Exam


----
## outline

<!-- vim-markdown-toc GFM -->

* buckling
* ideal pin-supported column
* columns with other supports

<!-- vim-markdown-toc -->

---
# buckling

----
## stability

-   In enineering problems, stability and instability relate how an object behaves when it experiences some random perturbation
-   A stable aircraft has aerodynamic features that tend to keep it flying level, small bumps of wind that would cause it to rotate will eventually get pushed back to level
-   Some aircraft are designed to be unstable (can have a tighter turn radius), but they need to be actively controlled, as a small perturbation will cause them to spiral out of control

----
## buckling

-   For long and slender structures, stability comes into play in the form of buckling
-   A structure that is subject to buckling is generally referred to as a column
-   Buckling is usually a very sudden and drastic failure, so we need to design columns to avoid buckling

----
## critical load

-   The critical load is the maximum load a column can hold before buckling
-   We can model the critical load by considering the column as a rigid truss with a spring force acting to maintain stability
-   When the loading force overcomes the spring force, buckling occurs

----
## critical load

![](..\images\buckling-truss.jpg) <!-- .element width="30%" -->

----
## critical load

-   The balance of forces will be
    *F* = *kΔ* = *P*tan*θ*
-   For small *θ*, we can further say that *Δ* = *θ*(*L*/2) and tan*θ* = *θ*

----
## critical load

-   We find that, for stability, we need

`$$P < \frac{kL}{4}$$`

---
# ideal pin-supported column

----
## ideal column

-   Our previous analysis treated a column as a two-member truss with a spring, but we can be more precise
-   An ideal column is made of homogeneous linear elastic material and is perfectly straight before loading
-   The load is assumed to be applied through the centroid of the cross section

----
## euler-bernoulli

-   We can treat the column as a beam and use the familiar relationship

$$EI \\frac{d^2v}{dx^2} = M$$

----
## euler-bernoulli

![](..\images\column-fbd.jpg) <!-- .element width="30%" -->

----
## solution

-   We see by equilibrium that *M* = −*Pv*, which gives the differential equation

$$\\begin{aligned}
  EI \\frac{d^2v}{dx^2} &= -Pv \\\\
  \\frac{d^2v}{dx^2} + \\frac{P}{EI}v &= 0
\\end{aligned}$$

-   Which has the solution

$$v = C\_1 \\sin \\left( \\sqrt{\\frac{P}{EI}}x \\right) + C\_2 \\cos \\left( \\sqrt{\\frac{P}{EI}}x \\right)$$

----
## boundary conditions

-   We know that for *v* = 0 at *x* = 0, *C*<sub>2</sub> = 0
-   We also know that *v* = 0 at *x* = *L* which gives

$$C\_1 \\sin \\left( \\sqrt{\\frac{P}{EI}}L \\right) = 0$$

-   *C*<sub>1</sub> = 0 would give the trivial solution, or we can say that

$$\\sqrt{\\frac{P}{EI}}L = n \\pi$$

----
## critical load

-   The smallest value where this occurs is when *n* = 1 and gives the critical load of

$$P\_{cr} = \\frac{\\pi^2 EI}{L^2}$$

-   This is sometimes called the “Euler Load”
-   We can increase *P*<sub>*cr*</sub> by decreasing *L*, increasing *E*, or increasing *I*

----
## radius of gyration

-   Sometimes we desire to find the critical stress instead of the critical load
-   We re-formulate the equation with *I* = *Ar*<sup>2</sup> (where *r* is the radius of gyration)
-   This gives

$$\\sigma\_{cr} = \\frac{\\pi^2 E}{(L/r)^2}$$

-   L/r is often called the slenderness ratio

----
## example 13.1

![](..\images\example-13-1.jpg) <!-- .element width="20%" -->

Find the largest axial load the A992 steel member shown can support before it buckles or yields, use σ <sub>y</sub>=50 ksi.

---
# columns with other supports

----
## other supports

- we can still use Euler-Bernoulli beam theory when handling columns with other supports
- the general derivation is the same, but with different boundary conditions

----
## effective length

- One simple way to use the same formula for different supports is to modify the effective length of the column
- We can also use a length factor, *K*, to define the effective length

`$L_e = K L$`

----
## length factors

<div class="left">
![](..\images\col-free.jpg) 
</div>

<div class="right">
![](..\images\col-fixed-free.jpg) <!-- .element width="80%" -->
</div>

----
## length factors

<div class="left">
![](..\images\col-fixed-fixed.jpg) 
</div>

<div class="right">
![](..\images\col-fixed-pinned.jpg) <!-- .element width="70%" -->
</div>

----
## effective length

- The formulas now become

`$ P_{cr} = \frac{\pi^2 EI}{(KL)^2} $`

- or 

`$ \sigma_{cr} = \frac{\pi^2 E}{(KL/r)^2} $`

----
## example 13.2

![](..\images\example-13-2.jpg) <!-- .element width="20%" -->

The column shown is braced by cables preventing movement in *x*.
Determine the largest *P* that can be applied if *E=70* GPa, σ<sub>y</sub>=215 MPa, *A* = 7.5 (10<sup>3</sup>) m<sup>2</sup>, I<sub>x</sub> = 61.3 (10<sup>-6</sup>) m<sup>4</sup> and I<sub>y</sub> = 23.2(10<sup>-6</sup>) m<sup>4</sup>.

----
## example 13.3

![](..\images\example-13-3.jpg) <!-- .element width="20%" -->

A W6 x 15 steel column is fixed at its ends and braced in the *y-y* axis assumed to be pinned at the midpoint.
Determine the maximum load before buckling or yield with E<sub>st</sub> = 29 Msi and σ<sub>y</sub> = 60 ksi.
