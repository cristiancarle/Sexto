class calculo():
    def sumatoria(valorA:int, valorB:int, valorC:int)->int:
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
        suma=valorA + valorB + valorC
        return suma
matematica=calculo()
matematica.sumatoria(10,20,30)