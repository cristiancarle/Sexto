n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))

##########
matriz = []
a=1
for indicef in range(1,6):
    fila = []
    for indicec in range(1,6):
        if a%2==0:
            fila.append(1)
        else:
            fila.append(0)
        a+=1
    matriz.append(fila)

for fila in matriz:
    for elemento in fila:
        print(elemento," ",end=" ")
    print()