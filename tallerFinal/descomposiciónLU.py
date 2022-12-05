#Trabajo realizado por Jesús Barros, Michael Donado y Daniel Lerma

from scipy.linalg import lu_factor
import numpy as np

def crear_matriz(n, m):
    matriz = np.zeros((n, m))
    
    print('Ingresa los datos de la matriz')
    
    for i in range(n):
        for j in range(m):
            x = float(input("Ingrese ({},{}): ".format(i,j)))
            matriz[i][j] = x
    
    return matriz

def descomposicion_lu():
    n = int(input("Ingrese el tamaño de la matriz: "))
    A = crear_matriz(n, n)
    lu, piv = lu_factor(A)
    print('Solucion: ',piv)