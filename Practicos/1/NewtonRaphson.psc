Funcion yf <- f ( x )
	yf=cos(x)-x^3
Fin Funcion
Funcion yf_prima <- f_prima ( x )
	yf_prima=-sen(x)-3*x^2
Fin Funcion
Algoritmo NewtonRaphson
	Definir Xo Como Real
	Escribir "Ingrese un valor de prueba"
	Leer Xo
	Definir t Como Real
	Escribir "Ingrese un valor de tolerancia"
	Leer t
	X1=Xo-f(Xo)/f_prima(Xo)
	Mientras abs(X1-Xo)>t
		Xo=X1
		X1=Xo-f(Xo)/f_prima(Xo)
	FinMientras
	Escribir "El valor de la raiz es:"
	Escribir Xo
FinAlgoritmo
