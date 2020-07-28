<span>upcoming schedule</span>

  - 12 Sep - HW 3 Due, Exam Review

  - 17 Sep - Exam 1

  - 19 Sep - Exam Return, Stress Lecture

  - 21 Sep - Stress Lecture

### outline

\[sections numbered\]

# exam format

<span>exam format</span>

  - 4 questions

  - Graphing calculator?

  - Equation sheet is on blackboard

  - I use a linear curve on exam scores

# topics

<span>index notation</span>

  - Dummy and free indexes

  - Substitution, multiplication and factoring

  - Kronecker delta, permutation symbol

<span>tensor algebra</span>

  - Transformation law

  - Symmetry and antisymmetry

  - Eigenvalues and eigenvectors

<span>tensor calculus</span>

  - Partial derivatives

  - Gradient

  - Directional derivative

  - Other coordinate systems (polar, cylindrical, spherical)

<span>kinematics</span>

  - Material and spatial coordinates

  - Motion

  - Material derivative

  - Displacement

<span>kinematics</span>

  - Infinitesimal deformation

  - Rigid body motion

  - Physical interpretation of strain tensor

  - Principal strain and dilatation

<span>kinematics</span>

  - Conservation of mass

  - Compatibility

  - Deformation gradient

  - Finite deformation

  - Polar decomposition

# tensors

<span>index notation</span>

Free index vs. dummy index

Free index is not repeated (on any term)

Free index takes all values (1,2,3)

e.g. \(u_i = \langle u_1, u_2, u_3 \rangle\)

Free indexes must match across terms in an expression or equation

Dummy index is repeated on at least one term

Dummy index indicates summation over all values

e.g. \(\sigma_{ii} = \sigma_{11} + \sigma_{22} + \sigma_{33}\)

Index can not be used more than twice in the same term
(\(A_{ij}B_{jk}C_{kl}\) is good, \(A_{ij}B_{ij}C_{ij}\) is not)

