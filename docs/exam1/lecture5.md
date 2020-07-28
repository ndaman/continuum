<span>upcoming schedule</span>

  - 5 Sep - Conservation and Compatibility, HW2 Due

  - 10 Sep - Polar Decomposition, HW3 Due

  - 12 Sep - Stress, Exam Review

  - 17 Sep - Exam 1

### outline

\[sections numbered\]

# deformation

<span>infinitesimal deformation</span>

<span>0.3</span>

![image](../Figures/f03-07-01-H8560.jpg)
<span id="fig:f03-07-01-H8560" label="fig:f03-07-01-H8560">\[fig:f03-07-01-H8560\]</span>

<span>0.7</span>

  - We recall \(P\), which undergoes some displacement, \(u\)

  - A neighboring point, \(Q\), at \(X_i + dX_i\) arrives at
    \(x_i + dx_i\)

  - \[x_i + dx_i = X_i + dX_i + u_i(X_i + dX_i, t)\]

  - Subtracting \(dx_i\) and using the definition of the gradient of a
    vector function, we have \[dx_i = dX_i + u_{i,j} dX_j\]

<span>infinitesimal deformation</span>

  - We can re-write (4.24) \[\begin{aligned}
            dx_i &= dX_i + u_{i,j} dX_j\\
            dx_i &= dX_j \delta_{ij} + u_{i,j} dX_j\\
            dx_i &= (u_{i,j} + \delta_{ij}) dX_j
            \end{aligned}\]

  - We define the deformation gradient, \(F\) as
    \(F = u_{i,j} +  \delta_{ij}\)

<span>infinitesimal deformation</span>

  - We can find some interesting information by finding the length of
    \(dx_i\) relative to the undeformed length of \(dX_i\)

  - \[dx_i dx_i = F_{ij} dX_j F_{ik} dX_k\]

  - We can rearrange this to \[dx_i dx_i =  dX_j F_{ij} F_{ik} dX_k\]

  - We now define the right Cauchy-Green deformation tensor as
    \(C_{jk} = F_{ij} F_{ik}\), and note that if
    \(C_{jk} = \delta_{jk}\), then the deformed length is equal to the
    original length, corresponding to rigid body motion

<span>lagrange strain tensor</span>

  - We can break down the right Cauchy-Green deformation tensor to
    derive the Lagrange strain tensor

  - \[\begin{gathered}
            C_{ij} = F_{ki} F_{kj} = F^TF = (I+\nabla u)^T(I+\nabla u) = \\
            \qquad I + \nabla u + (\nabla u)^T + (\nabla u)^T (\nabla u)
        \end{gathered}\]

  - We recall that \(C = I\) refers to rigid body motion, and thus
    define the Lagrange strain tensor as one-half of the deformation
    with no rigid body motion

  - \[E^* = \frac{1}{2} \left[\nabla u + (\nabla u)^T + (\nabla u)^T (\nabla u)\right]\]

<span>lagrange strain tensor</span>

  - The Lagrange strain tensor is a finite deformation tensor

  - For infinitesimal deformations, we assume that
    \((\nabla u)^T (\nabla u)\) is negligible when compared with
    \(\nabla u\)

  - In this case the Lagrange strain tensor would reduce to
    \[E = \frac{1}{2} \left[\nabla u + (\nabla u)^T\right]\]

  - Which is simply the symmetric portion of \(\nabla u\)

  - In rectangular coordinates, we have
    \[E_{ij} = \frac{1}{2} (u_{i,j} + u_{j,i})\]

<span>physical meaning</span>

  - If we consider two elements, \(dX_i^{(1)}\) and \(dX_i^{(2)}\)

  - Due to motion they become \(dx_i^{(1)}\) and \(dx_i^{(2)}\)

  - For small deformations, we know that \[\begin{gathered}
            dx_i^{(1)} dx_i^{(2)} = F_{ij} dX_j^{(1)} F_{ik} dX_k^{(2)} = dX_j^{(1)} C_{jk} dX_k^{(2)} = \\
            \qquad dX_j^{(1)} (\delta_{jk} + 2E_{jk}) dX_k^{(2)}
        \end{gathered}\]

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

