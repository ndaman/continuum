<span>upcoming schedule</span>

  - 10 Sep - Polar Decomposition, HW3 Due

  - 12 Sep - Stress, Exam Review

  - 17 Sep - Exam 1

  - 19 Sep - Stress

### outline

\[sections numbered\]

# conservation of mass and compatibility

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

<span>conservation of mass</span>

  - Some materials (large deformation rubbers and many liquids) are
    treated as incompressible

  - For an incompressible material, the material derivative of density
    is zero, thus the conservation of mass reduces to \[v_{i,i} = 0\]

<span>compatibility</span>

  - Conservation of mass gives one form of "continuity," but
    displacements must also be continuous

  - It is possible to have a strain field for which no continuous
    displacement field can be found

  - Consider the following strain tensor \[E = \begin{bmatrix}
            kX_2^2 & 0 & 0\\
            0 & 0 & 0 \\
            0 & 0 & 0
            \end{bmatrix}\]

  - Since no displacement can satisfy this strain field, we say that the
    strain field is incompatible

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

<span>example</span>

  - Is the following strain field compatible? \[E = \begin{Bmatrix}
            -\frac{X_2}{X_1^2 + X_2^2} & \frac{X_1}{2(X_1^2 + X_2^2)} & 0\\
            \frac{X_1}{2(X_1^2 + X_2^2)} & 0 & 0 \\
            0 & 0 & 0
            \end{Bmatrix}\]

<span>compatibility for rate of deformation</span>

  - As with strain, when the velocity functions exist, we can always
    determine the deformation components

  - If we have only the deformation tensor, however, compatibility must
    be satisfied (they are identical to the strain compatibility
    equations)

  - In fluid mechanics we usually deal directly with velocity functions,
    in which case compatibility is not a concern

# finite deformation

<span>deformation gradient</span>

  - If we recall the definition of the deformation gradient, we have
    \[dx_i = F_{ij} dX_j\] \[F = I + \nabla u_i = \nabla x_i = x_{i,j}\]

  - We will now consider a few physical requirements

  - First, \(dx_i\) can be zero only if \(dX_i\) is zero, thus we know
    \(F^{-1}\) exists \[dX_i = F^{-1} dx_i\]

  - We can also ensure no reflections occur in deformation by ensuring
    that \(\det (F_{ij}) > 0\)

<span>finite deformation</span>

  - Let us use the notation \(U_{ij} = F_{ij}\) for the special case
    when \(U_{ij}\) is symmetric and positive definite

  - This means that for any vector, \(a_i\) \[a_i U_{ij} a_j = 0\]

  - In this case all eigenvalues will be positive

  - The eigenvalues of \(U_{ij}\) are the principal stretches, they
    include the maximum and minimum stretches

<span>rigid body motion</span>

  - Another special case of \(F\) is the case when
    \(F_{ij}F_{ik} = \delta_{jk}\) and \(\det F_{ij} = 1\)

  - This gives a rigid body rotation, and can be denoted as a rotation
    tensor, \(R_{ij}\)

# polar decomposition

