# Minimización de energía de una molécula de etano (C₂H₆) mediante dinámica molecular

Estos scripts realizan una simulación molecular simplificada y la **minimización de energía** del etano (C₂H₆) usando Python, incorporando visualización interactiva y generación de archivos XYZ y de energía para análisis estructural y trayectorial.

### Objetivo principal

- Representan la geometría y dinámica básica del etano, considerando enlaces C-H, C-C y fuerzas angulares H–C–H, con evolución de posiciones, velocidades, energías y distancias interatómicas.

### Componentes y funciones principales

- **Parámetros físicos:** Incluyen masas (C y H), constantes de enlace (C-H, C-C), constantes angulares y dihedral (aunque la dihedral no se usa directamente), distancia de equilibrio para enlaces y ángulos tetraédricos.
- **Inicialización (etano):** Los átomos se disponen en la configuración ideal tetraédrica, con hidrógenos alrededor de cada carbono y una pequeña rotación en el segundo carbono para representar una conformación escalonada.
- **Cálculo de fuerzas:** Se considera
  - Fuerzas armónicas de enlace C–C y C–H.
  - Fuerzas angulares para mantener ángulos H–C–H cercanos al valor ideal ($$109.47^{\circ}$$).
  - Fuerzas de amortiguamiento para acelerar la relajación hacia el mínimo energético.
  - No simula fuerzas dihedrales explícitas ni efectos electrónicos.
- **Simulación:** Utilizan **Velocity Verlet** para actualizar posiciones y velocidades y guardar información de la evolución del sistema.
- **Visualización:** Actualizan en tiempo real:
  - La geometría molecular 3D, con enlaces dibujados y átomos diferenciados por color.
  - Distancias C-H y C-C conforme avanzan los pasos.
  - Energías potencial, cinética y total.
- **Salida a archivo XYZ:** Registran frames periódicamente en formato XYZ, permitiendo análisis y visualización posterior en programas externos como VMD, Ovito o Xmakemol.
- **Salida de energías:** Se guarda un archivo con el historial de energías en cada paso, útil para análisis cuantitativo.

### Análisis final

- Calculan distancias finales C–H y C–C, ángulos H–C–H para cada centro de carbono y desviación respecto al ángulo tetraédrico ideal.
- Imprimen estos resultados, junto con la energía total final y los nombres de los archivos generados.
- Dan instrucciones para visualizar la trayectoria molecular usando software popular.

### Aplicaciones

- Permiten entender la geometría y relajación de una molécula realista mediante un modelo armónico, útil en docencia, desarrollo de modelos y análisis visual básico de trayectorias moleculares.
- Los archivos generados permiten la exploración visual externa y la comparación con simulaciones más avanzadas.

Este enfoque puede ser extendido a moléculas más grandes y complejas, o mejorado con potenciales más realistas y fuerzas adicionales según necesidades de simulación.
