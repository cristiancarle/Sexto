def cubrecadena(S, t):
    L = len(S)
    dp = [0] * (L + 1)  # Inicializamos dp con 0
    for i in range(1, L + 1):
        dp[i] = dp[i - 1] + 1  # Inicialmente asumimos que el carácter en i no se cubre
        for block in t:
            block_len = len(block)
            if i >= block_len and S[i - block_len:i] == block:
                dp[i] = min(dp[i], dp[i - block_len])
    return dp[L]

# Ejemplo de uso
S = "ABCDECDE"
t = ["ABC", "CDE", "DEC"]
print(cubrecadena(S, t))  # Salida esperada: 2