#include<iostream>
#include<cmath>
using namespace std;

float f(float x) {
	return -6*pow(x, 2) + 9*x + 2;
}

float g(float a, float b) {
	return (a+b)/2;
}

int main() {
	float a;
	float b;
	float acc;
	
	std::cout << "Introduzca el limite inferior ";
	std::cin >> a;
	
	std::cout << "Introduzca el limite superior ";
	std::cin >> b;
	
	std::cout << "Introduzca la presicion ";
	std::cin >> acc;
	
	if(f(a)*f(b) < 0) {
		std::cout << "En el intervalo hay al menos una raiz" << '\n';
		
		while (abs(a-b)>=acc) {
			float c = g(a, b);
			
			if(f(a)*f(c) < 0)  b = c;
			else a = c;
			
			std::cout << "Mid val: " << c << '\n';
		}
		
		std::cout << "El valor es: " << f(g(a, b)) << '\n';
	}
	else {
		std::cout << "No hay raices" << '\n';
	}
	
	return 0;
}
