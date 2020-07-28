<span>upcoming schedule</span>

  - 12 Nov - Newtonian Fluids

  - 14 Nov - Reynolds Transport Theorem

  - 19 Nov - Viscoelastic Materials

  - 21 Nov - No class (thanksgiving)

# flow conditions

<span>nonslip</span>

  - A common assumption is that of *nonslip* boundaries

  - Agrees well with experiments

  - Both Newtonian and non-Newtonian fluids

  - Fluid moves with boundary, for rigid boundaries the velocity at the
    boundary is 0

<span>streamline</span>

  - In general, fluid flow is characterized by a velocity field

  - As a vector field, there are different ways in which to visualize
    the field

  - Streamlines, pathlines, streaklines and timelines are common ways we
    talk about fluids

<span>steady and unsteady flow</span>

  - A flow is called *steady* if it is fixed in time (at a fixed
    location)

  - Otherwise it is called unsteady

  - Steady flow does not mean the material derivative is zero
    (\(D\Psi/Dt \ne 0\))

  - But it does mean that the partial derivative with respect to time is
    zero (\(\partial \Psi / \partial t = 0\))

  - For steady flow, streamlines, streaklines, and pathlines are the
    same

<span>streamline</span>

  - A streamline is a curve which is instantaneously tangent to the
    velocity vector

  - Experimentally, streamlines can be found on the surface of a fluid
    by sprinkling reflective particles and making a short-time exposure
    photograph

  - Mathematically, streamlines can be found by considering a parametric
    equation for a curve \(x_i = x_i(s)\)

  - We choose \(s\) so that \(dx_i/ds = v_i\) and \(s=0\) corresponds to
    the point \(x_0\), which is the originating point of our streamline

<span>streamline example</span>

  - Given the velocity field
    \[v_i = \langle \frac{kx_1}{1+\alpha t}, kx_2, 0 \rangle\] find the
    streamline passing through \((a_1,a_2,a_3)\) at time \(t\)

<span>pathline</span>

  - A pathline is the path traversed by a fluid particle

  - Experimentally, pathlines can be found by using one reflective
    particle and a long-time exposure photograph

  - Mathematically, the pathline can be obtained from the velocity field
    as follows \[\begin{aligned}
            \frac{dx_i}{dt} &= v_i(x_i,t)\\
            x_i(t_0) = X_i
            \end{aligned}\]

<span>pathline example</span>

  - Given the velocity field
    \[v_i = \langle \frac{kx_1}{1+\alpha t}, kx_2, 0 \rangle\] find the
    pathline passing through \((a_1,a_2,a_3)\) at time \(t\)

<span>streakline</span>

  - Streaklines are commonly found experimentally, but are difficult to
    express mathematically

  - A streakline is formed when dye is steadily injected into a fluid
    from a fixed point

  - The path that the very first point of dye follows is a pathline

  - But the dye following behind is altered by the changing flow field,
    which makes the streakline left by the continuously injected dye
    different from a pathline

<span>timeline</span>

  - The final common method for visualizing fluid flows is known as a
    timeline

  - Fluid particles are marked at a given instance of time (often
    forming a line at \(t_0\))

  - After set intervals of time, lines are drawn between these particles

  - These lines are called timelines

<span>animation</span>

<span>laminar flow</span>

  - Laminar flow is very orderly

  - Fluid particles move in smooth layers (*laminae*)

  - Occurs when fluid flow is relatively slow

<span>reynolds number</span>

  - Dimensionless parameter to compare how "fast" or "slow" a fluid is
    moving

  - For experiments under otherwise identical conditions, reynolds
    number is used to determine whether flow will be laminar

  - Ratio of inertial forces to viscous forces

  - In a tube, Reynolds number is \[N_R = \frac{v_m \rho d}{\mu}\]

  - For water in a tube, \(N_R < 2100\) gives laminar flow

<span>turbulent flow</span>

  - In laminar flow, small perturbations are quickly overcome

  - For turbulent flow, unsteady vortices appear and interact with each
    other

  - Turbulent flows are highly irregular and chaotic

  - Turbulence increases diffusivity, causing fluids to mix more quickly

  - High Reynolds numbers correspond to turbulence, but how high depends
    on the specific experiment

  - There is often a large transition range between laminar and
    turbulent flow

# flow models

<span>plane couette flow</span>

