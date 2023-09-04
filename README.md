# Text Encryption Command-Line Tool

This is a command-line tool for text encryption and decryption using various algorithms. It supports multiple encryption algorithms, including Caesar cipher, ROT13, Atbash cipher, and a custom `crot13` algorithm. You can use this tool to secure your text-based information or decode encrypted messages.

## Table of Contents

- [Supported Algorithms](#supported-algorithms)
- [Usage Cases](#usage-cases)
- [Installation](#installation)
- [Usage Options](#usage-options)
- [Examples](#examples)

## Supported Algorithms

1. **Caesar Cipher:**
   - The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a fixed number of places down or up the alphabet.
   - For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.
   - In the script, the `caesar_cipher` function takes a text input and a shift value as parameters and returns the encrypted text.

2. **ROT13 Cipher:**
   - ROT13 is a special case of the Caesar cipher with a fixed shift of 13 places.
   - It's often used for obscuring text in online forums or for creating puzzles.
   - In the script, the `rot13_cipher` function uses the `codecs.encode` function with 'rot_13' encoding to perform ROT13 encryption.

3. **Atbash Cipher:**
   - The Atbash cipher is a substitution cipher where each letter in the plaintext is replaced with its corresponding letter in the reverse alphabet.
   - For example, 'A' becomes 'Z', 'B' becomes 'Y', and so on.
   - In the script, the `atbash_cipher` function takes a text input and returns the encrypted text.

4. **Custom crot13 Algorithm:**
   - The `crot13` algorithm combines Caesar and ROT13 ciphers for encryption and decryption. When encrypting, it first applies the Caesar cipher with the specified shift value and then applies ROT13. When decrypting, it reverses the process: it first applies ROT13 and then applies the Caesar cipher with a negated shift value.

These algorithms are used for different purposes and have varying levels of security. Caesar and ROT13 ciphers are very simple and offer minimal security, while the Atbash cipher provides a bit more complexity. However, it's important to note that none of these ciphers are considered secure for modern cryptography. They are mainly used for educational and recreational purposes. For secure text encryption, it's recommended to use strong encryption algorithms like AES (Advanced Encryption Standard) provided by cryptographic libraries.

## Usage Cases

- **Secure Messaging**: You can use this tool to encrypt sensitive text messages before sending them, ensuring that only authorized recipients can decrypt and read the messages.

- **Obfuscation**: The ROT13 and Atbash ciphers are often used to obfuscate text for various purposes, such as hiding spoilers or creating puzzles.

- **Learning Cryptography**: This tool is a practical way to learn about classic encryption algorithms like the Caesar cipher and ROT13.

## Installation

To install and use the Text Encryption Command-Line Tool, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/text-encryption-tool.git
   ```

2. Navigate to the project directory:

   ```shell
   cd text-encryption-tool
   ```

3. Run the provided installation script to set up the environment, install dependencies, and make the command-line tool available:

   ```shell
   chmod +x install
   ./install
   ```

The script will take care of installing Python 3, `pip`, Python 3 `venv`, creating a virtual environment, installing the required packages from `requirements.txt`, and building and installing the command-line tool. It will also clean up temporary files and deactivate and delete the virtual environment when done.

## Usage Options

The command-line tool provides several options to customize the encryption or decryption process:

- `--file`: Input file to read text from.

- `--text`: Text to encrypt or decrypt.

- `--shift`: Shift value for Caesar cipher (default: 3).

- `--decrypt`: Flag to indicate decryption (default is encryption).

- `--output`: Output file to write the result to.

- `--algorithm`: Encryption algorithm to use (default: Caesar cipher). Supported options are 'caesar', 'rot13', 'atbash', and 'crot13'.

### Version
The check the installed version of caesar you have installed
```shell
caesar --version
```

## Examples

### Encrypt text using Caesar cipher:

```shell
python text_encryptor.py --text "Hello, World!" --shift 3
```

### Decrypt text using ROT13:

```shell
python text_encryptor.py --text "Uryyb, Jbeyq!" --algorithm rot13 --decrypt
```

### Encrypt text using the custom `crot13` algorithm:

```shell
python text_encryptor.py --text "Hello, World!" --algorithm crot13 --shift 3
```

### Decrypt text from a file and save the result to another file using ROT13:

```shell
python text_encryptor.py --file encrypted.txt --output decrypted.txt --algorithm rot13 --decrypt
```

### Encrypt text from a file and display the result in the terminal using the Atbash cipher:

```shell
python text_encryptor.py --file input.txt --algorithm atbash
```

### Encrypt text from a file and display the result in the terminal using the custom `crot13` algorithm:

```shell
python text_encryptor.py --file input.txt --algorithm crot13 --shift 3
```

### Decrypt text from a file and display the result in the terminal using the custom `crot13` algorithm:

```shell
python text_encryptor.py --file encrypted.txt --algorithm crot13 --decrypt --shift 3
```

### Encrypt text from a file and save the result to another file using Caesar cipher:

```shell
python text_encryptor.py --file input.txt --output encrypted.txt --shift 5
```

### Decrypt text from a file and save the result to another file using ROT13:

```shell
python text_encryptor.py --file encrypted.txt --output decrypted.txt --algorithm rot13 --decrypt
```

### Encrypt text from a file and display the result in the terminal using the Atbash cipher:

```shell
python text_encryptor.py --file input.txt --algorithm atbash
```

### Encrypt text from a file and display the result in the terminal using the custom `crot13` algorithm:

```shell
python text_encryptor.py --file input.txt --algorithm crot13 --shift 3
```

### Decrypt text from a file and display the result in the terminal using the custom `crot13` algorithm:

```shell
python text_encryptor.py --file encrypted.txt --algorithm crot13 --decrypt --shift 3
```

These examples demonstrate how to use the Text Encryption Command-Line Tool with file inputs and outputs, allowing you to perform encryption and decryption on text stored in files.