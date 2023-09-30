//Define una equacion cualquiera
Funcion _y <- f(x)
	_y <- sen(x) //PlaceHolder
FinFuncion

//Define la derivada de la equacion anterior
Funcion _y <- fd(x)
	_y <- cos(x)
FinFuncion

Algoritmo PuntoFijo
	Escribir "Ingrese un punto inicial"
	Leer Xo //Lee el punto inicual
	Escribir "Ingrese la presicion"
	Leer acc //Lee el punto superior
	
	Si abs(fd(Xo)) < 1 Entonces //Comprueba la condicion de convergencia del metodo
		Escribir "La funcion se puede calcular"
		X1 <- f(Xo) //Obtengo F(x) en el punto inicial para evaluar la precision de la aproximacion
		
		//Me mantengo dentro del bucle while mientras la precision alcanzada sea mayor que la requerida
	    Mientras abs(X1-Xo) >= acc Hacer
			Xo <- X1 //Igualo el resultado de la iteracion anterior para valuar nuevamente la ecuacion
			X1 <- f(Xo) //Valuo la ecuacion para resolver g(x) = x
		Fin Mientras
		
		Escribir "El resultado es: " Xo
		
	SiNo
		Escribir "La funcion no se puede aproximar por este metodo"
	FinSi
FinAlgoritmo