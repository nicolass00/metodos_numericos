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
	float Xo;
	float acc;
	
	std::cout << "Ingrse un punto inicial ";
	std::cin >> Xo; //Lee el punto inicial
	
	std::cout << "Introduzca la presicion ";
	std::cin >> acc; //Lee la presicion
	
	if(abs(fd(Xo)) < 1) { //Comprueba la condicion de convergencia del metodo
		std::cout << "En el intervalo hay al menos una raiz" << '\n';
		
		float X1 = f(Xo); //Evaluo la ecuacion y su derivada en el punto inicial
		while (abs(X1-Xo) >= acc) {
			Xo = X1; //Evaluo la ecuacion y su derivada en el punto inicial
			X1 = Xo-f(Xo)/fd(Xo); //Evaluo la ecuacion y su derivada en el punto inicial
		}
		
		std::cout << "El valor es: " << Xo << '\n';
	}
	else {
		std::cout << "No hay raices" << '\n';
	}
	
	return 0;
}
