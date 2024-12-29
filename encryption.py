from cryptography.fernet import Fernet
import os

# Generate key if not exists
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("key.key", "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

def encrypt_password(password):
    """Encrypt a password."""
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    """Decrypt a password."""
    return cipher.decrypt(encrypted_password.encode()).decode()
