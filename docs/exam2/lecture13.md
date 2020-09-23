# AE831
## Continuum Mechanics
Lecture 10 - Airy Stress<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

1 October, 2020

----
## schedule

- 1 Oct - Airy Stress
- 6 Oct - Elastic Solid
- 8 Oct - Elastic Solid
- 13 Oct - Exam Review

----
## outline

<!-- vim-markdown-toc GFM -->

* planar problems
* airy stress function
* examples

<!-- vim-markdown-toc -->

---
# planar problems

----
## plane strain

- If motion in any one direction (for example `\(x_3\)`) is restricted, such that `\(u_3 = 0\)`, a body is said to be in a state of plane strain
- The plane strain is often used for very thick materials, where `\(u_3 \ll u_1, u_2\)`, but is also applicable any time `\(u_3\)` is restricted

----
## plane strain

- Under plane strain conditions we have 
`\[\begin{aligned}
	E_{13} &= E_{23} = E_{33} = 0\\
	E_{11} &= E_{11}(x_1, x_2)\\
	E_{22} &= E_{22}(x_1, x_2)\\
	E_{12} &= E_{12}(x_1,x_2)
\end{aligned}\]`

----
## plane strain

- Using Hooke's Law, we find that `\(T_{13} = T_{23} = 0\)`, but
`\[T_{33} = \nu (T_{11} + T_{22})\]`

- While the other stress components, `\(T_{11}\)`, `\(T_{12}\)` and `\(T_{22}\)` are all functions of `\(x_1\)` and `\(x_2\)`

----
## plane strain

- In the absence of body forces, we find the equilibrium equations as
`\[\begin{aligned}
	\frac{\partial T_{11}}{\partial x_1} + \frac{\partial T_{12}}{\partial x_2} &= 0\\
	\frac{\partial T_{21}}{\partial x_1} + \frac{\partial T_{22}}{\partial x_2} &= 0\\
	\frac{\partial T_{33}}{\partial x_3} &= 0
\end{aligned}\]`

----
## plane stress

- For very thin bodies, we often make the assumption that `\(\sigma_{13} = \sigma_{23} = \sigma_{33} = 0\)`
- Since we have started from an assumption in stress instead of displacement, it is not yet apparent whether this stress field is allowable

----
## plane stress

- To simplify calculations for equilibrium and compatibility, we define a stress function, `\(\varphi\)` such that 
`\[\begin{aligned}
	\sigma_{11} &= \varphi_{,22}\\
	\sigma_{22} &= \varphi_{,11}\\
	\sigma_{12} &= -\varphi_{,12}
\end{aligned}\]`

----
## plane stress

- We can quickly verify that this satisfies equilibrium
`\[\begin{aligned}
	\varphi_{,221} - \varphi_{,122} &= 0\\
	\varphi_{,121} - \varphi_{,112} &= 0
\end{aligned}\]`

- We will not follow all the details, but from compatibility we find
`\[\varphi = \varphi_0(x_1,x_2) - \frac{\nu}{1+\nu}\Psi(x_1,x_2)\frac{1}{2}x_3^2\]`

----
## plane stress

- For plane stress problems, we generally consider the case where `\(x_3 \ll x_1, x_2\)`, and thus we can neglect the second term, giving our stresses as functions of `\(x_1\)` and `\(x_2\)` only
- Note that in general plane stress solutions only approximately satisfy compatibility

----
## beltrami-mitchell

- It is convenient to write the compatibility equations in terms of stress
- This is known as the Beltrami-Mitchell equations
- For planar problems, the Beltrami-Mitchell equations are
`\[\nabla^2 (\sigma_{11} + \sigma_{22}) = -\frac{4\rho}{1+\kappa} \left(b_{1,1} + b_{2,2}\right)\]`


----
## beltrami-mitchell

- `\(\kappa\)` is used to differentiate between plane strain and plane stress
`\[\kappa=\begin{cases}
	3 - 4\nu & \text{Plane Strain}\\
	\frac{3-\nu}{1+\nu} & \text{Plane Stress}
\end{cases}\]`

----
## polar coordinates

- Many planar problems are more conveniently expressed in polar coordinates
- For planar problems in polar coordinates the Beltrami-Mitchell equations become
`\[\nabla^2 (\sigma_{rr} + \sigma_{\theta \theta}) = -\frac{4\rho}{1+ \kappa} \left(b_{r,r} + \frac{1}{r} b_{\theta,\theta}\right)\]`

- There is a good summary of in-plane field equations in the supplemental elasticity text on page 127 (Cartesian) and 131-132 (Polar)

---
# airy stress function

----
## body forces

