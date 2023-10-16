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
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(message) + padder.finalize()

    cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return ciphertext


def decrypt_message(ciphertext, key):
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(64).unpadder()
    message = unpadder.update(padded_data) + unpadder.finalize()

    return message

if __name__ == "__main__":
    password = b"UnaClave64Bits"
    salt = b"SalParaKDF"

    key = generate_key(password, salt)
    message = "Prueba tarea DSS".encode('utf-8')

    ciphertext = encrypt_message(message, key)
    decrypted_message = decrypt_message(ciphertext, key)

    print(f"Mensaje original: {message.decode('utf-8')}")
    print(f"Mensaje cifrado: {ciphertext}")
    print(f"Mensaje descifrado: {decrypted_message.decode('utf-8')}")
    print(f"Mensaje cifrado: {key}")

