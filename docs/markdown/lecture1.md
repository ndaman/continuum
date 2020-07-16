# AE333
## Mechanics of Materials
Lecture 1 - Equilibrium
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

January 23, 2019

----

## schedule

- 23 Jan - Introduction, Equilibrium
- 25 Jan - Stress
- 28 Jan - Average stress, Intro HW Due
- 30 Jan - Assessment Test

----

## outline

  - introduction
  - syllabus
  - mechanics
  - equilibrium

---

# introduction

----

## about me
![family picture](images\IMG_5266_edit.jpg)

----

## education
  - B.S. in Mechanical Engineering from Brigham Young University
    - Worked with ATK to develop tab-less gripping system for tensile testing composite tow specimens
    - Needed to align the specimen, as well as grip it without causing a stress concentration

----

## education
  - M.S. and Ph.D. from School of Aeronautics and Astronautics at Purdue University
    - Worked with Boeing to simulate mold flows
    - First ever mold simulation with anisotropic viscosity

----

## research
![picture of chopped carbon fiber prepreg](images\Formosa_Chopped_Carbon_Fiber_CSc_bw.jpg)

----

## research
![picture of lamborghini symbol made from compression molded chopped carbon fiber](images\lamborghini-chopped-fiber-badges-rough.jpg)

----

## research

  - No simulation is currently able to predict fiber orientation from these processes
  - Part of the challenge is that we only have information from initial state and final state
  - I want to quantify intermediate stages using a transparent mold

----

## research

  <div class='left'>
![picture illustrating the fused deposition modeling 3D printing process, where plastic filament is melted and deposited next to other filament, and fuses together](images\3D-printing.png)
  </div>

  <div class='right'>
  <ul>
  <li> Composites are being used in 3D printing now </li>
  <li> Printing patterns are optimized for isotropic materials </li>
  <li> Sometimes composites hurt more than they help when not utilized properly </li>
  </div>

----

## introductions

  - Name
  - One interesting thing to remember you by

---

# syllabus and schedule

----

## course textbook

-  R.C. Hibbeler - Mechanics of Materials
-  We WILL be using Mastering Engineering for homework, so you will need a license/account for that to submit homework assignments

----

## office hourse

-   I will e-mail everyone in the course a Doodle link we can use to
    find the optimal office hours
-   Let me know if you do not receive the e-mail, you may need to update
    your information in Blackboard
-   If the regular office hours do not work for your schedule, send me
    an e-mail and we can work out a time to meet

----

## tentative course outline

-   Section 1 - stress, strain, mechanical properties
    -   Ch 1 - Stress (23 Jan)
    -   Ch 2 - Strain (30 Jan)
    -   Ch 3 - Mechanical Properties (4 Feb)
    -   Exam 1 (8 Feb)

----

## tentative course outline

-   Section 2 - loading
    -   Ch 4 - Axial Load (11 Feb)
    -   Ch 5 - Torsion (18 Feb)
    -   Ch 6 - Bending (25 Feb)
    -   Ch 7 - Transverse Shear (4 Mar)
    -   Exam 2 (8 Mar)

----

## tentative course outline

-   Section 3 - beams, shafts, combined loading
    -   Ch 8 - Combined Loading (18 Mar)
    -   Ch 9 - Stress Transformation (25 Mar)
    -   Ch 10 - Strain Transformation (1 Apr)
    -   Ch 12 - Deflection of Beams and Shafts (8 Apr)
    -   Exam 3 (26 Apr)

----

## tentative course outline

-   Section 4 - buckling, stress concentration
    -   Ch 4.7, 5.8, 6.9 - Stress concentration (29 Apr)
    -   Ch 13 - Buckling (6 May)
    -   Final Exam (comprehensive) (15 May)

----

## grades

-   Grade breakdown
    -   Assessment Test 2%
    -   Class Participation 3%
    -   Homework 10%
    -   Exam 1 20%
    -   Exam 2 20%
    -   Exam 3 20%
    -   Final Exam 25%

----

## grades

-   Follow a traditional grading scale
-   (80% B-, 83% B, 87% B+, etc.)

----

## curve

-   I do NOT curve final grades
-   Instead, each individual exam is curved on a best-fit linear scale
-   This scale is somewhat subjective, best score is mapped to 100, I
    pick one other score to map that I feel is representative of a C or
    a B
-   The end goal of this curve is to get a standard deviation close to
    10% and a class average representative of the performance on the
    exam, usually between a C and a B

