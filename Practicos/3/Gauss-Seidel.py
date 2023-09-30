import numpy as np

def seidel(Y, V ,I):
    #Encuentro la longitud de 'Y'       
    n = len(Y)                   
    #Itero n veces para calcular V1, V2, ... ,Vn
    for j in range(0, n):        
        #Almaceno I[j]
        d = I[j]                  
          
        #Y calculo V1i, V2i, ... ,Vni
        for i in range(0, n):     
            if(j != i):
                d-=Y[j][i] * V[i]
        #Actualizo el valor de solucion        
        V[j] = d / Y[j][j]
    #Devuelvo el nuevo valor           
    return V    

#Creo en una Matriz Y de prueba                                                                                     
Y = np.genfromtxt('matrix.csv', delimiter=',', dtype = "complex_")
n = len(Y)
#Creo un vector I que toma valores complejos aleatorios entre 0 y 50
Ix = np.array(50*(np.random.rand(n)), dtype = "complex_")
Iy = np.array(50j*(np.random.rand(n)), dtype = "complex_")
I = np.sum([Ix, Iy], axis=0, dtype = "complex_")
print(I)
#Propongo un vector V de ceros como solución
V = np.zeros(n, dtype = "complex_") 
print(V)
  
#Realizo 15 iteraciones de aproximacion
for i in range(0, 15):            
    V = seidel(Y, V, I)
    #Imprime la solución aproximada cada iteracion
    print(V) 
