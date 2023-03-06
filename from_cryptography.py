from cryptography.fernet import Fernet

# generate a new symmetric encryption key
key = Fernet.generate_key()

# create a new Fernet instance with the key
fernet = Fernet(key)

# encrypt a message
message = b"Hello, World!"
encrypted_message = fernet.encrypt(message)

# decrypt the message
decrypted_message = fernet.decrypt(encrypted_message)

print(message)
print(encrypted_message)
print(decrypted_message)
