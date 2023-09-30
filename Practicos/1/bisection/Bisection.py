#Define una equacion cualquiera
def f(x):
    return -6*x**2 + 9*x + 2 #PlaceHolder

#Esta funcion se utiliza para obtener el punto medio entre dos puntos
def g(a, b) :
    return (a+b)/2

if __name__ == "__main__": #Verifico si el programa se llama desde thread el principal
    a = float(input("Introduzca limite inferior: ")) #Lee el punto inferior
    b = float(input("Introduzca limite superior: ")) #Lee el punto superior
    acc = float(input("Introduzca la presicion de la estimacion: ")) #Lee la presicion

    if f(a) * f(b) < 0:  # Comprueba si existe una raiz en el intervalo dado
        print("En el intervalo hay al menos una raiz")

        c = g(a, b)

        if f(a) * f(c) < 0:  # Comprueba si existe una raiz en el intervalo [a,c]
            b = c
        else:  # Sino existe una raiz en el intervalo [c,b]
            a = c

        """
        En este bloque while se hace antes descripto, 
        mientras que la presicion 
        sea menor que la presicion hasta el momento
        """
        while abs(a - b) > acc:
            c = g(a, b)
            if f(a) * f(c) < 0:  # Comprueba si existe una raiz en el intervalo [a,c]
                b = c
            else:  # Sino existe una raiz en el intervalo [c,b]
                a = c

            print("Mid val: " + str(c))  # Imprime el valor de la Raiz calculada hasta ahora

        print("El valor es: " + str(c))  # Imprime el valor de la Raiz calculada
    else:
        print("No hay raices")