<span>polar decomposition</span>

  - It can be shown that for any real tensor \(F_{ij}\) with a nonzero
    determinant \[\label{eq:polar-right}
            F_{ij} = R_{ik} U_{kj}\]

  - And \[\label{eq:polar-left}
            F_{ij} = V_{ik} R_{kj}\]

  - Where \(U_{ij}\) is known as the right stretch tensor and \(V_{ij}\)
    is known as the left stretch tensor

  - &nbsp;[\[eq:polar-right\]](#eq:polar-right) and
    &nbsp;[\[eq:polar-left\]](#eq:polar-left) are known as the Polar
    Decomposition Theorem

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

<span>right cauchy-green deformation tensor</span>

  - We can follow the same development as with small strain to extract
    physical meaning from the right Cauchy-Green deformation tensor
    \[dx_i^{(1)} dx_i^{(2)} = F_{ji} dX_i^{(1)} F_{jk} dX_k^{(2)} = dX_i^{(1)} F_{ji}  F_{jk} dX_k^{(2)} = dX_i^{(1)} C_{ik} dX_k^{(2)}\]

  - We find that \(C_{11} = \left(\frac{ds_1}{dS_1}\right)^2\)

  - Following a similar development for shear, we find
    \[C_{12} = \frac{ds_1 ds_2}{dS_1 dS_2}\cos (dx_i^{(1)},dx_i^{(2)})\]

<span>left cauchy-green deformation tensor</span>

  - Sometimes it is more advantageous to use the left cauchy-green
    deformation tensor

  - If we express the direction vector \(dX_i = dS R_{ji}e_j\) we can
    write the physical meaning of \(B_{ij}\) in the same way as
    \(C_{ij}\) \[\begin{aligned}
            B_{11} &= \left(\frac{ds_1}{dS_1}\right)^2\\
            B_{12} &= \frac{ds_1 ds_2}{dS_1 dS_2}\cos (dx_i^{(1)},dx_i^{(2)})
            \end{aligned}\]

<span>polar decomposition</span>

  - An object deforms according to the motion \[\begin{aligned}
            x_1 &= X_1 + 2X_2 \sin t + 0.5X_3\\
            x_2 &= -\frac{1}{3} X_1  + X_2 - X_3 \sin t\\
            x_3 &= X_1^2 \sin 2t + 1.5 X_3
            \end{aligned}\]

  - Find \(U\) and \(R\) at the point \(X=(1,1,1)\) after \(t=0.25\)

# finite strain tensors

<span>lagrangian strain tensor</span>

  - Recall the Lagrangian strain tensor
    \[E^*_{ij} = \frac{1}{2}(C_{ij} - \delta_{ij})\]

  - Following the same development as done previously, we can find the
    physical meaning of the Lagrangian strain tensor \[\begin{aligned}
            E_{11}^* &= \frac{ds_1^2 - dS_1^2}{2dS_1^2}\\
            2E_{12}^* &= \frac{ds_1 ds_2}{dS_1 dS_2} \cos (n_i, m_i)
            \end{aligned}\]

  - We can compare this to the infinitesimal strain tensor
    \[\begin{aligned}
            E_{11} &= \frac{ds - dS}{dS}\\
            2E_{12} &= \gamma
            \end{aligned}\]

<span>lagrangian strain tensor</span>

  - We can also write the Lagrangian strain tensor in terms of
    displacement

  - Recall that \(C=F^TF\) and \(F = I + \nabla u\) \[\begin{gathered}
            E^* = \frac{1}{2}(F^TF - I) = \frac{1}{2}\left[(I + \nabla u)^T(I + \nabla u) - I\right] = \\
            \frac{1}{2}\left[(\nabla u)^T \nabla u + \nabla u + (\nabla u)^T \right]
            \end{gathered}\]

<span>eulerian strain tensor</span>

  - The Eulerian strain tensor is defined as
    \[e^* = \frac{1}{2}(I - B^{-1})\]

  - Following the same procedure for identifying physical meaning, but
    using the inverse of \(F_{ij}\), we find \[\begin{aligned}
            e_{11}^* &= \frac{ds_1^2 - dS_1^2}{2ds_1^2}\\
            e_{12}^* &= -\frac{dS_1dS_2}{ds_1ds_2}\cos (n_i, m_i)
            \end{aligned}\]

<span>eulerian strain tensor</span>

  - If we express the eulerian strain tensor in terms of displacement,
    we find

  - \[e^* = \frac{1}{2}\left[-(\nabla_x u)^T \nabla_x u + \nabla_x u + (\nabla_x u)^T \right]\]

  - Notice that for small deformations, \(e^* \approx E^*\)

<span>change in volume</span>

  - If we consider three material elements, \(dX_i^{(1)} = dS_1 e_1\),
    \(dX_i^{(2)} = dS_2 e_2\) and \(dX_i^{(3)} = dS_3 e_3\) the volume
    in the reference configuration is given by \[dV_0 = dS_1 dS_2 dS_3\]

  - After deformation, we find that \[dV = dV_0 |\det F|\]

  - For convenience, \(J = |\det F|\) is often used

# finite elements

<span>finite element mapping</span>

  - Finite elements are often used to solve continuum mechanics problems

  - It is helpful to know how important quantities, such as the
    deformation gradient, are calculated

  - Reference on this topic can be found from the open source continuum
    mechanics text:
    <http://continuummechanics.org/finiteelementmapping.html>

<span>finite element mapping</span>

![image](../Figures/FE_mapping_example.png)
<span id="fig:femappingexample" label="fig:femappingexample">\[fig:femappingexample\]</span>

<span>finite element mapping</span>

  - The equations to map this deformation are generally written as
    \[\begin{aligned}
            u(X,Y) &= \phi_1(X,Y) u_1 + \phi_2(X,Y) u_2 + \phi_3(X,Y) u_3 + \phi_4(X,Y) u_4\\
            v(X,Y) &= \phi_1(X,Y) v_1 + \phi_2(X,Y) v_2 + \phi_3(X,Y) v_3 + \phi_4(X,Y) v_4
            \end{aligned}\]

  - Where \(\phi_i\) are the shape functions for each node in the
    element \[\begin{aligned}
            \phi_1 &= \frac{1}{4}(1-X)(1-Y)\\
            \phi_2 &= \frac{1}{4}(1+X)(1-Y)\\
            \phi_3 &= \frac{1}{4}(1+X)(1+Y)\\
            \phi_4 &= \frac{1}{4}(1-X)(1+Y)\\
            \end{aligned}\]

<span>deformation gradients</span>

  - Recall that the deformation gradient in terms of displacement is
    \[F_{ij} = \delta_{ij} + u_{i,j}\]

  - We can readily calculate this for individual terms of the
    deformation gradient
