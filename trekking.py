import heapq

def trekking(mapa):
    N = len(mapa)
    M = len(mapa[0])
    
    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Inicializamos la matriz de esfuerzo con infinito
    inf = float('inf')
    esfuerzo = [[inf] * M for _ in range(N)]
    esfuerzo[0][0] = 0
    
    # Min-heap para Dijkstra
    heap = [(0, 0, 0)]  # (esfuerzo_acumulado, x, y)
    
    while heap:
        esfuerzo_acumulado, x, y = heapq.heappop(heap)
        
        # Si llegamos al destino, retornamos el esfuerzo acumulado
        if (x, y) == (N-1, M-1):
            return esfuerzo_acumulado
        
        # Si ya encontramos una mejor ruta, continuamos
        if esfuerzo_acumulado > esfuerzo[x][y]:
            continue
        
        # Exploramos las celdas vecinas
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                diff = abs(mapa[x][y] - mapa[nx][ny])
                if diff <= 150:
                    nuevo_esfuerzo = esfuerzo_acumulado + diff ** 2
                    if nuevo_esfuerzo < esfuerzo[nx][ny]:
                        esfuerzo[nx][ny] = nuevo_esfuerzo
                        heapq.heappush(heap, (nuevo_esfuerzo, nx, ny))
    
    # Si no encontramos un camino, retornamos -1
    return -1

# Ejemplo de uso
N, M = 3, 3
mapa = [
    [100, 150, 200],
    [130, 180, 250],
    [120, 100, 90]
]
print(trekking(mapa))  # Salida esperada: 9700