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
