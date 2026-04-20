contador = 0
acumulador = 0

for i in range(1,21):
    if i % 2 == 0:
        acumulador += i
        contador += 1

print("El total de números pares que hay en la lista es: ", contador)
print("La suma de los números pares que hay en la lista es: ", acumulador)