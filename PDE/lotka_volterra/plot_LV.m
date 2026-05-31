x0 = [35; 4];
t = linspace(0, 20, 200)';
y = lsode(@lotka_volterra, x0, t);
plot(t, y(:,1), 'g', t, y(:,2), 'b');
xlabel('Años desde 1900');
ylabel('Población (miles)');
legend('Liebre', 'Lince');
title('Modelo Lotka-Volterra Hudson Bay Company');


