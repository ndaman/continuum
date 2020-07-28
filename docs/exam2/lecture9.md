<span>upcoming schedule</span>

  - 24 Sep - Stress Lecture

  - 26 Sep - Elastic Solid, HW4 Due

  - 1 Oct - Elastic Solid

  - 3 Oct - Elastic Solid, HW5 Due

### outline

\[sections numbered\]

# linear momentum and static equilibrium

<span>linear momentum</span>

  - From the principle of linear momentum, we know that \(F=ma\)

  - If we consider some internal body force, \(B\), and use the
    knowledge that tractions on opposing faces must be equal, we find
    (in Cartesian coordinates) \[T_{ij,j} + \rho B_i = \rho a_i\]

  - These are known as Cauchy&rsquo;s equations of motion

  - For a body to be in static equilibrium \(a_i = 0\)

<span>static equilibrium</span>

  - Most of the time, we will deal with bodies which are not in motion,
    and can use the condition of static equilibrium
    \[T_{ij,j} + \rho B_i = 0\]

  - In some cases, the body forces (usually gravity) are negligible
    compared with other forces acting on a body

  - In invariant form, we can write this as
    \[\text{div} T_{ij} + \rho B_i = \rho a_i\] which is valid in any
    coordinate system

<span>example</span>

  - Is the following stress distribution in static equilibrium?
    \[T_{ij} = \begin{bmatrix}
            x_2^2 + \nu (x_1^2 - x_2^2) & -2\nu x_1 x_2 & 0\\
            -2\nu x_1 x_2 & x_1^2 + \nu (x_2^2 - x_1^2) &  0\\
            0 & 0 & \nu(x_1^2 + x_2^2)
            \end{bmatrix}\]

<span>boundary conditions</span>

  - In most problems, we don&rsquo;t know anything about the internal
    stress state, but we do know what is applied on the surface

  - We apply these as traction boundary conditions, which can be used to
    find the internal stress tensor

  - If a surface is "free" with no boundary or force constraints, it is
    a traction-free boundary condition

<span>example</span>

  - Suppose a cylinder has a variable density given by \(\rho = r^2\)

  - Find the state of stress from gravity in these conditions

<span>example</span>

  - There is no traction along the outer surfaces

  - Using Cauchy&rsquo;s stress theorem with the normal
    \(n = \langle 1, 0, 0 \rangle\) we can find \[\begin{aligned}
            t_j &= \sigma_{ij} n_i\\
            &= \langle \sigma_{rr}n_r + \sigma_{r\theta} n_\theta + \sigma_{rz} n_z, \sigma_{\theta r}n_r + \sigma_{\theta \theta} n_\theta + \sigma_{\theta z} n_z, \sigma_{zr}n_r + \sigma_{z\theta} n_\theta + \sigma_{zz} n_z\rangle \\
            &= \langle \sigma_{rr}, \sigma_{\theta r}, \sigma_{z r} \rangle
            \end{aligned}\]

  - And choosing another normal, we find

  - \(\sigma_{r} = \sigma_{r \theta} = \sigma_{\theta} = \sigma_{rz} = \sigma_{\theta_z} = 0\)

  - We can also find that \(\sigma_z = 0\) at the free surface

<span>example</span>

  - Since gravity only acts in the \(z\)-direction, we make the
    assumption that all stress functions be functions of \(z\) only

  - To find the stress in the \(z\) direction, we use the third
    equilibrium equation
    \[\frac{\partial \tau_{r z}}{\partial r} + \frac{1}{r} \frac{\partial \tau_{\theta z}}{\partial \theta} + \frac{\partial \sigma_z}{\partial z} + \frac{1}{r}\tau_{rz} + \rho B_z = 0\]

  - We can substitute known values to find that
    \[\frac{\partial \sigma_z}{\partial z} + r^2 g = 0\]

<span>example</span>

  - Since we desire to find the stress at any point, we introduce a
    variable to indicate the coordinate of our free body diagram cut

<span>example</span>

  - We integrate over this free body to find \[\begin{aligned}
            \sigma_z &=  -\int_L^z r^2 g dz\\
            &= r^2 g (L-z)
            \end{aligned}\]

  - In this case, the stress is a function of radial distance (just like
    the body force was)

# piola kirchoff stress tensors

<span>piola kirchoff stress tensors</span>

  - The Cauchy stress tensor is based on the differential area at the
    current position (deformed state)

  - The first and second Piola Kirchoff stress tensors are based on the
    undeformed area

  - Equations of motion can be formulated in either the deformed or
    un-deformed configuration, based on which is more convenient for a
    given problem

  - For large deformation problems, whether the rate of deformation
    tensor \(D_{ij}\), \(D F_{ij}/ Dt\), or \(D E_{ij}^*/Dt\) is used
    facilitates the use of Cauchy or one of the Piola Kirchoff Stress
    tensors

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

# equations of motion

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
