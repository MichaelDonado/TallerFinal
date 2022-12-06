#Trabajo realizado por Jesús Barros, Michael Donado y Daniel Lerma

from math import*
from pprint import pprint

def distinf(x, y):
    """Implementación de la distancia dada por la norma infinito"""
    return max([abs(x[i]-y[i]) for i in range(len(x))])


def GaussSeidel(A, b, x0, TOL, MAX):
    """ Implementación del método de Gauss-Seidel
        Entradas:
        A = matriz cuadrada
        b = vector
        x0 = aproximación inicial
        TOL = tolerancia
        MAX = número máximo de iteraciones
        Salida:
        x = aproximación a solución del sistema Ax = b
        None = cuando se agoten las iteraciones o se presenten errores 
    """
    n = len(A)
    x = [0.0 for x in range(n)]
    k = 1
    while k <= MAX:
        for i in range(n):
            if abs(A[i] [i]) <= 1e-15:
                print("No se puede iterar")
                return None
            s1 = sum([A[i][j]*x[j] for j in range(i)])
            s2 = sum([A[i][j]*x0[j] for j in range(i+1, n)])
            x[i] = (b[i] - s1 - s2)/A[i][i]
        pprint(x)
        if distinf(x, x0) < TOL:
            print(r"Resultado encontrado")
            return x
        k += 1
        for i in range(n):
            x0[i] = x[i]
    print("Iteraciones agotadas")
    return None

def mainGaussSeidel():
    A = [[4, 3], [8, 10]]
    b = [11, 13]
    x0 = [1, 1]
    print("Matriz A:")
    pprint(A)
    print("Vector b:")
    pprint(b)
    print("Semilla x0:")
    pprint(x0)
    print("Iteración de Gauss-Seidel")
    # TOL = 10−5, MAX = 50
    GaussSeidel(A, b, x0, 1e-5, 50)
