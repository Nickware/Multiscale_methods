% Lotka-Volterra model for the Hudson Bay Company data
% The data is from the Hudson Bay Company, which recorded the populations of lynx and hares over time. The model is given by the following system of ordinary differential equations:
% dx/dt = ax - bxy
% dy/dt = -cy + dxy
% where x is the population of hares, y is the population of lynx, and a, b, c, d are positive constants that represent the interaction between the two species. The parameters can be estimated from the data, and the model can be used to predict the population dynamics of
% the two species over time.

x0 = [35; 4];
t = linspace(0, 20, 200)';
y = lsode(@lotka_volterra, x0, t);
plot(t, y(:,1), 'g', t, y(:,2), 'b');
xlabel('Años desde 1900');
ylabel('Población (miles)');
legend('Liebre', 'Lince');
title('Modelo Lotka-Volterra Hudson Bay Company');


