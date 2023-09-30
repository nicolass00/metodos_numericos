def FLAGR(datos_x, datos_y, d, xm):   #Codgigo de la funcion FLAGR
    ym=0                      #Establezco inicialmente a ym igual a cero
    for i in range(0,d):      #Comienzo a evaluar cada polinomio de lagrange en xm
        Li=datos_y[i]         #Establezco inicialmente al polinomio i-esimo de lagrange evaluado en xm como yi
        for j in range(0,d):  #Evaluo el polinomio i-esimo de lagrange en xm a traves de una productoria
            if j != i:        #Desprecio un termino si j=i
                Li*=(xm-datos_x[j])/(datos_x[i]-datos_x[j])     #Realizo la productoria
        ym+=Li                #Sumo el resultado de la productoria a ym
    return ym                 #Devuelvo como salida de la funcion a ym

x = input('Ingrese los valores de x separados por ",": ') #Instruccion para ingresar un dato x
datos_x = x.replace(" ", "").split(",") #Convierte el ingreso de datos a un formato lista
n = len(datos_x) #Almacena en n la longitud de la lista anterior

y = input("Ingrese los valores de y separado por ',' de longitud " + str(n) + ": ") #Instruccion para ingresar un dato y
datos_y = y.replace(" ", "").split(",") #Convierte el ingreso de datos a un formato lista

if n == len(datos_y): #Comprueba la longitud de las dos listas
  d = int(input('Ingrese el grado del polinomio interpolante de Lagrange: '))   #Instruccion para ingresar el grado d
  xm = float(input('Ingrese el punto x que desea evaluar: '))                   #Instruccion para ingresar el punto xm

  X = [float(x) for x in datos_x] #Conversion de toda la lista en formato de string a float ej: ['1', '2'] a [1.0, 2.0]
  Y = [float(y) for y in datos_y] #Conversion de toda la lista en formato de string a float ej: ['1', '2'] a [1.0, 2.0]

  if n<(d+1):  #Si la cantidad de datos es menor a d+1, no se puede realizar la interpolacion
    print('Error: la interpolacion no es posible')    #Imprimo en pantalla mensaje de error
  else:        #Si no, procedo con la interpolacion
    ym=FLAGR(X, Y, d, xm)       #Ejecuto la funcion FLAGR con los datos de entrada
    print('La estimacion y(x) es: ', ym)    #Imprimo en pantalla el resultado ym

else:
  print("La longitud de los vectores no son iguales")
