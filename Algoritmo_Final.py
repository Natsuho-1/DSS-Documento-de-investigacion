import os
import random as rd

def generate_polymorphic_key(key_length):
    return os.urandom(key_length)

def encrypt(message, key):
    encrypted_message = bytearray(len(message))
    for i in range(len(message)):
        encrypted_message[i] = message[i] ^ key[i % len(key)]

    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = bytearray(len(encrypted_message))
    for i in range(len(encrypted_message)):
        decrypted_message[i] = encrypted_message[i] ^ key[i % len(key)]

    return decrypted_message

# Example usage
if __name__ == "__main__":
    key_length = 8  # 64 bits (8 bytes)
    #key = generate_polymorphic_key(key_length)
    numero = int(input("cuantas claves se generaran: "))

    claves=[]
    for i in range(numero):
        clave=generate_polymorphic_key(key_length)
        claves.append(clave)
    print(claves)
    key=claves[rd.randrange(0,numero)]
    print(key)
    message = b"hola dss"  # Bytes representation of the message

    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print("Original Message:", message.decode())
    print("Key (Hexadecimal):", key.hex())
    print("Encrypted Message (Hexadecimal):", encrypted_message.hex())
    print("Decrypted Message:", decrypted_message.decode())


"""

keymsg = '8d4e400d4c37eb34'
bytemsg = 'e13b236c3f179214ea2b326c3e5384'

encrypted_message = bytearray.fromhex(bytemsg)
key = bytearray.fromhex(keymsg)

def decrypt(encrypted_message, key):
    decrypted_message = bytearray(len(encrypted_message))
    for i in range(len(encrypted_message)):
        decrypted_message[i] = encrypted_message[i] ^ key[i % len(key)]

    return decrypted_message

# Example usage
if __name__ == "__main__":

    decrypted_message = decrypt(encrypted_message, key)

    print("Key (Hexadecimal):", key)
    print("Encrypted Message:", encrypted_message)
    print("Mensaje desencriptado ----->:", decrypted_message.decode())



"""