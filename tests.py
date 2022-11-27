from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16) # 16 bytes = 128 bits la longitud de la clave
def Encriptar(texto): #Crear una funcion para encriptar
        cipher = AES.new(key, AES.MODE_EAX) #Crear un objeto AES
        nonce = cipher.nonce #Crear un nonce que es un numero aleatorio
        ciphertext, tag = cipher.encrypt_and_digest(texto.encode("ascii")) #Encriptar el texto
        return nonce, ciphertext, tag #Devolver el nonce, el texto encriptado y el tag

def Desencriptar(nonce, ciphertext, tag): #Crear una funcion para desencriptar
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce) #Crear un objeto AES 
        plaintext = cipher.decrypt(ciphertext) #Desencriptar el texto
        try: #Intentar verificar el tag
            cipher.verify(tag) #Verificar el tag
            return plaintext.decode("ascii") #Devolver el texto desencriptado
        except ValueError: #Si no se puede verificar el tag
            print("Key incorrect or message corrupted") #Mostrar un mensaje de error

nonce, ciphertext, tag = Encriptar("Hola") #Encriptar el texto
plaintext = Desencriptar(nonce, ciphertext, tag) #Desencriptar el texto
print(plaintext) #Mostrar el texto desencriptado
if not plaintext: #Si no se pudo desencriptar el texto
    print("Incorrect key or message corrupted") #Mostrar un mensaje de error
else : #Si se pudo desencriptar el texto
    print("The message is: ", plaintext) #Mostrar el texto desencriptado
print(key) #Mostrar la llave