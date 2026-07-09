# Modelo Lotka-Volterra

Es un sistema de ecuaciones diferenciales no lineales que se usa sobre todo para describir la interacción entre una **presa** y un **depredador**. En su forma clásica, predice oscilaciones cíclicas en las poblaciones: cuando abundan las presas, crecen los depredadores; cuando aumentan los depredadores, disminuyen las presas; y así sucesivamente. [es.wikipedia](https://es.wikipedia.org/wiki/Ecuaciones_de_Lotka-Volterra)

## Forma clásica

La formulación más conocida es:

$\[\frac{dx}{dt} = \alpha x - \beta xy\]$

$\[\frac{dy}{dt} = \delta xy - \gamma y\]$

Donde $\(x\)$ es la población de presas y $\(y\)$ la de depredadores. [pt.wikipedia](https://pt.wikipedia.org/wiki/Equa%C3%A7%C3%A3o_de_Lotka-Volterra)
Aquí, $\(\alpha\)$ representa el crecimiento natural de las presas, \(\beta\) el efecto de depredación, $\(\delta\)$ la conversión de presas en nuevos depredadores y \(\gamma\) la mortalidad natural de los depredadores. [pt.wikipedia](https://pt.wikipedia.org/wiki/Equa%C3%A7%C3%A3o_de_Lotka-Volterra)

## Qué asume el modelo

El modelo clásico hace varias simplificaciones fuertes: las presas crecen exponencialmente si no hay depredadores, los depredadores mueren si no hay presas, y la interacción entre ambas especies es proporcional al producto $\(xy\)$. Eso lo convierte en un modelo muy útil para entender dinámicas básicas, pero bastante idealizado. [es.wikipedia](https://es.wikipedia.org/wiki/Ecuaciones_de_Lotka-Volterra)

## Qué predice

En el caso ideal, el sistema produce ciclos periódicos o cuasiperiódicos de presa y depredador. Sin embargo, en sistemas reales estos ciclos suelen deformarse por factores como competencia interna, recursos limitados, migración, enfermedades o cambios ambientales. [nationalgeographic.com](https://www.nationalgeographic.com.es/ciencia/lotka-volterra-ecuaciones-que-comparten-biologos-y-economistas_23153)

## Extensiones útiles

También existe una versión de **competencia** de Lotka–Volterra para dos especies que compiten por recursos, donde aparecen términos de capacidad de carga e interferencia entre especies. Esa formulación es muy usada en ecología matemática porque permite estudiar coexistencia, exclusión competitiva y equilibrio entre poblaciones. [espanol.libretexts](https://espanol.libretexts.org/Bookshelves/Biologia/Ecologia/Ecolog%C3%ADa_Cuantitativa_-_Un_Nuevo_Enfoque_Unificado_(Lehman,_Loberg_y_Clark)/16:_Competencia/16.08:_Formulaci%C3%B3n_Lotka-Volterra)

## Cómo leerlo desde tu enfoque

Si se mira desde un modelado computacional, Lotka–Volterra es un excelente punto de partida porque permite explorar estabilidad, retratos de fase, sensibilidad paramétrica e intuición sobre sistemas no lineales. También es una base natural para pasar a modelos más realistas con términos logísticos, retardos, difusión espacial o formulaciones PDE.
