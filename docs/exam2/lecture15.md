# AE831
## Continuum Mechanics
Lecture 12 - Large Deformation<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

13 October, 2020

----
## schedule

- 13 Oct - Large Deformation, HW 6 Due
- 15 Oct - Anisotropy and Large Deformation
- 20 Oct - Exam Review, HW 7 Due, HW 6 Self-Grade Due
- 22 Oct - Exam 2

----
## outline

<!-- vim-markdown-toc GFM -->

* anisotropic solution techniques
* large deformation
* simple deformation modes

<!-- vim-markdown-toc -->

---
# anisotropic solution techniques

----
## planar problems

- Many of our usual solution techniques are more difficult to apply to anisotropic materials
- For a general anisotropic material under the assumption of plane strain (`\(u_i = \langle u_1(x_1,x_2), u_2(x_1,x_2)\rangle\)`) the equilibrium equations (in terms of displacement) are
`\[\begin{aligned}
	C_{11} u_{1,11} + C_{66} u_{1,22} + C_{16} (2u_{1,12} + u_{2,11}) + C_{26} u_{2,22} + (C_{12}+C_{66})u_{2,12} &=0\\
	C_{16} u_{1,11} + C_{26} u_{1,22} + (C_{66} + C_{12}) u_{1,12} + C_{66} u_{2,11} + C_{22}u_{2,22} + 2C_{26}u_{2,12} &=0\\
	C_{15} u_{1,11} + C_{46} u_{1,22} + (C_{56} + C_{14})u_{1,12} + C_{56}u_{2,11} + C_{24} u_{2,22} + (C_{25}+C_{46})u_{2,12} &=0
\end{aligned}\]` <!-- .element position: relative, left: "-30%" -->

----
## planar problems

- Only two of these three equations can be solved with a plane strain displacement assumption
- This means that a general anisotropic body cannot be solved in plane strain
- However if a material possesses at least monoclinic symmetry, enough terms vanish that plane strain is an acceptable solution
- Alternatively, a generalized plane strain solution can be used for any anisotropic body
`\[u = \langle u_1(x_1,x_2), u_2(x_1,x_2), u_3(x_1,x_2) \rangle\]`

----
## stroh representation

- Stroh developed a complex variable representation for generalized plane strain solutions in anisotropic materials
- If we assume a displacement field in the form `\(u_i = a_i f(z)\)` where `\(z = x_1 + px_2\)` the equilibrium equations in terms of displacement then become `\[C_{ijkl} u_{k,il} = 0\]`

----
## stroh representation

- Since `\(\partial z/ \partial x_i = \delta_{i1} + p \delta_{i2}\)`, we find that
`\[u_{k,l} = a_k (\delta_{l1} + p \delta_{l2})f^\prime(z) \qquad u_{k,il} = a_k(\delta_{l1 + p\delta_{l2}})(\delta_{j1} + p\delta_{j2})f^{\prime\prime}(z)\]`

----
## stroh representation

- The equilibrium equations with a generalized plane strain displacement function now become
`\[C_{ijkl}(\delta_{l1} + p\delta_{l2})(\delta_{j1} + p\delta_{j2})a_kf^{\prime \prime}(z) = 0\]`

- For non-trivial solutions (when `\(f^{\prime \prime}(z) \ne 0\)`), we can re-write the equations as 
`\[a_k = 0\]`

----
## stroh representation

- If we define the following quantities in terms of the stiffness tensor 
`\[Q = \begin{bmatrix}
	C_{11} & C_{16} & C_{15}\\
	C_{16} & C_{66} & C_{56}\\
	C_{15} & C_{56} & C_{55}
\end{bmatrix} \qquad R = \begin{bmatrix}
	C_{16} & C_{12} & C_{14}\\
	C_{66} & C_{26} & C_{46}\\
	C_{56} & C_{25} & C_{45}
\end{bmatrix} \\
T = \begin{bmatrix}
	C_{66} & C_{26} & C_{46}\\
	C_{26} & C_{22} & C_{24}\\
	C_{46} & C_{24} & C_{44}
\end{bmatrix}\]`

----
## stroh representation

- we can now re-write the equilibrium equations in matrix form as
`\[a=0\]`

- This is a type of eigenvalue problem

----
## stroh representation

- Mathematically, it can be shown that for a material with physically admissible elastic constants, `\(p\)` will always be complex
- There will be three pairs of solutions `\((p,\bar{p})\)`, and three pairs of complex-valued eigenvectors, `\((a_i,\bar{a_i})\)`

----
## stroh representation

- Stress solutions can be calculated by defining `\(b_i\)` vectors
`\[a^{(i)} = b^{(i)}\]`

- Which gives stress solutions as
`\[\sigma_{i1} = -pb_if^\prime(z) \qquad \sigma_{i2} = b_i f^\prime(z)\]`

---
# large deformation

----
## change of frame

- For small deformations, the current and deformed frame have negligible differences
- For large deformations, we need to ensure that our constitutive law is objective, or frame-indifferent

----
## change of frame

- Examples:
	- distance between two material points is a frame-indifferent scalar
	- speed of a material point is not frame-independent (non-objective)
	- position vector and velocity vector of a material point are non-objective
	- relative velocity between two material points is objective

----
## change of frame

