# Método Monte Carlo

El método Monte Carlo es una técnica computacional que utiliza muestreo aleatorio repetido para aproximar soluciones numéricas a problemas determinísticos o estocásticos complejos, como integrales multidimensionales, optimización y modelado de sistemas con incertidumbre. Basado en la ley de los grandes números, genera entradas aleatorias en un dominio definido, evalúa funciones deterministas y promedia resultados para estimar expectativas matemáticas, con precisión que mejora como $1/\sqrt{N}$ donde $N$ es el número de muestras. Originado en los años 1940 para física nuclear (difusión de neutrones), se aplica en finanzas, física molecular, ingeniería y machine learning, superando métodos analíticos en alta dimensionalidad.[wikipedia+1](https://en.wikipedia.org/wiki/Monte_Carlo_method)

## Mecánica Básica

El algoritmo sigue pasos estándar: 

1. definir variables aleatorias con distribución de probabilidad adecuada; 
2. Generar muestras independientes (o correlacionadas en variantes); 
3. Calcular observables; 
4. Estimar medias y varianzas vía promedios empíricos. Para reducir error estadístico, se usan técnicas de varianza reducida. En física computacional, relevante para tu trabajo en dinámica molecular, modela ensembles termodinámicos y propiedades macroscópicas.[wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)

## Variantes Principales

Estas mejoran eficiencia, convergencia o adaptabilidad:

- **Monte Carlo Simple**: Promedia simulaciones independientes para valores esperados, como estimar $\pi$ inscribiendo un círculo en un cuadrado y contando proporciones de puntos aleatorios dentro.[wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- **Quasi-Monte Carlo**: Emplea secuencias deterministas de baja discrepancia (ej. Halton, Sobol) para muestreo uniforme superior al aleatorio puro, convergiendo como $O((\log N)^d / N)$ en $d$ dimensiones.[wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- **Monte Carlo de Importancia**: Reescribe integrales como expectativas bajo distribución tilted $q(x)$ que enfatiza regiones de alta contribución, reduciendo varianza: $\mathbb{E}_q [f(x) w(x)]$ con $w(x) = p(x)/q(x)$.[wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- **Markov Chain Monte Carlo (MCMC)**: Explora distribuciones $p(x)$ vía cadenas de Markov ergódicas, con propuestas Metropolis-Hastings -- aceptación -- $(\min(1,p(x')/p(x)))$ o Gibbs sampling para componentes condicionales; clave en inferencia bayesiana y muestreo de Boltzmann en física estadística.[wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)

## Variantes Especializadas

- **Direct Simulation Monte Carlo (DSMC)**: Para flujos raros (Knudsen >1), simula partículas representando moléculas: movimiento balístico, colisiones probabilísticas (modelos VHS), muestreo macroscópico; usado en aerodinámica hipersónica y reentrada espacial.[wikipedia](https://en.wikipedia.org/wiki/Direct_simulation_Monte_Carlo)
- **Monte Carlo Tree Search (MCTS)**: Árbol de búsqueda expandido por simulaciones aleatorias (rollouts), balanceando exploración/explotación vía UCT; base de AlphaGo para juegos y optimización secuencial.[wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- **Grand Canonical Monte Carlo (GCMC)**: Para ensemble $(\mu, V, T)$, alterna desplazamientos Metropolis con inserciones/eliminaciones de partículas, aceptadas por $\exp(-\beta \Delta U \pm \beta \mu)$; ideal para adsorción en nanoporos y termodinámica de materiales.[scm](https://www.scm.com/doc/AMS/Tasks/GCMC.html)

Otras incluyen Monte Carlo en finanzas (valoración de opciones), kinetic Monte Carlo para procesos raros y híbridos con dinámica molecular. En simulaciones moleculares como las tuyas, combinan con MD para ensembles híbridos, ofreciendo flexibilidad en sistemas abiertos.[pubs.acs+1](https://pubs.acs.org/doi/10.1021/jp908058n)

## Workflow del Método Monte Carlo Básico

El workflow estándar del método Monte Carlo sigue un ciclo iterativo para aproximar soluciones mediante muestreo aleatorio, basado en la mecánica descrita previamente.[wikipedia+1](https://es.wikipedia.org/wiki/Método_de_Montecarlo)

1. **Definir el problema y modelo**: Identifica el dominio de variables de entrada $x$ (ej. intervalo o espacio multidimensional), la función objetivo $f(x)$ a evaluar (ej. integral $\int f(x) p(x) dx$) y la distribución de probabilidad $p(x)$ que gobierna las entradas.[wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
2. **Generar números pseudoaleatorios**: Usa un generador (ej. Mersenne Twister) para producir secuencias uniformes en [0,1), transformadas a $p(x)$ vía métodos de inversión, rechazo o tablas acumuladas para variables discretas/continuas.[ehu+1](http://www.sc.ehu.es/sbweb/fisica_/numerico/montecarlo/montecarlo.html)
3. **Ejecutar simulaciones independientes**: Para cada muestra $i = 1$ a $N$ (miles/millones), dibuja $x_i \sim p(x)$, calcula $y_i = f(x_i)$ y almacena resultados; opcionalmente computa pesos para variantes como importancia sampling.[asana](https://asana.com/es/resources/montecarlo-method)
4. **Calcular estadísticos**: Estima el valor esperado $\hat{\mu} = \frac{1}{N} \sum y_i$, varianza $\hat{\sigma}^2 = \frac{1}{N-1} \sum (y_i - \hat{\mu})^2$ y intervalos de confianza (ej. $\hat{\mu} \pm 1.96 \hat{\sigma}/\sqrt{N}$ al 95%).[wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
5. **Evaluar convergencia y refinar**: Monitorea error estadístico $(O(1/\sqrt{N}))$; si insuficiente, incrementa $N$ o aplica técnicas de reducción de varianza; visualiza distribuciones (histogramas) para validar.[aws.amazon](https://aws.amazon.com/es/what-is/monte-carlo-simulation/)

## Ejemplo Práctico: Aproximación de $\pi$

- Dibujar cuadrado de lado 2 centrado en origen y círculo unitario.
- Generar $N$ puntos $(x,y)$ uniformes en $[-1,1]^2$.
- Contar proporción $k/N$ dentro del círculo ($x^2 + y^2 \leq 1$).
- Estimar $\pi \approx 4 k / N$.[wikipedia](https://es.wikipedia.org/wiki/Método_de_Montecarlo)

### Compilación y Ejecución

```bash
g++ -O3 -std=c++11 -o monte_carlo_pi monte_carlo_pi.cpp -lm
./monte_carlo_pi
```
### Visualización con xmgrace

```bash
xmgrace -nxy inside.dat outside.dat -param plot.xmgr
```

### Resultados Esperados

Con $N=10^6$, obtendrás $\pi \approx 3.1415 \pm 0.0018$ (error ~0.06%). Los puntos rojos forman el círculo unitario, azules el cuadrado exterior. Escalable a GPU con Thrust/CUDA para $N>10^9$ en simulaciones moleculares.[wikipedia+1](https://en.wikipedia.org/wiki/Monte_Carlo_method)


Este workflow se adapta directamente a variantes: en MCMC agrega propuestas Metropolis; en DSMC, pasos de movimiento/colisión; en GCMC, inserciones/eliminaciones. En simulaciones moleculares, se usa regularmente para promediar energías o propiedades en ensembles.[scm+1](https://www.scm.com/doc/AMS/Tasks/GCMC.html)

1. [https://es.wikipedia.org/wiki/M%C3%A9todo_de_Montecarlo](https://es.wikipedia.org/wiki/Método_de_Montecarlo)
2. https://www.ibm.com/es-es/topics/monte-carlo-simulation
3. https://asana.com/es/resources/montecarlo-method
4. https://aws.amazon.com/es/what-is/monte-carlo-simulation/
5. http://www.sc.ehu.es/sbweb/fisica_/numerico/montecarlo/montecarlo.html
6. https://metodotrading.com/simulacion-de-monte-carlo/
7. https://www.datacamp.com/es/tutorial/monte-carlo-simulation-in-excel
8. https://www.questionpro.com/blog/es/simulacion-de-monte-carlo/
9. https://www.youtube.com/watch?v=WJjDr67frtM
10. https://www.famaf.unc.edu.ar/~pperez1/manuales/cim/cap6.html
11. https://en.wikipedia.org/wiki/Monte_Carlo_method
12. https://www.scm.com/doc/AMS/Tasks/GCMC.html

1. https://en.wikipedia.org/wiki/Monte_Carlo_method
2. https://www.britannica.com/science/Monte-Carlo-method
3. https://en.wikipedia.org/wiki/Direct_simulation_Monte_Carlo
4. https://www.scm.com/doc/AMS/Tasks/GCMC.html
5. https://pubs.acs.org/doi/10.1021/jp908058n
