#Import the numpy module
import numpy as np

#Load csv files
matrixL = np.matrix(np.genfromtxt('datos_de_linea.csv', delimiter=';'))
matrixN = np.matrix(np.genfromtxt('datos_de_nodos.csv', delimiter=';'))

outputAccuracy = 5 #Sets the number of decimals in the output matrix
busNumer = int(np.amax(matrixL)) #Loads number of nodes

#For all the vars instanced like {} the format look like
#{"key": value}

#Este bloque crea las variables necesarias para la capacitancia parásita entre nodos
#Y para la admitancia de nodo
capPar = {}
nAdmitance = {}
for i in range(1, busNumer +1): #Se itera el numero de nodos
    j=np.where(matrixL==(i)) #Se busca por nodos, esto devuelve todos los nodos conectados al nodo i
    capVal = 0;
    nodeAdmitance = complex(0, 0)

    for k in j[0]: #Se itera el resultado de la busqueda
        capVal += matrixL[k,4] #Suma la capacitancia entre nodos
        nodeAdmitance += 1/complex(matrixL[k,2], matrixL[k,3]) #Suma la admitancia entre nodos

    #Añade la capacitancia y admitanca a sus respectivas variables
    capPar[str(i)] = complex(0, capVal)
    nAdmitance[str(i)] = nodeAdmitance

#Este bloque crea busca la admitancia entre nodos
admitance = {}
for i in range(matrixL.shape[0]):
    #Almacena la llave en la forma de min:max donde representa el numero de los nodos implicados
    key = str(min(int(matrixL[i,0]), int(matrixL[i,1]))) + str(max(int(matrixL[i,0]), int(matrixL[i,1])))
    admitance[key] = 1/complex(matrixL[i,2], matrixL[i,3])

#Este bloque crea las variables necesarias para la capacitancia shunt
shuntCap = {}
for i in range(matrixN.shape[0]):
    shuntCap[str(int(matrixN[i,0]))] = complex(0, matrixN[i,1]) #Add shunt capacitance

#Create the matrix
ybus = [] #Esta variable representa el vector vertical de la matriz
for i in range(1, busNumer+1): #Itera en forma vertical para crear la matriz
    xbus = [] #Esta variable representa los vectores horizontales de la matriz
    for j in range(1, busNumer+1): #Itera en forma horizontal para crear la matriz
        if i==j: #Si es la diagonal principal:
          val = 0; #Crea una variable para almacenar y sumar los valores

          key = str(i)
          if key in nAdmitance: #Busca si la admitancia de nodo existe
            val = nAdmitance[key] #Suma la admitancia de nodo

          if key in capPar: #Busca si la capacitancia parasita entre nodos existe
            val += capPar[key] #Suma la capacitancia

          if key in shuntCap: #Busca si la capacitancia shunt existe
            val += shuntCap[key] #Suma la capacitancia

          #Añade el valor obtenido al vector
          xbus.append(round(val.real, outputAccuracy) + round(val.imag, outputAccuracy) * 1j)
        else: #Si no es la diagonal principal:
          key = str(min(i, j)) + str(max(i, j)) #Crea una variable de la forma min:max entre i, j
          if key in admitance: #Busca si existe una admitancia entre nodos
            adm = -admitance[key] #Obtiene el valor de la admitancia con signo cambiado
            #Añade la admitancia al vector
            xbus.append(round(adm.real, outputAccuracy) + round(adm.imag, outputAccuracy) * 1j)
          else: #Si no existe una admitancia entre nodos
            xbus.append(0) #Añade un cero al vector
    ybus.append(xbus)


"""s = str(ybus)
s = s.replace("], [", "],\n [")
s = s.replace("[[", "[\n [")
s = s.replace("]]", "]\n]")


print(s, len(ybus))"""

#Format the matrix for csv standard
formattedMatrix = str(ybus)
formattedMatrix = formattedMatrix.replace("], [", "\n")
formattedMatrix = formattedMatrix.replace("[[", "")
formattedMatrix = formattedMatrix.replace("]]", "")
formattedMatrix = formattedMatrix.replace(",", ";")

#print(formattedMatrix)

#Write file
fw = open('matrix.csv','w')
fw.writelines(formattedMatrix)
fw.close()
