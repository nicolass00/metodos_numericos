from math import sin, cos

#Define una equacion cualquiera
def f(x):
    return sin(x) #PlaceHolder

#Define la derivada de la equacion anterior
def fd(x) :
    return cos(x)

if __name__ == "__main__":
    Xo = float(input("Ingrese un punto inicial: ")) #Lee el punto inicial
    acc = float(input("Introduzca la presicion de la estimacion: ")) #Lee la presicion

    if abs(fd(Xo)) < 1: #Comprueba la condicion de convergencia del metodo
        print("En el intervalo hay al menos una raiz")

        X1 = f(Xo) #Evaluo la ecuacion y su derivada en el punto inicial
        while abs(X1-Xo) >= acc:
            Xo = X1 #Evaluo la ecuacion y su derivada en el punto inicial
            X1 = Xo-f(Xo)/fd(Xo) #Evaluo la ecuacion y su derivada en el punto inicial

        print("El valor es: " + str(Xo))
    else:
        print("No hay raices")