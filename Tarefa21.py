import random

seed = 12345  
random.seed(seed)

# Valores fornecidos
p = 1041607122029938459843911326429539139964006065005940226363139
g = 10

# Gerar um valor b com pelo menos 40 dígitos e menor que p, usando a seed
b = random.randint(10**39, p - 1)

# Calcular B = g^b mod p
B = pow(g, b, p)

# Mostrar o valor de b e B
print(f"Valor de b (decimal): {b}")
print(f"Valor de B (decimal): {B}")

# Valor fornecido por Alice
A = 105008283869277434967871522668292359874644989537271965222162

# Calcular v = A^b mod p
v = pow(A, b, p)

# Mostrar o valor de v
print(f"Valor de v (decimal): {v}")
