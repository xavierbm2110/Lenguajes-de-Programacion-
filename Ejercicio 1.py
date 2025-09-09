def factorial(n):
    """Calcula el factorial de un número."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



num = input("Ingresa un número entero: ")

if num.isdigit():
    num = int(num)  
    print(f"El factorial de {num} es {factorial(num)}")
else:
    print(" Debes ingresar un número entero válido.")
