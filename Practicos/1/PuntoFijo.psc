Funcion _y <- f(x)
	_y <- -0.1*x^2+0.05*x+2
FinFuncion
Funcion _y <- f1(x)
	_y <- -(-0.1*x^2+2)/0.5
FinFuncion
Funcion _y <- fd(x)
	_y <- -0.2*x+0.05
FinFuncion

Algoritmo PuntoFijo
	Leer X0
	Leer acc
	
	Si abs(fd(X0)) < 1 Entonces
		Escribir "La funcion se puede calcular"
		X1 <- f1(X0)
		Escribir "El resultado x0: " X0
		Escribir "El resultado f(x0): " f1(X0)
		
	    Mientras abs(X1-X0) >= acc Hacer
		//Mientras abs(f1(X0)) >= acc Hacer
			X0 <- X1
			X1 <- f1(X0)
			
			Escribir "El resultado x0: " X0
			Escribir "El resultado f(x0): " f1(X0)
			
		Fin Mientras
		
		Escribir "El resultado es: " x0
		
	SiNo
		Escribir "La funcion no se puede aproximar por este metodo"
	FinSi
FinAlgoritmo