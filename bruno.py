ai =[]
final=[]
def cadenas (a):
    todoslosnumeros= []
    suma=0
    for j in range (a):
        todoslosnumeros.append(a-j)
        
    for i in range(a):
        if a % todoslosnumeros[i] == 0:
            suma+=(todoslosnumeros[i])
            a=todoslosnumeros[i]
    return suma

n=int(input())
a=input()
ai=a.split()
for i in range (n):
    num=int(ai[i])
    sumafinal=cadenas(num)
    final.append(sumafinal)
print (final)