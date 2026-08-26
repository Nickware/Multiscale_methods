# Métodos Multiescala

Los métodos multiescala son técnicas computacionales y matemáticas diseñadas para abordar problemas que involucran fenómenos que ocurren en múltiples escalas de tiempo, espacio o energía. Son esenciales en ciencia de materiales, biología, ingeniería y ciencias de la Tierra, donde los procesos en una escala influyen significativamente en los de otra. A continuación se describen los métodos multiescala más comunes, con referencias bibliográficas verificables, propuestas de implementación numérica y software libre representativo de cada uno.

---

## 1. Métodos de Enlace de Escalas (Atomístico-Continuo)

Conectan explícitamente dos descripciones —dinámica molecular (DM) y mecánica de medios continuos (MMC)— mediante una región de transición donde ambas escalas se superponen e intercambian información.

**Implementación numérica posible:** acoplamiento vía una región de traslape (*handshake region*) donde los desplazamientos atómicos se promedian hacia nodos de un mallado de elementos finitos, y las fuerzas continuas se interpolan de vuelta hacia los átomos en la frontera; variantes como CADD (*Coupled Atomistic/Discrete-Dislocation*) permiten además el paso de dislocaciones entre dominios.

**Software libre de referencia:**
- **LAMMPS** — simulador de dinámica molecular de código abierto (GPLv2) que incluye la librería *Atom-to-Continuum* (ATC) para acoplar átomos con una malla de elementos finitos superpuesta.
- **CAC-LAMMPS** — implementación paralela del método *Concurrent Atomistic-Continuum* (CAC) integrada en LAMMPS, con escalado O(N/P) para sistemas con elementos finitos, partículas discretas y fuerzas no locales.
- **HacFoam** — solver híbrido que combina LAMMPS (dominio atomístico) con OpenFOAM (dominio continuo, ecuaciones de Navier-Stokes) mediante una región de traslape.

**Referencias:**
- Diaz, A., Gu, B., Plimpton, S. J., Chen, Y., McDowell, D. L. *A parallel algorithm for the concurrent atomistic-continuum methodology*, Journal of Computational Physics (2022). https://doi.org/10.1016/j.jcp.2022.111038
- Pavia, F., Curtin, W. A. *Parallel algorithm for multiscale atomistic/continuum simulations using LAMMPS*, Modelling and Simulation in Materials Science and Engineering, 23(5) (2015). https://doi.org/10.1088/0965-0393/23/5/055002
- *A hybrid atomistic–continuum model for fluid flow using LAMMPS and OpenFOAM*, Computer Physics Communications, 184(9) (2013). https://doi.org/10.1016/j.cpc.2013.03.012
- Thompson, A. P. et al. *LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales*, Computer Physics Communications (2022). https://doi.org/10.1016/j.cpc.2021.108171

---

## 2. Métodos de Homogeneización

Derivan ecuaciones o propiedades efectivas de un medio heterogéneo promediando el comportamiento de su microestructura, sin resolver explícitamente cada detalle fino en el dominio macroscópico.

**Implementación numérica posible:** esquema FE² (elementos finitos anidados en dos escalas), donde cada punto de integración macroscópico resuelve un problema de valor en la frontera sobre un volumen representativo (RVE) para obtener la respuesta constitutiva efectiva; alternativamente, solvers espectrales basados en FFT para homogeneización de microestructuras periódicas.

**Software libre de referencia:**
- **FEniCS / FEniCSx** — plataforma de elementos finitos de código abierto (LGPL) para resolver ecuaciones diferenciales en forma variacional, base de varias implementaciones de homogeneización computacional.
- **micmacsfenics** — implementación de FE² y homogeneización computacional construida sobre FEniCSx.
- **SfePy** — paquete de elementos finitos en Python con un motor de homogeneización dedicado a problemas multiescala (p. ej. estructuras piezoeléctricas).
- **FANS** — solver de homogeneización basado en FFT, paralelo, para problemas multifísicos a microescala.

**Referencias:**
- Cimrman, R., Lukeš, V., Rohan, E. *Multiscale finite element calculations in Python using SfePy*, Advances in Computational Mathematics (2019). arXiv:1810.00674
- Rocha, F., Deparis, S., Antolin, P., Buffa, A. *DeepBND: A machine learning approach to enhance multiscale solid mechanics*, Journal of Computational Physics (2023). https://doi.org/10.1016/j.jcp.2023.111996
- Diercks, P. et al. *Multiscale modeling of linear elastic heterogeneous structures via localized model order reduction*, International Journal for Numerical Methods in Engineering (2023). arXiv:2201.10374
- Feyel, F., Chaboche, J. L. *FE² multiscale approach for modelling the elastoviscoplastic behaviour of long fibre SiC/Ti composite materials*, Computer Methods in Applied Mechanics and Engineering, 183(3-4) (2000).

