'''
Grupo 5: Proyecto 1
Integrantes: Jose Hernandez, Pablo Gonzalez, Javier Mombiela
Seccion:

Proyecto 1: Analizando el problema computacional, KnapSack Problem (0/1 Knapsack Problem)
'''

import time
import random
import matplotlib.pyplot as plt
from divideandconquer import knapSack as knapsack_divide
from dynamicprogramming import knapsack as knapsack_dynamic

if __name__ == '__main__':

    # Creación de entradas de prueba
    test_cases = []
    for i in range(10, 51, 10):
        weights = [random.randint(1, 50) for _ in range(i)]
        values = [random.randint(1, 100) for _ in range(i)]
        capacity = random.randint(50, 100)
        test_cases.append((weights, values, capacity))

    # Medición de tiempos de ejecución
    times_dc = []
    times_dp = []

    for wt, val, W in test_cases:
        n = len(wt)

        # Tiempo de ejecución de Divide and Conquer
        start_time = time.time()
        knapsack_divide(W, wt, val, n)
        end_time = time.time()
        
        times_dc.append(end_time - start_time)

        # Tiempo de ejecución de Programación Dinámica
        t = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
        start_time = time.time()
        knapsack_dynamic(wt, val, W, n, t)
        end_time = time.time()
        times_dp.append(end_time - start_time)

    print(times_dc)
    print(times_dp)

    # Gráficas de tiempos de ejecución
    x = [len(wt) for wt, _, _ in test_cases]

    # Gráfica de Divide and Conquer
    plt.figure()
    plt.plot(x, times_dc, label='Divide and Conquer')
    plt.xlabel('Número de elementos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución de Divide and Conquer')
    plt.legend()
    plt.show()

    # Gráfica de Programación Dinámica
    plt.figure()
    plt.plot(x, times_dp, label='Dynamic Programming')
    plt.xlabel('Número de elementos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución de Programación Dinámica')
    plt.legend()
    plt.show()

    # Gráfica combinada
    plt.figure()
    plt.plot(x, times_dc, label='Divide and Conquer')
    plt.plot(x, times_dp, label='Dynamic Programming')
    plt.xlabel('Número de elementos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución')
    plt.legend()
    plt.show()