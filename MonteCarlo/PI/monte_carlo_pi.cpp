#include <iostream>
#include <fstream>
#include <random>
#include <vector>
#include <cmath>
#include <iomanip>

int main() {
    const int N = 1000000;  // Número de puntos (ajustable para precisión)
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> dis(-1.0, 1.0);

    int inside = 0;
    std::vector<double> x_inside, y_inside, x_outside, y_outside;

    // Generar puntos y contar
    for (int i = 0; i < N; ++i) {
        double x = dis(gen);
        double y = dis(gen);
        if (x*x + y*y <= 1.0) {
            ++inside;
            x_inside.push_back(x);
            y_inside.push_back(y);
        } else {
            x_outside.push_back(x);
            y_outside.push_back(y);
        }
    }

    double pi_estimate = 4.0 * inside / N;
    double error = 1.96 * std::sqrt(4.0 * pi_estimate * (1.0 - pi_estimate / 4.0) / N); // IC 95%

    std::cout << std::fixed << std::setprecision(6);
    std::cout << "Estimación de π: " << pi_estimate << " ± " << error << std::endl;
    std::cout << "Puntos dentro: " << inside << "/" << N << std::endl;
    std::cout << "Error relativo: " << std::abs(pi_estimate - M_PI)/M_PI*100 << "%" << std::endl;

    // Generar archivos para xmgrace
    std::ofstream file_inside("inside.dat");
    std::ofstream file_outside("outside.dat");
    
    for (size_t i = 0; i < x_inside.size(); ++i) {
        file_inside << x_inside[i] << " " << y_inside[i] << "\n";
    }
    for (size_t i = 0; i < x_outside.size(); ++i) {
        file_outside << x_outside[i] << " " << y_outside[i] << "\n";
    }
    
    file_inside.close();
    file_outside.close();

    std::cout << "\nArchivos generados: inside.dat, outside.dat" << std::endl;
    std::cout << "Usa xmgrace -nxy inside.dat outside.dat para visualizar" << std::endl;
    
    return 0;
}
