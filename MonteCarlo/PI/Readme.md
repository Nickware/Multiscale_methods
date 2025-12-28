# Estimación de π con Monte Carlo en C++ y xmgrace

Este proyecto implementa un ejemplo clásico del método de Monte Carlo para estimar el valor de $\(\pi\)$ generando puntos aleatorios en un cuadrado y contando cuántos caen dentro de un círculo unitario inscrito. La salida numérica se muestra por consola y los puntos se guardan en archivos para visualizarse con xmgrace, una herramienta de gráficos 2D.

## Descripción del método

El algoritmo genera \(N\) puntos \((x, y)\) distribuidos uniformemente en el cuadrado $\([-1, 1] \times [-1, 1]\)$.  
- Si el punto cumple $\(x^2 + y^2 \le 1\)$, se considera dentro del círculo unitario.  
- La fracción de puntos dentro del círculo $\(k/N\)$ aproxima el cociente de áreas $\(\pi / 4\)$, por lo que $\(\pi \approx 4k/N\)$.[1]

El programa:  
- Cuenta cuántos puntos caen dentro del círculo.  
- Calcula una estimación de $\(\pi\)$.  
- Estima un intervalo de confianza aproximado al 95%.  
- Escribe los puntos en dos archivos: `inside.dat` (dentro del círculo) y `outside.dat` (fuera).

## Requisitos

- Compilador C++ compatible con C++11 o superior (por ejemplo, `g++`).  
- Biblioteca estándar de C++ (no se requieren dependencias externas).  
- `xmgrace` instalado para la visualización gráfica de los puntos. En sistemas tipo Debian/Ubuntu se puede instalar con:  
  ```bash
  sudo apt install grace
  ```


## Compilación

Guarda el código en un archivo, por ejemplo `monte_carlo_pi.cpp`, y compila:

```bash
g++ -O3 -std=gnu++11 -o monte_carlo_pi monte_carlo_pi.cpp -lm
```

Notas:  
- Se usa `-std=gnu++11` o `-std=c++11` para asegurar soporte de `<random>`.  
- La opción `-O3` optimiza la ejecución para grandes valores de `N`.  
- `-lm` puede ser necesario en algunas plataformas para funciones matemáticas.

## Ejecución

Ejecuta el binario:

```bash
./monte_carlo_pi
```

La salida típica en consola incluye:

- Estimación numérica de $\(\pi\)$ y su intervalo de confianza aproximado.  
- Número de puntos dentro del círculo respecto al total.  
- Error relativo porcentual respecto a $\(\pi\)$ de la biblioteca estándar.

Además, se generan dos archivos de texto plano:

- `inside.dat`: contiene los puntos $\((x, y)\)$ que caen dentro del círculo.  
- `outside.dat`: contiene los puntos $\((x, y)\)$ que quedan fuera del círculo.

Cada archivo tiene dos columnas (x y y) separadas por espacios, una muestra por línea, en formato adecuado para ser leído por xmgrace.

## Visualización con xmgrace

Para visualizar los puntos y ver geométricamente cómo se estima $\(\pi\)$, ejecuta:

```bash
xmgrace -nxy inside.dat outside.dat
```

Esto abrirá xmgrace con dos conjuntos de datos:  
- `S0`: puntos dentro del círculo (`inside.dat`).  
- `S1`: puntos fuera del círculo (`outside.dat`).  

Dentro de la interfaz de xmgrace, se recomienda:

1. Ir a **Plot → Set appearance** (o botón “Set”).  
2. Seleccionar `S0` y configurar:  
   - **Symbol**: tipo de símbolo (por ejemplo, `circle`).  
   - **Fill**: activado (para que los puntos se vean sólidos).  
   - **Color**: rojo.  
3. Seleccionar `S1` y configurar:  
   - **Symbol**: mismo tipo o similar.  
   - **Fill**: activado.  
   - **Color**: azul.  
4. Ajustar los límites del gráfico a $\([-1.1, 1.1]\)$ en ambos ejes para ver bien el círculo inscrito.  

Con un número grande de puntos \(N\), los puntos rojos llenarán el disco unitario y los azules completarán el cuadrado, ilustrando visualmente el cociente de áreas que lleva a la estimación de $\(\pi\)$.[1]

## Parámetros y modificaciones

- El parámetro `N` controla el número de muestras y, por tanto, la precisión estadística del resultado.  
  ```cpp
  const int N = 1000000;  // Número de puntos
  ```
  Puedes aumentarlo o disminuirlo según el tiempo de cómputo disponible.  

- La región de muestreo está fijada en $\([-1, 1]\)$ para ambos ejes mediante:
  ```cpp
  std::uniform_real_distribution<double> dis(-1.0, 1.0);
  ```

- El programa usa `std::mt19937` inicializado con `std::random_device` para generar números pseudoaleatorios de alta calidad.[1]

- El cálculo del error utiliza una aproximación basada en un intervalo de confianza al 95% asumiendo comportamiento aproximadamente binomial/normal para la proporción de puntos dentro del círculo.

## Estructura del código

Bloques principales:

1. **Inicialización de generador y distribución**  
   - Definir `N`, generador Mersenne Twister y distribución uniforme en 2D.  

2. **Bucle de muestreo**  
   - Generar puntos, los clasifica como dentro/fuera del círculo, acumula contadores y almacena coordenadas.  

3. **Cálculo de estadísticos**  
   - Estimación de $\(\pi\)$.  
   - Estimación de error e impresión formateada por consola.  

4. **Salida a archivos**  
   - Escribir `inside.dat` y `outside.dat` para la visualización.  

5. **Mensaje final**  
   - Indicar los nombres de los archivos generados y cómo invocar xmgrace.

Este ejemplo sirve como plantilla básica para otros experimentos de Monte Carlo: basta con cambiar la región de aceptación (la condición `x*x + y*y <= 1.0`) y la función de interés para adaptarlo a nuevas integrales o problemas probabilísticos.[1]

[1](https://es.wikipedia.org/wiki/M%C3%A9todo_de_Montecarlo)
