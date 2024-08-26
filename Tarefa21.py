import random

# Valores fornecidos
p = 1041607122029938459843911326429539139964006065005940226363139
g = 10

# Gerar um valor b aleatório com pelo menos 40 dígitos e menor que p
b = random.randint(10**39, p - 1)

# Calcular B = g^b mod p
B = pow(g, b, p)

# Mostrar o valor de b e B
print(f"Valor de b (decimal): {b}")
print(f"Valor de B (decimal): {B}")
