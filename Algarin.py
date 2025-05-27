def algarin_escape(m, n, grid):
    # Inicializar 
    dp = [[-1] * n for _ in range(m)]
    
    # Chequeo de celdas
    def is_valid(i, j):
        return 0 <= i < m and 0 <= j < n
    
    
    for i in range(m):
        if grid[i][0] == 'A':
            dp[i][0] = 0  
        elif grid[i][0] == 'M':
            dp[i][0] = -1  
    
    # de Izquierda a derecha
    for j in range(1, n):
        for i in range(m):
            if grid[i][j] == 'M':
                dp[i][j] = -1  
            else:
                joyas = -1
                # Posibles movimientos 
                if is_valid(i - 1, j - 1) and dp[i - 1][j - 1] != -1:
                    joyas = max(joyas, dp[i - 1][j - 1])
                if is_valid(i, j - 1) and dp[i][j - 1] != -1:
                    joyas = max(joyas, dp[i][j - 1])
                if is_valid(i + 1, j - 1) and dp[i + 1][j - 1] != -1:
                    joyas = max(joyas, dp[i + 1][j - 1])
                
                if joyas == -1:
                    dp[i][j] = -1  
                else:
                    dp[i][j] = joyas + (1 if grid[i][j] == 'J' else 0)
    
    
    coleccion_joyas = -1
    for i in range(m):
        if dp[i][n - 1] > coleccion_joyas:
            coleccion_joyas = dp[i][n - 1]
    
    return coleccion_joyas


import sys
input = sys.stdin.read().strip().split('\n')

m, n = map(int, input[0].split())
grid = [list(input[i + 1]) for i in range(m)]

# Call the function and output the result
resultado = algarin_escape(m, n, grid)

if resultado == -1:
    print("SIN SALIDA")
else:
    print(resultado)