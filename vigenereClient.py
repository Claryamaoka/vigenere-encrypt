from socket import *

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr((ord(char) + shift) % 256)
        encrypted_message += encrypted_char
    return encrypted_message

def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
   
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            # Determine the shift value based on the corresponding key character
            key_char = key[i % key_length]
            shift = ord(key_char.upper()) - ord('A')
           
            # Encrypt the character
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_char = char
       
        encrypted_text += encrypted_char

    return encrypted_text

serverName = "127.0.0.1"  # IPv4 // ::1 IPv6
serverPort = 15600
clientSocket = socket(AF_INET, SOCK_DGRAM)  # AF_INET6
print("UDP Client\n")
while True:
    message = input("Input message: ")
    if message == "exit":
        break
    
    key = "chaVe"  # Shift para a cifra de César
    
    encrypted_message = encrypt_vigenere(message, key)    
    clientSocket.sendto(bytes(encrypted_message, "utf-8"), (serverName, serverPort))

clientSocket.close()