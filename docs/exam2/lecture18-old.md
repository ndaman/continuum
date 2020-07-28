<span>upcoming schedule</span>

  - 31 Oct - Exam Review

  - 2 Nov - HW 8 Due, Recitation, Newtonian Fluids

  - 7 Nov - Exam 2

  - 9 Nov - Exam return, Newtonian Fluids

### outline

\[sections numbered\]

# exam content

<span>exam content</span>

  - Stress
    
      - Traction vectors
    
      - Boundary conditions
    
      - Piola-Kirchhoff stress tensors
    
      - Equilibrium equations
    
      - Stress power

<span>exam content</span>

  - Isotropic linear elasticity
    
      - Hooke&rsquo;s Law
    
      - Lam&eacute; constants
    
      - Navier Equations
    
      - Planar problems
    
      - Beltrami-Michell
    
      - Airy Stress

<span>exam content</span>

  - Anisotropic linear elasticity
    
      - Material symmetry
    
      - Monoclinic, orthotropic, transversely isotropic
    
      - Physical interpretations
    
      - Experimental considerations

<span>exam content</span>

  - Large deformation
    
      - Objective tensors
    
      - Co-rotational derivative
    
      - Stretch ratio
    
      - Constitutive laws
    
      - Thermodynamic formulation

<span>exam format</span>

  - Three problems

  - Similar to homework problems

  - Short answer, explain the significance of your calculations

  - Will not ask you to solve problem with Airy stress function, but you
    should understand conceptually what the Airy stress function is and
    how it helps

# stress

<span>traction</span>

![image](../Figures/traction.PNG)
<span id="fig:traction" label="fig:traction">\[fig:traction\]</span>

<span>traction</span>

  - The traction vector is defined as
    \[\hat{t}^n(x,\hat{n}) = \lim\limits_{\Delta A \to 0} \frac{\Delta \hat{f}}{\Delta A}\]

  - By Newton&rsquo;s third law (action-reaction principle)
    \[\hat{t}^n(x,\hat{n}) = -\hat{t}^n(x,-\hat{n})\]

<span>stress tensor</span>

  - To simplify the notation, we introduce the stress tensor
    \[\sigma_{ij} = t_j^{(\hat{e}_i)}\]

<span>traction</span>

  - We can further combine these results in index notation as
    \[t_j = \sigma_{ij} n_i\]

  - This means with knowledge of the nine components of \(\sigma_{ij}\),
    we can find the traction vector at any point on any surface

<span>boundary conditions</span>

  - In most problems, we don&rsquo;t know anything about the internal
    stress state, but we do know what is applied on the surface

  - We apply these as traction boundary conditions, which can be used to
    find the internal stress tensor

  - If a surface is "free" with no boundary or force constraints, it is
    a traction-free boundary condition

<span>saint venant&rsquo;s principle</span>

  - Some boundary conditions are cumbersome to model exactly

  - In this case we can use Saint Venant&rsquo;s principle to express a
    statically equivalent version of the boundary conditions

  - For example, for a beam with applied bending moments, we may not
    know the exact traction distribution along the ends, but we know
    that \[\begin{aligned}
            \int_{-c}^{c}\sigma_x (\pm l,y)dy &= 0\\
            \int_{-c}^{c}\sigma_x (\pm l,y)ydy &= -M
            \end{aligned}\]

  - Since these boundary conditions are approximate, it is possible to
    find multiple solutions which satisfy these boundary conditions

  - We usually choose the simplest polynomial which can satisfy them.

<span>saint venant&rsquo;s principle</span>

  - Displacement boundary conditions are cumbersome to implement when
    solving a problem with stress functions

  - Would need to convert stress to displacement to apply the condition

  - We can use Saint Venant&rsquo;s principle to express the statically
    equivalent traction boundary conditions for those displacement
    conditions

<span>pinned beam</span>

<span>first piola kirchoff stress tensor</span>

  - For the first Piola Kirchoff stress tensor (also known as the
    Lagrangian stress tensor), we let \[df_i = t^0_i dA^0\]

  - Note that \(t^0_i\) is a pseudo traction vector, and does not
    describe the actual intensity of \(df_i\), which is acting on the
    deformed area

  - Also note that since \(df_i\) is the acting on the deformed area,
    \(t^0_i\) acts in the same direction as \(t_i\)

  - We can now formulate the stress tensor in the same way as the Cauchy
    stress tensor \[t^0_i = T^0_{ij}n^0_j\]

