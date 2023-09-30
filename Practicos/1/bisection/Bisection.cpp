#include<iostream>
#include<cmath>
using namespace std;

//Define una equacion cualquiera
float f(float x) {
	return -6*pow(x, 2) + 9*x + 2; //PlaceHolder
}

//Esta funcion se utiliza para obtener el punto medio entre dos puntos
float g(float a, float b) {
	return (a+b)/2;
}

int main() {
    //Declara las variables necesarias
	float a;
	float b;
	float acc;
	
	std::cout << "Introduzca el limite inferior ";
	std::cin >> a; //Lee el punto inferior
	
	std::cout << "Introduzca el limite superior ";
	std::cin >> b; //Lee el punto superior
	
	std::cout << "Introduzca la presicion ";
	std::cin >> acc; //Lee la presicion
	
	if(f(a)*f(b) < 0) { //Comprueba si existe una raiz en el intervalo dado
		std::cout << "En el intervalo hay al menos una raiz" << '\n';

        //En este bloque while se hace antes descripto, mientras que la presicion sea menor que la presicion hasta el momento
		while (abs(a-b)>=acc) {
			float c = g(a, b);

			if(f(a)*f(c) < 0)  b = c; //Comprueba si existe una raiz en el intervalo [a,c]
			else a = c; //Sino existe una raiz en el intervalo [c,b]

			std::cout << "Mid val: " << c << '\n'; //Imprime el valor de la Raiz calculada hasta ahora
		}

		std::cout << "El valor es: " << f(g(a, b)) << '\n'; //Imprime el valor de la Raiz calculada
	}
	else {
		std::cout << "No hay raices" << '\n';
	}
	
	return 0;
}