- Body forces are often neglected, but they can be included in the Airy stress formulation by defining a potential function as follows
`\[\begin{aligned}
	\rho b_1 &= - \frac{\partial \mathcal{V}}{\partial x_1}\\
	\rho b_2 &= - \frac{\partial \mathcal{V}}{\partial x_2}
\end{aligned}\]`

----
## airy stress

- Let us now define the Airy stress function, `\(\varphi (x_1,x_2)\)` such that
`\[\begin{aligned}
	T_{11} &= \frac{\partial^2 \varphi}{\partial x_2^2} + \mathcal{V}\\
	T_{12} &= -\frac{\partial^2 \varphi}{\partial x_1 \partial x_2}\\
	T_{22} &= \frac{\partial^2 \varphi}{\partial x_1^2} + \mathcal{V}
\end{aligned}\]`

----
## airy stress

- We can verify that any stress function obtained in this fashion will satisfy the equilibrium equations 
`\[\begin{aligned}
	\varphi_{,221} + \mathcal{V}_{,1} - \varphi_{,122} - \mathcal{V}_{,1} &= 0\\
	\varphi_{,121} + \mathcal{V}_{,2} - \varphi_{,112} - \mathcal{V}_{,2} &= 0
\end{aligned}\]`

- We use the Beltrami-Mitchell equation for compatibility
`\[\nabla^2 \nabla^2 \varphi = - \frac{2(\kappa-1)}{1+ \kappa} \nabla^2 \mathcal{V}\]`

----
## airy stress

- The general solution to the Beltrami-Mitchell equation can be written in the form
`\[\varphi = \varphi_c + \varphi_p\]`

- Where the complementary solution is a bi-harmonic function, while the particular solution depends on the body force

----
## airy stress

- Note: written in this manner the airy stress function is equally valid in polar or Cartesian coordinates, but note that
`\[\nabla^2 = \frac{\partial ^2}{\partial r^2} + \frac{1}{r} \frac{\partial }{\partial r} + \frac{1}{r^2} \frac{\partial^2}{\partial \theta^2}\]`

----
## airy solutions

- To solve a problem using Airy stress functions, we need to solve this biharmonic equation
`\[\frac{\partial^4 \phi}{\partial x^4} + 2\frac{\partial^4 \phi}{\partial x^2 \partial y^2} + \frac{\partial^4 \phi}{\partial y^4} = 0\]`

- One solution to this is the power series
`\[\phi(x,y) = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty} A_{mn} x^m y^n\]`

----
## power series solution

- Note that terms for `\(m + n \le 1\)` do not contribute to the stress, and can be neglected
- Also note that for `\(m + n \le 3\)` compatibility is automatically satisfied
- For `\(m + n \ge 4\)` the coefficients must be related for compatibility to be satisfied

----
## fourier methods

- While polynomial methods are very useful, they are somewhat ad-hoc
- Fourier methods provide a more direct approach
- Consider a separable Airy Stress Function of the form 
`\[\phi(x,y) = X(x) Y(y)\]`

- Where `\(X=e^{\alpha x}\)` and `\(Y=e^{\beta y}\)`

----
## fourier methods

- Substituting these values into the compatibility equation gives the requirement
`\[(\alpha^4 + 2\alpha^2 \beta^2 + \beta^4)e^{\alpha x}e^{\beta y} = 0\]`

- For this equation to be satisfied, 
`\[(\alpha^2 + \beta^2)^2 = 0\]`

- Which means `\(\alpha = \pm i\beta\)`

----
## fourier methods

- Substituting this result back into the general expression for `\(\phi\)` and converting to trigonometric and hyperbolic forms gives
`\[\begin{aligned}
	\phi &= \sin \beta x \left[(A+C\beta y)\sinh \beta y + (B + D\beta y) \cosh \beta y\right] \\
	&+ \cos \beta x \left[ (A^\prime + C^\prime \beta y) \sinh \beta y + (B^\prime + D^\prime \beta y)\cosh \beta y \right] \\
	&+ \sin \alpha y \left[(E+G\alpha x)\sinh \alpha x + (F+H\alpha x) \cosh \alpha x \right] \\
	&+ \cos \alpha y \left[ (E^\prime + G^\prime \alpha x) \sinh \alpha x + (F^\prime + H^\prime \alpha x)\cosh \alpha x \right] \\
	&+ \phi_{\alpha=0} + \phi_{\beta=0}
\end{aligned}\]`

----
## fourier methods

- Some problems with sinusoidal boundary conditions can be solved using the form developed, but a more general solution method incorporates a Fourier series
- Any periodic function with period `\(2L\)` can be represented as
`\[f(x) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty} \left(a_n \cos \frac{n \pi x}{L} + b_n \sin \frac{n \pi x}{L}\right)\]`


