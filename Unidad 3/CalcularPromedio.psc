Algoritmo CalcularPromedio
	Definir  calificacion1, calificacion2, calificacion3, suma, promedio Como Real
	
	Escribir "Ingresa la calificacion1:"
	Leer calificacion1
	
	Escribir "Ingresa la calificacion2:"
	Leer calificacion2
	
	Escribir "Ingresa la calificacion3:"
	Leer calificacion3
	
	suma = calificacion1 + calificacion2 + calificacion3
	promedio = suma / 3
	
	Escribir "El promedio es; ", promedio
	
	Si calificacion1 > calificacion2 Entonces
		temp = calificacion1
		calificacion1 = calificacion2
		calificacion2 = temp
	FinSi
	
	Si calificacion2 > calificacion3 Entonces
		temp = calificacion2
		calificacion2 = calificacion3
		calificacion3 = temp
		
		Si calificacion1 > calificacion2 Entonces
			temp = calificacion1
			calificacion1 = calificacion2
			calificacion2 = temp
		FinSi
	FinSi
	
	Escribir "Calificaciones ordenadas de menor a mayor: " ,calificacion1 ", ", calificacion2 ", ", calificacion3
FinAlgoritmo
