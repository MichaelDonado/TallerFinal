#Trabajo realizado por Jesús Barros, Michael Donado y Daniel Lerma

from scipy.linalg import lu_factor
import numpy as np

def creaMatriz(n, m):
    matriz = np.zeros((n, m))
    
    print('Digite los datos de la matriz')
    
    for i in range(n):
        for j in range(m):
            x = float(input("Digite ({},{}): ".format(i,j)))
            matriz[i][j] = x
    
    return matriz

def descomposicionLU():
    n = int(input("Digite el tamaño de la matriz: "))
    A = creaMatriz(n, n)
    lu, piv = lu_factor(A)
    print('Resultado: ',piv)

descomposicionLU()