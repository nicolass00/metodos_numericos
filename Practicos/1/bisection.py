def f(x):
    return -6*x**2 + 9*x + 2

def g(a, b) :
    return (a+b)/2

if __name__ == "__main__":
    a = float(input("Introduzca limite inferior: "))
    b = float(input("Introduzca limite superior: "))
    acc = float(input("Introduzca la presicion de la estimacion: ")) 

    if f(a)*f(b) < 0:
        print("En el intervalo hay al menos una raiz")

        c = g(a, b)

        if f(a)*f(c) < 0:
            b = c
        else :
            a = c

        while abs(a-b) > acc:
            c = g(a, b)
            if f(a)*f(c) < 0:
                b = c
            else :
                a = c

            print("Mid val: " + str(c))

        print("El valor es: " + str(f(c)))
    else:
        print("No hay raices")