![Plane Couette flow](../Figures/f06-11-01-H8560.jpg)

  - Steady unidirectional flow of an incompressible fluid between two
    horizontal plates with no pressure gradient in the flow direction is
    known as plane Couette flow

  - one plate is fixed and the other moves with a constant velocity
    \(v_0\)

  - From the continuity equation \[v_i = \langle v(x_2), 0, 0 \rangle\]

  - From Navier-Stokes we find \[v(x_2) = \frac{v_0 x_2}{d}\]

<span>plane poiseuille flow</span>

  - Steady, unidirectional flow between two fixed plates

  - Initial form for \(v_i\) is same as plane Couette flow

  - Navier-Stokes gives \[\begin{aligned}
                \frac{\partial p}{\partial x_1} &= \mu \frac{d^2 v}{dx_2^2}\\
                \frac{\partial p}{\partial x_2} &= 0\\
                \frac{\partial p}{\partial x_3} &= 0
                \end{aligned}\]

![plane Poiseuille flow](../Figures/f06-12-01-H8560.jpg)

<span>hagen-poiseuille flow</span>

  - Steady, unidirectional axisymmetric flow in a circular cylinder
    \[v_r = v_\theta = 0, \qquad v_z = v(r)\]

  - From the Navier-Stokes equations, we find \[\begin{aligned}
            \frac{\partial p}{\partial r} &= 0\\
            \frac{\partial p}{\partial \theta} &= 0\\
            -\frac{\partial p}{\partial z} + \mu \left[\frac{1}{r} \frac{d}{dr}\left(r\frac{dv}{dr}\right)\right] &= 0
            \end{aligned}\]

<span>example</span>

  - Find the velocity field if there are two fluids (in layers) in plane
    couette flow
    
    ![Two fluids in plane couette flow](../Figures/f06-14-01-H8560.jpg)

<span>couette flow</span>

  - Laminar, steady flow of an incompressible fluid between two rotating
    coaxial cylinders is called Couette flow

  - The velocity field has the form
    \[v_r = 0, \qquad v_\theta = v(r), \qquad v_z = 0\]

  - Continuity is automatically satisfied, Navier-Stokes gives
    \[\frac{d^2v}{dr^2} + \frac{1}{r}\frac{dv}{dr}-\frac{v}{r^2} = 0\]

![couette flow](../Figures/f06-15-01-H8560.jpg)

<span>oscillating plane</span>

  - Flow near an oscillating plane will have the form
    \[v_i = \langle v(x_2,t), 0, 0 \rangle\]

  - The only non-trivial Navier-Stokes equation gives
    \[\rho \frac{\partial v}{\partial t} = \mu \frac{\partial ^2 v}{\partial x_2^2}\]

  - Which has the solution
    \[v = ae^{-\beta x_2} \cos (\omega t - \beta x_2 + \epsilon)\]

# experimental rheology

<span>rotational cylinder</span>

![rotating cylinder viscometer](../Figures/rotating_cylinder.png)

<span>rotational cylinder</span>

  - Couette flow with one of the cylinders fixed

  - Shear rate is applied through a constant angular velocity of one of
    the cylinders

  - Torque on the other cylinder is measured

  - Used for fluids with very low viscosity

<span>cone and plate</span>

![Cone and plate rheometer](../Figures/Cone_and_plate.jpg)

<span>cone and plate</span>

  - One of the two plates is held fixed and torque is measured

  - The other rotates at an applied angular velocity

  - Cones are used to provide a constant shear rate, also use less fluid
    volume

  - Parallel plates are more flexible in the spacing, also used for very
    temperature-sensitive tests

<span>capillary rheometer</span>

![capillary rheometer](../Figures/capillary-rheometer-1.jpg)

<span>capillary rheometer</span>

  - Used for testing higher shear-rates than rotational rheometers

  - Commonly used for polymers (which are non-newtonian and have
    rate-dependent viscosity)

  - Usually flow-rate is controlled and pressure drop is measured (but
    either can be controlled)

  - Flow-rate can be converted to find the shear-rate, pressure drop can
    be converted to shear stress

<span>dynamic</span>

  - For materials which are viscoelastic, dynamic tests are used

  - Either an oscillating rotational rheometer (for more liquid)

  - Or an oscillating tensile test (for more elastic materials)

<span>extensional rheometry</span>

![extensional rheometry](../Figures/extensional.jpg)

<span>extensional rheometry</span>

  - Another common test for polymer melts and viscoelastic materials

  - Extensional viscosity is a function of both the applied stretch rate
    and the total deformation of the material

  - Extrusion-based processes depend on extensional viscosity

<span>reading</span>

  - pp 375-402
