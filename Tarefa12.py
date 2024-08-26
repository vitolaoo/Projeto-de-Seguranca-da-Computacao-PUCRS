from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii
import os

# Dados fornecidos
chave = binascii.unhexlify("33A18467DB4AF474B051523A73DDA955")
nome = "Arthur Bueno Vitola".encode('utf-8')

# Gerar um IV (counter) aleatório de 128 bits
iv = int.from_bytes(os.urandom(16), byteorder='big')
ctr = Counter.new(128, initial_value=iv)

# Cifrar usando AES CTR
cipher = AES.new(chave, AES.MODE_CTR, counter=ctr)
texto_cifrado = cipher.encrypt(nome)

# Mostrar o resultado em hexadecimal
print(f"IV: {hex(iv)}")
print(f"Texto Cifrado: {binascii.hexlify(texto_cifrado).decode('utf-8')}")