- In general, a "frame" can have its own time scale, origin, and directionality
- a change of frame would then be given by
`\[x_i^* = c_i(t) + Q_{ij}(t)(x_j-x^{0}_j)\]`

----
## change of frame

- If we consider the position vector of two material points, in the starred frame we have
`\[x_1^* = c(t) + Q(t)(x_1-x_0) \qquad x_2^* = c(t) + Q(t)(x_2-x_0)\]`

- The relative position vector, `\(b=x_1-x_2\)` can also be found in the starred frame as 
`\[b^* = x_1^*-x_2^* = Q(t)(x_1-x_2)\]`

- Any vector which obeys this law is known as an objective vector

----
## change of frame

- If we consider some tensor, `\(T_{ij}\)` which transforms an objective vector `\(b_j\)` into another objective vector, `\(c_i\)`
`\[c_i = T_{ij}b_j\]`

- Since both `\(b\)` and `\(c\)` are objective vectors, we can write
`\[c_i^* = Q_{ik} c_k = Q_{ik} T_{kj} b_j = Q_{ik} T_{kj} Q_{lj} b_l\]`

----
## change of frame

- This means that for `\(T_{ij}\)` to be objective it must satisfy
`\[T_{ij}^* = Q_{ik} T_{kl} Q_{jl}\]`

----
## examples

- `\(dx_i\)`
- `\(ds\)`
- `\(v_i\)`
- `\(F_{ij}\)`
- `\(C_{ij}\)`
- `\(B_{ij}\)`

----
## group problems

- Group 1: Is the first Piola-Kirchhoff stress tensor objective? How does it transform? Recall: 
`\[T_{ij}^0 = J T_{ik} F_{jk}^{-1}\]`
- Group 2: Is the second Piola-Kirchhoff stress tensor objective? How does it transform? Recall:
`\[\tilde{T_{ij}} = J F_{ik}^{-1} T_{kl} F_{jl}^{-1}\]`

----
## constitutive equations

- For large deformation, a constitutive law must be objective
- `\(T_{ij} = f(C_{ij})\)` is not an acceptable form, but `\(T_{ij} = f(B_{ij})\)` is
- `\(\tilde{T}_{ij} = f(C_{ij})\)` is also an acceptable form of the constitutive equation
- If we assume our material to be isotropic, it can be shown that, with no loss of generality
`\[f(B_{ij}) = a_0 \delta_{ij} + a_1 B_{ij} + a_2 B_{ij}^2\]`

----
## constitutive equations

- A commonly used alternate form of the constitutive equation is
`\[T_{ij} = \varphi_0 \delta_{ij} + \varphi_1 B_{ij} + \varphi_2 B_{ij}^{-1}\]`

- If the material is incompressible, the stress is indeterminate to some arbitrary hydrostatic pressure
`\[T_{ij} = -p \delta_{ij} + \varphi_1 B_{ij} + \varphi_2 B_{ij}^{-1}\]`

----
## money rivlin

- This is known as the Mooney-Rivlin model, which can be written in different ways
`\[T_{ij} = -p \delta_{ij} + \mu \left(\frac{1}{2} + \beta\right) B_{ij} - \mu \left(\frac{1}{2} - \beta\right) B_{ij}^{-1}\]`

----
## neo-hookean solid

- A simpler model, which is only accurate for strains less than 20%, is the neo-Hookean solid
- For incompressible materials, the neo-Hookean equation is
`\[T_{ij} = -p \delta_{ij} + 2C_1 B_{ij}\]`

----
## neo-hookean solid

- Where, for consistency with Hooke's Law, `\(2 C_1 = \mu\)`
- When large tensile strains are not important, the neo-Hookean model is popular because it only needs one material constant, which has more physical meaning than Mooney-Rivlin constants.

---
# simple deformation modes

----
## incompressible stretch

- In large deformation problems, the stretch ratio, `\(\lambda\)` is often used (instead of strain)
- `\(\lambda_1\)` represents the ratio of deformed length in `\(x_1\)` to undeformed length in `\(x_1\)`
- For uniaxial extension we have 
`\[\begin{aligned}
	x_1 &= \lambda_1 X_1\\
	x_2 &= \lambda_2 X_2\\
	x_3 &= \lambda_2 X_3
\end{aligned}\]`

- Also if the material is incompressible we know
`\[\lambda_1 \lambda_2^2 = 1\]`

----
## simple shear

- For large shear deformation, we have 
`\[\begin{aligned}
	x_1 &= X_1 + KX_2\\
	x_2 &= X_2\\
	x_3 &= X_3\\
\end{aligned}\]`

- And we find `\(B\)` and `\(B^{-1}\)` as
`\[B_{ij} = \begin{bmatrix}
	1+K^2 & K & 0\\
	K & 1 & 0\\
	0 & 0 & 1
\end{bmatrix} \qquad B_{ij}^{-1} = \begin{bmatrix}
	1 & -K & 0\\
	-K & 1+ K^2 & 0\\
	0 & 0 & 1
\end{bmatrix}\]`

----
## reading material

- Thermodynamics formulation of Mooney-Rivlin models - [link](http://continuummechanics.org/mooneyrivlin.html)
- Anisotropy in large deformation - "A New Constitutive Framework for Arterial Wall Mechanics and a Comparative Study of Material Models"
- Paper is interesting, but long, pp 10-21 are the most relevant.
