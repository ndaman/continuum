# AE831
## Continuum Mechanics
Lecture 13 - Anisotropic Hyperelasticity<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

15 October, 2020

----
## schedule

- 15 Oct - Anisotropy and Large Deformation
- 20 Oct - Exam Review, HW7 Due, HW6 Self-Grade Due
- 22 Oct - Exam 2
- 27 Oct - Newtonian Fluids

----
## outline

<!-- vim-markdown-toc GFM -->

* large deformation
* simple deformation modes
* thermodynamics formulation
* anisotropic hyperelasticity

<!-- vim-markdown-toc -->

---
# large deformation

----
## change of frame

- For small deformations, the current and deformed frame have negligible differences
- For large deformations, we need to ensure that our constitutive law is objective, or frame-indifferent
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

- If we consider the position vector of two material points, in the starred frame we have
`\[x_1^* = c(t) + Q(t)(x_1-x_0) \qquad x_2^* = c(t) + Q(t)(x_2-x_0)\]`

----
## change of frame

- The relative position vector, `\(b=x_1-x_2\)` can also be found in the starred frame as 
`\[b^* = x_1^*-x_2^* = Q(t)(x_1-x_2)\]`

- Any vector which obeys this law is known as an objective vector

----
## change of frame

- If we consider some tensor, `\(T_{ij}\)` which transforms an objective vector `\(b_j\)` into another objective vector, `\(c_i\)`
`\[c_i = T_{ij}b_j\]`

- Since both `\(b\)` and `\(c\)` are objective vectors, we can write
`\[c_i^* = Q_{ik} c_k = Q_{ik} T_{kj} b_j = Q_{ik} T_{kj} Q_{lj} b_l\]`

- This means that for `\(T_{ij}\)` to be objective it must satisfy
`\[T_{ij}^* = Q_{ik} T_{kl} Q_{jl}\]`

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

- This is known as the Mooney-Rivlin model, which can be written in different ways
`\[T_{ij} = -p \delta_{ij} + \mu \left(\frac{1}{2} + \beta\right) B_{ij} - \mu \left(\frac{1}{2} - \beta\right) B_{ij}^{-1}\]`

----
## neo-hookean solid

- A simpler model, which is only accurate for strains less than 20%, is the neo-Hookean solid
- For incompressible materials, the neo-Hookean equation is
`\[T_{ij} = -p \delta_{ij} + 2C_1 B_{ij}\]`

- Where, for consistency with Hooke's Law, `\(2 C_1 = \mu\)`
- When large tensile strains are not important, the neo-Hookean model is popular because it only needs one material constant, which has more physical meaning than Mooney-Rivlin constants.

---
# simple deformation modes

----
## incompressible uniaxial stretch

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

---
# thermodynamics formulation

----
## helmholtz free energy

- Large deformation constitutive laws are generally formulated from an energy framework
- From thermodynamics, it can be shown that the second Piola-Kirchhoff stress is the partial derivative of the Helmholtz free energy with respect to the Green strain
`\[\tilde{T}_{ij} = \rho_0 \frac{\partial \Psi}{\partial E_{ij}}\]`

----
## helmholtz free energy

- The Helmholtz free energy has both thermal and mechanical strain energy components, but in general we neglect the thermal portion, and use `\(W\)` to represent the mechanical work done (with density included) 
`\[\tilde{T}_{ij} = \frac{\partial W}{\partial E_{ij}}\]`

----
## hyperelastic materials

- Most commonly, the strain energy density, `\(W\)` is formulated as a function of the invariants of `\(B_{ij}\)` 
`\[\begin{aligned}
	I_B &= B_{kk}\\
	II_B &= \frac{1}{2}(I_B^2 - B_{ik}B_{ki})\\
	III_B &= J^2
\end{aligned}\]`

----
## hyperelastic materials

- For nearly incompressible materials, it is often more convenient to write an alternate form of the invariants 
`\[\begin{aligned}
	\bar{I}_B &= \frac{B_{kk}}{J^{2/3}}\\
	\bar{II}_B &= \frac{1}{2}(\bar{I}_B^2 -\frac{ B_{ik}B_{ki}}{J^{4/3}})\\
	\bar{III}_B &= J = \sqrt{\text{det}(B_{ij})}
\end{aligned}\]`

