## AE333
## Mechanics of Materials
Lecture 30 - Statically Indeterminate Beams<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

17 Apr, 2019

----

## schedule

- 17 Apr - Statically Indeterminate Beams
- 19 Apr - Statically Indeterminate Beams
- 22 Apr - Exam 3 Review, HW 10 Due
- 24 Apr - Exam 3


----
## outline

<!-- vim-markdown-toc GFM -->

* statically indeterminate beams
* indeterminate beams - superposition

<!-- vim-markdown-toc -->

---
# statically indeterminate beams

----
## statically indeterminate

-   If we have redundant supports, we can have some difficulty finding the displacement
-   There are several approaches to solve these problems, we will consider direct integration and superposition

----
## integration

-   We can take the extra unknowns and include them in our formulation for *M*(*x*)
-   They will be solved for with the extra boundary conditions applied

----
## example 12.17

![](..\images\example-12-17.jpg)

----
## example 12.18

![](..\images\example-12-18.jpg)

---
# indeterminate beams - superposition

----
## superposition

-   To use superposition for finding deflection of statically indeterminate beams, we must first identify redundant reactions
-   We initially remove these, then superpose them back such that the deflection at that point is 0
-   The choice of which reaction(s) is redundant is arbitrary, we can choose whatever we are most comfortable with
-   We use Appendix C to find deflection and slope

----
## superposition

![](..\images\indeterminate-deflection.jpg)

We can consider any reaction to be redundant.

----
## higher order indeterminacy

![](..\images\higher-order.jpg)

We need to treat each reaction separately to match Appendix C.

----
## example 12.22

![](..\images\example-12-22.jpg)

Determine the moment at B.
