n = int(input("Ingrese la cantidad de notas a evaluar: "))

suma = 0
aprobados = 0

nota = float(input("Ingrese nota 1: "))

mayor = nota
menor = nota
suma += nota

if nota >= 11:
    aprobados += 1

for i in range(2, n + 1):
    nota = float(input(f"Ingrese nota {i}: "))

    suma += nota

    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

    if nota >= 11:
        aprobados += 1

promedio = suma / n

print("----- ESTADÍSTICAS -----")
print("Promedio: ", promedio)
print("Nota más alta: ", mayor)
print("Nota más baja: ", menor)
print("Aprobados: ", aprobados)