from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

# Dados fornecidos
chave_hex = "240B31B44A27BEC5062B3A74C63271A4"
iv_hex = "C4AB0DF3D808D72AAADBC68206483B18"
texto_cifrado_hex = "EF794476D605765572683CE849FBD4555CE8EC1382019662E277F31B8035E285787C1DA9D2CC5B3441F5CB900C41BA70902A932209C3966B83FB4387ABBC95E0"

# Converter de hexadecimal para bytes
chave = binascii.unhexlify(chave_hex)
iv = binascii.unhexlify(iv_hex)
texto_cifrado = binascii.unhexlify(texto_cifrado_hex)

# Configurar AES em modo CBC com a chave e IV fornecidos
cipher = AES.new(chave, AES.MODE_CBC, iv)

# Decifrar o texto cifrado
texto_claro = unpad(cipher.decrypt(texto_cifrado), AES.block_size)

# Converter o texto claro para UTF-8
print(texto_claro.decode('utf-8'))
