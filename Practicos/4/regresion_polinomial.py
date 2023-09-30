import numpy as np      #Importo la libreria numpy
from math import sqrt   #De la libreria math importo la funcion sqrt

x = input('Ingrese los valores de x separados por ",": ') #Instruccion para ingresar un dato x
x_arr = x.replace(" ", "").split(",") #Convierte el ingreso de datos a un formato lista
n = len(x_arr) #Almacena en n la longitud de la lista anterior

y = input("Ingrese los valores de y separado por ',' de longitud " + str(n) + ": ") #Instruccion para ingresar un dato y
y_arr = y.replace(" ", "").split(",") #Convierte el ingreso de datos a un formato lista

if n == len(y_arr): #Comprueba la longitud de las dos listas
  m = int(input('Ingrese el grado de la regresion polinomial: '))   #Instruccion para ingresar el grado m

  datos_x = [float(x) for x in x_arr] #Conversion de toda la lista en formato de string a float ej: ['1', '2'] a [1.0, 2.0]
  datos_y = [float(y) for y in y_arr] #Conversion de toda la lista en formato de string a float ej: ['1', '2'] a [1.0, 2.0]

  if n<(m+1):  #Si la cantidad de datos es menor a m+1, no se puede realizar la regresion
      print('Error: la regresion no es posible')                #Imprimo mensaje de error
  else:
      Y=[]              #Vector Y que corresponde al sistema lineal Xa=Y
      X=[]              #Matriz X que corresponde al sistema lineal Xa=Y

      for i in range(0,(m+1)):                 #Creo la matriz X
          xi=[]                                #Array nulo que almacenara los datos de fila
          for j in range(0,(m+1)):             #Creo cada fila de X
              xj=0                             #Variable que almacenara un elemento de la matriz
              for k in range(0,n):             #Creo cada elemento de la fila
                  xj+=(datos_x[k])**(2*m-j-i)  #Hago la sumatoria de los datos de x elevados a una potencia
              xi.append(xj)                    #Almaceno el resultado en xi
          X.append(xi)                         #Completa la fila xi, la almaceno en la matriz X

      for i in range(0,(m+1)):                 #Creo el vector Y
          yi=0                                 #Variable que almacenara un elemento del vector
          for k in range(0,n):                 #Creo cada elemento del vector
              #Hago la sumatoria del producto de los datos de x e y. Con x elevado a una potencia
              yi+=(datos_y[k])*((datos_x[k])**(m-i))
          Y.append(yi)                         #Almaceno el resultado en el vector Y

  X = np.array(X, dtype = "float")    #Con la matriz X ya completa, la convierto a ndarray
  Y = np.array(Y, dtype = "float")    #Con el vector Y ya completo, lo convierto a ndarray
  a = np.linalg.solve(X, Y)           #Resuelvo el sistema lineal Xa=Y
  print('Los coeficientes del polinomio de regresion son:', a)   #Imprimo el vector de coeficientes solucion

  Sr=0                                     #Variable que almacenara la sumatoria de cuadrados de residuo
  for i in range(0,n):                     #Calculo la sumatoria de cuadrados de residuo
      ei=datos_y[i]                        #Establezco al residuio i-esimo como el dato yi
      for j in range(0,(m+1)):             #Bucle for para calcular el residuo i-esimo completo
          ei-=a[m-j]*(datos_x[i]**j)       #Comienzo a restarle terminos aj*xi**j
      Sr+=ei**2                            #Elevo al cuadrado el residuo i-esimo y lo agrego en la suma

  Syx=sqrt(Sr/(n-(m+1)))                   #Calculo el error estandar
  print('El error estandar para la regresion es:', Syx)      #Imprimo en pantalla el error estandar

else:
  print("La longitud de los vectores no son iguales")
