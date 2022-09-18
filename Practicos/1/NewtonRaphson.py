# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sin, cos

# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducción no es correcta.

def f(x):
	yf = cos(x)-x**3
	return yf

def f_prima(x):
	yf_prima = -sin(x)-3*x**2
	return yf_prima

if __name__ == '__main__':
	xo = float()
	print("Ingrese un valor de prueba")
	xo = float(input())
	t = float()
	print("Ingrese un valor de tolerancia")
	t = float(input())
	x1 = xo-f(xo)/f_prima(xo)
	while abs(x1-xo)>t:
		xo = x1
		x1 = xo-f(xo)/f_prima(xo)
	print("El valor de la raiz es: " + str(xo))