<span>upcoming schedule</span>

  - 30 Nov - Viscoelastic Materials

  - 5 Dec - Viscoelastic Materials

  - 7 Dec - Homework 10 Due, Final Review

  - 14 Dec - Final Exam 3:00 - 4:50

### outline

\[sections numbered\]

# non-newtonian fluids

<span>non-newtonian fluids</span>

  - For a fluid to be Newtonian we assumed that \(T_{ij}^\prime\) is
    linearly dependent on \(D_{ij}\) and nothing else

  - In many fluids \(T_{ij}^\prime\) is not linearly dependent on
    \(D_{ij}\)

  - These fluids are most commonly referred to as shear-thinning or
    shear-thickening fluids

  - Their viscosity is a function of the strain-rate applied

<span>shear thinning fluids</span>

  - Shear-thinning fluids decrease in viscosity with an increase in
    strain-rate

  - Some examples are ketchup, paint, whipped cream, quicksand and blood

  - Shear-thinning is generally only an effect in complex fluids
    (polymers and solutions)

  - At the molecular level, research is still being done to discover why
    a fluid would be shear-thinning

<span>shear-thickening fluids</span>

  - Shear-thickening fluids increase viscosity with an increased
    strain-rate

  - Generally occurs in suspensions (many polymer melts are suspensions)

  - Cornstarch and water, silica and polyethylene glycol

  - Uses include body armor and brake pads

<span>generalized newtonian fluids</span>

  - Many non-newtonian fluids have a viscosity which does not depend on
    the history, only on the current shear-rate

  - In this case, the fluid can be modeled as a generalized Newtonian
    fluid \[T_{ij}^\prime = \mu (D_{ij}) D_{ij}\]

  - Some common models for \(\mu (D_{ij})\) are Power-Law, Cross, and
    Carreau

<span>linear viscoelasticity</span>

  - We discussed fluids where \(T_{ij}^\prime\) is not linearly
    dependent on \(D_{ij}\), but if \(T_{ij}^\prime\) depends on some
    other measure (such as strain), the fluid is also non-newtonian

  - Linear viscoelastic materials have a linear dependence on
    \(D_{ij}\), but also depend on \(E_{ij}\)

  - Viscoelasticity can be used to model behavior in both liquids (die
    swell in polymer melts) and solids (creep and stress relaxation)

# maxwell fluid

<span>maxwell fluid</span>

  - In general, a Maxwell fluid is defined by the constitutive equation
    \[T_{ij} = -p \delta_{ij} + S_{ij}\]

  - Where \(S\) is the "extra stress"
    \[S_{ij} + \lambda \frac{\partial S_{ij}}{\partial t} = 2 \mu D_{ij}\]

  - In 1D, a Maxwell fluid can be considered as a spring and dashpot
    connected in series

<span>maxwell fluid</span>

![image](../Figures/f08-01-01-H8560.jpg)
<span id="fig:f08-01-01-h8560" label="fig:f08-01-01-h8560">\[fig:f08-01-01-h8560\]</span>

<span>creep</span>

  - We can model the creep behavior of a 1D Maxwell fluid by considering
    a constant applied force, \(F_0\)

  - For a 1D Maxwell fluid we have
    \[F + \lambda \frac{dF}{dt} = \eta \frac{d \epsilon}{dt}\]

  - If \(F=F_0\), then \(\frac{dF}{dt}=0\) so we have
    \[F_0 = \eta \frac{d \epsilon}{dt}\]

  - So the strain will be given by
    \[\epsilon = \int \frac{F_0}{\eta} dt = \frac{F_0}{\eta}t + \epsilon_0\]

<span>creep</span>

  - Since \(\epsilon_0\) represents the initial strain, we can write
    \(\epsilon_0 = F_0/G\) where \(G\) is the spring constant

  - In shear the creep compliance is often called \(J(t)\), and
    represents the strain divided by the applied force

  - For this fluid the creep compliance function is
    \[J(t) = \frac{\epsilon}{F_0} = \frac{1}{\eta} t + \frac{1}{G}\]

<span>stress relaxation</span>

  - To model stress relaxation, we consider a constant applied strain,
    \(\epsilon_0\), and see what effect that has on the stress

  - In this case \(\frac{d \epsilon}{dt}=0\) and we have
    \[F + \lambda \frac{dF}{dt} = 0\]

  - solving this differential equation gives
    \[F = F_0 e^{-t G/\eta} = G\epsilon_0e^{-t G/\eta}\]

  - The stress relaxation function, \(\phi(t)\) is \(F/\epsilon_0\)
    which gives \[\phi(t) = Ge^{-t G/\eta}\]