---

## 3. Métodos de Coarse-Graining (Granulación Gruesa)

Reducen los grados de libertad de un sistema agrupando átomos o monómeros en "pseudo-partículas" (*beads*), simplificando polímeros, proteínas o líquidos moleculares para acceder a escalas espaciotemporales mayores.

**Implementación numérica posible:** derivación de potenciales de grano grueso mediante *force matching* (coincidencia de fuerzas, también llamado MS-CG), inversión de Boltzmann iterativa (IBI) o minimización de entropía relativa, comparando distribuciones radiales entre el sistema atomístico de referencia y el modelo de grano grueso.

**Software libre de referencia:**
- **VOTCA** — conjunto de herramientas de código abierto para coarse-graining sistemático (inversión de Boltzmann, Monte Carlo inverso, *force matching*, entropía relativa) e interfaz con motores de DM como GROMACS y LAMMPS.
- **BOCS** (*Bottom-up Open-source Coarse-graining Software*) — implementa el método MS-CG por *force matching* y el método g-YBG para el diseño de potenciales de grano grueso.
- **MARTINI** — campo de fuerza de grano grueso ampliamente usado para biomoléculas y polímeros, distribuido como parámetros libres para motores como GROMACS.

**Referencias:**
- Baumeier, B. et al. *VOTCA: multiscale frameworks for quantum and classical simulations in soft matter*, Journal of Open Source Software, 9(99), 6864 (2024). https://doi.org/10.21105/joss.06864
- Rühle, V. et al. *Versatile Object-Oriented Toolkit for Coarse-Graining Applications* (VOTCA), Journal of Chemical Theory and Computation (2009).
- Dunn, N. J. H., Lebold, K. M., DeLyser, M. R., Rudzinski, J. F., Noid, W. G. *BOCS: Bottom-Up Open-Source Coarse-Graining Software*, Journal of Physical Chemistry B (2018). https://doi.org/10.1021/acs.jpcb.7b09993

---

## 4. Simulaciones Concurrentes (Descomposición de Dominios)

Ejecutan simultáneamente modelos correspondientes a distintas escalas en diferentes regiones del dominio, intercambiando información en las fronteras entre subdominios finos y gruesos.

**Implementación numérica posible:** particionamiento espacial del dominio (p. ej. vía METIS/ParMETIS), con comunicación de variables de estado en la interfaz mediante paso de mensajes (MPI) en cada paso de tiempo; el método CAC descrito en la sección 1 es un caso particular de esta familia.

**Software libre de referencia:**
- **deal.II** — biblioteca de elementos finitos de código abierto orientada a problemas con mallas adaptativas y descomposición de dominios, ampliamente usada como base de esquemas multiescala concurrentes.
- **PETSc** — biblioteca de cómputo científico paralelo (solvers, precondicionadores, descomposición de dominios) usada como backend numérico de FEniCS, SfePy y deal.II.
- **LAMMPS** — su descomposición espacial estándar es la base sobre la que se construyen los acoplamientos concurrentes atomístico-continuo mencionados en la sección 1.

**Referencias:**
- Balay, S. et al. *PETSc Users Manual*, Argonne National Laboratory (2018).
- Arndt, D. et al. *The deal.II Library, Version 9.x*, Journal of Numerical Mathematics.

---

## 5. Métodos de Escalado Temporal

Abordan fenómenos con dinámicas rápidas y lentas simultáneas, integrando cada una con un paso de tiempo distinto para evitar el costo de resolver todo el sistema al paso más restrictivo.

**Implementación numérica posible:** integración tipo r-RESPA (*reversible REference System Propagator Algorithm*), donde las fuerzas de corto alcance (enlaces, ángulos) se integran con pasos pequeños y las de largo alcance (electrostáticas) con pasos más grandes, anidados jerárquicamente.

**Software libre de referencia:**
- **LAMMPS** — implementa el integrador `run_style respa`, con soporte nativo para múltiples niveles de paso de tiempo.
- **GROMACS** — motor de DM de código abierto con esquemas de integración de múltiples pasos de tiempo para simulaciones bioquímicas de gran escala.

**Referencias:**
- Tuckerman, M., Berne, B. J., Martyna, G. J. *Reversible multiple time scale molecular dynamics*, The Journal of Chemical Physics, 97(3) (1992).

---

