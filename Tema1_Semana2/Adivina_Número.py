import random
numero_secreto = random.randint(1, 100)

intentos = 0 
intento = int(input("Adivina el número entre 01 al 100: "))
intentos += 1

while intento != numero_secreto:
    if intento < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    intento = int(input("Intenta otra vez: "))
    intentos += 1

print(f"¡Correcto! Lo lograste en {intentos} intentos")