----

## class expectations

-   Consider the cost (to you or others) of your being in class
-   I ask that you refrain from distracting behaviors during class
-   When you have something more important than class to take care of,
    please take care of it outside of class

----

## homework

-   In general, homework assignments will be due every Monday by
    midnight
-   We use Mastering Engineering for homework in this class
-   You are allowed 5 incorrect answers (-3% for each incorrect answer)
-   The first assignment is graded as pass/fail and is to help you
    become familiar with the online homework system

----

## assessment test

-   The assessment test will be graded, and accounts for 2% of your
    final grade
-   You should do your best, but it is meant as a measure of what you
    have learned before starting this class, so no study or preparation
    materials will be provided
-   You will be provided with an equation sheet taken from the inside
    cover of your textbook
-   Bring a scientific calculator (capable of sine and cosine)

----

## assessment test topics

-   Vector mechanics (cartesian vector notation, summation of vectors)
-   Friction (static coefficient of friction)
-   Dot product
-   Torque (i.e. moment due to offset forces)
-   Equilibrium (extension of vector mechanics)

----

## assessment test

-   Test will consist of both multiple choice and working problems
-   The test will be fixed at 50 minutes
-   The purpose is to determine how well-prepared you are for mechanics
    of materials
-   We are trying to determine which students need extra help (both you
    individually and in general for future students), this test is part
    of ongoing research and is optionally accompanied by a survey

---

# mechanics

----

## mechanics

-   Generally subdivided into three branches
  -   Rigid-body mechanics
  -   Deformable-body mechanics
  -   Fluid mechanics

----

## rigid-body mechanics

-   Statics - bodies in equilibrium (rest or constant velocity)
-   Dynamics - bodies under accelerated motion (`$F=ma$`)

---

# equilibrium of a deformable body

----

## loads

-   Surface loads act on the surface of a body, can be either
    concentrated forces or distributed loads
-   Body forces are developed inside a body, some examples are gravity
    or electromagnetic fields

----

## support reactions

-   In general, if a support prevents translation in a given direction,
    then a reaction force must be developed in that direction
-   Similarly, if a support prevents rotation about an axis, then a
    couple moment must be developed about that axis

----

## equilibrium

-   For a body to be in equilibrium the balance of forces and the
    balance of moments must both be zero
`$$\sum F_i =0$$ $$\sum M_i =0$$`
-   For 2D problems, this reduces to
`$$\begin{aligned}
  \sum F_x &= 0\\
  \sum F_y &= 0\\
  \sum M_O &= 0
\end{aligned}$$
`

----

## internal resultant loadings

-   We use statics to find resultant loadings acting within a body
-   This is done using the method of sections

----

## internal resultant loadings

-   Normal Force, N - acts perpendicular to an area
-   Shear Force, V - lies in the plane of an area, causes two segments
    to slide over one another
-   Torsional Moment, T - tendency to twist about an axis perpendicular
    to an area
-   Bending Moment, M - tendency to bend the body about an axis lying
    within the plane of the area

----

## planar problems

-   In planar problems, where all forces lie in the same plane, we only
    have
    -   Normal Force
    -   Shear Force
    -   Bending Moment

----

## summary

-   Support reactions
-   Free body diagram
-   Equations of equilibrium

---
# examples

----

## example 1.1

![Example 1.1 from the text, showing a cantilever beam with a distributed load, 270 newtons per meter at the end closest to the fixed support decreasing linearly to 0 newtons per meter at the end. The beam is 9 meters long and we need to find the internal forces at Point C, located 3 meters away from the fixed end.](images\example-1-1.png)<!-- .element width="70%" -->

Find the internal forces at point C.

<!-- spring 2019 we finished in the middle of this problem-->

----

## example 1.4
<div class="left">
![Example 1.4 from the text, depicting an l-shaped shaft with the two legs being 1.25 meters long. If we consider the fixed end of the shaft to be the origin, the shaft proceeds 1.25 meters along the y-axis, then angles 90 degrees to continue 1.25 meters along the x-axis. At the free end, there is a 70 newton-meter couple moment applied about the x-axis, as well as a 50 newton load in the negative z-direction and a 30 newton load in the positive y-direction. Find the internal forces at point d, located 0.75 meters from the fixed end (along the y-axis).](images\example-1-4.jpg)<!-- .element width="90%" -->
</div>
<div class="right">
Find the internal forces at point D.
</div>
