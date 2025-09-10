import random as r

valores = []

for i in range(10):
    valor = r.randint(1, 100)  
    valores.append(valor)
    print(f"Valor {i+1}: {valor}") 

suma_total = sum(valores)
prom = suma_total / 10

print(f"\nLa suma total es: {suma_total}")
print(f"El promedio de esta suma es: {prom}")


