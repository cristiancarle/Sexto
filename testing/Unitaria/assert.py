# Assert
# Es una palabra reservada que se utiliza para verificar si una condición es verdadera. 
# Si la condición es falsa, se lanza una excepción AssertionError. 
# Esto se utiliza comúnmente para realizar pruebas y depuración en el código.

def sumatorial(valorA, valorB, valorC): 
    """
        Esta función hace el calculo de la suma de los valores
        argumentos:
        valorA: primer valor a sumar
        valorB: segundo valor a sumar
        valorC: tercer valor a sumar

        implementación:
        Ejemplo:
        sumatiroal(1,2,3) => 6
        
    """
    assert valorA >= 0 and valorB >=0 and valorC >=0, "valorA debe ser mayor o igual a 0"
    suma=valorA + valorB + valorC
    return suma
sumatorial(1,-2,3)



