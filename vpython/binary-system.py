# Simulación de un sistema binario con VPython
# En este ejemplo se simula un sistema binario con dos objetos que se atraen mutuamente por la fuerza gravitacional.
# El objeto "giant" es más masivo que el objeto "dwarf", por lo que ambos objetos orbitan alrededor de un centro de masa común.
# Para ejecutar este código, asegúrate de tener VPython instalado y ejecuta el script en un entorno compatible con VPython (como Jupyter Notebook o un entorno de desarrollo que soporte VPython).
# Nota: Este código es una simplificación de un sistema binario real y no tiene en cuenta factores como la relatividad, la resistencia del aire, o la interacción con otros objetos en el espacio. Es solo una simulación básica para ilustrar los conceptos de la gravedad y el movimiento orbital.
# Para mejorar la simulación, puedes ajustar los parámetros como las masas, las posiciones iniciales, y las velocidades de los objetos. También puedes agregar más objetos al sistema para simular un sistema solar completo o una galaxia. ¡Diviértete experimentando con la simulación!
# Importamos la biblioteca VPython para crear la simulación visual
# VPython es una biblioteca de Python que permite crear gráficos 3D interactivos de manera sencilla, ideal para simular fenómenos físicos como el movimiento de objetos bajo la influencia de fuerzas.
# En este caso, utilizaremos VPython para simular un sistema binario, donde dos objetos se atraen mutuamente por la fuerza gravitacional. La simulación mostrará cómo ambos objetos orbitan alrededor de un centro de masa común debido a esta atracción.
# Asegúrate de tener VPython instalado en tu entorno de Python para ejecutar este código. Puedes instalarlo usando pip:
# pip install vpython
# Una vez que tengas VPython instalado, puedes ejecutar este código en un entorno compatible, como Jupyter Notebook o cualquier entorno de desarrollo que soporte VPython. Al ejecutar el código, verás una representación visual de dos esferas (representando los objetos del sistema binario) orbitando alrededor de un punto común debido a la fuerza gravitacional entre ellas. Puedes ajustar los parámetros como las masas, las posiciones iniciales y las velocidades para observar diferentes comportamientos en la simulación. ¡Disfruta explorando el fascinante mundo de la física con VPython!
# El código simula un sistema binario con dos objetos que se atraen mutuamente por la fuerza gravitacional. El objeto "giant" es más masivo que el objeto "dwarf", por lo que ambos objetos orbitan alrededor de un centro de masa común. La simulación muestra cómo ambos objetos se mueven bajo la influencia de la gravedad, y puedes ajustar los parámetros para observar diferentes comportamientos en la simulación.
# Para mejorar la simulación, puedes agregar más objetos al sistema para simular un sistema solar completo o una galaxia, o incluso incluir efectos relativistas para una simulación más precisa. ¡Diviértete experimentando con la simulación y explorando los conceptos de la física con VPython!
# Simulación de un sistema binario con VPython
from vpython import *

scene.caption = ""
scene.forward = vector(0,-.3,-1)

G = 6.7e-11 # Constante Gravitacional

#Primer Objeto
giant = sphere(pos=vector(-1e11,0,0), radius=2e10, color=color.red, 
                make_trail=True, trail_type='points', interval=10, retain=50)
# Su masa
giant.mass = 2e30
giant.p = vector(0, 0, -1e4) * giant.mass

#Segundo Objeto
dwarf = sphere(pos=vector(1.5e11,0,0), radius=1e10, color=color.yellow,
                make_trail=True, interval=10, retain=50)
# Su masa
dwarf.mass = 1e30
dwarf.p = -giant.p

# Paso de tiempo
dt = 1e5
while True:
    rate(200)
    r = dwarf.pos - giant.pos # Distancia entre ambos objetos
    F = G * giant.mass * dwarf.mass * r.hat / mag2(r) # Fuerza gravitacional    
    # ¿Que unidades fisicas tiene giant.p?     
    giant.p = giant.p + F*dt
    # ¿Que unidades fisicas tiene dwarf.p?    
    dwarf.p = dwarf.p - F*dt
    # ¿A que ecuacion de cinematica se les parece estas ecuaciones?     
    giant.pos = giant.pos + (giant.p/giant.mass) * dt 
    dwarf.pos = dwarf.pos + (dwarf.p/dwarf.mass) * dt