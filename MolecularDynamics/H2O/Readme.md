# Simulación de la molécula de agua ($$\text{H}_2\text{O}$$) emplenando dinámica molecular simplificada usando un modelo de resortes

Este script simula la dinámica molecular simplificada de una molécula de agua ($$\text{H}_2\text{O}$$) usando un modelo de resortes para los enlaces O-H en dos dimensiones, con disipación incluida para representar fricción. La integración numérica emplea el algoritmo Velocity-Verlet para actualizar posiciones y velocidades.

### Descripción General

- La molécula se modela con 3 partículas: un átomo de oxígeno en el centro y dos átomos de hidrógeno moviéndose en el plano $$xy$$.
- Los enlaces O–H se representan como resortes con constante elástica $$k$$ y longitud de equilibrio $$r_{eq}$$.
- Se incluye un término de fricción viscosa con coeficiente $$\gamma$$ para simular la disipación de energía (modelo tipo Langevin simplificado).

### Parámetros Físicos

- Constante de resorte $$k = 100$$ kcal/mol/Å² — controla la fuerza restauradora de los enlaces.
- Longitud de equilibrio $$r_{eq} = 0.96\, $$ Å — distancia natural del enlace O-H.
- Paso temporal $$dt = 0.001$$ y número de pasos $$10000$$, simulando dinámica extendida.
- Masas relativas: Oxígeno (16 u), Hidrógeno (1 u).

### Dinámica y Cálculo de Fuerzas

- La función `spring_force` calcula la fuerza restauradora elástica entre un par de átomos unidos por resorte aplicando la Ley de Hooke vectorial:
  $$
  \vec{F} = -k (|\vec{r}| - r_{eq}) \hat{r}
  $$
- Se calcula la fuerza entre el oxígeno y cada hidrógeno, aplicando la fuerza de fricción proporcional a la velocidad para cada átomo.

### Integración Numérica

- La dinámica evoluciona con el método **Velocity-Verlet**:
  - Se calcula aceleración a partir de las fuerzas presentes.
  - Se actualizan velocidades y posiciones en cada paso temporal.
- Se almacenan posiciones y velocidades para análisis posterior.

### Resultados y Visualización

- Se grafican las posiciones en la coordenada $$x$$ de cada átomo a lo largo del tiempo, mostrando la relajación tras perturbaciones iniciales.
- Se representa el estado de fase (posición vs velocidad en $$x$$) para observar dinámicas oscilatorias amortiguadas características de sistemas disipativos.

### Aplicaciones y Relevancia

- Este modelo permite estudiar cómo los enlaces químicamente modelados con resortes responden a perturbaciones en presencia de disipación.
- Es útil para entender fenómenos de relajación vibracional y efectos disipativos en moléculas pequeñas.
- Esta aproximación se puede extender para simular dinámica molecular más realista o añadir temperatura via ruido estocástico.

***

El script combina conceptos físicos clásicos con simulación numérica para explorar el comportamiento dinámico y disipativo de un sistema molecular modelo en 2D, visualizando tanto oscilaciones como procesos de relajación.
