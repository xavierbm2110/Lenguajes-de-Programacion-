#include <iostream>
#include <random>
#include <iomanip> 
using namespace std;

int main() {
    int pares = 0, impares = 0;

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(50, 100);

    cout << "Numeros generados:\n";

    for (int i = 0; i < 500; i++) {
        int numero = dist(gen);
        cout << numero << " "; 
        
        if (numero % 2 == 0) {
            pares++;
        } else {
            impares++;
        }

 
        if ((i + 1) % 20 == 0) cout << "\n";
    }

    cout << "\n\nCantidad de numeros pares: " << pares << "\n";
    cout << "Cantidad de numeros impares: " << impares << "\n";

    double total = pares + impares;
    cout << fixed << setprecision(2); 
    cout << "Porcentaje pares: " << (pares / total) * 100 << "%\n";
    cout << "Porcentaje impares: " << (impares / total) * 100 << "%\n";

    return 0;
}
