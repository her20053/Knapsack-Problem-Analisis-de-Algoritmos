import time
import numpy as np
import matplotlib.pyplot as plt
from divideandconquer import knapSack as knapsack_divide
from dynamicprogramming import knapsack as knapsack_dynamic

# Función para generar entradas de prueba
def generate_inputs(size):
    wt = list(range(1, size+1))
    val = [i*10 for i in wt]
    W = size*2
    return wt, val, W, size

# Función para medir el tiempo de ejecución del algoritmo de divide and conquer
def timeKnapDaC(wt, val, W, n):
    start_time = time.time()
    knapsack_divide(W, wt, val, n)
    return time.time() - start_time

# Función para medir el tiempo de ejecución del algoritmo de memoización
def timeKnapDP(wt, val, W, n):
    global t
    t = [[-1 for j in range(W+1)] for i in range(n+1)]
    start_time = time.time()
    knapsack_dynamic(wt, val, W, n, t)
    return time.time() - start_time

def plot_line_of_best_fit(x, y, label):
    # calculate the slope and intercept of the line of best fit
    slope, intercept = np.polyfit(x, y, 1)

    # create an array of x values spanning the range of the data
    x_range = np.linspace(np.min(x), np.max(x), 100)

    # calculate the corresponding y values for the line of best fit
    y_range = slope * x_range + intercept

    # plot the data and the line of best fit
    plt.plot(x, y, 'o', label=label)
    plt.plot(x_range, y_range, '-', label='Line of best fit')

    # add a legend and axis labels
    plt.legend()
    plt.xlabel('Size of input')
    plt.ylabel('Time (s)')
    plt.title('Line of best fit')

    # show the plot
    plt.show()

# Listas para almacenar los tiempos de ejecución de cada algoritmo
dc_times = []
memo_times = []
sizes = list(range(1, 51))

# Medir tiempos de ejecución para diferentes tamaños de entrada
for size in sizes:
    wt, val, W, n = generate_inputs(size)
    dc_times.append(timeKnapDaC(wt, val, W, n))
    memo_times.append(timeKnapDP(wt, val, W, n))


# Graficar los tiempos de ejecución de cada algoritmo en función del tamaño de entrada (separadamente)
plt.plot(sizes, dc_times, label="Divide and conquer")
plt.xlabel("Tamaño de entrada")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Divide and conquer")
plt.show()

plt.plot(sizes, memo_times, label="Dynamic Programming")
plt.xlabel("Tamaño de entrada")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Dynamic Programming")
plt.show()
plot_line_of_best_fit(sizes, memo_times, 'Divide and conquer')

# Graficar los tiempos de ejecución de cada algoritmo en función del tamaño de entrada (juntos)
plt.plot(sizes, dc_times, label="Divide and conquer")
plt.plot(sizes, memo_times, label="Dynamic Programming")
plt.xlabel("Tamaño de entrada")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.show()