----
## hyperelastic models

- The algebra involved in taking the partial derivative to calculate stress can get tedious
- Cauchy stress for compressible materials (in terms of the invariants of `\(B_{ij}\)`) can be expressed as
`\[\sigma_{ij} = \frac{2}{\sqrt{I_3}} \left[ \left(\frac{\partial W}{\partial I_B} + I_B \frac{\partial W}{\partial II_B}\right)B_{ij} - \frac{\partial U}{\partial II_B}B_{ik}B_{kj}\right] + 2\sqrt{III_B} \frac{\partial U}{\partial III_B} \delta_{ij}\]`

----
## hyperelastic models

- For nearly incompressible materials (in terms of `\(\bar{I}\)`), we have
`\[\sigma_{ij} = \frac{2}{J} \left[ \frac{1}{J^{2/3}} \left(\frac{\partial W}{\partial \bar{I}_B} + \bar{I}_B \frac{\partial W}{\partial \bar{II}_B}\right)B_{ij} - \left(\bar{I}_B \frac{\partial W}{\partial \bar{I}_B} + 2 \bar{II}_B \frac{\partial W}{\partial \bar{II}_B}\right)\frac{\delta_{ij}}{3} - \frac{1}{J^{4/3}} \frac{\partial W}{\partial \bar{II}_B} B_{ik} B_{kj}\right] + \frac{\partial W}{\partial J}\delta_{ij}\]`

- Sometimes `\(W\)` is expressed in terms of `\(F_{ij}\)`, which gives
`\[\sigma_{ij} = \frac{1}{J} F_{ik} \frac{W}{\partial F_{kj}}\]`

----
## hyperelastic materials

- `\(W\)` can also be expressed in terms of the stretch ratios, `\(\lambda_1\)`, `\(\lambda_2\)` and `\(\lambda_3\)` and the unit eigenvectors of `\(B_{ij}\)` `(\(b_i^{(j)}\))` 
`\[\sigma_{ij} = \frac{\lambda_1}{\lambda_1 \lambda_2 \lambda_3} \frac{\partial W}{\partial \lambda_1} b_i^{(1)} b_j^{(1)} + \frac{\lambda_2}{\lambda_1 \lambda_2 \lambda_3} \frac{\partial W}{\partial \lambda_2} b_i^{(2)} b_j^{(2)} + \frac{\lambda_3}{\lambda_1 \lambda_2 \lambda_3} \frac{\partial W}{\partial \lambda_3} b_i^{(3)} b_j^{(3)}\]`

----
## neo-hookean solid

- The neo-hookean solid we discussed earlier can be expressed in this form 
`\[W = \frac{\mu_1}{2} (\bar{I}_B-3) + \frac{K_1}{2}(J-1)^2\]`
- Where `\(\mu_1\)` and `\(K_1\)` correspond to the shear modulus and bulk modulus, respectively, at small deformations
- Should be used for rubbers with very limited compressiblity (`\(K_1 >> \mu_1\)`)

----
## mooney-rivlin

- The Mooney-Rivlin Model can also be expressed in this form
`\[W = \frac{\mu_1}{2} (\bar{I}_B-3) + \frac{\mu_2}{2} (\bar{II}_B-3) + \frac{K_1}{2}(J-1)^2\]`

- Once again, this applies best with limited compressibility
- `\(\mu = \mu_1 + \mu_2\)`

----
## rivlin models

- While the text shows one simplified version of the Mooney-Rivlin material model the generalized Rivlin model has the form
`\[W = \sum_{p,q=0}^{N} C_{pq} (\bar{I}_B-3)^p(\bar{II}_B-3)^q + \sum_{m=1}^M D_m(J-1)^{2m}\]`

with `\(C_{00} = 0\)`

- For consistency with linear elasticity, we know that
`\[K = 2 D_1 \qquad \mu = 2(C_{01} + C_{10})\]`

