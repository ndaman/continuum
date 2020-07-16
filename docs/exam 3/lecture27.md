## AE333
## Mechanics of Materials
Lecture 27 - Discontinuity Functions<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

10 Apr, 2019

----

## schedule

- 10 Apr - Discontinuity Functions
- 12 Apr - Superposition
- 15 Apr - Deflection of Beams, HW 9 Due
- 17 Apr - Deflection of Beams
- 19 Apr - Deflection of Beams
- 22 Apr - Exam 3 Review, HW 10 Due
- 24 Apr - Exam 3


----
## outline

<!-- vim-markdown-toc GFM -->

* slope and displacement
* discontinuity functions

<!-- vim-markdown-toc -->

---
# slope and displacement

----
## curvature

-   When talking about displacement in beams, we use the coordinates *v* and *x*, where *v* is the vertical displacement and *x* is the horizontal position
-   In this notation, curvature is formally related to displacement according to

$$\\frac{1}{\\rho} = \\frac{d^2v/dx^2}{\[1+(dv/dx)^2\]^{3/2}} = \\frac{M}{EI}$$

----
## curvature

-   The previous equation is difficult to solve in general, but for cases of small displacement, (*dv*/*dx*)<sup>2</sup> will be negligible compared to 1, which then simplifies to

$$\\frac{d^2v}{dx^2} = \\frac{M}{EI}$$

----
## flexural rigidity

-   In general, *M*, is a function of *x*, but *EI* (known as the flexural rigidity) is a constant along the length of the beam
-   In this case, we can say

$$\\begin{aligned}
  EI\\frac{d^2v}{dx^2} &= M(x) \\\\
  EI\\frac{d^3v}{dx^3} &= V(x) \\\\
  EI\\frac{d^4v}{dx^4} &= w(x)
\\end{aligned}$$

----
## boundary conditions

-   If a support restricts displacement, but not rotation, we will have a boundary condition of *v* = 0 at that point
-   Supports that restrict rotation give a boundary condition that *θ* = 0

----
## continuity conditions

-   If we have a piecewise function for *M*(*x*), not all integration constants can be found from the boundary conditions
-   Instead, we must also use continuity conditions to ensure that the slope and displacement are continuous at every point
-   In other words, for two sets of functions, *θ*<sub>1</sub>(*x*) and *v*<sub>1</sub>(*x*), *θ*<sub>2</sub>(*x*), and *v*<sub>2</sub>(*x*), *θ*<sub>1</sub>(*a*)=*θ*<sub>2</sub>(*a*) and *v*<sub>1</sub>(*a*)=*v*<sub>2</sub>(*a*)

----
## slope

-   For small displacements, we have
    *θ* ≈ tan*θ* = *dv*/*dx*

----
## example 12.1

![](..\images\example-12-1.jpg) <!-- .element width="60%" -->

Determine the maximum deflection if EI is constant.

----
## example 12.4

![](..\images\example-12-4.jpg) <!-- .element width="60%" -->

Determine the displacement at C, EI is constant.

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
