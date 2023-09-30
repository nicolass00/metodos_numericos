//Define una equacion cualquiera
Funcion _y <- f(x)
	_y <- sen(x) //PlaceHolder
FinFuncion

//Define la derivada de la equacion anterior
Funcion _y <- fd(x)
	_y <- cos(x)
FinFuncion

Algoritmo NewtonRaphson
	Escribir "Ingrese un punto inicial"
	Leer Xo //Lee el punto inicial
	Escribir "Ingrese la presicion"
	Leer acc //Lee la presicion
	
	X1 <- Xo-f(Xo)/fd(Xo) //Evaluo la ecuacion y su derivada en el punto inicial 
	Mientras abs(X1-Xo) > acc Hacer
		Xo <- X1 //Evaluo la ecuacion y su derivada en el punto inicial
		X1 <- Xo-f(Xo)/fd(Xo) //Evaluo la ecuacion y su derivada en el punto inicial 
		
		Escribir "El resultado x0: " Xo
		Escribir "El resultado f(x0): " f(Xo)
	FinMientras
	
	Escribir "El resultado es: " Xo
FinAlgoritmo