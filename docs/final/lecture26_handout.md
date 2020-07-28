<span>upcoming schedule</span>

  - 5 Dec - Viscoelastic Materials

  - 7 Dec - Homework 10 Due, Final Review

  - 14 Dec - Final Exam 3:00 - 4:50

### outline

\[sections numbered\]

# dynamic properties

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

<span>complex representation</span>

  - Similarly, we can find the compliance \[\begin{aligned}
            D^* &= \epsilon^*/\sigma^*\\
            &= \frac{\epsilon_0 }{ \sigma_0} \exp (-i \delta)\\
            &= \frac{\sigma_0 }{ \epsilon_0} (\cos \delta - i \sin \delta)\\
            &= D^\prime - i D^{\prime \prime}
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
    80 Hz. \[D^{\prime \prime} = 40 \text{ ksi}^{-1}\]

# time temperature superposition

<span>temperature dependency</span>

  - In both the time and frequency domain, many viscoelastic materials
    are temperature dependent

  - In terms of our 1D models, the viscous portion is much more
    temperature dependent than the elastic portion

  - The two most common models of temperature dependence are the
    Arrhenius model and the Williams-Landel-Ferry (WLF) model

<span>time-temperature</span>

![image](../Figures/ViscoelasticTimeTemperatureDependence.png)

<span>frequency-temperature</span>

![image](../Figures/ViscoelasticFrequencyTemperatureDependence.png)

<span>temperature shift</span>

  - Both Arrhenius and WLF models us the parameter \(a_T\) as the
    temperature shift

  - \(a_T = a_T(T,T_0)\)

  - For compliance (\(J\) and \(D\)) \[J^{T_0}(t) = J^T(a_T t)\]

  - And for stiffness (\(G\) and \(E\))
    \[D^{T_0}(t) = D^{T}(\frac{t}{a_T})\]

<span>arrhenius</span>

  - The Arrhenius function only uses one curve-fit parameter
    \[a_T = \exp \left(\frac{\Delta H}{R} \left[\frac{1}{T}-\frac{1}{T_R}\right]\right)\]

  - \(R\) is the universal gas constant

  - Theoretically, \(\Delta H\) is the activation enthalpy of the
    relaxation

  - \(T\) is the temperature and \(T_0\) is the reference temperature

  - Popular model because the constants have some physical meaning, but
    they are still curve fit

<span>williams-landel-ferry</span>

  - The Williams-Landel-Ferry model is given by
    \[\log(a_T) = \frac{-C_1 (T-T_R)}{C_2 + (T-T_R)}\]

  - \(C_1\) and \(C_2\) are the curve-fit parameters

  - Most optimization algorithms perform poorly with exponential
    functions, so it is best to solve for \(\log(a_T)\)

<span>characterization example</span> rendered version of example can be
found at
<http://nbviewer.jupyter.org/github/ndaman/continuum/blob/master/tts/time-temperature-superposition.ipynb>

# boltzman superposition

<span>boltzman superposition</span>

  - What if we had one load applied at \(t_0 = 0\), we would have
    \[\epsilon_0 = \sigma_0 D(t)\]

  - And some other load applied at \(t_1\) would give
    \[\epsilon_1 = \sigma_1 D(t-t_1)\]

  - Thus the total strain would be:
    \[\epsilon = \epsilon_0 + \epsilon_1 = \sigma_0 D(t) + \sigma_1 D(t-t_1)\]

<span>boltzman superposition</span>

  - For \(N\) applied loads, we have
    \[\epsilon(t) = \Delta \sigma_1 D(t-t_1) + \Delta \sigma_2 D(t-t_2) + ... + \Delta \sigma_N D(t-t_N)\]

  - For some general, arbitrary loading function, this gives
    \[\epsilon(t) = \int_{0}^t D(t-u) \frac{d\sigma}{du}du\]

<span>example</span>

  - For example, when we apply a load and then remove it, we have
    \[\epsilon(t) = \sigma_0 D(t) - \sigma_0 D(t-t_1)\]

  - If we consider \(D=1.2t^{0.1} \text{ GPa}^{-1}\) and let
    \(\sigma_0 = 1 \text { MPa}\) and \(t_1 = 1\text{ s}\), then we have
    \[\epsilon(t) = \left( 1.2 t^{0.1} - 1.2(t-1)^{0.1} \right)\]

<span>example</span>

![image](../Figures/superposition1.png)

<span>example</span>

![image](../Figures/superposition2.png)

# experimental characterization

<span>experimental characterization</span>

  - In practice, both the dynamic properties and time-temperature
    superposition are often used to characterize viscoelastic materials

  - Dynamic experiments are much faster than creep experiments, and can
    give the same information

  - There are physical limitations to the frequencies that can be
    applied

  - To go beyond those frequencies, a range of temperatures are tested

  - This can typically be done using a Dyanmic Mechanical Analyzer (DMA)

<span>dynamic mechanical analyzer</span>

  - To characterize a viscoelastic material in a DMA, tests are run over
    a range of frequencies

  - At each frequency we measure both the stress and strain

  - Plotting both, we can find the complex modulus (or compliance) at
    that frequency

  - Over a range of frequencies this gives the complex modulus as a
    function of frequency

  - Only a few cycles are needed to fit the curve

<span>other considerations</span>

  - When creep and/or stress relaxation experiments must be done,
    time-temperature superposition can still be used

  - Creep or relaxation experiments are run under various temperatures,
    as in our example
