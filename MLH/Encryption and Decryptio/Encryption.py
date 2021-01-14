from cryptography.fernet import Fernet
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b'SuperSecretpassword')
with open('Password.txt', 'wb') as file_object:  file_object.write(ciphered_text)