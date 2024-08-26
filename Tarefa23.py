import hashlib

# Valor de v calculado na Tarefa 2.2
v = 145959650117478257566722577223744825176256923001733444236133

# Converter o valor de v para string e depois para bytes
v_bytes = str(v).encode('utf-8')

# Calcular o hash SHA-256 do valor de v
hash_v = hashlib.sha256(v_bytes).hexdigest()

# Pegar os primeiros 128 bits (32 caracteres hexadecimais) do hash
k = hash_v[:32]

# Mostrar a chave k
print(f"Chave k (128 bits em hexadecimal): {k}")