<span>notation</span>

  - Creep and stress relaxation work often uses a different notation
    than what we are accustomed to

  - \(J(t)\) is shear creep compliance, \(D(t)\) is tensile creep
    compliance

  - Compliance is most commonly used, but sometimes \(G(t)\) for shear
    stiffness and \(E(t)\) for tensile stiffness are used

  - Due to the time history dependence, in general \[G(t) \ne 1/J(t)\]

<span>example</span>

  - A rod is initially 12" long and 2" in diameter

  - Find the strech after a 20 lb weight is hung for 24 hours

  - Tensile compliance is given by
    \[D = 0.5-\exp(-0.03t) \text{ Mpsi}^{-1}\]

# other viscoelastic models

<span>solids</span>

  - A Maxwell fluid has an elastic portion, but behaves mostly like a
    fluid

  - Many viscoelastic models are for solids, which have some viscous or
    damping behavior, but are mostly solid-like

  - The Kelvin-Voigt model connects a spring and dashpot in parallel,
    and is the simplest form of viscoelastic model for solids

<span>kelvin-voigt</span>

![image](../Figures/Kelvin_Voigt_diagram_svg.png)
<span id="fig:kelvinvoigtdiagram" label="fig:kelvinvoigtdiagram">\[fig:kelvinvoigtdiagram\]</span>

<span>zener model</span>

  - Both the Maxwell and Kelvin-Voigt models are overly simple to
    describe many real viscoelastic materials

  - The Zener model combines the two, it can be viewed either as a
    spring in series with a Kelvin-Voigt solid or as a spring in
    parallel with a Maxwell fluid

  - Also called a standard linear solid

  - Can be further extended for polymers with a distribution of
    relaxation times

  - Multiple Kelvin-Voigt elements are connected in series, with a
    spring connected in series

<span>zener model</span>

![image](../Figures/SLS_svg.png)
<span id="fig:sls" label="fig:sls">\[fig:sls\]</span>

# dynamic properties

<span>dynamic properties</span>

  - You have probably noticed that plastic cups do not ring as long as
    glasses or metal objects

  - This is due to the damping properties of viscoelastic materials

  - Polymers are often used to dampen vibrations for this reason

  - Damping will vary with frequency, we can model the effects

<span>dynamic properties</span>

  - If we assume some sinusoidal applied strain,
    \(\epsilon(t) = \epsilon_0 \sin \omega t\)

  - In general, the viscoelastic stress response will be out of phase
    \[\sigma = \sigma_0 \sin (\omega t + \delta)\]

  - We can re-write this as
    \[\sigma = (\sigma_0 \cos \delta) \sin \omega t + (\sigma_0 \sin \delta) \cos \omega t\]

<span>dynamic properties</span>

  - We can further re-write the equation in terms of a so-called
    "storage modulus" and "loss modulus"
    \[\sigma = \epsilon_0[ E^\prime \sin \omega t + E^{\prime \prime} \cos \omega t]\]

  - The storage modulus, \(E^\prime\) corresponds to the elastic
    response

  - The loss modulus, \(E^{\prime \prime}\) corresponds to the viscous
    response

<span>complex representation</span>

  - The dynamic response is analogous to electric circuits, and can be
    expressed in a similar fashion using a complex representation
    \[\begin{aligned}
            \epsilon^* &= \epsilon_0 \exp i \omega t\\
            \sigma^* &= \sigma_0 \exp i(\omega t + \delta)
            \end{aligned}\]

  - This gives the complex modulus as \[\begin{aligned}
            E^* &= \sigma^*/\epsilon^*\\
            &= \frac{\sigma_0 }{ \epsilon_0} \exp i \delta\\
            &= \frac{\sigma_0 }{ \epsilon_0} (\cos \delta + i \sin \delta)\\
            &= E^\prime + i E^{\prime \prime}
            \end{aligned}\]

<span>damping</span>

  - We can characterize the amount of damping in a viscoelastic material
    with \(\delta\)
    \[\tan \delta = \frac{D^{\prime \prime}}{D^\prime} = \frac{E^{\prime \prime}}{E^\prime}\]

  - When \(\delta = 0\) there is no viscous damping (most metals have
    \(\delta \approx 0\))

  - Polymers in certain temperature ranges can have \(\delta\) as high
    as \(30^\circ\)

  - Note: at the same temperature and frequency, \(E^* = 1/D^*\) and
    \(G^* = 1/J^*\)

<span>example</span>

  - Consider the same bar as before (12" long and 2" in diameter)

  - The bar is subjected to a sinusoidal force with \(F_0 = 50\) lbs and
    80 Hz. \[D^{\prime \prime} = 40 \text{ ksi}\]

<span>reading</span>

  - Linear Viscoelasticity - 443-456

  - Supplemental viscoelasticity chapter (Blackboard)

  - Next time
    
      - Temperature dependence
    
      - Boltzman superposition
    
      - Time-Temperature superposition
