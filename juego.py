import random

def adivina_el_numero():
    print("¡Bienvenido al juego 'Adivina el número'!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    while True:
        try:
            adivina = int(input("Introduce tu adivinanza: "))
            intentos += 1
            
            if adivina < numero_secreto:
                print("¡Demasiado bajo! Intenta de nuevo.")
            elif adivina > numero_secreto:
                print("¡Demasiado alto! Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

# Ejecutar el juego
adivina_el_numero()






