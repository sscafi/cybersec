"""
Script for using the Fernet symmetric encryption from the cryptography library.

Requirements:
    - cryptography library: `pip install cryptography`

Usage:
    - Generate a new encryption key using `Fernet.generate_key()`.
    - Create a Fernet instance with the generated key.
    - Encrypt a message using `fernet.encrypt(message)`.
    - Decrypt an encrypted message using `fernet.decrypt(encrypted_message)`.

Note:
    - Keep the encryption key (`key`) secure and private.
    - Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.
"""

from cryptography.fernet import Fernet

# Generate a new symmetric encryption key
key = Fernet.generate_key()

# Create a new Fernet instance with the key
fernet = Fernet(key)

# Encrypt a message
message = b"Hello, World!"
encrypted_message = fernet.encrypt(message)

# Decrypt the message
decrypted_message = fernet.decrypt(encrypted_message)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
