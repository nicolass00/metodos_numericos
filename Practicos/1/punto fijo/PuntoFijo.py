from math import sin, cos

#Define una equacion cualquiera
def f(x):
    return sin(x) #PlaceHolder

#Define la derivada de la equacion anterior
def fd(x) :
    return cos(x)

if __name__ == "__main__":
    Xo = float(input("Ingrese un punto inicial: ")) #Lee el punto inicual
    acc = float(input("Introduzca la presicion de la estimacion: ")) #Lee el punto superior

    if abs(fd(Xo)) < 1: #Comprueba la condicion de convergencia del metodo
        print("En el intervalo hay al menos una raiz")

        X1 = f(Xo) #Obtengo F(x) en el punto inicial para evaluar la precision de la aproximacion
        #Me mantengo dentro del bucle while mientras la precision alcanzada sea mayor que la requerida
        while abs(X1-Xo) >= acc:
            Xo = X1 #Igualo el resultado de la iteracion anterior para valuar nuevamente la ecuacion
            X1 = f(Xo) #Valuo la ecuacion para resolver g(x) = x

        print("El valor es: " + str(Xo))
    else:
        print("No hay raices")