<span>physical meaning</span>

  - If we consider two unit vectors, \(m_i\) and \(n_i\) which are
    initially perpendicular, we have \(dX_i^{(1)} = dS_1 m_i\) and
    \(dX_i^{(2)} = dS_2n_i\)

  - We can find the angle between the two deformed vectors,
    \(dx_i^{(1)}\) and \(dx_i^{(2)}\)

  - \[dx_i^{(1)} dx_i^{(2)} = ds_1 ds_2 \cos \theta = 2E_{jk}dS_1 m_j dS_2 n_k\]

  - Since the angle between the vectors was originally \(\pi/2\), we
    define the change in angle as \(\gamma = \pi/2 - \theta\)

<span>physical meaning</span>

  - We also note that
    \(\cos \theta = \cos (\pi/2 - \gamma) = \sin \gamma\)

  - For small deformations (i.e. small \(\gamma\)) we have
    \(\sin \gamma \approx \gamma\) and \(\frac{ds_1}{dS_1} \approx 1\)
    and \(\frac{ds_2}{dS_2} \approx 1\)

  - This gives \[\gamma = 2 E_{ij} m_i n_j\]

  - We can isolate off-diagonal terms in \(E_{ij}\) by letting
    \(m_i = \langle 1, 0, 0 \rangle\) and
    \(n_j = \langle 0,1,0 \rangle\) (and other perpendicular directions)

  - This means that \(2E_{12}\) gives the change in angle between two
    elements initially in the \(x_1\) and \(x_2\) directions

# review

<span>Group 1</span>

  - Describe the difference between a material (Lagrangian) and a
    spatial (Eulerian) description

  - Give some examples of situations where each would be more convenient

<span>Group 2</span>

  - What is the material derivative?

  - Why is it calculated differently in material and spatial
    descriptions?

<span>Group 3</span>

  - What is the physical meaning of the components of the infinitesimal
    strain tensor?

  - Describe (in general) how we can derive this physical meaning

# infinitesimal strain

<span>principal strains</span>

  - Principal strains and their corresponding directions can be
    calculated just as any other eigenvalues and vectors

  - Since there is no shear in the principal directions, a unit cube in
    the principal directions will only undergo stretching

  - From this idea, we can derive the dilatation (change in volume)
    \[e = E_{ii}\]

<span>rotation tensor</span>

  - The strain tensor was found by taking the symmetric portion of the
    deformation tensor

  - The anti-symmetric portion of the deformation tensor is known as the
    rotation tensor, \(\Omega\) \[\nabla u = E + \Omega\]

<span>rate of deformation</span>

  - The change in a material element is given by
    \[dx_i = x_i (X_i + dX_i, t) - x_i (X_i, t)\]

  - We obtain the rate of change by taking the material derivative
    \[\frac{D}{Dt} dx_i = \frac{D}{Dt} x_i (X_i + dX_i, t) - \frac{D}{Dt} x_i (X_i, t)\]

  - Since \(\frac{D}{Dt} x_i = v_i\), we have
    \[\frac{D}{Dt} dx_i = v_i (X_i + dX_i, t) - v_i (X_i, t) = \nabla v_i = v_{i,j}\]

<span>rate of deformation</span>

  - As with the strain tensor, we can de-compose the velocity gradient
    into symmetric and anti-symmetric portions
    \[v_{i,j} = D_{ij} + W_{ij}\]

  - \(D_{ij}\) is known as the rate of deformation tensor

  - \(W_{ij}\) is known as the spin tensor

<span>rate of deformation</span>

  - We can develop expressions for the physical meaning of \(D_{ij}\)
    the same way we did for \(E_{ij}\)

  - If we let \(dx_i = ds n_i\) then we can express the magnitude of
    \(dx_i\) as \[dx_i dx_i = (ds)^2\]

  - Since we are concerned with the rate of deformation, we take the
    material derivative of both sides
    \[2 dx_i \frac{D}{Dt} dx_i = 2ds \frac{D}{Dt}ds\]

