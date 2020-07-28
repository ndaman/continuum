<span>upcoming schedule</span>

  - 19 Nov - Dissipation and Vorticity

  - 21 Nov - No class (thanksgiving)

  - 26 Nov - Reynolds Transport Theorem, Viscoelastic Materials

# energy, rotation, and vorticity

<span>energy dissipation</span>

  - Fluids can be used to dissipate energy

  - <https://www.youtube.com/watch?v=b59Twm_d-K8>

  - We can use the concept of stress power to find the energy dissipated
    in a fluid

<span>incompressible newtonian fluid</span>

  - For an incompressible Newtonian fluid, we have
    \[T_{ij} = -p \delta_{ij} + T^\prime_{ij}\]

  - If we multiply both sides by the velocity gradient, \(v_{i,j}\), we
    find \[T_{ij}v_{i,j} = -p v_{i,i} + T^\prime_{ij} v_{i,j}\]

  - But for an incompressible fluid, we know that \(v_{i,i} = 0\),
    therefore \[\label{eq:str_power}
            T_{ij}v_{i,j} = T^\prime_{ij} v_{i,j}\]

<span>incompressible newtonian fluid</span>

  - Note that \(T_{ij}v_{i,j} = T_{ij}(D_{ij}+W_{ij})\)

  - Since \(T_{ij}\) is symmetric and \(W_{ij}\) is antisymmetric, we
    find that \(T_{ij}v_{i,j} = T_{ij}D_{ij}\), which is an expression
    for stress power

  - The right sight of ([\[eq:str\_power\]](#eq:str_power)) can be
    written as
    \[T^\prime_{ij} v_{i,j} = 2\mu D_{ij} v_{i,j} = 2\mu D_{ij}(D_{ij}+W_{ij})\]

  - But \(D_{ij}W_{ij}=0\), since \(D_{ij}\) is symmetric and \(W_{ij}\)
    is antisymmetric

<span>incompressible newtonian fluid</span>

  - Thus the stress power is given as
    \[P_s = 2\mu D_{ij} D_{ij} = 2\mu (D_{11}^2+D_{22}^2+D_{33}^2+2D_{12}^2+2D_{13}^2+2D_{23}^2)\]

  - This represents the work done per unit volume to change the shape

  - Is also known as the dissipation function for an incompressible
    Newtonian fluid

<span>compressible newtonian fluid</span>

  - For a compressible Newtonian fluid, the continuity equation does not
    reduce as conveniently

  - Recall that for a compressible Newtonian fluid
    \[T_{ij}^\prime = \lambda D_{kk} \delta_{ij} + 2\mu D_{ij}\]

  - Where \(D_{kk} = v_{i,i}\)

  - Multiplying both sides of the constitutive equation as before, we
    find the stress power to be
    \[P_s = -p v_{i,i} + \lambda v_{i,i}^2 + 2\mu D_{ij}D_{ij}\]

<span>compressible newtonian fluid</span>

  - From the equation for \(P_s\), \(-p v_{i,i}\) represents the work
    done to change the volume of the fluid

  - \(\lambda v_{i,i}^2 + 2\mu D_{ij}D_{ij}\) represents the rate at
    which work is converted to heat

  - This is known as the dissipation function for compressible Newtonian
    fluids

<span>energy equation</span>

  - Recall that the energy equation for a continuum is
    \[\rho \frac{D u}{Dt} = T_{ij} v_{i,j} - q_{i,i} + \rho q_s\]

  - We see that the change in energy is related to the stress power,
    plus heat which enters the continuum from internal or external
    sources

<span>energy equation</span>

  - In fluids the internal energy is often express as \(u = c \Theta\),
    where \(c\) is the specific heat and \(\Theta\) is the temperature

  - If we assume that the only heat transfer follows Fourier&rsquo;s law
    (and there is no internal heat source) we find
    \[\rho c \frac{D \Theta}{Dt} = P_s + \kappa \frac{\partial ^2 \Theta}{\partial x_j \partial x_j}\]

<span>example</span>

  - As an example, we can consider plane Couette flow with prescribed
    temperatures at the boundaries

  - Use the energy equation to find the steady-state temperature
    distribution

<span>vorticity vector</span>

  - We know that \(W_{ij}\) is the antisymmetric part of the velocity
    gradient

  - We also know that antisymmetric tensors can be expressed as some
    dual vector such that \[W x = \omega \times x\]

  - Where the angular velocity vector, \(\omega\) is given by
    \[\omega_i = -\langle W_{23}, W_{31}, W_{12} \rangle\]

<span>vorticity vector</span>

  - The angular velocity vector can be expressed directly in terms of
    components of the velocity gradient
    \[\omega = \frac{1}{2} \langle v_{3,2} - v_{2,3}, v_{1,3}-v_{3,1}, v_{2,1}-v_{1,2} \rangle\]

  - The vorticity vector is defined to eliminate the \(1/2\) from the
    angular velocity vector
    \[\zeta = 2\omega = \langle v_{3,2} - v_{2,3}, v_{1,3}-v_{3,1}, v_{2,1}-v_{1,2} \rangle\]

  - In index notation, we can write \[\zeta = \epsilon_{ijk} v_{k,j}\]

  - Or in direct notation \(\zeta = \text{curl } v\)

<span>irrotational flow</span>

  - If the vorticity vector is zero, the flow is considered irrotational

  - If we consider some function \(\varphi(x_1,x_2,x_3,t)\) and derive
    the velocity field from that function such that
    \[v_i = -\frac{\partial \varphi}{\partial x_i}\]

  - We find that the vorticity vector will be zero

<span>irrotational flow</span>

  - For an incompressible fluid, we know that \(v_{k,k} = 0\)

  - Substituting \(\varphi\) into this equation gives the Lapplacian
    equation
    \[\frac{\partial^2 \varphi}{\partial x_j \partial x_j} = 0\]

<span>inviscid incompressible flow</span>

  - If viscosity is 0 (or negligible), the equations of motion reduce to
    \[\rho \left(\frac{\partial v_i}{\partial t} + v_j \frac{\partial v_i}{\partial x_j}\right) = -\frac{\partial p}{\partial x_i} + \rho B_i\]

  - These are known as Euler&rsquo;s equations of motion

  - If \(rho\) is constant and body forces are express as
    \[B_i = - \frac{\partial \Omega}{\partial x_i}\] then we can write
    \[\frac{\partial v_i}{\partial t} + v_j \frac{\partial v_i}{\partial x_j} = - \frac{\partial }{\partial x_i} \left(\frac{p}{\rho} + \Omega\right)\]

<span>inviscid incompressible flow</span>

  - For irrotational flow, the velocity gradient will be symmetric
    \[v_j \frac{\partial v_i}{\partial x_j} = v_j \frac{\partial v_j}{\partial x_i} = \frac{1}{2}\frac{\partial}{\partial x_i}(v_jv_j)\]

  - We now let \(v^2 = v_iv_i\) and write
    \[\frac{\partial}{\partial x_i} \left(-\frac{\partial \varphi}{\partial t} + \frac{v^2}{2} + \frac{p}{\rho} + \Omega\right) = 0\]

<span>inviscid incompressible flow</span>

  - The portion inside the parenthesis must be a function of time only

  - For steady flow, it will be equal to a constant and the \(\varphi\)
    term will vanish \[\frac{v^2}{2} + \frac{p}{\rho} + \Omega = C\]

  - This is Bernoulli&rsquo;s equation, and shows that irrotational
    flows are always possible when density is constant in an inviscid,
    incompressible flow

# compressible flow

<span>compressible flow</span>

  - For a compressible fluid, we still need the pressure \(p\) to not be
    a function of deformation rate

  - The pressure will be some function of density and temperature

  - For example, ideal gases will follow the ideal gas law
    \(p = R\rho \Theta\)

  - The constitutive equation for a compressible Newtonian fluid are
    \[T_{ij} = -p(\rho, \Theta) \delta_{ij} + \lambda \frac{\partial v_k}{\partial x_k} \delta_{ij} + 2\mu D_{ij}\]

  - And the contraction of that is
    \[T_{ii}/3 = -p(\rho, \Theta) + k \frac{\partial v_k}{\partial x_k}\]
    where \(k=\lambda + \frac{2}{3}\mu\) (the bulk viscosity)

<span>compressible flow</span>

  - Some gases have zero bulk viscosity

  - The assumption that \(k=0\) is known as the Stokes assumption, valid
    for monatomic gases

  - We can also write the constitutive equation in terms of \(\mu\) and
    \(k\)
    \[T_{ij} = -p(\rho, \Theta) \delta_{ij} + \lambda \frac{\partial v_k}{\partial x_k} \delta_{ij} + 2\mu D_{ij}\]

<span>compressible flow</span>

  - The Navier-Stokes equations are
    \[\rho \frac{D v_i}{Dt} = -\rho B_i - \frac{\partial P}{\partial x_i} + \frac{\mu}{3} \frac{\partial }{\partial x_i}\left(\frac{\partial v_j}{\partial x_j}\right) + \mu \frac{\partial ^2 v_i}{\partial x_j \partial x_j} + k \frac{\partial}{\partial x_i} \left(\frac{\partial v_j}{\partial x_j}\right)\]

  - And the energy equation is
    \[\rho \frac{D u}{Dt} = T_{ij} \frac{\partial v_i}{\partial x_j} + \kappa \frac{\partial ^2 \Theta}{\partial x_j \partial x_j}\]

  - We also recall the continuity equation
    \[\frac{D \rho}{Dt} + \rho \frac{\partial v_j}{\partial x_j} = 0\]

  - Together with some equation \(p = p(\rho, \Theta)\) and
    \(u = u(\rho,\Theta)\) gives 7 equations

  - The 7 unknowns are \(v_i\), \(p\), \(\rho\), \(\Theta\), and \(u\)

<span>acoustic waves</span>

  - Let us consider the propagation of sound in an inviscid fluid with
    negligible body forces

  - The equations of motion reduce to
    \[\frac{\partial v_i}{\partial t} + v_j \frac{\partial v_i}{\partial x_j} = -\frac{1}{\rho} \frac{\partial p}{\partial x_i}\]

  - If the fluid is initially at rest (\(v_i=0, \rho = \rho_0, p=p_0\))
    with some perturbation such that
    \[v_i = v_i^\prime(x_i,t) \qquad \rho = \rho_0 + \rho^\prime(x_i,t) \qquad p = p_0 + p^\prime(x_i,t)\]

  - Substituting gives \[\label{eq:navier}
            \frac{\partial v_i^\prime}{\partial t} + v_j^\prime \frac{\partial v_i^\prime}{\partial x_j} = -\frac{1}{\rho_0(1+\rho^\prime/\rho_0)} \frac{\partial p^\prime}{\partial x_i}\]

<span>acoustic waves</span>

  - If the disturbance is infinitesimal, then
    \(v_j^\prime \frac{\partial v_i^\prime}{\partial x_j}\) will be
    negligible compared to \(\frac{\partial v_i^\prime}{\partial t}\)
    and \(\rho^\prime/\rho_0\) will be negligible compared to 1
    \[\frac{\partial v_i^\prime}{\partial t}= -\frac{1}{\rho_0} \frac{\partial p^\prime}{\partial x_i}\]

  - Similarly the continuity equation
    \[\frac{\partial \rho^\prime}{\partial t} + v_j^\prime \frac{\partial \rho^\prime}{\partial x_j} + \rho_0(1 + \rho^\prime/\rho_0) \frac{\partial v_i^\prime}{\partial x_i} = 0\]

  - Which reduces to \[\label{eq:continuity}
            \frac{\partial v_i^\prime}{\partial x_i} = -\frac{1}{\rho_0}\frac{\partial \rho^\prime}{\partial t}\]

<span>acoustic waves</span>

  - We can differentiate &nbsp;[\[eq:navier\]](#eq:navier) with respect
    to \(x_i\) and &nbsp;[\[eq:continuity\]](#eq:continuity) with
    respect to \(t\) to eliminate velocity from both equations
    \[\frac{\partial ^2 p^\prime}{\partial x_i \partial x_i} = \frac{\partial ^2 p^\prime}{\partial t^2}\]

  - If pressure depends only on density (barotropic flow) then we can
    expand the pressure function as a Taylor series
    \[p = p_0 + \left(\frac{d p}{d\rho}\right)_{\rho_0} (\rho-\rho_0) + ...\]

  - Neglecting higher-order terms and re-arranging gives
    \[p - p_0 = \left(\frac{d p}{d\rho}\right)_{\rho_0} (\rho-\rho_0)\]

  - if we let \(c_0^2 = \left(\frac{d p}{d\rho}\right)_{\rho_0}\) then
    we can write \[p^\prime = c_0^2 \rho^\prime\]

<span>acoustic waves</span>

  - For barotropic flow this gives
    \[c_0^2 \frac{\partial^2 p^\prime}{\partial x_i \partial x_i} = \frac{\partial ^2 p^\prime}{\partial t^2}\]

  - \(c_0\) is the speed of sound at stagnation

# reynolds transport

<span>reynolds transport theorem</span>

  - Reynolds transport theorem is the general framework we use to
    convert conservation equations from "control mass" to "control
    volume"

  - Arbitrary control volume can be fixed or moving

  - "Control mass" equations are things like
    
      - Conservation of mass
    
      - \(F=ma\)
    
      - First and second laws of thermodynamics

<span>reynolds transport theorem</span>

  - In general, Reynolds Transport Theorem states that for some scalar
    or tensor function of spatial coordinates and time, \(T(x_i,t)\)

  - Where \(V_m\) is a material volume which consists of the same
    material particles at all times and \(S_m\) is the boundary of this
    volume
    \[\frac{D}{Dt} \int_{V_m(t)} T(x_i,t) dV = \int_{V_c} \frac{\partial T(x_i,t)}{\partial t} dV + \int_{S_c} T(v_i n_i) dS\]
    or
    \[\frac{D}{Dt} \int_{V_m(t)} T(x_i,t) dV = \int_{V_c} \left( \frac{D T}{D t} + T \text{div} v\right) dV\]

  - Mathematically, this gives us a framework for moving derivatives
    inside an integral

<span>conservation of mass</span>

  - The conservation of mass states that the total mass of a material
    must remain constant

  - We can write this as \[\frac{D}{Dt} \int_{V_m} \rho (x_i,t) dV = 0\]

<span>linear momentum</span>

  - We can write the global form of \(F=ma\) as
    \[\int_{S_c} t_i dS + \int_{V_c} \rho B_i dV = \frac{D}{Dt} \int_{V_m} \rho v_i dV\]

<span>examples</span>

  - rope sliding from table

  - jet of water on a curved pane

<span>moving frames</span>

  - If we define two frames, \(F_1\) and \(F_2\)

  - The position vector \(r_i\) denotes the position of some
    differential mass, \(dm\) relative to \(F_1\)

  - \(x_i\) denotes position relative to \(F_2\), we define velocity in
    the respective frames as \[\begin{aligned}
            (dr_i/dt)_{F_1} &= v_{F_1}\\
            (dx_i/dt)_{F_2} &= v_{F_2}
            \end{aligned}\]

<span>moving frames</span>

![image](../Figures/f07-07-01-H8560.jpg)
<span id="fig:f07-07-01-h8560" label="fig:f07-07-01-h8560">\[fig:f07-07-01-h8560\]</span>

<span>moving frames</span>

  - Since we can write \(r_i = R_i + x_i\), we can say that
    \[\left(\frac{dr_i}{dt}\right)_{F_1} = \left(\frac{dR_i}{dt}\right)_{F_1} + \left(\frac{dx_i}{dt}\right)_{F_1}\]

  - Which we can define as
    \[\left(\frac{dr_i}{dt}\right)_{F_1} = \left(v_0\right)_{F_1} + \left(\frac{dx_i}{dt}\right)_{F_1}\]

  - We also know that for any vector \(b_i\)
    \[\left(\frac{db_i}{dt}\right)_{F_1} = \left(\frac{db_i}{dt}\right)_{F_2} + \omega_i \times b_i\]
    where \(\omega_i\) is the angular velocity of \(F_2\) relative to
    \(F_1\)

<span>moving frames</span>

  - We find \[v_{F_1} = (v_0)_{F_1} + v_{F_2} + \omega_i \times x_i\]

  - Taking the global form we find
    \[\left(\frac{D}{Dt}\right)_{F_1} \int v_{F_1} dm = \left(\frac{D}{Dt}\right)_{F_1} \left[ \int (v_0)_{F_1} dm + \int v_{F_2} dm + \omega_i \times x_i dm \right]\]

<span>moving frames</span>

  - If \(F_1\) is the inertial frame, then we have
    \[\left(\frac{D}{Dt}\right)_{F_1} \int v_{F_1} dm = \int t_i dS + \int \rho B_i dV\]

  - And in the moving frame \[\begin{gathered}
            \left(\frac{D}{Dt}\right)_{F_2} \int v_{F_2} dm = \int t_i dS + \int \rho B_i dV - \\
            \left[m(a_0) + 2\omega \times \int v_{F_2} + \dot{\omega} \times \int x_i dm + \omega \times \left(\omega \times \int x_i dm \right)\right]
            \end{gathered}\]

  - Where \(a_0\) is the acceleration of the moving frame with respect
    to the inertial frame

<span>reading</span>

  - Linear Viscoelasticity - 443-456
