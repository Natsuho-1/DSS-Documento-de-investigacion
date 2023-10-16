from Lucasalgoritmo import *
key_length = 8 
numero = int(input("cuantas claves se generaran: "))
claves=[]
for i in range(numero):
    clave=generate_polymorphic_key(key_length)
    claves.append(clave)
print(claves)
psn=claves[1]