----
## fourier methods

- Where 
`\[\begin{aligned}
	a_n &= \frac{1}{L} \int_{-L}^L f(\xi) \cos \frac{n \pi \xi}{L} d\xi & n = 0,1,2, ...\\
	b_n &= \frac{1}{L} \int_{-L}^L f(\xi) \sin \frac{n \pi \xi}{L} d\xi & n = 1,2,3, ...
\end{aligned}\]`

----
## fourier methods

- There are many computational advantages to using a Fourier series (Fast Fourier Transform algorithms can be used)
- Analytically, Fourier Methods are particularly convenient when a boundary is known to either be an even or an odd function
- `\(\sin\)` terms drop from even functions, while `\(\cos\)` terms drop from odd functions

----
## polar coordinates

- All solutions to the Beltrami-Mitchell equations in polar coordinates which are periodic in `\(\theta\)` can be summarized as
`\[\begin{aligned}
	\phi &= a_0 + a_1 \log r + a_2 r^2 + a_3 r^2 \log r \\
	&+ (a_4 + a_5 \log r + a_6 r^2 + a_7 r^2 \log r)\theta \\
	&+ \left(a_{11}r + a_{12}r\log r + \frac{a_{13}}{r} + a_{14}r^3 + a_{15}r\theta + a_{16} r\theta \log r\right) \cos \theta\\
	&+  \left(b_{11}r + b_{12}r\log r + \frac{b_{13}}{r} + b_{14}r^3 + b_{15}r\theta + b_{16} r\theta \log r\right) \sin \theta\\
	&+ \sum_{n=2}^{\infty} (a_{n1}r^n + a_{n2}r^{2+n}+a_{n3}r^{-n}+a_{n4}r^{2-n})\cos n\theta\\
	&+ \sum_{n=2}^{\infty} (b_{n1}r^n + b_{n2}r^{2+n}+a_{n3}r^{-n}+b_{n4}r^{2-n})\sin n\theta\\
\end{aligned}\]`

----
## polar coordinates

- For axisymmetric problems, all field quantities are independent of `\(\theta\)`
- This reduces the general solution to
`\[\phi = a_0 + a_1 \log r + a_2 r^2 + a_3 r^2 \log r\]`

----
## polar coordinates

![image](../images/polar_table.PNG) <!-- .element width="70%" -->

---
# examples

----
## pinned beam

![pinned beam for example](../images/pinnedbeam.svg) <!-- .element width="70%" -->

----
## example

![image](../images/bending.PNG)

----
## example

- Locally along the ends, there will be some tractions in order to apply the bending moment
- These tractions will cancel out, however, so we can use Saint Venant's principle to avoid modeling them explicitly

----
## example

`\[\begin{aligned}
	\sigma_y (x, \pm c) &= 0\\
	\tau_{xy} (x, \pm c) &= \tau_{xy} (\pm L, y) = 0\\
	\int_{-c}^{c}\sigma_x (\pm l,y)dy &= 0\\
	\int_{-c}^{c}\sigma_x (\pm l,y)ydy &= -M
\end{aligned}\]`

----
## example

- What is the simplest form of polynomial stress function that would satisfy these boundary conditions? 
`\[\begin{aligned}
	\sigma_{xx} &= \frac{\partial^2 \phi}{\partial y^2} + V\\
	\sigma_{yy} &= \frac{\partial^2 \phi}{\partial x^2} + V\\
	\tau_{xy} &= -\frac{\partial^2 \phi}{\partial x \partial y}
\end{aligned}\]`

----
## example

![image](../images/distributed.PNG)

----
## example

- In this case we can write the boundary conditions as
`\[\begin{aligned}
	\tau_{xy}(x, \pm c) &= 0\\
	\sigma_y (x,c) &= 0\\
	\sigma_y (x,-c) &= -w\\
	\int_{-c}^{c} \sigma_x (\pm l, y) dy &= 0\\
	\int_{-c}^{c} \sigma_x (\pm l, y) ydy &= 0\\
	\int_{-c}^{c} \tau_{xy} (\pm l, y) dy &= \mp wl\\
\end{aligned}\]`

----
## example

- And find that the stress function
`\[\phi = Ax^2 + Bx^2 y + Cx^2 y^3 + Dy^3 - \frac{1}{5}C y^5\]`

- Can satisfy the boundary conditions as well as compatibility

----
## example

![image](../images/rotating_disk.PNG)

----
## reading for next class

- Anisotropic elasticity - pp. 319 - 333
