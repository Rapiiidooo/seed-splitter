import sys
import base64
import getpass
from cryptography.fernet import Fernet
from argon2 import PasswordHasher


def generate_key(password: str, salt: bytes = b"fixed-salt") -> bytes:
    """Generate a key from the password using Argon2 with a fixed salt."""
    ph = PasswordHasher()
    # Use the fixed salt to ensure the same key is generated each time
    hash_key = ph.hash(password, salt=salt)
    key = base64.urlsafe_b64encode(hash_key.encode()[:32])  # Ensuring 32 bytes key for Fernet
    return key


def encrypt_data(data: str, key: bytes) -> bytes:
    """Encrypt data using Fernet encryption."""
    cipher = Fernet(key)
    return cipher.encrypt(data.encode())


def decrypt_data(encrypted_data: bytes, key: bytes) -> str:
    """Decrypt data using Fernet encryption."""
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data).decode()


def split_and_encrypt_seed_phrase(seed_phrase: str, passwords: list[str]):
    words = seed_phrase.strip().split()
    num_parts = len(passwords)
    n = len(words)

    if n % num_parts != 0:
        print(f"The seed phrase must contain a number of words divisible by {num_parts}.")
        sys.exit(1)

    chunk_size = n // num_parts
    keys = [generate_key(passwords[i]) for i in range(num_parts)]

    for i in range(num_parts):
        part = " ".join(words[i * chunk_size : (i + 1) * chunk_size])
        filename = f"seed-{i + 1}.txt"
        with open(filename, "wb") as f:
            f.write(encrypt_data(part, keys[i]))

    print(f"Encrypted files seed-1.txt to seed-{num_parts}.txt have been created.")


def decrypt_seed_files(passwords: list[str]):
    num_parts = len(passwords)
    keys = [generate_key(passwords[i]) for i in range(num_parts)]

    decrypted_parts = []
    for i in range(num_parts):
        filename = f"seed-{i + 1}.txt"
        try:
            with open(filename, "rb") as f:
                encrypted_data = f.read()
                decrypted_parts.append(decrypt_data(encrypted_data, keys[i]))
        except FileNotFoundError:
            print(f"File {filename} not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error decrypting {filename}: {str(e)}")
            sys.exit(1)

    full_seed_phrase = " ".join(decrypted_parts)
    print("Decrypted Seed Phrase:")
    print(full_seed_phrase)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Encrypt: python seed-splitter.py encrypt")
        print("  Decrypt: python seed-splitter.py decrypt")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "encrypt":
        # Prompt the user to enter the seed phrase securely
        seed_phrase = getpass.getpass("Enter the seed phrase: ")

        # Ask for the number of passwords
        num_passwords = int(input("Enter the number of passwords to use: "))
        passwords = [getpass.getpass(f"Enter password {i + 1}: ") for i in range(num_passwords)]

        split_and_encrypt_seed_phrase(seed_phrase, passwords)
    elif mode == "decrypt":
        # Ask for the number of passwords
        num_passwords = int(input("Enter the number of passwords to use: "))
        passwords = [getpass.getpass(f"Enter password {i + 1}: ") for i in range(num_passwords)]

        decrypt_seed_files(passwords)
    else:
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)
