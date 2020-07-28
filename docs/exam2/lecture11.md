<span>upcoming schedule</span>

  - 1 Oct - Elastic Solid

  - 3 Oct - Elastic Solid, HW5 Due

  - 8 Oct - Elastic Solid

  - 10 Oct - Elastic Solid

### outline

\[sections numbered\]

# plane of maximum shear

<span>plane of maximum shear</span>

![image](../Figures/f04-06-01-H8560.jpg)
<span id="fig:f04-06-01-h8560" label="fig:f04-06-01-h8560">\[fig:f04-06-01-h8560\]</span>

<span>plane of maximum shear</span>

  - Table 4.1 gives the planes (relative to the principal directions)
    for maximum shear stress

  - Which pair of planes corresponds to the maximum depends which of the
    stable values is the maximum

  - Use rotation matrix from principal directions to rotate back into
    global frame

# corotational derivative

<span>corotational derivative</span>

  - Note: textbook addresses co-rotational derivative on pp. 483-486

  - Rigid body rotations can cause problems when taking derivatives

  - In our last example, the stress rotated from the \(1\) direction to
    the \(2\) direction, thus we can see that
    \(\dot{\sigma_{ij}} \ne 0\)

  - However, the rate of deformation tensor, \(D_{ij}\) is zero because
    there is no deformation

<span>material indifference</span>

  - We have many different stress (Cauchy, Piola-Kirchhoff) and strain
    (right and left Cauchy, Lagrangian, Eulierian) tensors

  - A proper constitutive equation should be invariant under
    transformation \[T_{ij}^* = Q_{im}(t) T_{mn} Q_{jn}(t)\]

  - This dictates which stress and strain tensors can be related in a
    constitutive equation

  - We can show that the Right Cauchy-Green strain tensor should not be
    used with the Cauchy Stress tensor

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

<span>corotational derivative</span>

  - If we now take the material derivative we find
    \[\dot{\sigma}_{ij} = -\frac{\dot{J}}{J^2} F_{im} C_{mnop} E_{op} F_{jn} + \frac{1}{J} \dot{F}_{im} C_{mnop} E_{op} F_{jn} + \frac{1}{J} F_{im} C_{mnop} \dot{E}_{op} F_{jn} + \frac{1}{J} F_{im} C_{mnop} E_{op} \dot{F}_{jn}\]

  - We can now substitute several identities,
    \(\frac{\dot{J}}{J} = D_{ii}\), \(\dot{F}_{ij} = v_{i,m} F_{mj}\),
    and \(\dot{E}^*_{ij} = F_{mi} D_{mn} F_{nj}\) to find
    \[\begin{gathered}
            \dot{\sigma}_{ij} = \frac{1}{J} \left[-D_{kk} F_{im} C_{mnop} E_{op} F_{jn} + v_{i,k}F_{km} C_{mnop} E_{op} F_{jn} + \right.\\
            \left. F_{im} C_{mnop} F_{ko}D_{kl}F_{lp} F_{jn} + F_{im} C_{mnop} E_{op} F_{kj} v_{n,k}\right]
            \end{gathered}\]

