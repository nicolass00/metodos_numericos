// Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
// Es posible que el codigo generado no sea completamente correcto. Si encuentra
// errores por favor reportelos en el foro (http://pseint.sourceforge.net).

#include<iostream>
#include<cmath>
using namespace std;

// Para leer variables de texto se utiliza el operador << del objeto cin, que
// lee solo una palabra. Para leer una linea completa (es decir, incluyendo los
// espacios en blanco) se debe utilzar getline (ej, reemplazar cin>>x por
// getline(cin,x)), pero obliga a agregar un cin.ignore() si antes del getline
// se leyó otra variable con >>.

// Declaraciones adelantadas de las funciones
float f(float x);
float f_prima(float x);

float f(float x) {
	float yf;
	yf = cos(x)-pow(x,3);
	return yf;
}

float f_prima(float x) {
	float yf_prima;
	yf_prima = -sin(x)-3*pow(x,2);
	return yf_prima;
}

int main() {
	float t;
	float x1;
	float xo;
	cout << "Ingrese un valor de prueba" << endl;
	cin >> xo;
	cout << "Ingrese un valor de tolerancia" << endl;
	cin >> t;
	x1 = xo-f(xo)/f_prima(xo);
	while (abs(x1-xo)>t) {
		xo = x1;
		x1 = xo-f(xo)/f_prima(xo);
	}
	cout << "El valor de la raiz es:" << endl;
	cout << xo << endl;
	return 0;
}