<span>first piola kirchoff stress tensor</span>

  - We can also relate the first Piola-Kirchoff stress tensor to the
    Cauchy stress tensor

  - \[T^0_{ij} = J T_{im}F_{jm}^{-1}\]

  - And the inverse relationship is
    \[T_{ij} = \frac{1}{J}T^0_{im}F_{jm}\]

  - In general, the first Piola-Kirchoff stress tensor is not symmetric

<span>second piola kirchoff stress tensor</span>

  - If instead we consider a pseudo-differential force acting on the
    un-deformed area \[d\tilde{f}_i = \tilde{t}_i dA^0\] where
    \[df_i = F_{ij}d\tilde{f}_j\]

  - In general, the traction vector \(\tilde{t}_i\) is in a different
    direction that \(t_i\) and \(t^0_i\)

  - Once again, we can formulate the second Piola-Kirchoff stress tensor
    as the others \[\tilde{t}_i = \tilde{T}_{ij}n^0_j\]

<span>second piola kirchoff stress tensor</span>

  - We can easily relate the Second and First Piola Kirchoff stress
    tensors \[\tilde{T}_{ij} = F_{im}^{-1}T^0_{mj}\]

  - We can now substitute to relate the Second Piola Kirchoff stress
    tensor to the Cauchy stress tensor
    \[\tilde{T}_{ij} = J F_{im}^{-1}T_{mn}F_{jn}^{-1}\]

  - For a symmetric stress tensor, \(T_{ij}\), the Second Piola Kirchoff
    stress tensor is symmetric

<span>reference configuration</span>

  - At this point it is desirable to formulate equations of motion in
    terms of the first and second Piola-Kirchhoff stress tensors

  - Recall for Cauchy stress \[T_{ij,j} + \rho B_i = \rho a_i\]

  - Now we substitute \(T_{ij} = \frac{1}{J} T_{im}^0F_{jm}\) to get
    \[T_{ij,j} = \frac{\partial}{\partial x_j} \left(\frac{1}{J} T_{im}^0F_{jm}\right) = \frac{F_{jm}}{J} \frac{\partial T^0_{im}}{\partial x_j} + T^0_{im} \frac{\partial}{\partial x_j} \frac{F_{im}}{J}= \frac{F_{jm}}{J} \frac{\partial T^0_{im}}{\partial x_j}\]

<span>reference configuration</span>

  - Since \(T_{ij}^0\) is expressed in terms of the reference
    configuration, we desire to change the partial derivative from
    \(x_j\) to \(X_j\), which we can do as follows
    \[\frac{\partial T_{ij}}{\partial x_j}\frac{F_{jm}}{J} \frac{\partial T^0_{im}}{\partial x_j} = \frac{1}{J} \frac{\partial x_j}{\partial X_m} \frac{\partial T^0_{im}}{\partial X_n}\frac{\partial X_n}{\partial x_j} = \frac{1}{J} \delta_{mn} \frac{\partial T^0_{im}}{\partial X_n}\]

  - Substituting this into the equation of motion, and multiplying both
    sides by \(J\) gives
    \[\frac{\partial T^0_{ij}}{\partial X_j} + J \rho B_i = J \rho a_i\]

  - The quantity \(J \rho\) is sometimes written as \(\rho^0\)

<span>stress power</span>

  - Stress power, \(P_s\), is the rate at which work is done to change
    the volume and shape of a particle

  - In Cauchy stress, we find that \(P_s = T_{ij} D_{ij}\)

  - For the first Piola-Kirchoff stress tensor, we find
    \[P_s = \frac{\rho}{\rho^0}T^0_{ij} \frac{D F_{ij}}{Dt}\]

  - And for the second Piola-Kirchoff stress tensor
    \[P_s = \frac{\rho}{\rho^0} \tilde{T_{ij}} \frac{D E^*_{ij}}{Dt}\]

# isotropic linear elasticity

