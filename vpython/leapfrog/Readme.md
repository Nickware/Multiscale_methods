# Método Leapfro

El **método Leapfrog** es un integrador numérico muy usado en dinámica molecular para resolver las ecuaciones de movimiento de Newton porque es simple, estable y conserva bien la energía a largo plazo. [en.wikipedia](https://en.wikipedia.org/wiki/Leapfrog_integration)

## Idea básica  

En Leapfrog, las **posiciones** y las **velocidades** no se calculan en el mismo instante de tiempo, sino desfasadas medio paso de tiempo $\(\Delta t/2\)$:  
- Las posiciones $\(x(t)\)$ se conocen en tiempos enteros $\(t, t+\Delta t, t+2\Delta t,\dots\)$.  
- Las velocidades $\(v(t+\Delta t/2)\)$ se conocen en tiempos medios $\(t+\Delta t/2, t+3\Delta t/2,\dots\)$. [manual.gromacs](https://manual.gromacs.org/documentation/2020-beta2/reference-manual/algorithms/molecular-dynamics.html)

Por eso se dice que “posiciones y velocidades se van saltando como ranas una sobre otra” (de ahí el nombre *leap-frog*). [manual.gromacs](https://manual.gromacs.org/documentation/2020-beta2/reference-manual/algorithms/molecular-dynamics.html)

## Ecuaciones del esquema Leapfrog  

Para una partícula de masa $\(m\)$ y fuerza $\(F(x)\)$:  
1. Actualización de velocidades a medio paso:  
$\[
v\left(t+\frac{\Delta t}{2}\right) = v\left(t-\frac{\Delta t}{2}\right) + \frac{F(x(t))}{m}\,\Delta t
$\]  
2. Actualización de posiciones a paso entero:  
$\[
x(t+\Delta t) = x(t) + v\left(t+\frac{\Delta t}{2}\right)\,\Delta t
$\]  
Estas fórmulas dan un método de **orden 2** en el tiempo (el error global decrece como $\(\Delta t^2\))$. [physics.bu](http://physics.bu.edu/py502/lectures3/cmotion.pdf)

## Propiedades importantes  

- **Simplicidad y bajo costo**: solo requiere una evaluación de fuerzas por paso de tiempo, lo que lo hace eficiente en grandes simulaciones de dinámica molecular. [en.wikipedia](https://en.wikipedia.org/wiki/Leapfrog_integration)
- Es un integrador **símplectico**: preserva la estructura de la dinámica Hamiltoniana, lo que se traduce en una buena conservación de la energía a largo plazo, con oscilaciones acotadas en lugar de deriva sistemática. [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0021999197957405)
- Es **reversible en el tiempo**: si se invierte el signo de las velocidades y se integra hacia atrás el mismo número de pasos, el sistema retorna (numéricamente) al estado inicial. [physics.bu](http://physics.bu.edu/py502/lectures3/cmotion.pdf)
- Esto hace que sea muy adecuado para:  
  - Simulaciones de dinámica molecular de biomoléculas (por ejemplo, en GROMACS es el integrador por defecto). [pubs.aip](https://pubs.aip.org/aip/jcp/article/127/18/184102/928429/On-the-calculation-of-velocity-dependent)
  - Problemas de órbitas y sistemas hamiltonianos en general. [academic.oup](https://academic.oup.com/mnras/article/415/4/3168/1747341)

## Relación con Verlet y aplicaciones en DM  

El Leapfrog está estrechamente relacionado con el integrador de **Verlet**, y muchas veces se habla de “Verlet/Leapfrog” como una misma familia de esquemas de segundo orden para dinámica molecular. [people.bath.ac](https://people.bath.ac.uk/chsscp/teach/md.bho/Theory/verlet.html)
- En códigos como GROMACS se usa el Leapfrog para integrar trayectorias clásicas y luego, a partir de las velocidades a medio paso, se calculan propiedades como temperatura y presión con correcciones para reducir el sesgo numérico. [pubs.aip](https://pubs.aip.org/aip/jcp/article/127/18/184102/928429/On-the-calculation-of-velocity-dependent)

En dinámica molecular, Leapfrog es uno de los **métodos de integración numérica clásicos** que equilibra bien precisión, conservación de energía y costo computacional, siendo una opción estándar para simulaciones largas con pasos de tiempo del orden de femtosegundos.

# Movimiento gravitacional de dos esferas con algoritmo de integración Leapfrog

Este script de **Python** utiliza la biblioteca **VPython** para simular el movimiento gravitacional de dos esferas (representando dos cuerpos celestes) según la física clásica. Emplea la integración Leapfrog para la actualización precisa de posiciones y velocidades en el contexto de la interacción gravitatoria.

## Descripción General

El guion crea dos esferas llamadas **giant** y **dwarf**, con diferentes masas, radios, colores y trayectorias visibles. Representan un cuerpo masivo (como una estrella gigante) y uno menos masivo (como una enana).

## Constantes y Objetos

- La constante **G**, $$6.7 \times 10^{-11}$$, es la **constante de gravitación universal**.
- Se definen las posiciones, velocidades y masas iniciales:
  - giant: posición $(-1 \times 10^{11}, 0, 0)$, masa $2 \times 10^{30}$, velocidad $(0, 0, -1 \times 10^4)$.
  - dwarf: posición $(1.5 \times 10^{11}, 0, 0)$, masa $1 \times 10^{30}$, velocidad calculada para conservar el momento lineal total.

## Cálculo de la Fuerza Gravitacional

- Se usa la función **gravitational_force** para calcular la fuerza gravitacional entre ambos cuerpos, usando la ley de Newton:
  $\vec{F} = G \frac{m_1 m_2}{|\vec{r}|^2} \hat{r}$
  donde $$\vec{r}$$ es el vector que une ambos cuerpos.

## Integración Leapfrog

- El método **Leapfrog** es un esquema numérico de integración que mejora la estabilidad de sistemas dinámicos como órbitas:
  - Inicializa velocidades a $$t = -dt/2$$.
  - En cada iteración:
    - Actualiza posiciones con velocidades actuales.
    - Calcula la fuerza gravitacional con las nuevas posiciones.
    - Actualiza velocidades usando la fuerza.

## Visualización y Ejecución

- El bucle **while True** ejecuta la simulación en tiempo real, permitiendo ver cómo ambos cuerpos se atraen y sus trayectorias se generan en la pantalla.
- Se emplea **giant.make_trail=True** y **dwarf.make_trail=True** para mostrar la historia del movimiento de cada objeto como puntos.

## Aplicaciones y Relevancia

- Este tipo de simulaciones es fundamental para **entender órbitas**, colisiones y dinámica de sistemas gravitacionales en física o astronomía.
- El script puede modificarse para más cuerpos o diferentes parámetros físicos.

***

La simulación es una herramienta didáctica eficaz para visualizar interacciones gravitacionales y el uso de algoritmos de integración avanzados como **Leapfrog**.
