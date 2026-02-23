# Oscilaciones moleculares del dióxido de carbono ($$\text{CO}_2$$) 

Este script simula las **oscilaciones moleculares** del dióxido de carbono ($$\text{CO}_2$$) usando un modelo físico en una dimensión y el algoritmo **Velocity Verlet** para la integración numérica.

### Descripción General

El código modela a la molécula de $CO_{2}$ como tres masas alineadas ($$\text{O}_1$$, $$\text{C}$$, $$\text{O}_2$$) conectadas por dos "resortes" (enlaces químicos). Una **perturbación inicial** desplaza el oxígeno derecho para iniciar el movimiento de oscilación.

### Parámetros Físicos y Modelo

- **Masas:** Oxígeno ($m_O=16$), carbono ($m_C=12$). Las unidades son arbitrarias y se usan para mantener proporciones similares a las reales.
- **Constante de resorte ($$k$$):** Simula la rigidez del enlace. Un valor alto implica que los átomos tienden a regresar rápidamente a la posición de equilibrio.
- **Longitud de equilibrio ($$r_{eq}$$):** Distancia natural $C=O$ en la molécula.
- **Posiciones:** Inicialmente, cada átomo está en reposo y en equilibrio; el oxígeno derecho se desplaza para perturbar la molécula.

### Dinámica y Algoritmo

- **Fuerzas:** La función `compute_forces` calcula las fuerzas restauradoras para cada átomo basadas en el estiramiento o compresión de los enlaces respecto a su equilibrio. Se aplica la ley de Hooke para cada resorte:
  $F = -k (x - r_{eq})$
  donde $x$ es la distancia actual entre átomos y $r_{eq}$ es la de equilibrio.
- **Velocity Verlet:** Método de integración eficiente y estable para sistemas dinámicos. Actualiza posiciones y velocidades en cada paso considerando aceleraciones medias.

### Resultados y Gráfica

- Se simulan 5000 pasos temporales con un pequeño intervalo ($dt = 0.001$).
- La trayectoria de cada átomo se almacena y finalmente se grafica para visualizar la evolución de sus posiciones en el tiempo.
- El gráfico muestra **oscilaciones típicas de una molécula** donde los átomos vibran alrededor de sus posiciones de equilibrio luego de una perturbación inicial.

### Aplicaciones y Relevancia

- Este tipo de simulaciones es clave para entender la **vibración molecular**, espectros vibracionales y propiedades dinámicas de moléculas.
- El algoritmo y modelo pueden extenderse a moléculas más complejas o dimensiones adicionales.

***

El script es una excelente muestra de cómo la física y la programación pueden unirse para analizar **dinámica molecular** y visualizar procesos que ocurren a nivel microscópico usando modelos sencillos pero representativos.
