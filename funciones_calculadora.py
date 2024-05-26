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

def sumar(a: int, b: int) -> int:
    """Calcula la suma de dos números."""
    return a + b

def restar(a: int, b: int) -> int:
    """Calcula la resta de dos números."""
    return a - b

def dividir(a: int, b: int) -> float:
    """Calcula la división de dos números.
    
    Retorna un mensaje de error si el divisor es cero.
    """
    if b == 0:
        return "No es posible dividir por cero"
    return a / b

def multiplicar(a: int, b: int) -> int:
    """Calcula la multiplicación de dos números."""
    return a * b

def factorial(n: int) -> int:
    """Calcula el factorial de un número entero positivo."""
    if n < 0:
        return "No se puede calcular el factorial de un número negativo"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado






