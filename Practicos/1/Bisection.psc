Funcion _y <- f(x)
	_y <- -6*x^2+9*x+2
FinFuncion

Funcion _y <- g(a, b)
	_y <- (a+b)/2
FinFuncion

Algoritmo Bisection
	Leer a
	Leer b
	Leer acc
	
	Definir c Como Real
	
	Si f(a)*f(b) < 0 Entonces
		Escribir "En el intervalo hay una raiz"
		c <- g(a, b)
		
		Si f(a)*f(c) < 0 Entonces
			b <- c
		SiNo
			a <- c
		FinSi
		
		Mientras abs(a-b) >= acc
			Si f(a)*f(b) < 0 Entonces
				c <- g(a, b)
				
				Si f(a)*f(c) < 0 Entonces
					b <- c
				SiNo
					a <- c
				FinSi
				
				Escribir "Mid val " c
				//Escribir "A " a
				//Escribir "B" b
			FinSi
			
		FinMientras
		
		Escribir "El valor es: " f(b)
	SiNo
		Escribir "No hay raices"
	FinSi
FinAlgoritmo
