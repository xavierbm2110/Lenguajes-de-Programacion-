#include <iostream>
#include <random>
using namespace std;

int main() {
    int valores[10];  
    int suma = 0;     
    float promedio;   

    random_device rd;  
    mt19937 gen(rd()); 
    uniform_int_distribution<> dist(1, 100);

    cout << "Valores generados aleatoriamente:\n";
    for(int i = 0; i < 10; i++) {
        valores[i] = dist(gen); 
        cout << " Valor " << i + 1 << ": " << valores[i] << endl;
        suma += valores[i];  
    }

    promedio = suma / 10.0;

    cout << "\nLa suma de los valores es: " << suma << endl;
    cout << "El promedio de los valores es: " << promedio << endl;

    return 0;
}
