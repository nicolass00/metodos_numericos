import numpy as np      #Importo la libreria numpy

x = input('Ingrese los valores de x separados por ",": ') #Instruccion para ingresar un dato x
datos_x = x.replace(" ", "").split(",") #Convierte el ingreso de datos a un formato lista
n = len(datos_x) #Almacena en n la longitud de la lista anterior

y = input("Ingrese los valores de y separado por ',' de longitud " + str(n) + ": ") #Instruccion para ingresar un dato y
datos_y = y.replace(" ", "").split(",") #Convierte el ingreso de datos a un formato lista

if n == len(datos_y): #Comprueba la longitud de las dos listas

  Y = [float(y) for y in datos_y] #Conversion de toda la lista en formato de string a float ej: ['1', '2'] a [1.0, 2.0]
  
  X=[]                       #Vector X que corresponde al sistema lineal Xa=Y
  for i in range(n):         #Creo la matriz X
    xi=[]                    #Array nulo que almacenara los datos de fila
    for j in range(n):     #Creo cada fila de X
        xj=(float(datos_x[i]))**j   #Tomo un dato de X y lo elevo a la potencia igual a su posicion en su columna
        xi.append(xj)        #Almaceno el resultado en xi
    X.append(xi)             #Completa la fila xi, la almaceno en la matriz X

  X = np.array(X, dtype = "float")    #Con la matriz X ya completa, la convierto a ndarray
  Y = np.array(Y, dtype = "float")    #Convierto el vector Y a ndarray
  a = np.linalg.solve(X, Y)           #Resuelvo el sistema lineal Xa=Y

  print('Los coeficientes del polinomio interpolante son:', a)      #Imprimo en pantalla el vector de coeficientes solucion

else:
  print("La longitud de los vectores no son iguales")
