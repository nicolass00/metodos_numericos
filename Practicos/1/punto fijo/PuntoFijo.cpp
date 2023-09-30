#include<iostream>
#include<cmath>
using namespace std;

//Define una equacion cualquiera
float f(float x) {
	return sin(x); //PlaceHolder
}

//Define la derivada de la equacion anterior
float fd(float x) {
	return cos(x);
}

int main() {
    //Declara las variables necesarias
	float Xo;
	float acc;
	
	std::cout << "Ingrse un punto inicial ";
	std::cin >> Xo; //Lee el punto inicual
	
	std::cout << "Introduzca la presicion ";
	std::cin >> acc; //Lee el punto superior
	
	if(abs(fd(Xo)) < 1) { //Comprueba la condicion de convergencia del metodo
		std::cout << "En el intervalo hay al menos una raiz" << '\n';
		
		float X1 = f(Xo); //Obtengo F(x) en el punto inicial para evaluar la precision de la aproximacion
		//Me mantengo dentro del bucle while mientras la precision alcanzada sea mayor que la requerida
		while (abs(X1-Xo) >= acc) {
			Xo = X1; //Igualo el resultado de la iteracion anterior para valuar nuevamente la ecuacion
			X1 = f(Xo); //Valuo la ecuacion para resolver g(x) = x
		}
		
		std::cout << "El valor es: " << Xo << '\n';
	}
	else {
		std::cout << "No hay raices" << '\n';
	}
	
	return 0;
}
