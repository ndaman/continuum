
# AE333
## Mechanics of Materials
Lecture 7 - Axial Load<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

February 11, 2019

----

## schedule

- 11 Feb - Exam 1 Return, Axial Load
- 13 Feb - Axial Load
- 15 Feb - Torsion
- 18 Feb - Torsion, HW3 Due

----
## outline
- saint venant's principle
- elastic axial deformation
- superposition
- statically indeterminate

---
# exam 1

----
## scores
- class average: 66.7 -> 74.9
- curve formula: old score x 0.926 + 12.963
- hardest question: 3
- easiest question: 4

---
# saint venant's principle

----
## saint venant's principle

-   We use Saint Venant's principle to generalize various loading applications
-   If we apply a concentrated force, near where we apply it (for example, along a pin), the stress will not be very uniform
-   Far away from that point, however, the stess will be uniform, whether we apply the force with 1 pin, 2 pins, or via a uniform grip

----
## saint venant's principle

-   We use *saint venant's principle* to replace difficult to model loads with easier ones
-   There are two conditions
    1.  The load must be statically equivalent
    2.  Our region of interest must be far enough away from the point where the load was applied

----
## saint venant's principle

![An image showing what the stress field looks like in a body both near to an applied load and far away.](images\st-venant.jpg)

---
# elastic axial deformation

----
## axially loaded member

-   We can use Hooke's Law to find the deformation of a general body under axial loading (below the elastic limit)

![If we consider some homogeneous body with an applied load, we can look at a small section of this body with an applied load of N(x) which is initially dx wide, but under load stretches an additional d delta.](images\axial-load.jpg)

----
## axially loaded member

-   For some differential element, we can consider the internal forces and stresses
$$\\sigma = \\frac{N(x)}{A(x)} = E(x) \\epsilon(x) = E(x) \\left(\\frac{d\\delta}{dx}\\right)$$
-   We can solve this for `$d\delta$` to find
$$d \\delta = \\frac{N(x) dx}{A(x)E(x)}$$
-   We integrate this over the length of the bar to find the total displacement

----
## sign convention

-   In general, we consider a force or stress to be positive if it causes tension and elongation
-   It is negative if it causes compression and contraction

----
## example 4.2

![The steel rod is 600 mm long and has an 80 kN load applied at the right end, the aluminum collar is 400 mm long.](images\example-4-2.jpg)<!-- .element width="60%" -->

A steel rod with a 10mm diameter is attached to a rigid collar passing through an aluminum tube with cross-sectional area of 400 mm<sup>2</sup>. Find the displacement at C if `$E_{st} = 200$` GPa and `$E_{al} = 70$` GPa.

----
## example 4.4

<div class="left">
![A cone has a radius of 0.3 m and a length of 3 m. The large end is fixed while the pointed end hangs down.](images\example-4-4.jpg)
</div>
<div class="right">
The cone shown has a specific weight of $\gamma = 6$ kN/m<sup>3</sup> and $E=9$ GPa.
Determine how far the end is displaced due to gravity.
</div>

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
