function dx = lotka_volterra(x, t)
  a1 = 0.48;
  a2 = 0.025;
  b1 = 0.93;
  b2 = 0.028;
  dx = zeros(2,1);
  dx(1) = a1*x(1) - a2*x(1)*x(2);  # Ecuación para la presa
  dx(2) = -b1*x(2) + b2*x(1)*x(2); # Ecuación para el depredador
endfunction

