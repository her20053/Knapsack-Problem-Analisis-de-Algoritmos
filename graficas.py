import time
import matplotlib.pyplot as plt
import random

# Definición de las funciones dadas

def knapSack(W, wt, val, n):
    
	# Base Case
	if n == 0 or W == 0:
		return 0

	# If weight of the nth item is
	# more than Knapsack of capacity W,
	# then this item cannot be included
	# in the optimal solution
	if (wt[n-1] > W):
     
		return knapSack(W, wt, val, n-1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		return max(
			val[n-1] + knapSack(
				W-wt[n-1], wt, val, n-1),
			knapSack(W, wt, val, n-1))

def knapsack(wt, val, W, n, t):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
 
    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1, t),
            knapsack(wt, val, W, n-1, t))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1, t)
        return t[n][W]

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
    knapSack(W, wt, val, n)
    end_time = time.time()
    
    times_dc.append(end_time - start_time)

    # Tiempo de ejecución de Programación Dinámica
    t = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
    start_time = time.time()
    knapsack(wt, val, W, n, t)
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


