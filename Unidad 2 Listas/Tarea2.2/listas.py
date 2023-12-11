#Listas Practica 1
Itic3 = ["Jonathan de Jesus Garcia Rodriguez","Nahum Santiago Espinoza Herrera","Eduardo Flores Gallegos","Juan De Dios Prieto Roman","Sajith Alexandro Montaño Grimaldo"]
Carreras_Itpa = ["Logistica", "ITIC", "Gestion Empresarial","Mecatronica","Industrial"]
Edades = [18, 18, 19, 20, 20, 19, 19, 18, 19, 19, 19, 19]

#Imprimir lista 
print(Carreras_Itpa)
print(Itic3)
print(Edades)

#Imprimr el tercer campo de cada lista
print(Carreras_Itpa[2])

#Agregar elementos al final de la lista
Itic3.append('Xitlali')
print(Itic3)

#Agregar otra lista
Itic3.extend('Juan')
print(Itic3)

#Agregar elemento en la posicion 5 
Itic3.insert(4,"Pikillo")
print(Itic3)

#Borrar un elemento determinado
del Edades[0]
print(Edades)

#Ver el tamaño de nuestras listas
print(len(Edades))
print(len(Itic3))
print(len(Carreras_Itpa))

#Eliminar un elemento en especifico
Edades.remove(19)
print(Edades)
print("-----------------------------------------")
#Ordenar elementos
print(Edades)
Edades.sort()
print(Edades)