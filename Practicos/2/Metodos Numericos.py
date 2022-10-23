#Import the numpy module
import numpy as np

#Load csv files
matrixL = np.matrix(np.genfromtxt('datos_de_linea.csv', delimiter=';'))
matrixN = np.matrix(np.genfromtxt('datos_de_nodos.csv', delimiter=';'))

outputAccuracy = 5 #Sets the number of decimals in the output matrix
busNumer = int(np.amax(matrixL)) #Loads number of nodes

#For all the vars instanced like {} the format look like
#{"key": value}

capPar = {}
nAdmitance = {}
for i in range(1, busNumer +1):
    j=np.where(matrixL==(i))
    capVal = 0;
    nodeAdmitance = complex(0, 0)

    for k in j[0]:
        capVal += matrixL[k,4]
        nodeAdmitance += 1/complex(matrixL[k,2], matrixL[k,3])

    capPar[str(i)] = complex(0, capVal)
    nAdmitance[str(i)] = nodeAdmitance


admitance = {}
for i in range(matrixL.shape[0]):
    key = str(min(int(matrixL[i,0]), int(matrixL[i,1]))) + str(max(int(matrixL[i,0]), int(matrixL[i,1])))
    admitance[key] = 1/complex(matrixL[i,2], matrixL[i,3])

shuntCap = {}
for i in range(matrixN.shape[0]):
    shuntCap[str(int(matrixN[i,0]))] = complex(0, matrixN[i,1]) #Add shunt capacitance


#Create the matrix
ybus = []
for i in range(1, busNumer+1):
    xbus = []
    for j in range(1, busNumer+1):
        if i==j:
          val = 0;

          key = str(i)
          if key in nAdmitance:
            val = nAdmitance[key]

          if key in capPar:
            val += capPar[key]

          if key in shuntCap:
            val += shuntCap[key]
          xbus.append(round(val.real, outputAccuracy) + round(val.imag, outputAccuracy) * 1j)
        else:
          key = str(min(i, j)) + str(max(i, j))
          if key in admitance:
            adm = -admitance[key]
            xbus.append(round(adm.real, outputAccuracy) + round(adm.imag, outputAccuracy) * 1j)
          else:
            xbus.append(0)
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
