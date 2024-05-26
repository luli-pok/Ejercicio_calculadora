# Enunciado
# Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones:
# 1. Ingresar 1er operando (A=x)
# 2. Ingresar 2do operando (B=y)
# 3. Calcular todas las operaciones
# a) Calcular la suma (A+B)
# b) Calcular la resta (A-B)
# c) Calcular la división(A/B)
# d) Calcular la multiplicación(A*B)
# e) Calcular factorial(A!)
# 4. Informar resultados
# a) “El resultado de A+B es: r”
# b) “El resultado de A-B es: r”
# c) “El resultado de A/B es: r” o “No es posible dividir por cero”
# d) “El resultado de A*B es: r”
# e) “El factorial de A es: r1 y El factorial de B es: r2”
# 5. Salir
# • Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
# para realizar las cinco operaciones.
# • En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
# se debe mostrar el número cargado)
# • Deberán contemplarse los casos de error (división por cero, etc.)
# • Documentar todas las funciones
from funciones_calculadora import*

def imprimir_menu(a, b):
    """Imprime el menú principal con los valores actuales de A y B."""
    print(f"1. Ingresar 1er operando (A={a})")
    print(f"2. Ingresar 2do operando (B={b})")
    print("3. Calcular todas las operaciones")
    print("4. Informar resultados")
    print("5. Salir")

def menu_calculadora():
    a, b = None, None
    resultados = {}

    while True:
        imprimir_menu(a, b)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                a = int(input("Ingresar 1er operando (A=x): "))
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")
                a = None
        elif opcion == "2":
            try:
                b = int(input("Ingresar 2do operando (B=y): "))
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")
                b = None
        elif opcion == "3":
            if a is not None and b is not None:
                resultados["suma"] = sumar(a, b)
                resultados["resta"] = restar(a, b)
                resultados["division"] = dividir(a, b)
                resultados["multiplicacion"] = multiplicar(a, b)
                resultados["factorial_a"] = factorial(a)
                resultados["factorial_b"] = factorial(b)
            else:
                print("Falta uno o ambos operandos, seleccione la opción 1 y 2 antes de acceder a esta opción.")
        elif opcion == "4":
            if resultados:
                print(f"a) El resultado de A+B es: {resultados['suma']}")
                print(f"b) El resultado de A-B es: {resultados['resta']}")
                division_result = resultados['division']
                if division_result == "No es posible dividir por cero":
                    print("c) No es posible dividir por cero")
                else:
                    print(f"c) El resultado de A/B es: {division_result}")
                print(f"d) El resultado de A*B es: {resultados['multiplicacion']}")
                print(f"e) El factorial de A es: {resultados['factorial_a']} y el factorial de B es: {resultados['factorial_b']}")
            else:
                print("Primero debe calcular las operaciones (opción 3).")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


