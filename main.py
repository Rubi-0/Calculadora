from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N números")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", dividir(a, b))
    elif opcion == "5":
        numeros = list(map(float, input("Ingresa los números separados por espacios: ").split()))
        print("Resultado:", suma_avanzada(*numeros))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    menu()
