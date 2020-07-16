## AE333
## Mechanics of Materials
Lecture 29 - Statically Indeterminate Beams<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

15 Apr, 2019

----

## schedule

- 15 Apr - Statically Indeterminate Beams, HW 9 Due
- 17 Apr - Statically Indeterminate Beams
- 19 Apr - Statically Indeterminate Beams
- 22 Apr - Exam 3 Review, HW 10 Due
- 24 Apr - Exam 3


----
## outline

<!-- vim-markdown-toc GFM -->

* superposition
* statically indeterminate beams

<!-- vim-markdown-toc -->

---
# superposition

----
## superposition

-   The differential equation *EId*<sup>4</sup>*v*/*dx*<sup>4</sup> = *w*(*x*) satisfies the requirements for superposition
-   *w*(*x*) is linearly related to *v*(*x*)
-   Load does not significantly change the shape of the beam

----
## superposition

-   This means we can superpose multiple deflection solutions from simpler cases
-   Appendix C in the text has many solutions that can be superposed

----
## example 12.13

![](..\images\example-12-13.jpg)

Use superposition to find the displacement at C and the slope at A

----
## example 12.15

![](..\images\example-12-15.jpg)

Use superposition to find the displacement at C

----
## example 12.16

![](..\images\example-12-16.jpg)

The steel bar is supported by springs with k=15 kip/ft originally unstretched. For the force shown, determine the displacement at C. Take `$E_{st}=29$` Msi and `$I=12\text{ in}^4$`.

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
