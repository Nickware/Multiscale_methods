# Movimiento gravitacional de dos esferas con algoritmo de integración Leapfrog

Este script de **Python** utiliza la biblioteca **VPython** para simular el movimiento gravitacional de dos esferas (representando dos cuerpos celestes) según la física clásica. Emplea integración Leapfrog para la actualización precisa de posiciones y velocidades en el contexto de la interacción gravitatoria.

## Descripción General

El guion crea dos esferas llamadas **giant** y **dwarf**, con diferentes masas, radios, colores y trayectorias visibles. Representan un cuerpo masivo (como una estrella gigante) y uno menos masivo (como una enana).

## Constantes y Objetos

- La constante **G**, $$6.7 \times 10^{-11}$$, es la **constante de gravitación universal**.
- Se definen las posiciones, velocidades y masas iniciales:
  - giant: posición $$(-1 \times 10^{11}, 0, 0)$$, masa $$2 \times 10^{30}$$, velocidad $$(0, 0, -1 \times 10^4)$$.
  - dwarf: posición $$(1.5 \times 10^{11}, 0, 0)$$, masa $$1 \times 10^{30}$$, velocidad calculada para conservar el momento lineal total.

## Cálculo de la Fuerza Gravitacional

- Se usa la función **gravitational_force** para calcular la fuerza gravitacional entre ambos cuerpos, usando la ley de Newton:
  $$
  \vec{F} = G \frac{m_1 m_2}{|\vec{r}|^2} \hat{r}
  $$
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
