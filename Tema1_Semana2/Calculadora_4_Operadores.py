num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operador = (input("Ingrese el operador (+,-,*,/): "))

match operador:
    case "+":
        print(f"La suma de los número es: {num1+num2}")
    case "-":
        print(f"La resta de los número es: {num1-num2}")
    case "*":
        print(f"La multiplicación de los números es: {num1*num2}")
    case "/":
        if num2 == 0:
            print(f"No se puede dividir entre 0")
        else:
            print(f"La división de los números es: {num1/num2}")