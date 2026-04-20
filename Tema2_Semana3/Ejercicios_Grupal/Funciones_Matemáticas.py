#realizar un algoritmo que permita arrojar con funciones 
#la suma resta multiplicación residuo y el factorial de 
#los 2 números ingresado en consola
#suma = a+b
#resta = a-b
#multiplicación = a*b
#división = a/b
#residuo = a% b
#factorial A = a!
#factorial B = b!

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicación(a,b):
    return a*b

def división(a,b):
    return a/b

def residuo(a,b):
    return a%b

def factorial(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i
    return resultado

print("--------------------------")
print("--------Resultados--------")
print("--------------------------")
print("La suma es: ", suma(a,b))
print("La resta es: ", resta(a,b))
print("La multiplicación es: ", multiplicación(a,b))
print("La división es: ", división(a,b))
print("El residuo es: ", residuo(a,b))
print("El factorial es: ", factorial(a))
print("El factorial es: ", factorial(b))