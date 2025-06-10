def calcular_suma_maxima(a, memo):
    if a in memo:
        return memo[a]
    
   
    max_suma = a
    divisor = a // 2
    
    
    while divisor >= 1:
        if a % divisor == 0:
            max_suma = max(max_suma, a + calcular_suma_maxima(divisor, memo))
            break
        divisor -= 1
    
    memo[a] = max_suma
    return memo[a]

def cadenas(a):
    memo = {1: 1}  
    resultados = []
    
    for num in a:
        resultados.append(calcular_suma_maxima(num, memo))
    
    return resultados


N = 5
a = [60, 100, 120, 15, 30]
print(cadenas(a)) 