<span>Hooke&rsquo;s Law</span>

  - Most engineering materials are isotropic, this means the stiffness
    is the same in any direction \[C_{ijkl}^\prime = C_{ijkl}\]

  - A fourth-order isotropic tensor can be written as
    \[C_{ijkl} = \lambda \delta_{ij} \delta_{kl} + \alpha \delta_{ik} \delta_{jl} + \beta \delta_{il}\delta_{jk}\]

  - If we substitute this into Hooke&rsquo;s Law
    \[T_{ij} = \lambda E_{kk} \delta_{ij} + (\alpha + \beta) E_{ij}\]
    which is often written as \[\label{eq:hooke}
            T_{ij} = \lambda E_{kk} \delta_{ij} + 2\mu E_{ij}\]

<span>lam&eacute; constants</span>

  - \(\lambda\) and \(\mu\) are known as Lam&eacute; constants

  - They are purely mathematical, but we can relate them to physical
    parameters

  - We can solve ([\[eq:hooke\]](#eq:hooke)) for \(E_{ij}\) to find
    \[E_{ij} = \frac{1}{2\mu} \left[T_{ij} - \frac{\lambda}{3\lambda + 2\mu}T_{kk}\delta_{ij}\right]\]

  - If we consider a state of uniaxial stress (as in a simple tension
    test) we find \[\begin{aligned}
            E_{11} &= \frac{\lambda + \mu}{\mu(3\lambda+2\mu)}T_{11}\\
            E_{22} &= E_{33} = - \frac{\lambda}{2\mu(3\lambda+2\mu)}T_{11}\\
            E_{12} &= E_{23} = E_{13} = 0
            \end{aligned}\]

<span>navier equations of motion</span>

  - Navier&rsquo;s equations use Hooke&rsquo;s Law and the strain
    displacement relations to re-write the equations of motion in terms
    of displacement only

  - First we re-write Hooke&rsquo;s Law in terms of displacement
    \[T_{ij} = \lambda E_{kk} \delta_{ij} + 2\mu E_{ij} = \lambda e \delta_{ij} + \mu \left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)\]

  - Where \(e\) is the dilatation, or change in volume

<span>navier equations of motion</span>

  - Now we note a couple of things when we take \(T_{ij,j}\)

  - \[T_{ij,j} = \lambda \frac{\partial e}{\partial x_j} \delta_{ij} + \mu \left( \frac{\partial^2 u_i}{\partial x_j \partial x_j} + \frac{\partial u_j}{\partial x_j \partial x_i}\right)\]

  - \[\frac{\partial e}{\partial x_j} \delta_{ij} = \frac{\partial e}{\partial x_j}\]

  - Since order of differentiation does not matter, we can write
    \[\frac{\partial u_j}{\partial x_j \partial x_i} = \frac{\partial}{\partial x_i} \left( \frac{\partial u_j}{\partial x_j}\right) = \frac{\partial e}{\partial x_i}\]

  - Which gives the Navier equations as
    \[\rho_0 \frac{\partial^2 u_i}{\partial t^2} = \rho_0 B_i + (\lambda + \mu) \frac{\partial e}{\partial x_i} + \mu \frac{\partial^2 u_i}{\partial x_j \partial x_j}\]

<span>plane strain</span>

  - If motion in any one direction (for example \(x_3\)) is restricted,
    such that \(u_3 = 0\), a body is said to be in a state of plane
    strain

  - The plane strain is often used for very thick materials, where
    \(u_3 \ll u_1, u_2\), but is also applicable any time \(u_3\) is
    restricted

  - Under plane strain conditions we have \[\begin{aligned}
            E_{13} &= E_{23} = E_{33} = 0\\
            E_{11} &= E_{11}(x_1, x_2)\\
            E_{22} &= E_{22}(x_1, x_2)\\
            E_{12} &= E_{12}(x_1,x_2)
            \end{aligned}\]

<span>plane strain</span>

  - Using Hooke&rsquo;s Law, we find that \(T_{13} = T_{23} = 0\), but
    \[T_{33} = \nu (T_{11} + T_{22})\]

  - While the other stress components, \(T_{11}\), \(T_{12}\) and
    \(T_{22}\) are all functions of \(x_1\) and \(x_2\)

  - In the absence of body forces, we find the equilibrium equations as
    \[\begin{aligned}
            \frac{\partial T_{11}}{\partial x_1} + \frac{\partial T_{12}}{\partial x_2} &= 0\\
            \frac{\partial T_{21}}{\partial x_1} + \frac{\partial T_{22}}{\partial x_2} &= 0\\
            \frac{\partial T_{33}}{\partial x_3} &= 0
            \end{aligned}\]

<span>plane stress</span>

  - For very thin bodies, we often make the assumption that
    \(\sigma_{13} = \sigma_{23} = \sigma_{33} = 0\)

  - Since we have started from an assumption in stress instead of
    displacement, it is not yet apparent whether this stress field is
    allowable

  - To simplify calculations for equilibrium and compatibility, we
    define a stress function, \(\varphi\) such that \[\begin{aligned}
            \sigma_{11} &= \varphi_{,22}\\
            \sigma_{22} &= \varphi_{,11}\\
            \sigma_{12} &= -\varphi_{,12}
            \end{aligned}\]

<span>plane stress</span>

  - We can quickly verify that this satisfies equilibrium
    \[\begin{aligned}
            \varphi_{,221} - \varphi_{,122} &= 0\\
            \varphi_{,121} - \varphi_{,112} &= 0
            \end{aligned}\]

  - We will not follow all the details, but from compatibility we find
    \[\varphi = \varphi_0(x_1,x_2) - \frac{\nu}{1+\nu}\Psi(x_1,x_2)\frac{1}{2}x_3^2\]

  - For plane stress problems, we generally consider the case where
    \(x_3 \ll x_1, x_2\), and thus we can neglect the second term,
    giving our stresses as functions of \(x_1\) and \(x_2\) only

  - Note that in general plane stress solutions only approximately
    satisfy compatibility

<span>beltrami-mitchell</span>

  - It is convenient to write the compatibility equations in terms of
    stress

  - This is known as the Beltrami-Mitchell equations

  - For planar problems, the Beltrami-Mitchell equations are
    \[\nabla^2 (\sigma_{11} + \sigma_{22}) = -\frac{4\rho}{1+\kappa} \left(b_{1,1} + b_{2,2}\right)\]

  - \(\kappa\) is used to differentiate between plane strain and plane
    stress \[\kappa=\begin{cases}
            3 - 4\nu & \text{Plane Strain}\\
            \frac{3-\nu}{1+\nu} & \text{Plane Stress}
            \end{cases}\]

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

<span>airy stress</span> \[\begin{aligned}
    T_{rr} &= \frac{1}{r}\frac{\partial \varphi}{\partial r} + \frac{1}{r^2}\frac{\partial^2 \varphi}{\partial \theta^2} + \mathcal{V}\\
    T_{r\theta} &= -\frac{\partial}{\partial r}\left(\frac{1}{r}\frac{\partial \varphi}{\partial \theta}\right)\\
    T_{\theta\theta} &= \frac{\partial^2 \varphi}{\partial r^2} + \mathcal{V}
    \end{aligned}\]

# anisotropic linear elasticity

<span>hooke&rsquo;s law</span>

  - Although it cannot be simplified as much as for isotropic materials,
    Hooke&rsquo;s Law still applies to linear anisotropic materials
    \[T_{ij} = C_{ijkl}E_{kl}\]

  - Or, written in "engineering" form \[\begin{bmatrix}
            T_{11}\\ T_{22} \\ T_{33} \\T_{23} \\ T_{13} \\ T_{12}
            \end{bmatrix}
            = \begin{bmatrix}
            C_{1111} & C_{1122} & C_{1133} & C_{1123} & C_{1113} & C_{1112} \\
            C_{1122} & C_{2222} & C_{2233} & C_{2223} & C_{1322} & C_{1222} \\
            C_{1133} & C_{2233} & C_{3333} & C_{2333} & C_{1333} & C_{1233} \\
            C_{1123} & C_{2223} & C_{2333} & C_{2323} & C_{1323} & C_{1223} \\
            C_{1113} & C_{1322} & C_{1333} & C_{1323} & C_{1313} & C_{1213} \\
            C_{1112} & C_{1222} & C_{1233} & C_{1223} & C_{1213} & C_{1212} 
            \end{bmatrix}\begin{bmatrix}
            E_{11}\\ E_{22} \\ E_{33} \\2E_{23} \\ 2E_{13} \\ 2E_{12}
            \end{bmatrix}\]

<span>material symmetries</span>

  - Very few anisotropic materials are fully anisotropic

  - Most have some degree of symmetry

  - We will consider monoclinic, transversely isotropic, and orthotropic
    symmetries

<span>symmetry</span>

  - Let \(S_1\) be the plane with a normal in the 1-direction

  - The transformation describing a reflection with respect to the plane
    \(S_1\) is \[Q = \begin{bmatrix}
            -1 & 0 & 0\\
            0 & 1 & 0\\
            0 & 0 & 1
            \end{bmatrix}\]

  - If a material is symmetric about \(S_1\), we know that
    \[\label{eq:mono}
            C_{ijkl} = C_{ijkl}^\prime = Q_{mi}Q_{nj}Q_{ok}Q_{pl} C_{mnop}\]

<span>monoclinic symmetry</span>

  - A monoclinic material is symmetric about one plane

  - If we consider the 1-direction to be the plane of material symmetry,
    we can use ([\[eq:mono\]](#eq:mono)) with the \(Q\) found earlier

  - As an example, we find the
    \(C_{1112} = Q_{m1}Q_{n1}Q_{o1}Q_{p2}C_{mnop}\), however when
    \(i\ne j\), \(Q_{ij}=0\)

  - This means we have \(C_{1112} = (-1)^3(1) C_{1112}\), which can only
    be satisfied when \(C_{1112} = 0\)

  - We similarly can show that
    \(C_{1113} = C_{1222} = C_{1223} C_{1233} = C_{1322} = C_{1323} = C_{1333} =0\)

<span>monoclinic symmetry</span> \[\begin{bmatrix}
    T_{11}\\ T_{22} \\ T_{33} \\T_{23} \\ T_{13} \\ T_{12}
    \end{bmatrix}
    = \begin{bmatrix}
    C_{1111} & C_{1122} & C_{1133} & C_{1123} & 0 & 0 \\
    C_{1122} & C_{2222} & C_{2233} & C_{2223} & 0 & 0 \\
    C_{1133} & C_{2233} & C_{3333} & C_{2333} & 0 & 0 \\
    C_{1123} & C_{2223} & C_{2333} & C_{2323} & 0 & 0 \\
    0 & 0 & 0 & 0 & C_{1313} & C_{1213} \\
    0 & 0 & 0 & 0 & C_{1213} & C_{1212} 
    \end{bmatrix}\begin{bmatrix}
    E_{11}\\ E_{22} \\ E_{33} \\2E_{23} \\ 2E_{13} \\ 2E_{12}
    \end{bmatrix}\]

<span>orthotropic symmetry</span>

  - If a material has two mutually perpendicular planes of symmetry (for
    example, \(S_1\) and \(S_2\) with normals in the 1 and 2
    directions), then \(S_3\) plane will also automatically be plane of
    symmetry

  - This state of symmetry is known orthotropy

  - Orthotropic materials are more common in engineering use than
    monoclinic

  - All shear coupling terms are zero for orthotropic materials

<span>orthotropic symmetry</span> \[\begin{bmatrix}
    T_{11}\\ T_{22} \\ T_{33} \\T_{23} \\ T_{13} \\ T_{12}
    \end{bmatrix}
    = \begin{bmatrix}
    C_{1111} & C_{1122} & C_{1133} & 0 & 0 & 0 \\
    C_{1122} & C_{2222} & C_{2233} & 0 & 0 & 0 \\
    C_{1133} & C_{2233} & C_{3333} & 0 & 0 & 0 \\
    0 & 0 & 0 & C_{2323} & 0 & 0 \\
    0 & 0 & 0 & 0 & C_{1313} & 0 \\
    0 & 0 & 0 & 0 & 0 & C_{1212} 
    \end{bmatrix}\begin{bmatrix}
    E_{11}\\ E_{22} \\ E_{33} \\2E_{23} \\ 2E_{13} \\ 2E_{12}
    \end{bmatrix}\]

<span>transversely isotropic symmetry</span>

  - If there exists a plane, such as the \(S_3\) plane, where any plane
    perpendicular to that plane is a plane of symmetry, we call this
    transverse isotropy

  - The direction normal to that plane is the axis of transverse
    isotropy

<span>transversely isotropic symmetry</span> \[\begin{bmatrix}
    T_{11}\\ T_{22} \\ T_{33} \\T_{23} \\ T_{13} \\ T_{12}
    \end{bmatrix}
    = \begin{bmatrix}
    C_{1111} & C_{1122} & C_{1133} & 0 & 0 & 0 \\
    C_{1122} & C_{1111} & C_{1133} & 0 & 0 & 0 \\
    C_{1133} & C_{1133} & C_{3333} & 0 & 0 & 0 \\
    0 & 0 & 0 & C_{1313} & 0 & 0 \\
    0 & 0 & 0 & 0 & C_{1313} & 0 \\
    0 & 0 & 0 & 0 & 0 & 1/2(C_{1111}-C_{2222})
    \end{bmatrix}\begin{bmatrix}
    E_{11}\\ E_{22} \\ E_{33} \\2E_{23} \\ 2E_{13} \\ 2E_{12}
    \end{bmatrix}\]

<span>physical interpretation</span>

  - To find the physical interpretation of elastic constants in
    Hooke&rsquo;s Law, it is easiest to use the inverse form
    \[T_{ij} = C_{ijkl}E_{kl}\]

  - And the inverse form, where the compliance tensor,
    \(S_{ijkl} = C_{ijkl}^{-1}\) is \[E_{ij} = S_{ijkl} T_{kl}\]

<span>physical interpretation</span>

  - If we now consider the case of uniaxial tension, we see that
    \[\begin{aligned}
            E_{11} &= S_{1111} T_{11}\\
            E_{22} &= S_{1122} T_{11}\\
            E_{33} &= S_{1133} T_{11}\\
            2E_{23} &= S_{1123} T_{11}\\
            2E_{13} &= S_{1113} T_{11}\\
            2E_{12} &= S_{1112} T_{11}
            \end{aligned}\]

  - \(S_{1111}\) is familiar, acting like \(1/E_Y\)

<span>poisson&rsquo;s ratio</span>

  - For isotropic materials we defined Poisson&rsquo;s ratio as
    \(\nu = -E_{22}/E_{11}\)

  - For anisotropic materials, we can have a different Poisson&rsquo;s
    ratio acting in different directions

  - We define \(\nu_{ij} = -E_{jj}/E_{ii}\) (with no summation), the
    ratio of the transverse strain in the \(j\) direction when stress is
    applied in the \(i\) direction

  - For this example we can find \(\nu_{12}\) and \(\nu_{13}\) as
    \[\begin{aligned}
            \nu_{12} &= -E_{22}/E_{11} = -S_{1122}/S_{1111}\\
            \nu_{13} &= -E_{33}/E_{11} = -S_{1133}/S_{1111}
            \end{aligned}\]

<span>poisson&rsquo;s ratio</span>

  - Note that we cannot, in general, say that \(\nu_{12} = \nu_{21}\)

  - However, due to the symmetry of the stiffness/compliance tensors, we
    know that \[\begin{aligned}
            \nu_{21} E_{x} &= \nu_{12} E_{y}\\
            \nu_{31} E_{x} &= \nu_{13} E_{z}\\
            \nu_{32} E_{y} &= \nu_{23} E_{z}
            \end{aligned}\]

  - Where \(E_{x}\) refer&rsquo;s to the Young&rsquo;s Modulus in the
    \(x\)-direction, etc.

<span>shear coupling coefficients</span>

  - An unfamiliar effect is that shear strains are introduced from a
    normal stress

  - We define shear coupling coefficients as
    \(\eta_{1112} = \eta_{16} = -2E_{12}/E_{11}\) due to \(T_{11}\)

  - These coupling terms can also effect shear strain in a different
    plane from the applied shear stress

  - Like the Poisson&rsquo;s ratio, these are not entirely independent
    \[\eta_{61} E_{x} = \eta_{16} G_{6}\]

  - Where \(G_6\) is the shear modulus in the \(12\) plane

<span>characterizing anisotropic materials</span>

  - Characterizing anisotropic materials is not as simple as isotropic
    materials

  - Requires additional testing

  - 2 unique properties for isotropic (can be found with one test)

  - 5 unique properties for transversely isotropic

  - 9 unique properties for orthotropic

  - Also can be difficult to obtain state of pure shear/tension with
    traditional gripping

  - If material is heterogeneous that can introduce other challenges

  - Specimen alignment is much more important than for isotropic
    materials

<span>tensile testing</span>

  - If we consider an orthotropic material (such as a composite lamina),
    no shear is introduced when the fibers are perfectly aligned in the
    load direction

  - When orthotropic (or transversely isotropic) material is rotated,
    shear-coupling terms can be introduced

  - This shear deformation can cause failure at the grips

<span>tensile testing</span>

![image](../Figures/fiber_shear.PNG)
<span id="fig:fibershear" label="fig:fibershear">\[fig:fibershear\]</span>

![image](../Figures/fiber_warp.PNG)
<span id="fig:fiberwarp" label="fig:fiberwarp">\[fig:fiberwarp\]</span>

<span>tensile testing</span>

![Oblique tabs developed by Sun and Chung in
1993](../Figures/oblique_tabs.PNG)

<span>shear testing</span>

  - Just as grip constraints can make a state of pure tension difficult
    to obtain, it can be difficult to obtain a pure state of shear

  - There are many different shear test methods for anisotropic
    materials, most involve specialized grips and specialized specimen
    geometry

<span>iosipescu shear</span>

![image](../Figures/iosipescu.png)
<span id="fig:iosipescu" label="fig:iosipescu">\[fig:iosipescu\]</span>

<span>two-rail shear</span>

![image](../Figures/two-rail.jpg)
<span id="fig:two-rail" label="fig:two-rail">\[fig:two-rail\]</span>

# large deformation

<span>change of frame</span>

  - For small deformations, the current and deformed frame have
    negligible differences

  - For large deformations, we need to ensure that our constitutive law
    is objective, or frame-indifferent

  - Examples:
    
      - distance between two material points is a frame-indifferent
        scalar
    
      - speed of a material point is not frame-independent
        (non-objective)
    
      - position vector and velocity vector of a material point are
        non-objective
    
      - relative velocity between two material points is objective

<span>change of frame</span>

  - In general, a "frame" can have its own time scale, origin, and
    directionality

  - a change of frame would then be given by
    \[x_i^* = c_i(t) + Q_{ij}(t)(x_j-x^{0}_j)\]

  - If we consider the position vector of two material points, in the
    starred frame we have
    \[x_1^* = c(t) + Q(t)(x_1-x_0) \qquad x_2^* = c(t) + Q(t)(x_2-x_0)\]

  - The relative position vector, \(b=x_1-x_2\) can also be found in the
    starred frame as \[b^* = x_1^*-x_2^* = Q(t)(x_1-x_2)\]

  - Any vector which obeys this law is known as an objective vector

<span>change of frame</span>

  - If we consider some tensor, \(T_{ij}\) which transforms an objective
    vector \(b_j\) into another objective vector, \(c_i\)
    \[c_i = T_{ij}b_j\]

  - Since both \(b\) and \(c\) are objective vectors, we can write
    \[c_i^* = Q_{ik} c_k = Q_{ik} T_{kj} b_j = Q_{ik} T_{kj} Q_{lj} b_l\]

  - This means that for \(T_{ij}\) to be objective it must satisfy
    \[T_{ij}^* = Q_{ik} T_{kl} Q_{jl}\]

<span>corotational derivative</span>

  - In general, the material derivative of a tensor which is material
    indifferent (also called an objective tensor) is not objective

  - This motivates a new derivative to find the objective rate tensor
    for an objective tensor

  - We can derive a corotational derivative for stress and strain by
    considering the most general form of linear materials
    \[\sigma^0_{ij} = C_{ijkl} E^*_{kl}\]

  - Now we substitute the Cauchy stress and solve to find
    \[\label{eq:cauchy}
            \sigma_{ij} = \frac{1}{J} F_{im} C_{mnop} E_{op} F_{jn}\]

<span>jaumann derivative</span>

  - For the special case when an object is rotating, but not deforming,
    we have \(D_{ij} = 0\) which gives
    \[\accentset{\nabla}{\sigma}_{ij} = \dot{\sigma}_{ij} -  v_{i,k}\sigma_{kj} - \sigma_{ik} v_{j,k} = 0\]

  - And we can more clearly see the terms which account for
    \(\dot{\sigma}_{ij} \ne 0\)

  - Since \(D_{ij} = 0\), we can also re-write
    \(v_{i,j} = D_{ij} + W_{ij} = W_{ij}\)

  - We also know that \(W_{ij} = -W_{ji}\) which leads to the Jaumann
    derivative
    \[\mathring{\sigma}_{ij} = \dot{\sigma}_{ij} - W_{ik} \sigma_{kj} + \sigma_{ik} W_{kj}\]

<span>incompressible uniaxial stretch</span>

  - In large deformation problems, the stretch ratio, \(\lambda\) is
    often used (instead of strain)

  - \(\lambda_1\) represents the ratio of deformed length in \(x_1\) to
    undeformed length in \(x_1\)

  - For uniaxial extension we have \[\begin{aligned}
            x_1 &= \lambda_1 X_1\\
            x_2 &= \lambda_2 X_2\\
            x_3 &= \lambda_2 X_3
            \end{aligned}\]

  - Also if the material is incompressible we know
    \[\lambda_1 \lambda_2^2 = 1\]

<span>constitutive equations</span>

  - For large deformation, a constitutive law must be objective

  - \(T_{ij} = f(C_{ij})\) is not an acceptable form, but
    \(T_{ij} = f(B_{ij})\) is

  - \(\tilde{T}_{ij} = f(C_{ij})\) is also an acceptable form of the
    constitutive equation

  - If we assume our material to be isotropic, it can be shown that,
    with no loss of generality
    \[f(B_{ij}) = a_0 \delta_{ij} + a_1 B_{ij} + a_2 B_{ij}^2\]

<span>constitutive equations</span>

  - A commonly used alternate form of the constitutive equation is
    \[T_{ij} = \varphi_0 \delta_{ij} + \varphi_1 B_{ij} + \varphi_2 B_{ij}^{-1}\]

  - If the material is incompressible, the stress is indeterminate to
    some arbitrary hydrostatic pressure
    \[T_{ij} = -p \delta_{ij} + \varphi_1 B_{ij} + \varphi_2 B_{ij}^{-1}\]

  - This is known as the Mooney-Rivlin model, which can be written in
    different ways
    \[T_{ij} = -p \delta_{ij} + \mu \left(\frac{1}{2} + \beta\right) B_{ij} - \mu \left(\frac{1}{2} - \beta\right) B_{ij}^{-1}\]

<span>neo-hookean solid</span>

  - A simpler model, which is only accurate for strains less than 20%,
    is the neo-Hookean solid

  - For incompressible materials, the neo-Hookean equation is
    \[T_{ij} = -p \delta_{ij} + 2C_1 B_{ij}\]

  - Where, for consistency with Hooke&rsquo;s Law, \(2 C_1 = \mu\)

  - When large tensile strains are not important, the neo-Hookean model
    is popular because it only needs one material constant, which has
    more physical meaning than Mooney-Rivlin constants.

<span>helmholtz free energy</span>

  - Large deformation constitutive laws are generally formulated from an
    energy framework

  - From thermodynamics, it can be shown that the second Piola-Kirchhoff
    stress is the partial derivative of the Helmholtz free energy with
    respect to the Green strain
    \[\tilde{T}_{ij} = \rho_0 \frac{\partial \Psi}{\partial E_{ij}}\]

  - The Helmholtz free energy has both thermal and mechanical strain
    energy components, but in general we neglect the thermal portion,
    and use \(W\) to represent the mechanical work done (with density
    included) \[\tilde{T}_{ij} = \frac{\partial W}{\partial E_{ij}}\]
