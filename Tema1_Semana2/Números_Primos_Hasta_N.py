num = int(input("Ingrese un número: "))

for i in range(2, num + 1):
    es_primo = True

    for j in range(2, i):
        if i % j == 0:
            es_primo = False
            break

    if es_primo:
        print(i)