- This is also known as the generalized polynomial rubber elasticity potential

----
## other models

- Many micro-features can effect the large deformation behavior of a material
- Several families of large-deformation materials
  - Foams
  - Rubbery foams
  - Thermoplastic polymers
  - Elastomers
  - Bio-tissue
  - There are many families of strain energy functions tailored to specific material responses

----
## material constants

- For simple models, elastic constants can be found easily from uniaxial tension
- If you are working with a rubbery material, you can generally assume it is incompressible
- Least-squares fit of uniaxial test is often used, but can lead to error
- If multi-axial performance is desired, it is more accurate to fit the constants to a multi-axial test
- Most rubbers have coupled volumetric and shear responses under large hydrostatic stress, Rivlin-derived models do not account for this coupling

---
# anisotropic hyperelasticity

----
## anisotropic hyperelasticity

- Most engineering materials are mostly isotropic under large deformation
- Hyperelasticity has other use cases
  - Biomechanics
  - Geophysics (soil compaction)
  - Foams, heterogeneous materials
  - Paper

----
## decomposition

- Although the paper by Hozapfel, Gasser and Ogden was developed specifically for arterial walls, it can be applied elsewhere and uses common techniques in the development
- `\(F_{ij}\)` (and by extension, `\(C_{ij}\)` and `\(B_{ij}\))` are decomposed into dilatational and distortional parts
`\[\begin{aligned}
	F &= (J^{1/3} I) \bar{F}\\
	C &= F^T F = J^{2/3} \bar{C}\\
	\bar{C} &= \bar{F}^T\bar{F}\\
	B &= F F^T = J^{2/3} \bar{B}\\
	\bar{B} &= \bar{F} \bar{F}^T
\end{aligned}\]`

----
## decomposition

- And the Green strain tensor 
`\[\begin{aligned}
	E &= \frac{1}{2}(C-I) = J^{2/3}\bar{E} + \frac{1}{2}(J^{2/3}-1)I\\
	\bar{E} &= \frac{1}{2}(\bar{C}-I)
\end{aligned}\]`

----
## helmholtz free energy

- The Helmholtz free energy is normally formulated in terms of one tensor, `\(A\)`
- Here, the authors assume a set of `\(n\)` second-order tensors to characterize the anisotropic effects on energy
- They further assume that the energy effects of dilatational and distortional contributions are completely decoupled, giving
`\[\Psi(E,A_1,...,A_n) = U(J) + \bar{\Psi}(\bar{E},A_1,...,A_n)\]`

----
## anisotropic contributions

- The authors propose further separating the helmholtz free energy into isotropic and anisotropic parts, they proceed to use `\(\bar{C}\)` instead of `\(\bar{E}\)`
`\[\bar{\Psi} (\bar{C},a_{01},a_{02}) = \bar{\Psi}_{iso} (\bar{C}) + \bar{\Psi}_{aniso}(\bar{C},a_{01},a_{02})\]`

- They proceed to define further invariants in terms of `\(\bar{C}\)`, `\(a_{01}\)` and `\(a_{02}\) `
`\[\begin{aligned}
	\bar{I}_4 &= \bar{C} \ddots A_1\\
	\bar{I}_6 &= \bar{C} \ddots A_2
\end{aligned}\]`

----
## stiffness model

- Now they choose a form which will give the anisotropic stiffness, since they observed a strong stiffening effect, they choose an exponential function
`\[\bar{\Psi}_{aniso} = \frac{k_1}{2k_2} \sum_{i=4,6} \exp[k_2(\bar{I}_i-1)^2]-1\]`

- Note that `\(k_1\)` and `\(k_2\)` are the only parameters to be found as a function of the material, as `\(\bar{I}_4\)` and `\(\bar{I}_6\)` are functions of the material orientation

----
## reading material

- Thermodynamics formulation of Mooney-Rivlin models [link](http://continuummechanics.org/mooneyrivlin.html)
- Anisotropy in large deformation - "A New Constitutive Framework for Arterial Wall Mechanics and a Comparative Study of Material Models"
- Paper is interesting, but long, pp 10-21 are the most relevant.
