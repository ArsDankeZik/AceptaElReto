#include <iostream>
#include <string>
/*
1. Lectura de datos
2. Parseo de datos
3. Ejecución de funciones
*/

void getInputData(std::string array){
    int n = 0;
    std::cout << "" << std::endl;
    std::cin >> n;

    for(int i = 0; i < n; i++){
        std::string aux = "";
        std::cin >> aux;
        array.push_back(aux);
    }
}

int main()
{

    return 0;
}
