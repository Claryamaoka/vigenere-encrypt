from socket import *

def caesar_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_char = chr((ord(char) - shift) % 256)
        decrypted_message += decrypted_char
    return decrypted_message

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            if char.islower():
                plaintext += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                plaintext += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            plaintext += char
    return plaintext

serverPort = 15600
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("UDP server\n")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    encrypted_text = str(message, "utf-8")
    
    key = "chaVe"  # Shift correspondente à cifra de César
    print(encrypted_text)
    decrypted_message = vigenere_decrypt(encrypted_text, key)
    print("Mensagem decriptografada:", decrypted_message)