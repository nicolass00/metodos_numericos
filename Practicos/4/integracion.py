from math import * #Este import agrega todas las funciones matematicas para ser introducidad por consola

f = lambda x: eval(fun) #Este bloque permite que se ingresen funciones por consola

#Algoritmo de integracion
def integracion(a,b,m):
    error = "null" #Esta variable almacena codigos de error
    i = 0 #Esta variable almacena el resultado de la integracion

    if m == 1:
        print('Metodo del Trapecio')
        if clase =='s':
            #Calculo directo con la formula
            i=(b-a)*(f(a)+f(b))/2
        elif clase =='c':
            #Divido el intervalo en n subintervalos y sumo los trapecios
            n=int(input('Ingrese cantidad de subintervalos>>'))
            h=(b-a)/n
            i=0
            for j in range(0,n):
                i+=h*(f(a+j*h)+f(a+(j+1)*h))/2
        else:
          error = "La clase del metodo no se reconoce, recuerda que podes escribir: Simple (s), Compuesta (c)"
    elif m == 2:
        print('Metodo de Simpson 1/3')
        if clase =='s':
            #Calculo directo con la formula
            h=(b-a)/2
            i=h*(f(a)+4*f((a+b)/2)+f(b))/3
        elif clase =='c':
            #Divido el intervalo en n subintervalos
            n=int(input('Ingrese cantidad de subintervalos>>'))
            h=(b-a)/n
            i=f(a)+f(b)
            #Calculo dos sumatorias
            for j in range(1,n):
                #Si j es par, multiplico por 2, caso contrario multiplico por 4 (Revisar formula para compuesta para mas info)
                if j%2 == 0:
                    i+=2*f(a+j*h)
                else:
                    i+=4*f(a+j*h)
            #Multiplico el resultado de las sumatorias por el factor 1/3
            i*=h/3
        else:
          error = "La clase del metodo no se reconoce, recuerda que podes escribir: Simple (s), Compuesta (c)"
    elif m == 3:
        print('Metodo de Simpson 3/8')
        if clase=='s':
            #Calculo directo con la formula
            h=(b-a)/3
            i=3*h*(f(a)+3*f((2*a+b)/3)+3*f((a+2*b)/3)+f(b))/8
        elif clase=='c':
            #Divido el intervalo en n subintervalos
            n=int(input('Ingrese cantidad de subintervalos>>'))
            h=(b-a)/n
            i=f(a)+f(b)
            #Calculo dos sumatorias
            for j in range(1,n):
                #Si j es multiplo de 3, multiplico por 2, caso contrario multiplico por 3 (Revisar formula para compuesta para mas info)
                if j%3 == 0:
                    i+=2*f(a+j*h)
                else:
                    i+=3*f(a+j*h)
            #Multiplico el resultado de las sumatorias por el factor 3/8
            i*=3*h/8
        else:
          error = "La clase del metodo no se reconoce, recuerda que podes escribir: Simple (s), Compuesta (c)"
    else:
      error = "El metodo de integracion no se reconoce, los metodos soportados son: Trapecio(1), Simpson 1/3 (2), Simpson 3/8 (3)>>"

    #Esto devuelve un JSON con el codigo de error si es que existe y el resultado de integracion
    return {
        "val": i,
        "error": error
    }

#Entrada de datos
a=float(input('Ingrese el limite inferior de integracion>>'))
b=float(input('Ingrese el limite superior de integracion>>'))
fun=input("Introduzca una funcion con 'x' como variable>>")
m=int(input('Seleccione el metodo de integracion: Trapecio(1), Simpson 1/3 (2), Simpson 3/8 (3)>>'))
clase=input('Ingrese clase del metodo: Simple (s), Compuesta (c)>>')

#Resultados
resultado=integracion(a,b,m)
#print(resultado)
if resultado["error"] == "null": #Si no hay errores entonces entonces imprime por consola el resultado
  print('El resultado de la integracion es:', resultado["val"])
else: #De lo contrario muestra el error
  print(resultado["error"])
