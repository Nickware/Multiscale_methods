% Lotka-Volterra model (predator-prey model)
% dx(1)/dt = a1*x(1) - a2*x(1
% dx(2)/dt = -b1*x(2) + b2*x(1)*x(2)
% a1: tasa de crecimiento de la presa
% a2: tasa de depredación
% b1: tasa de mortalidad del depredador
% b2: tasa de reproducción del depredador por cada presa consumida
% El sistema se resuelve numéricamente utilizando el método de Runge-Kutta de orden 4 (RK4).

function dx = lotka_volterra(x, t)
  a1 = 0.48;
  a2 = 0.025;
  b1 = 0.93;
  b2 = 0.028;
  dx = zeros(2,1);
  dx(1) = a1*x(1) - a2*x(1)*x(2);  # Ecuación para la presa
  dx(2) = -b1*x(2) + b2*x(1)*x(2); # Ecuación para el depredador
endfunction

