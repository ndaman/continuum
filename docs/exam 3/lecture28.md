## AE333
## Mechanics of Materials
Lecture 28 - Superposition<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

12 Apr, 2019

----

## schedule

- 12 Apr - Superposition
- 15 Apr - Deflection of Beams, HW 9 Due
- 17 Apr - Deflection of Beams
- 19 Apr - Deflection of Beams
- 22 Apr - Exam 3 Review, HW 10 Due
- 24 Apr - Exam 3


----
## outline

<!-- vim-markdown-toc GFM -->

* discontinuity functions
* group problems
* superposition

<!-- vim-markdown-toc -->

---
# discontinuity functions

----
## discontinuity functions

-   Direct integration can be very cumbersome if multiple loads or boundary conditions are applied
-   Instead of using a piecewise function, we can use discontinuity functions

----
## Macaulay functions

-   Macaulay functions can be used to describe various loading conditions, the general definition is

$$\\langle x-a\\rangle^n = \\begin{cases}
  0 & \\text{for } x &lt; a\\\\
  (x-a)^n & \\text{for } x \\ge a
\\end{cases}
n \ge 0$$

----
## singularity functions

-   Singularity functions are used for concentrated forces and can be written
    
$$w = P\\langle x-a\\rangle^{-1} = \\begin{cases}
  0 & \\text{for } x\\ne a\\\\
  P & \\text{for } x=a
\\end{cases}$$

----
## discontinuity functions

![](..\images\discontinuity.jpg) <!-- .element width="40%" -->

----
## discontinuity functions

1. We add these up for each loading case along our beam
2. We integrate as usual to find displacement from load, slope, or moment

----
## integration

- discontinuity functions follow special rules for integration
- when n &ge; 0, they integrate like a normal polynomial
- when n &lt; 0, they instead follow 

$$ \int \langle x-a \rangle ^n dx = \langle x - a \rangle ^{n+1} $$

----
## signs

- we need to be careful to match the sign convention
- loads are defined as positive when they act upward
- moments are defined as positive when they act clockwise

----
## example 12.5

![](..\images\example-12-5.jpg) 

---
# group problems

----
## group one

![](..\images\group-12-1.jpg) <!-- .element width="50%" -->

Find the maximum deflection using either direct integration or discontinuity functions.

----
## group two

![](..\images\group-12-2.jpg) <!-- .element width="50%" -->

Find the maximum deflection using either direct integration or discontinuity functions.

----
## group three

![](..\images\group-12-3.jpg) <!-- .element width="50%" -->

Find the maximum deflection using either direct integration or discontinuity functions.

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
