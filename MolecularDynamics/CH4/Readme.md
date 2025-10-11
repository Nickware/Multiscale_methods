# Minimización de energía de una molécula de metano (CH₄) mediante dinámica molecular

Estos scripts simulan la **minimización de energía** de una molécula de metano (CH₄) mediante dinámica molecular reducida en Python, mostrando en tiempo real su estructura, distancias y energías.

### Propósito y Características

- Simulan el comportamiento de una molécula de metano en 3D usando posiciones y velocidades de los átomos.
- Modelan los enlaces C-H a través de una aproximación de resorte armónico (modelo de Hooke).
- Incluyen **amortiguamiento** artificial para acelerar la convergencia a la estructura de mínimo energético.
- Visualizan en tiempo real la estructura, las distancias C-H y las energías (potencial, cinética y total).

### Componentes Clave

- **Parámetros físicos:** Masa de C y H, constante de enlace, distancia de equilibrio, damping y pasos de integración. Se usan valores realistas para simular una molécula física.
- **Inicialización:** Los átomos de H se disponen en la geometría ideal tetraédrica, normalizados a la distancia de enlace y perturbados aleatoriamente para evitar simetría perfecta.
- **Cálculo de fuerzas:** Las fuerzas se calculan para cada enlace C-H como fuerzas de resorte (Hooke), corrigiendo por amortiguamiento para simular disipación (minimización).
- **Simulación:** Utiliza el algoritmo Velocity Verlet para evolucionar posiciones y velocidades, guardando el historial de distancias y energías.
- **Visualización:** Presenta tres gráficos en tiempo real: estructura 3D, evolución de distancias y energías del sistema.
- **Análisis final:** Calcula distancias y ángulos H-C-H, compara con el ángulo tetraédrico ideal ($$109.47^\circ$$), y muestra la energía final.

### Aspectos destacables

- La dinámica está "amortiguada," lo que significa que busca el mínimo energético rápidamente más que simular movimiento térmico real.
- No incluyen interacciones ángulo o repulsión "realistas" entre hidrógenos; el modelo es idealizado pero útil para estudios educativos y visualización básica.
- Estos scripts son interactivos; los gráficos se actualizan cada 100 pasos y al final muestran los resultados.

### Ejemplo de salida final

- **Distancias C-H**: Cercanas al valor de equilibrio especificado (≈1.09 Å).
- **Ángulos H-C-H**: Cercanos al ángulo tetraédrico, y se muestra la desviación respecto al ideal.
- **Energía final**: Valor minimizado mostrado en kcal/mol.

### Aplicaciones y usos

- Enseñanza de conceptos de dinámica molecular y geometría molecular.
- Validación rápida de modelos armónicos y visualización de la convergencia del sistema.

Este tipo de script se utiliza para explorar, analizar y visualizar sistemas físicos moleculares elementales; puede ser extendido fácilmente para modelos de mayor complejidad y otros sistemas.