<span>corotational derivative</span>

  - Now we recall (&nbsp;[\[eq:cauchy\]](#eq:cauchy)) to simplify things
    somewhat
    \[\dot{\sigma}_{ij} = -D_{kk} \sigma_{ij} + v_{i,k}\sigma_{kj} + \sigma_{ik} v_{j,k} + \frac{1}{J}F_{im} C_{mnop} F_{ko}D_{kl}F_{lp} F_{jn}\]

  - This is often written as
    \[\dot{\sigma}_{ij} -  v_{i,k}\sigma_{kj} - \sigma_{ik} v_{j,k} = -D_{kk} \sigma_{ij} + \frac{1}{J}F_{im} C_{mnop} F_{ko}D_{kl}F_{lp} F_{jn}\]

  - The left hand side is called the Lie Derivative, and is usually
    written as \(\accentset{\nabla}{\sigma}_{ij}\)

  - \(D_{kk} \approx 0\) in almost all cases, and is usually neglected

  - We also define
    \(C^\prime_{ijkl} \equiv  \frac{1}{J}F_{im} F_{jn} C_{mnop} F_{ko} F_{lp}\)
    to find
    \[\accentset{\nabla}{\sigma}_{ij} = C^\prime _{ijkl} D_{kl}\]

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

<span>example</span>

  - Calculate \(\dot{\sigma}_{ij}\) and \(\mathring{\sigma}_{ij}\) for
    an object under constant stress \[\sigma = \begin{bmatrix}
            20 & 0 \\ 0 & 0
            \end{bmatrix}\]

  - With 2D rotation of \[R = \begin{bmatrix}
            \cos \theta &-\sin \theta\\ \sin \theta & \cos \theta
            \end{bmatrix}\] and \[\dot{R} = \omega\begin{bmatrix}
            -\sin \theta & -\cos \theta\\ \cos \theta & -\sin \theta
            \end{bmatrix}\]

# heat, energy, and entropy

<span>heat</span>

  - Let \(q_i\) be the vector whose magnitude gives the rate of heat
    flow across a unit area and whose direction indicates the direction
    of heat flow

  - The net flow of heat into a differential element is
    \[Q = -q_{i,i} dV\]

  - Using the Fourier heat conduction law in steady state conditions we
    find \[q_i = -\kappa \nabla \Theta\]

  - In steady state conditions, no should be no net rate of heat flow,
    which produces the governing Laplace equation
    \[\nabla^2 \Theta = 0\]

<span>energy</span>

  - If we consider only the energy contributions from strain energy,
    kinetic energy, and heat

  - by the conservation of energy, the rate of increase in energy for a
    particle equals the rate of work done plus the heat added
    \[\frac{D}{Dt}(U + KE) = P + Q_c + Q_s\]

  - Where \(P = \frac{D}{Dt}(KE) + T_{ij} v_{i,j}dV\) and
    \(Q_c = -q_{i,j}dV\)
    \[\frac{D U}{Dt} = T_{ij} v_{i,j}dV -q_{i,j}dV + Q_s\]

  - This is also sometimes written as energy per unit mass as
    \[\rho \frac{D u }{Dt} = T_{ij} v_{i,j} - q_{i,j} + \rho q_s\]

<span>entropy inequality</span>

  - Let \(\eta(x_i,t)\) denote the entropy per unit mass

  - The rate of entropy following a particle is
    \[\frac{D}{Dt}(\rho \eta dV) = \rho dV \frac{D \eta}{Dt} + \eta \frac{D}{Dt} (\rho dV) = \rho dV \frac{D \eta}{Dt}\]

  - The entropy inequality states that the rate of increase of entropy
    is always greater than or equal to the entropy inflow plus the
    entropy supply
    \[\rho \frac{D \eta}{Dt} \ge -\text{div} \left(\frac{q}{\Theta}\right) + \frac{\rho q_s}{\Theta}\]

<span>helmholtz energy function</span>

  - The Helmholtz energy function is defined as \[A = u - \Theta \eta\]

  - We can use this relationship to re-write the entropy inequality as
    \[-\left(\rho \frac{D A}{Dt} + \rho\eta \frac{D \Theta}{Dt}\right) + T_{ij}D_{ij}-\frac{q_i}{\Theta}\frac{\partial \Theta}{\partial x_i} \ge 0\]

# integral formulation

<span>integral formulation</span>

  - To this point, we have derived field equations using the
    differential element approach (this is sometimes referred to as
    local principles)

  - When can also formulate these principles globally by integrating
    over the volume. If the functions are smooth, these two methods will
    be equivalent

  - In certain problems the integral formulation may be more convenient,
    or more numerically accurate when solving problems numerically

<span>conservation of mass</span>

  - The conservation of mass states that the rate of increase of mass in
    a fixed part of a material is zero \[\begin{aligned}
            \frac{D}{Dt} \int_{V_m} \rho dV &= 0\\
            \int_{V_m} \frac{D}{Dt} (\rho dV) &= 0\\
            \int_{V_m} dV \frac{D}{Dt}\rho + \rho \frac{D}{Dt} dV &= 0
            \end{aligned}\]

<span>conservation of mass</span>

  - We previously found that \(D_{ii}\) is related to the rate of change
    of the volume, which we can write in terms of the velocity gradient
    as \[\frac{D dV}{Dt} = v_{i,i} dV\]

  - We can substitute this to find
    \[\int_{V_m} dV \frac{D}{Dt}\rho + \rho v_{i,i} dV = 0\]

  - Since this must be true for any volume, we find
    \[\frac{D}{Dt}\rho + \rho v_{i,i} = 0\]

# linear elasticity

<span>mechanical properties</span>

  - Work-hardening

  - Young&rsquo;s modulus

  - Poisson&rsquo;s ratio

  - Isotropic vs. anisotropic

  - Homogeneous vs. inhomogeneous

  - Bulk Modulus

  - Shear Modulus

<span>linear elasticity</span>

  - In linear elasticity we make the following assumptions
    
    1.  Load deformation relationship is linear
    
    2.  Load rate/strain rate do not change results
    
    3.  Completely elastic
    
    4.  Small deformations

  - In this case we can use Hooke&rsquo;s Law
    \[T_{ij} = C_{ijkl} E_{kl}\]

  - Although there are 81 terms in the stiffness tensor (\(3^4\)), only
    21 of them are unique

  - The symmetry of the stress and strain tensors, as well as the
    requirement that the strain energy function be positive definite
    reduces number of unique terms

<span>isotropic tensor</span>

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

<span>lam&eacute; constants</span>

  - We already know that the ratio of applied stress to strain in a
    uniaxial test is the Young&rsquo;s modulus
    \[E_Y = \frac{T_{11}}{E_{11}} = \frac{\mu(3\lambda + 2\mu)}{\lambda + \mu}\]

  - The Poisson&rsquo;s ratio is defined as the ratio of transverse
    strain to axial strain
    \[\nu = -\frac{E_{22}}{E_{11}} = \frac{\lambda}{2(\lambda + \mu)}\]

# equations of motion

<span>infinitesimal deformation</span>

  - For infinitesimal deformations, \(x_i \approx X_i\), so we find that
    \[a_i = \frac{\partial ^2 u_i}{\partial t^2}\]

  - Thus we find the equations of motion for small strains to be
    \[\rho_0 \frac{\partial ^2 u_i}{\partial t^2} = \rho_0 B_i T_{ij,j}\]

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

<span>principle of superposition</span>

  - Since Hooke&rsquo;s Law and the strain displacement relations are
    linear, we can add two separate solutions

  - This is known as the principle of superposition
    \[\rho_0 \frac{\partial^2}{\partial t^2} \left(u_i^{(1)}+u_i^{(2)}\right) = \rho_0 \left(B_i^{(1)}+B_i^{(2)}\right) + \frac{\partial}{\partial x_j} \left(T_{ij}^{(1)}+T_{ij}^{(2)}\right)\]

<span>suggested reading</span>

  - Next lecture we will discuss waves and some simple elasticity
    problems

  - Textbook pp 218 - 279
