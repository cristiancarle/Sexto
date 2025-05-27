#print("Ingrese los numeros para sacar la media")

def calcula_media(*args):
    return(sum(*args)/len(*args))


print(calcula_media([3, 7, 5]))

assert(calcula_media([3, 7, 5]) == 5.0)

assert(calcula_media([30, 0]) == 15.0)