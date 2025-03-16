# Seed Splitter

**Seed Splitter** is a command-line tool that allows you to split a seed phrase into multiple parts and encrypt each part using passwords. It also enables decryption and reconstruction of the original seed phrase from the encrypted files.

## Features

- **Seed Phrase Splitting**: Splits a seed phrase into multiple parts.
- **Encryption**: Encrypts each part with a unique password.
- **Decryption**: Decrypts the parts and reconstructs the original seed phrase.
- **Security**: Uses Argon2 for key generation and Fernet for encryption.

## Prerequisites

- Python 3.x
- Python Libraries: `cryptography`, `argon2-cffi`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Rapiiidooo/seed-splitter.git
cd seed-splitter
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Encryption
To encrypt a seed phrase, run:

```bash
python seed-splitter.py encrypt
```

You will be prompted to enter the seed phrase and the number of passwords to use. Then, enter each password when prompted.

### Decryption
To decrypt the files and reconstruct the seed phrase, run:

```bash
python seed-splitter.py decrypt
```

You will be prompted to enter the number of passwords used during encryption, followed by each password.

## Example

### Encryption
```bash
$ python seed-splitter.py encrypt
Enter the seed phrase:  # Enter your seed phrase here
Enter the number of passwords to use: 2
Enter password 1:  # Enter the first password
Enter password 2:  # Enter the second password
Encrypted files seed-1.txt to seed-2.txt have been created.
```

### Decryption
```bash
$ python seed-splitter.py decrypt
Enter the number of passwords to use: 2
Enter password 1:  # Enter the first password
Enter password 2:  # Enter the second password
Decrypted Seed Phrase:
# Your decrypted seed phrase will be displayed here
```

## Security
- **Passwords**: Ensure you use strong and unique passwords.
- **Storage**: Never share your encrypted files or passwords.
- **Salt Customization**: The script currently uses a default salt value (fixed-salt). For better security, you should replace it with a unique salt of your choice.

## Contribution
Contributions are welcome! Please open an issue or submit a pull request.

## Disclaimer
**Use this script at your own risk.** The author is not responsible for any loss of funds, security breaches, or misuse of this script. Always verify your encrypted backups and ensure that your passwords are stored securely. If you lose your passwords or encrypted files, **your seed phrase cannot be recovered.**

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions, feel free to open an issue or contact me.
