# Fuente: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

'''
Este codigo es la implenteacion del algoritmo de programacion dinamica para el problema de la mochila 0/1.
El algoritmos utiliza la tecnica de memoizacion para evitar la repeticion de subproblemas.
'''
 
 
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
 
# Driver code
if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
     
    # We initialize the matrix with -1 at first.
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    print(knapsack(weight, profit, W, n, t))
 
# This code is contributed by Prosun Kumar Sarkar