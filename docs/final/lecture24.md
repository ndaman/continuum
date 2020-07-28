<span>upcoming schedule</span>

  - 28 Nov - SPTE, Reynolds Transport

  - 30 Nov - Viscoelastic Materials

  - 5 Dec - Viscoelastic Materials

  - 7 Dec - Homework 10 Due, Final Review

  - 14 Dec - Final Exam 3:00 - 4:50

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

<span>acoustic waves</span>

  - if we let \(c_0^2 = \left(\frac{d p}{d\rho}\right)_{\rho_0}\) then
    we can write \[p^\prime = c_0^2 \rho^\prime\]

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
