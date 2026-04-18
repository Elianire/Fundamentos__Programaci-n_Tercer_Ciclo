nota = int(input("Ingrese la nota a evaluar (0-20): "))

if nota > 20:
    print("La nota debe ser menor o igual a 20")    #Prueba para validar que
elif nota < 0:                                      #la nota esté entre 0-20
    print("La nota debe ser mayor o igual a 0")
else:
    if nota >= 18:
        print("Excelente")
    elif nota >= 14:
        print("Bueno")
    elif nota >= 11:
        print("Regular")
    else:
        print("Desaprobado")