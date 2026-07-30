"""
Parámetros físicos para la simulación de minimización de energía del etano (C2H6).
"""

# Masas atómicas [uma]
m_C = 12.011
m_H = 1.008

# Constantes de enlace y ángulo
k_bond = 450.0     # constante de enlace [kcal/mol/Å^2]
k_angle = 60.0     # constante angular  [kcal/mol/rad^2]
k_dihedral = 2.0   # constante dihedral [kcal/mol] (declarada, no usada en este modelo)

# Geometría de equilibrio
r_eq = 1.09        # distancia de equilibrio C-H [Å]
r_CC_eq = 1.54     # distancia de equilibrio C-C [Å]
theta_eq = 109.47  # ángulo de equilibrio tetraédrico [grados]

# Integración temporal
dt = 0.001         # paso de tiempo reducido [fs] (ver nota de unidades en el README)
steps = 10000      # número de pasos de la simulación

# Amortiguamiento (para acelerar la relajación hacia el mínimo)
damping = 0.3

# Factor de conversión de unidades: convierte fuerza [kcal/mol/Å] y masa [uma]
# en aceleración [Å/fs^2]. Sin este factor, la aceleración resultante es ~2390
# veces mayor que la física real, lo que vuelve inestable al integrador
# (la energía diverge en vez de minimizarse). Ver README para la derivación.
ACCEL_CONV = 4.184e-4