<span>special symbols</span>

  - For convenience we define two symbols in index notation

  - *Kronecker delta* is a general tensor form of the Identity Matrix
    \[\delta_{ij} = \left\{
            \begin{array}{ll}
            1& \text{if $i=j$}\\
            0& \text{otherwise}
            \end{array}
            \right. = \begin{bmatrix}
            1 & 0 & 0\\
            0 & 1 & 0 \\
            0 & 0 & 1
            \end{bmatrix}\]

  - Is also used for higher order tensors

  - \(\delta_{ij} = \delta_{ji}\)

  - \(\delta_{ii} =\) \(3\)

  - \(\delta_{ij}a_j =\) \(a_i\)

  - \(\delta_{ij}a_{ij} =\) \(a_{ii}\)

<span>special symbols</span>

  - *alternating symbol* or *permutation symbol*
    \[\epsilon_{ijk} = \left\{
            \begin{array}{rl}
            1 & \text{if $ijk$ is an even permutation of 1,2,3}\\
            -1 & \text{if $ijk$ is an odd permutation of 1,2,3}\\
            0 & \text{otherwise}
            \end{array}
            \right.\]

  - This symbol is not used as frequently as the *Kronecker delta*

  - For our uses in this course, it is enough to know that 123, 231, and
    312 are even permutations

  - 321, 132, 213 are odd permutations

  - all other indexes are zero

  - \(\epsilon_{ijk} \epsilon_{imn} = \delta_{jm} \delta_{kn} - \delta_{jn} \delta_{mk}\)

<span>substitution</span>

  - We need to change the free index, \(i\), to \(m\) in
    ([\[eq:second\]](#eq:second))

  - Since \(m\) is already used as the dummy index, we need to change
    that too

  - \[\label{eq:seconda}
            b_m = V_{mj} c_j\]

  - We can now make the substitution

  - \[\label{eq:subbed}
            a_i = U_{im} V_{mj} c_j\]

<span>multiplication</span>

  - We need to be careful with indexes when multiplying expressions

  - \[p = a_m b_m \qquad \text{and} \qquad q = c_m d_m\]

  - We can express, \(pq\), but remember the dummy index cannot be
    repeated more than once

  - \[pq \ne a_m b_m c_m d_m\]

  - Instead we must change the dummy index in one of the expressions
    first

  - \[pq = a_m b_m c_n d_n\]

<span>factoring</span>

  - In the following expression, we would like to factor out \(n\), but
    it has different indexes

  - \[T_{ij}n_j - \lambda n_i =0\]

  - Recall \(\delta_{ij}a_j = a_i\), we can rewrite
    \(n_i = \delta_{ij} n_j\)

  - \[T_{ij}n_j - \lambda \delta_{ij} n_j =0\]

  - \[(T_{ij} - \lambda \delta_{ij}) n_j =0\]

<span>contraction</span>

  - \(T_{ii}\) is the contraction of \(T_{ij}\)

  - This can often be a useful tool in solving tensor equations

  - \[T_{ij} = \lambda \Delta \delta_{ij} + 2\mu E_{ij}\]

  - \[T_{ii} = \lambda \Delta \delta_{ii} + 2\mu E_{ii}\]

<span>general coordinate transformation</span>

  - Coordinate transformation can become much more complicated in three
    dimensions, and with higher-order tensors

  - It is convenient to define a general form of the coordinate
    transformation in index notation

  - We define \(Q_{ij}\) as the cosine of the angle between the
    \(x_i^\prime\) axis and the \(x_j\) axis.

  - This is also referred to as the "direction cosine"
    \[Q_{ij} = \cos (x_i^\prime, x_j)\]

<span>general coordinate transformation</span>

  - We can transform any-order tensor using \(Q_{ij}\)

  - Vectors (first-order tensors): \(v^\prime_i = Q_{ij}v_j\)

  - Matrices (second-order tensors):
    \(\sigma_{mn}^\prime =Q_{mi}Q_{nj}\sigma_{ij}\)

  - Fourth-order tensors:
    \(C_{ijkl}^\prime = Q_{im}Q_{jn}Q_{ko}Q_{lp}C_{mnop}\)

<span>principal values</span>

  - We can re-write the equation
    \[(a_{ij} - \lambda \delta_{ij})n_j = 0\]

  - This system of equations has a non-trivial solution if and only if
    \(\det [a_{ij} - \lambda \delta_{ij}] = 0\)

  - This equation is known as the characteristic equation, and we solve
    it to find the principal values of a tensor

<span>principal directions</span>

  - We defined principal directions earlier
    \[(a_{ij} - \lambda \delta_{ij})n_j = 0\]

  - \(\lambda\) are the principal values and \(n_j\) are the principal
    directions

  - For each eigenvalue there will be a principal direction

  - We find the principal direction by substituting the solution for
    \(\lambda\) back into this equation

<span>scalar fields</span>

  - A scalar-valued function of a position vector is known as a scalar
    field

  - Density, temperature, electric potential are all examples of scalar
    fields

  - The gradient, \(\nabla\), of a scalar field, \(\phi\) is defined as
    \[\nabla \phi = \frac{\partial \phi}{\partial x_i} = \langle \frac{\partial \phi}{\partial x_1}, \frac{\partial \phi}{\partial x_2}, \frac{\partial \phi}{\partial x_3} \rangle\]

<span>directional derivative</span>

  - The gradient can be used to find the directional derivative, or the
    rate of change of \(\phi\) in a certain direction

  - If \(r_i\) is a vector in a direction, then the directional
    derivative of the scalar field \(\phi\) in the \(r_i\) direction is
    \[\nabla \phi \cdot r = \phi_{,i} r_i\]

  - The vector produced by the gradient will be perpendicular to a
    surface of constant \(\phi\)

# kinematics

<span>motion of a continuum</span>

  - For a particle we define the path as a function of time
    \[r_i = r_i(t) = \langle x_1(t), x_2(t), x_3(t) \rangle\]

  - For N particles there will be N path lines

  - In a continuum, there are infinitely many particles

  - Instead of identifying particles by some identifying number, we
    identify them by their position
    \[x_i = x_i (X_1, X_2, X_3,t) \qquad \text{with} \qquad X_i = x_i (X_1, X_2, X_3, t_0)\]

  - \((X_1,X_2,X_3)\) are known as the material coordinates and are used
    to identify the different particles of a body, while equation 4.2
    describes a motion

<span>motion</span>

  - Group 1 - write equations and sketch motion for simple shear

  - Group 2 - write equations and sketch motion for biaxial tension
    (double stretch in x-direction with respect to y-direction)

  - Group 3 - write equations and sketch motion for rigid body rotation
    of some arbitrary angle, \(\theta\)

<span>material derivative</span>

  - The time rate of change of some quantity of a material particle is
    known as the material derivative

  - The material derivative is generally denoted as \(D/Dt\)

  - When using the material (Lagrangian) description, the material
    derivative is simply
    \[\frac{D \Theta}{Dt} = \left(\frac{\partial \hat{\Theta}}{\partial t}\right)_{X_i-fixed}\]

<span>material derivative</span>

  - For the spatial description, however, \(x_i\) are not constant for a
    given material with fixed \(X_i\), hence
    \[\frac{D \Theta}{Dt} = \left(\frac{D \tilde{\Theta}}{Dt}\right)_{X_i-fixed} = \left(\frac{\partial \tilde{\Theta}}{\partial x_i}\right)\frac{\partial x_i}{\partial t} + \left(\frac{\partial \tilde{\Theta}}{\partial t}\right)_{x_i-fixed}\]

  - Since \(\frac{\partial x_i}{\partial t}\) for fixed \(X_i\) are the
    velocity components of a given particle, we can also write
    \[\frac{D \Theta}{Dt} = \left(\frac{D \tilde{\Theta}}{Dt}\right)_{X_i-fixed} = \frac{\partial \tilde{\Theta}}{\partial t} + v_i \tilde{\Theta}_{,i}\]

<span>physical meaning</span>

  - If we consider two elements, \(dX_i^{(1)}\) and \(dX_i^{(2)}\)

  - Due to motion they become \(dx_i^{(1)}\) and \(dx_i^{(2)}\)

  - For small deformations, we know that
    \[dx_i^{(1)} dx_i^{(2)} = F_{ij} dX_j^{(1)} F_{ik} dX_k^{(2)} = dX_j^{(1)} C_{jk} dX_k^{(2)} = dX_j^{(1)} (\delta_{jk} + 2E_{jk}) dX_k^{(2)}\]

  - Which we can expand to
    \[dx_i^{(1)} dx_i^{(2)} = dX_i^{(1)}dX_i^{(2)} + 2E_{jk}dX_j^{(1)}dX_k^{(2)}\]

<span>physical meaning</span>

  - If we look at the length of a single material element,
    \(dX_i = dS dn_i\) we find the deformed length, \(ds\) to be
    \[ds^2 = dS^2 + 2dS^2 (n_i E_{ij} n_j)\]

  - For small deformations, we make the assumption that
    \[ds^2 - dS^2 = (ds + dS)(ds - dS) \approx 2dS(ds-dS)\]

  - Which leads to \[\frac{ds - dS}{dS} = n_i E_{ij} n_j\]

  - This means that the diagonal terms of \(E_{ij}\) give the unit
    elongation for an element originally in the \(1\), \(2\) or \(3\)
    directions

<span>conservation of mass</span>

  - While an element&rsquo;s volume and density may change, its mass
    must remain constant

  - Thus the material derivative of \(\rho dV\) will be zero
    \[\begin{aligned}
            \frac{D}{Dt}(\rho dV) &= 0\\
            \rho \frac{D}{Dt} dV +  dV \frac{D}{Dt} \rho &= 0\\
            \rho v_{i,i} + \frac{D}{Dt} \rho &= 0
            \end{aligned}\]

  - In the spatial description
    \[\frac{D}{Dt} \rho = \frac{\partial \rho}{\partial t} + v_i \rho_{,i}\]

  - In continuum mechanics, this is also referred to as the equation of
    continuity

<span>compatibility</span>

  - To satisfy compatibility a strain field must satisfy the following
    equations \[\begin{aligned}
            \frac{\partial^2 E_{11}}{\partial X_2^2} + \frac{\partial^2 E_{22}}{\partial X_1^2} &= 2 \frac{\partial^2 E_{12}}{\partial X_1 \partial X_2}\\
            \frac{\partial^2 E_{22}}{\partial X_3^2} + \frac{\partial^2 E_{33}}{\partial X_2^2} &= 2 \frac{\partial^2 E_{23}}{\partial X_2 \partial X_3}\\
            \frac{\partial^2 E_{33}}{\partial X_1^2} + \frac{\partial^2 E_{33}}{\partial X_2^2} &= 2 \frac{\partial^2 E_{31}}{\partial X_3 \partial X_1}\\
            \frac{\partial^2 E_{11}}{\partial X_2 \partial X_3} &= \frac{\partial}{\partial X_1} \left(-\frac{\partial E_{23}}{\partial X_1} + \frac{\partial E_{31}}{\partial X_2} + \frac{\partial E_{12}}{\partial X_3}\right)\\
            \frac{\partial^2 E_{22}}{\partial X_3 \partial X_1} &= \frac{\partial}{\partial X_2} \left(-\frac{\partial E_{31}}{\partial X_2} + \frac{\partial E_{12}}{\partial X_3} + \frac{\partial E_{23}}{\partial X_1}\right)\\
            \frac{\partial^2 E_{33}}{\partial X_1 \partial X_2} &= \frac{\partial}{\partial X_3} \left(-\frac{\partial E_{12}}{\partial X_3} + \frac{\partial E_{23}}{\partial X_1} + \frac{\partial E_{31}}{\partial X_2}\right)
            \end{aligned}\]

<span>polar decomposition</span>

  - It can be shown that for any real tensor \(F_{ij}\) with a nonzero
    determinant \[F_{ij} = R_{ik} U_{kj}\]

  - And \[F_{ij} = V_{ik} R_{kj}\]

  - Where \(U_{ij}\) is known as the right stretch tensor and \(V_{ij}\)
    is known as the left stretch tensor

  - (5.35) and (5.36) are known as the Polar Decomposition Theorem

<span>polar decomposition</span>

  - If we recall that the product of any matrix with its transpose gives
    a symmetric matrix, and apply it to the deformation gradient, we see
    \[F^T \cdot F = (R\cdot U)^T \cdot (R\cdot U) = U^T \cdot R^T \cdot R \cdot U\]

  - But, since \(R^T \cdot R = I\), we find that
    \[F^T \cdot F = (R\cdot U)^T \cdot (R\cdot U) = U^T \cdot R^T \cdot R \cdot U = U^T \cdot U\]

  - This is also equal to \(C\), the Right Cauchy-Green Deformation
    Tensor

  - We could use the same development using \(F \cdot F^T\) and
    substituting \(F= V \cdot R\) to find \[F \cdot F^T = V \cdot V^T\]

  - \(V \cdot V^T\) is often called \(B\), the Left Cauchy-Green
    Deformation Tensor

<span>polar decomposition</span>

  - The challenge now is to take the square root of \(F \cdot F^T\)

  - To calculate the square root of a matrix, we must first diagonalize
    it
    
    1.  Rotate matrix into principal direction
    
    2.  Calculate square root
    
    3.  Rotate back to original direction

  - We can use this method to calculate \(U\) or \(V\), and then we use
    the inverse to find \(R\)