## 6. Métodos de Aprendizaje Automático Multiescala

Usan modelos de aprendizaje automático (redes neuronales, *kernel methods*) entrenados con datos de una escala fina (p. ej. cálculos cuánticos) para predecir comportamientos en escalas más gruesas sin resolver explícitamente la física detallada en cada paso.

**Implementación numérica posible:** entrenamiento de un potencial interatómico basado en redes neuronales (*machine-learned interatomic potential*, MLIP) sobre datos de estructura electrónica (DFT), seguido de su despliegue como campo de fuerza dentro de un motor de dinámica molecular clásico para acceder a tamaños y tiempos inalcanzables por DFT puro.

**Software libre de referencia:**
- **DeePMD-kit** — paquete de código abierto para construir potenciales de aprendizaje profundo (*Deep Potential*) e integrarlos en motores de DM como LAMMPS, GROMACS, AMBER y OpenMM.
- **SchNetPack** — caja de herramientas de aprendizaje profundo para sistemas atomísticos, usada para construir potenciales tipo *message passing*.

**Referencias:**
- Zeng, J. et al. *DeePMD-kit v2: A software package for Deep Potential models*, The Journal of Chemical Physics, 159, 054801 (2023). https://doi.org/10.1063/5.0155600
- Wang, H., Zhang, L., Han, J., E, W. *DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics*, Computer Physics Communications, 228 (2018).
- Schütt, K. T. et al. *SchNetPack: A Deep Learning Toolbox for Atomistic Systems*, Journal of Chemical Theory and Computation, 15(1) (2019).

---

## 7. Métodos de Ecuaciones Diferenciales Parciales Multiescala

Resuelven ecuaciones diferenciales parciales cuyos coeficientes oscilan rápidamente en el espacio, construyendo funciones base o correcciones efectivas que capturan la heterogeneidad fina sin necesidad de mallar toda la microestructura.

**Implementación numérica posible:** Método de Elementos Finitos Multiescala (MsFEM), donde las funciones base de cada elemento grueso se calculan resolviendo un problema local en la microestructura correspondiente, en lugar de usar polinomios estándar; su generalización (GMsFEM) enriquece el espacio local con funciones espectrales adicionales.

**Software libre de referencia:**
- **FreeFEM** — solver de EDP de código abierto con implementaciones documentadas de FEM, MsFEM y GMsFEM para problemas elípticos en medios heterogéneos.
- **deal.II** / **MFEM** — bibliotecas de elementos finitos usadas como base para implementaciones propias de MsFEM y del método de homogeneización asintótica en medios porosos.

**Referencias:**
- Hou, T. Y., Wu, X.-H. *A multiscale finite element method for elliptic problems in composite materials and porous media*, Journal of Computational Physics, 134(1) (1997).
- Muljadi, B. P., Narski, J., Lozinski, A., Degond, P. *Non-Conforming Multiscale Finite Element Method for Stokes Flows in Heterogeneous Media*, SIAM Multiscale Modeling & Simulation, 13(4) (2015). arXiv:1404.2837
- Efendiev, Y., Galvis, J., Hou, T. Y. *Generalized Multiscale Finite Element Methods (GMsFEM)*, Journal of Computational Physics, 251 (2013).

---

## Ejemplo Práctico

En la ciencia de materiales, para estudiar la propagación de grietas se combinan típicamente tres escalas: dinámica molecular (LAMMPS) para la nucleación de la grieta a nivel atómico, modelos de dislocaciones (p. ej. CADD, acoplado también en LAMMPS) para su propagación a nivel de grano, y mecánica de fractura en un solver de elementos finitos (deal.II, FEniCS) para predecir el fallo macroscópico bajo carga.

## Desafíos

1. **Consistencia entre escalas:** asegurar que los modelos en diferentes escalas sean compatibles entre sí (p. ej. que la homogeneización no introduzca artefactos en la frontera entre dominios).
2. **Eficiencia computacional:** manejar la carga computacional al integrar múltiples escalas, especialmente en simulaciones concurrentes con comunicación MPI intensiva.
3. **Validación y verificación:** contrastar los modelos multiescala con datos experimentales y verificar su precisión frente a simulaciones de referencia en la escala fina.

En resumen, los métodos multiescala integran distintas escalas para obtener una visión más completa y computacionalmente tratable de sistemas complejos, y cuentan hoy con un ecosistema maduro de software libre (LAMMPS, FEniCS/FEniCSx, VOTCA, deal.II, DeePMD-kit, FreeFEM, entre otros) que permite su implementación práctica sin depender de herramientas propietarias.
