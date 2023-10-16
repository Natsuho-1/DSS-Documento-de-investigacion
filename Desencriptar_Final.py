from Algoritmo_Final import *

keymsg = '1c93ecf2d018a3a2'
bytemsg = '74fc8093f07cd0d1'

encrypted_message = bytearray.fromhex(bytemsg)
key = bytearray.fromhex(keymsg)

# Example usage
if __name__ == "__main__":

    decrypted_message = decrypt(encrypted_message, key)

    print("Key (Hexadecimal):", key)
    print("Encrypted Message:", encrypted_message)
    print("Mensaje desencriptado ----->:", decrypted_message.decode())

