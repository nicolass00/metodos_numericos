Algoritmo promAlumno
	Escribir "Ingrese la primera calificacion";
	Leer q1;
	
	Escribir "Ingrese la segunda calificacion";
	Leer q2;
	
	Escribir "Ingrese la tercera calificacion";
	Leer q3;
	
	final <- (q1+q2+q3) / 3;
	Escribir "Promedio: " final;
	
	Si final Es Menor A 4 Entonces
		Escribir "El alumno desaprobo"
	SiNo
		Escribir "El alumno aprobo"
	FinSi
FinAlgoritmo
