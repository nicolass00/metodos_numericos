//Define una equacion cualquiera
Funcion _y <- f(x)
	_y <- -6*x^2+9*x+2  //PlaceHolder
FinFuncion

//Esta funcion se utiliza para obtener el punto medio entre dos puntos
Funcion _y <- g(a, b)
	_y <- (a+b)/2
FinFuncion

Algoritmo Bisection
	Leer a //Lee el punto inferior
	Leer b //Lee el punto superior
	Leer acc //Lee la presicion
	
	Definir c Como Real
	
	Si f(a)*f(b) < 0 Entonces //Comprueba si existe una raiz en el intervalo dado
		Escribir "En el intervalo hay una raiz"
		c <- g(a, b)
		
		Si f(a)*f(c) < 0 Entonces //Comprueba si existe una raiz en el intervalo [a,c]
			b <- c
		SiNo //Sino existe una raiz en el intervalo [c,b]
			a <- c
		FinSi
		
		//En este bloque while se hace antes descripto, mientras que la presicion sea menor que la presicion hasta el momento 
		Mientras abs(a-b) >= acc
			Si f(a)*f(b) < 0 Entonces
				c <- g(a, b)
				
				Si f(a)*f(c) < 0 Entonces //Comprueba si existe una raiz en el intervalo [a,c]
					b <- c
				SiNo //Sino existe una raiz en el intervalo [c,b]
					a <- c
				FinSi
				
				Escribir "Mid val " c //Imprime el valor de la Raiz calculada hasta ahora
				//Escribir "A " a
				//Escribir "B" b
			FinSi
			
		FinMientras
		
		Escribir "El valor es: " c //Imprime el valor de la Raiz calculada
	SiNo
		Escribir "No hay raices"
	FinSi
FinAlgoritmo
