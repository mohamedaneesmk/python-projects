# Project 5:  Encryption Program

import random 
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

# Encrpytion process
plain_text = input("Enter the text : ")
cipher_text = ""

for char in plain_text:
    if char in chars:
        index = chars.index(char)
        cipher_text = cipher_text + keys[index]
    else:
        cipher_text += char 
print(cipher_text)

# Decryption process
cipher_input = input("Enter cipher: ")
decrypted_text = ""
for char in cipher_input:
    if char in keys:
        index = keys.index(char)
        decrypted_text += chars[index]
    else:
        decrypted_text += char
print(plain_text)

# print(chars)
# print(keys)