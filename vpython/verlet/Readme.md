# Método de Verlet

El **método de Verlet** es un integrador numérico de orden 2, muy usado en dinámica molecular para resolver las ecuaciones de movimiento de Newton porque es sencillo, estable y conserva bien la energía en simulaciones largas. [fismvaladez.wordpress](https://fismvaladez.wordpress.com/2018/05/19/marco-teorico-metodo-de-velocity-verlet-en-metodos-numericos/)

## Idea general  

En su forma clásica (Störmer–Verlet), el método usa posiciones en tres tiempos: \(x_{n-1}, x_n, x_{n+1}\).  
- A partir de la posición actual \(x_n\) y la anterior \(x_{n-1}\), y de la aceleración \(a_n = F(x_n)/m\), se calcula la nueva posición \(x_{n+1}\).  
- No usa explícitamente las velocidades en la fórmula principal; estas pueden reconstruirse después si se necesitan. [dynamics.unam](https://www.dynamics.unam.edu/integra/Manual-Tutoriales/Tesis.pdf)

La fórmula típica es:  
\[
x_{n+1} = x_n + x_n - x_{n-1} + a_n\,\Delta t^2
\]  
donde \(\Delta t\) es el paso de tiempo. [fismvaladez.wordpress](https://fismvaladez.wordpress.com/2018/05/19/marco-teorico-metodo-de-velocity-verlet-en-metodos-numericos/)

## Propiedades importantes  

- Es un integrador **explícito** y de **orden 2** (el error global escala como \(\Delta t^2\)). [dynamics.unam](https://www.dynamics.unam.edu/integra/Manual-Tutoriales/Tesis.pdf)
- Es **simpléctico** y **simétrico en el tiempo**, lo que significa que preserva bien la estructura Hamiltoniana del sistema y mantiene la energía total con oscilaciones acotadas en lugar de una deriva sistemática. [uvadoc.uva](https://uvadoc.uva.es/bitstream/handle/10324/71194/TFG-G6848.pdf?sequence=1&isAllowed=y)
- Solo requiere **una evaluación de fuerzas por paso**, a diferencia de métodos de orden similar como Runge–Kutta de orden 2, que suelen necesitar varias evaluaciones, por lo que resulta muy eficiente en dinámica molecular. [patents.google](https://patents.google.com/patent/ES2440415A2/es)

## Variantes de Verlet  

Existen varias formulaciones equivalentes que se usan en práctica:  
- **Position Verlet**: se escribe en términos de posición, velocidad y aceleración, pero mantiene la misma estructura de segundo orden.  
- **Velocity Verlet**: calcula posición y velocidad en los mismos instantes de tiempo, lo que facilita el cálculo de propiedades dependientes de la velocidad (temperatura, presión). [es.wikipedia](https://es.wikipedia.org/wiki/Din%C3%A1mica_molecular)
- **Leapfrog/Verlet (Störmer–Verlet)**: la versión “leapfrog” usa posiciones en tiempos enteros y velocidades en tiempos medios, pero es matemáticamente muy cercana al Verlet clásico. [patents.google](https://patents.google.com/patent/ES2440415A2/es)

## Uso en dinámica molecular  

En dinámica molecular:  
- Verlet y sus variantes son **integradores estándar** para simular la trayectoria de átomos y moléculas con pasos de tiempo del orden de femtosegundos. [authorea](https://www.authorea.com/users/317774/articles/447871-simulaci%C3%B3n-molecular)
- Su buena conservación de la energía y su bajo costo computacional lo hacen adecuado para simulaciones largas de proteínas, líquidos, sólidos, etc. [patents.google](https://patents.google.com/patent/ES2440415A2/es)

Verlet es uno de los métodos de **integración numérica simplécticos** que permiten equilibrar precisión y costo computacional, manteniendo la estabilidad energética necesaria en simulaciones de dinámica molecular.

# Movimiento gravitacional de dos esferas con algoritmo de Verlet

Este script de **Python** utiliza **VPython** para simular la interacción gravitacional de dos cuerpos, pero implementa la integración mediante el método **Verlet**, enfocado en el uso del **momento lineal** en vez de velocidades.

## Descripción General

El código define dos esferas: **giant** (gigante) y **dwarf** (enano), con propiedades físicas y trayectorias visibles. La simulación está orientada a conservar de manera precisa el **momento lineal** del sistema.

## Constantes y Objetos

- **G** representa la **constante de gravitación universal**, $$6.7 \times 10^{-11}$$.
- Las propiedades principales de los cuerpos:
  - giant: posición $$(-1 \times 10^{11}, 0, 0)$$, masa $$2 \times 10^{30}$$, radio $$2 \times 10^{10}$$, momento $$= \text{masa} \times \text{velocidad}$$.
  - dwarf: posición $$(1.5 \times 10^{11}, 0, 0)$$, masa $$1 \times 10^{30}$$, radio $$1 \times 10^{10}$$, momento igual en magnitud pero de dirección opuesta.

## Cálculo de la Fuerza Gravitacional

- La función **gravitational_force()** calcula la fuerza entre ambos cuerpos usando la ley de Newton:
  $$
  \vec{F} = G \frac{m_1 m_2}{|\vec{r}|^2} \hat{r}
  $$
  donde $$\vec{r}$$ es el vector de separación entre los dos objetos.

## Integración Tipo Verlet

- El método utilizado mezcla **Verlet** y **Leapfrog**, pero se basa directamente en el **momento lineal** ($$p = m v$$).
- El ciclo de actualización consiste en:
  - Calcular la fuerza gravitacional actual ($$F$$).
  - Actualizar posiciones considerando tanto la velocidad (por el momento) como la aceleración ($$F/m$$).
  - Calcular la nueva fuerza ($$F_{new}$$) tras mover los objetos.
  - Actualizar los momentos con la media de las dos fuerzas.

## Ventajas y Aplicaciones

- Usar el momento tiene ventajas respecto a la conservación de la cantidad de movimiento, crucial en sistemas cerrados y en problemas de física clásica.
- El script facilita la **visualización** de trayectorias y permite explorar conceptos como conservación de momento y energía en interacciones gravitacionales.

***

Esta simulación es adecuada para ilustrar la **dinámica de dos cuerpos bajo gravedad**, mostrando cómo evolucionan sus posiciones y momentos en el tiempo usando un método numéricamente estable.