<span>rate of deformation</span>

  - We also know that
    \[dx_i \frac{D}{Dt} dx_i = dx_i v_{i,j} dx_j = dx_i D_{ij} dx_j + dx_i W_{ij} dx_j\]

  - However since \(W_{ij}\) is antisymmetric, we know that
    \[dx_i W_{ij} dx_j = dx_i W_{ji} dx_j = - dx_i W_{ij} dx_j = 0\]

  - Which means that \[dx_i \frac{D}{Dt} dx_i = dx_i D_{ij} dx_j\]

<span>rate of deformation</span>

  - Substituting back into (5.8) we find
    \[dx_i \frac{D}{Dt} dx_i = dx_i D_{ij} dx_j = ds \frac{D}{Dt}ds\]

  - Since \(dx_i = ds n_i\) we can re-write this as
    \[ds n_i D_{ij} ds n_j = ds \frac{D}{Dt}ds\]

  - \(ds\) is a scalar, so we can divide both sides by \(ds^2\) to give
    \[n_i D_{ij} n_j = \frac{1}{ds} \frac{D}{Dt}ds\]

<span>physical interpretation</span>

  - Similar to the results we found for strain, \(D_{11}\) gives rate of
    extension (stretch) in the \(x_1\)-direction

  - We could also follow a similar development as used for the shear
    terms to see that \(2D_{12}\) gives the rate of decrease in angle
    between elements in the \(x_1\) and \(x_2\) directions

  - We can also find the rate of change of volume
    \[D_{11} + D_{22} + D_{33} = \frac{1}{V} \frac{D}{Dt}dV = v_{i,i}\]

<span>spin tensor</span>

  - Any anti-symmetric tensor, \(W_{ij}\) is equivalent to some vector,
    \(\omega\) in that \[W_{ij} a_j = \epsilon_{ijk} \omega_j a_k\]

  - Since \(a_j\) can be any vector, we can write
    \[W_{ij} dx_j = \epsilon_{ijk} \omega_j dx_k\]

  - Therefore
    \[\frac{D}{Dt} dx_i =  v_{i,j} dx_j = (D_{ij} + W_{ij})dx_j = D_{ij} dx_j + \epsilon_{ijk} \omega_j dx_k\]

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
    that \(det (F_{ij}) > 0\)

<span>finite deformation</span>

  - Let us use the notation \(U_{ij} = F_{ij}\) for the special case
    when \(U_{ij}\) is symmetric and positive definite

  - This means that for any vector, \(a_i\) \[a_i U_{ij} a_j = 0\]

  - In this case all eigenvalues will be positive

  - The eigenvalues of \(U_{ij}\) are the principal stretches, they
    include the maximum and minimum stretches

<span>rigid body motion</span>

  - Another special case of \(F\) is the case when
    \(F_{ij}F_{ik} = \delta_{jk}\) and \(det F_{ij} = 1\)

  - This gives a rigid body rotation, and can be denoted as a rotation
    tensor, \(R_{ij}\)

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

<span>polar decomposition</span>

  - An object deforms according to the motion \[\begin{aligned}
            x_1 &= X_1 + 2X_2 \sin t + 0.5X_3\\
            x_2 &= -\frac{1}{3} X_1  + X_2 - X_3 \sin t
            x_3 &= X_1^2 \sin 2t + 1.5 X_3
            \end{aligned}\]

  - Find \(U\) and \(R\) at the point \(X=(1,1,1)\) after \(t=0.25\)

<span>right cauchy-green deformation tensor</span>

  - We can follow the same development as with small strain to extract
    physical meaning from the right Cauchy-Green deformation tensor
    \[dx_i^{(1)} dx_i^{(2)} = F_{ji} dX_i^{(1)} F_{jk} dX_k^{(2)} = dX_i^{(1)} F_{ji}  F_{jk} dX_k^{(2)} = dX_i^{(1)} C_{ik} dX_k^{(2)}\]

  - We find that \(C_{11} = \left(\frac{ds_1}{dS_1}\right)^2\)

  - Following a similar development for shear, we find
    \[C_{12} = \frac{ds_1 ds_2}{dS_1 dS_2}\cos (dx_i^{(1)},dx_i^{(2)})\]
