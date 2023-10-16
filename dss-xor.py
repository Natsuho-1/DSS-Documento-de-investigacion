from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes


def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=8,
    )
    key = kdf.derive(password)
    return key

def encrypt_message(message, key):
    encrypted = b""
    for i in range(len(message)):
        encrypted_byte = message[i] ^ key[i % len(key)]
        encrypted += bytes([encrypted_byte])
    return encrypted

def decrypt_message(encrypted, key):
    decrypted = b""
    for i in range(len(encrypted)):
        decrypted_byte = encrypted[i] ^ key[i % len(key)]
        decrypted += bytes([decrypted_byte])
    return decrypted

# Ejemplo de uso
if __name__ == "__main__":
    message = b"Hello, world!"  # Mensaje con caracteres ASCII
    key = b"MyKey123"  # Clave de 8 bytes (64 bits)

    encrypted_message = encrypt_message(message, key)
    decrypted_message = decrypt_message(encrypted_message, key)

    print(f"Mensaje original: {message.decode('utf-8')}")
    print(f"Mensaje cifrado: {encrypted_message}")
    print(f"Mensaje descifrado: {decrypted_message.decode('utf-8')}")
