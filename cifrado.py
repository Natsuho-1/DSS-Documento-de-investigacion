class Cifrado_XOR(object):

 def __init__(self, key = 0):
  self.__key = key

 def encrypt(self, content, key):
  # pre-condición
  assert (isinstance(key,int) and isinstance(content,str))
  key = key or self.__key or 1
  while (key > 255):
   key -= 255
  # Esta lista sera retornada
  ans = []
  for ch in content:
   ans.append(chr(ord(ch) ^ key))
  return ans
 
 def decrypt(self,content,key):
  # pre-condición
  assert (isinstance(key,int) and isinstance(content,list))
  key = key or self.__key or 1
  while (key > 255):
   key -= 255
  # This will be returned
  ans = []
  for ch in content:
   ans.append(chr(ord(ch) ^ key))
  return ans

 def encrypt_string(self,content, key = 0):
        # Encriptar cadenas de texto
  # pre-condición
  assert (isinstance(key,int) and isinstance(content,str))
  key = key or self.__key or 1
  while (key > 255):
   key -= 255
  ans = ""
  for ch in content:
   ans += chr(ord(ch) ^ key)
  return ans

 def decrypt_string(self,content,key = 0):
  # Descifrar
  # pre-condición
  assert (isinstance(key,int) and isinstance(content,str))
  key = key or self.__key or 1
  while (key > 255):
   key -= 255
  ans = ""
  for ch in content:
   ans += chr(ord(ch) ^ key)
  return ans

 