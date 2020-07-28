<span>upcoming schedule</span>

  - 12 Oct - Airy Stress

  - 17 Oct - Fall Break (no class)

  - 19 Oct - HW6 Due, Anisotropic Materials

  - 24 Oct - Anisotropic Materials

  - 31 Oct - HW7 Due, Large Deformation

  - 2 Nov - Large Deformation

### outline

\[sections numbered\]

# homework

<span>homework</span>

  - Velocity vector - remember to use material derivative

  - Strain tensor definition - will always be symmetric

  - Be careful when copying results from another source

# airy stress function

<span>body forces</span>

  - Body forces are often neglected, but they can be included in the
    Airy stress formulation by defining a potential function as follows
    \[\begin{aligned}
            \rho b_1 &= - \frac{\partial \mathcal{V}}{\partial x_1}\\
            \rho b_2 &= - \frac{\partial \mathcal{V}}{\partial x_2}
            \end{aligned}\]

<span>airy stress</span>

  - Let us now define the Airy stress function, \(\varphi (x_1,x_2)\)
    such that \[\begin{aligned}
            T_{11} &= \frac{\partial^2 \varphi}{\partial x_2^2} + \mathcal{V}\\
            T_{12} &= -\frac{\partial^2 \varphi}{\partial x_1 \partial x_2}\\
            T_{22} &= \frac{\partial^2 \varphi}{\partial x_1^2} + \mathcal{V}
            \end{aligned}\]

<span>airy stress in polar coordinates</span>

  - In polar coordinates we have \[\begin{aligned}
            \rho b_r &= - \frac{\partial \mathcal{V}}{\partial r}\\
            \rho b_\theta &= -\frac{1}{r} \frac{\partial \mathcal{V}}{\partial \theta}
            \end{aligned}\]

  - And \[\begin{aligned}
            \sigma_{rr} &= \frac{1}{r} \frac{\partial \varphi}{\partial r} + \frac{1}{r^2}\frac{\partial^2 \varphi}{\partial \theta^2} + \mathcal{V}\\
            \sigma_{\theta\theta} &= \frac{\partial^2 \varphi}{\partial r^2} + \mathcal{V}\\
            \sigma_{rr} &= -\frac{\partial \varphi}{\partial r} \left(\frac{1}{r}\frac{\partial \varphi}{\partial \theta}\right) 
            \end{aligned}\]

<span>airy stress function solutions</span>

  - To solve a problem using Airy stress functions, we need to solve
    this biharmonic equation
    \[\frac{\partial^4 \phi}{\partial x^4} + 2\frac{\partial^4 \phi}{\partial x^2 \partial y^2} + \frac{\partial^4 \phi}{\partial y^4} = 0\]

  - One solution to this is the power series
    \[\phi(x,y) = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty} A_{mn} x^m y^n\]

<span>power series solution</span>

  - Note that terms for \(m + n \le 1\) do not contribute to the stress,
    and can be neglected

  - Also note that for \(m + n \le 3\) compatibility is automatically
    satisfied

  - For \(m + n \ge 4\) the coefficients must be related for
    compatibility to be satisfied

<span>polar coordinates</span>

  - All solutions to the Beltrami-Mitchell equations in polar
    coordinates which are periodic in \(\theta\) can be summarized as
    \[\begin{aligned}
            \phi &= a_0 + a_1 \log r + a_2 r^2 + a_3 r^2 \log r \\
            &+ (a_4 + a_5 \log r + a_6 r^2 + a_7 r^2 \log r)\theta \\
            &+ \left(a_{11}r + a_{12}r\log r + \frac{a_{13}}{r} + a_{14}r^3 + a_{15}r\theta + a_{16} r\theta \log r\right) \cos \theta\\
            &+  \left(b_{11}r + b_{12}r\log r + \frac{b_{13}}{r} + b_{14}r^3 + b_{15}r\theta + b_{16} r\theta \log r\right) \sin \theta\\
            &+ \sum_{n=2}^{\infty} (a_{n1}r^n + a_{n2}r^{2+n}+a_{n3}r^{-n}+a_{n4}r^{2-n})\cos n\theta\\
            &+ \sum_{n=2}^{\infty} (b_{n1}r^n + b_{n2}r^{2+n}+a_{n3}r^{-n}+b_{n4}r^{2-n})\sin n\theta\\
            \end{aligned}\]

<span>polar coordinates</span>

  - For axisymmetric problems, all field quantities are independent of
    \(\theta\)

  - This reduces the general solution to
    \[\phi = a_0 + a_1 \log r + a_2 r^2 + a_3 r^2 \log r\]

<span>polar coordinates</span>

![image](../Figures/polar_table.PNG)
<span id="fig:polar_table" label="fig:polar_table">\[fig:polar\_table\]</span>

<span>polar coordinates</span>

![image](../Figures/airy_cylindrical2.PNG)
<span id="fig:airycylindrical2" label="fig:airycylindrical2">\[fig:airycylindrical2\]</span>

# examples

<span>pinned beam</span>

<span>example</span>

![image](../Figures/rotating_disk.PNG)
<span id="fig:rotatingdisk" label="fig:rotatingdisk">\[fig:rotatingdisk\]</span>

# group problems

<span>group one</span>

  - Find the form of a polynomial Airy stress function to solve this
    problem

  - Carefully note boundary conditions, particularly when replaced using
    Saint Venant&rsquo;s principle

  - Is your solution different from the text (p. 255)? Why/why not?

<span>group two</span>

  - Find the form of an Airy stress function which can solve this
    problem

<span>group three</span>

  - Show that the following Airy stress function can solve the problem
    of a cantilever beam with a distributed load
    \[\varphi = Ax_1x_2 + Bx_1^2 + Cx_1^2x_2 + Dx_2^3 + Ex_1 x_2^3 + Fx_1^2x_2^3 + Gx_2^5\]

  - Note: use Saint Venant&rsquo;s principle on both ends of the beam

<span>circular hole in rectangular plate</span>

  - We prefer polar coordinates solution near the hole, but rectangular
    solutions are easier at the rectangular boundaries

  - We can transform the stress tensor from rectangular coordinates to
    polar using \(Q_{ij}\) with an arbitrary \(\theta\)

<span>reading for next class</span>

  - Anisotropic elasticity - pp. 319 - 333
