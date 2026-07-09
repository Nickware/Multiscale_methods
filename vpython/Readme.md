# Vpython 

Es una extensión de Python pensada para crear **visualizaciones 3D sencillas e interactivas** con muy poco código. Se usa mucho en enseñanza de física y programación porque permite construir esferas, flechas, vectores y trayectorias en tiempo real sin pelear tanto con gráficos de bajo nivel. [en.wikipedia](https://en.wikipedia.org/wiki/VPython)

## Qué lo hace útil

- Permite representar objetos 3D de forma natural, como `sphere`, `box`, `arrow` y vectores.
- Es muy práctico para simulaciones educativas, por ejemplo movimiento de proyectiles, osciladores, órbitas y choques.
- Ayuda a concentrarse en la física y no tanto en la interfaz gráfica. [wiki.python](https://wiki.python.org/moin/VPython)

## En qué se usa

VPython se ha usado sobre todo en educación, especialmente para enseñar física y programación científica. También aparece en contextos de visualización de datos o sistemas 3D más simples, aunque no compite con motores gráficos o herramientas CFD avanzadas. [en.wikipedia](https://en.wikipedia.org/wiki/VPython)

## Cómo se ve su enfoque

La idea típica es algo como:

- definir objetos en 3D,
- asignarles masa, velocidad o momento,
- calcular fuerzas,
- actualizar posiciones en un bucle,
- ver la animación mientras corre el programa.

Eso lo vuelve ideal para ejemplos como el script que me mostraste de gravitación entre dos cuerpos. [villate](https://villate.org/python/vpython.html)

## Limitaciones

VPython es excelente para didáctica y prototipos, pero no está pensado para simulaciones físicas de alta precisión ni para gráficos complejos de producción. Su fuerte es la **claridad conceptual** y la visualización rápida. [villate](https://villate.org/python/vpython.html)

## Ejemplo de uso

Si se quiere estudiar una órbita, se pueden representar dos esferas, calcular la fuerza gravitacional entre ellas y moverlas paso a paso. Eso convierte una ecuación abstracta en una animación fácil de interpretar. [wiki.python](https://wiki.python.org/moin/VPython)

## Simulación de Interacción Gravitacional entre Dos Cuerpos con VPython

Este script utiliza la librería **VPython** para simular y visualizar la interacción gravitacional entre dos cuerpos masivos en el espacio, mostrando sus trayectorias en 3D en tiempo real.

### Descripción General

El código implementa un modelo simple de dos cuerpos (un "gigante" y un "enano") que interactúan únicamente bajo la fuerza de gravedad. Utiliza integración numérica para actualizar sus posiciones y momentos lineales, permitiendo observar cómo se mueven bajo la influencia mutua.

### Características principales

- **Visualización 3D interactiva:** Gracias a VPython, puedes ver las trayectorias de ambos cuerpos con estelas que muestran su recorrido.
- **Modelo físico:** Aplica la ley de gravitación universal de Newton para calcular la fuerza entre los cuerpos.
- **Integración numérica:** Utiliza el método de Euler para actualizar posiciones y momentos.
- **Conservación del momento:** Los momentos iniciales están definidos de forma que el momento lineal total del sistema se conserve.

### Estructura del Script

1. **Configuración de la escena:**
   - Se ajusta la vista de la escena 3D para una mejor visualización.

2. **Definición de constantes físicas:**
   - Constante gravitacional $\( G \$).

3. **Creación de los objetos:**
   - Dos esferas (`giant` y `dwarf`) con posiciones, radios, colores y trayectorias personalizadas.
   - Asignación de masas y momentos lineales iniciales.

4. **Bucle principal de simulación:**
   - Cálculo de la fuerza gravitacional entre los cuerpos.
   - Actualización de los momentos lineales usando la segunda ley de Newton.
   - Actualización de las posiciones en función del momento y la masa.
   - Visualización continua de la evolución del sistema.

### Fragmento clave del algoritmo

```


# Actualización de momento y posición

giant.p = giant.p + F*dt
dwarf.p = dwarf.p - F*dt
giant.pos = giant.pos + (giant.p/giant.mass) * dt
dwarf.pos = dwarf.pos + (dwarf.p/dwarf.mass) * dt

```

### Conceptos físicos involucrados

- **Momento lineal**
  $\vec{p}$
  Unidades de kg·m/s.

- **Segunda ley de Newton:** 
  $\vec{F}=\frac{d\vec{p}}{dt}$
  
- **Ley de gravitación universal**
  $\vec{F} = G \frac{m_1 m_2}{r^2} \hat{r}$
  
- **Integración numérica (Euler):** Aproximación para actualizar variables físicas en pasos discretos de tiempo.

### Posibles extensiones

- Implementar métodos de integración más precisos (Verlet, Runge-Kutta).
- Añadir más cuerpos para simular sistemas planetarios complejos.
- Incluir condiciones de colisión o rebote.
- Modificar parámetros físicos para explorar diferentes escenarios.

### Requisitos

- Python 3.x
- VPython (instalación: `pip install vpython`)

### Ejecución

Guardar el script en un archivo `.py` y ejecútarlo. Se abrirá una ventana interactiva mostrando la simulación en 3D.

Este script es ideal para fines educativos, permitiendo experimentar y visualizar conceptos fundamentales de la dinámica gravitacional y la programación científica con Python.
