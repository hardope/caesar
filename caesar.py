import click
import codecs

# Define Caesar cipher encryption function
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = (char_code - ord('a') + shift) % 26 + ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            encrypted_text += char_code
        else:
            encrypted_text += char
    return encrypted_text

# Define ROT13 encryption function using codecs
def rot13_cipher(text):
    return codecs.encode(text, 'rot_13')

# Define Atbash cipher encryption function
def atbash_cipher(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = ord('z') - (char_code - ord('a'))
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            encrypted_text += char_code
        else:
            encrypted_text += char
    return encrypted_text

def crot13(text, shift, option):
    if option == 'encrypt':
        res = caesar_cipher(text, shift)
        return rot13_cipher(res)
    
    elif option == 'decrypt':
        res = caesar_cipher(text, -shift)  # Decrypt using Caesar cipher with a negative shift
        return rot13_cipher(res)


VERSION = '1.0'

encryption_algorithms = {
    'caesar': caesar_cipher,
    'rot13': rot13_cipher,
    'atbash': atbash_cipher,
    'crot13': crot13
}

@click.command()
@click.option('--file', type=click.File('r'), help='Input file to read text from.')
@click.option('--text', help='Text to encrypt or decrypt.')
@click.option('--shift', type=int, help='Shift value for Caesar cipher (default: 3).', default=3)
@click.option('--decrypt', is_flag=True, help='Decrypt the text (default is to encrypt).')
@click.option('--output', type=click.File('w'), help='Output file to write the result to.')
@click.option('--algorithm', type=click.Choice(['caesar', 'rot13', 'atbash', 'crot13'], case_sensitive=False), default='caesar', help='Encryption algorithm to use (default: Caesar cipher).')
@click.version_option(version=VERSION)  # Add a version option
def main(file, text, shift, decrypt, output, algorithm):
    if file and text: 
        click.echo("Error: Please provide either '--file' or '--text', not both.")
        return

    if not file and not text:
        text = click.prompt('Enter the text to encrypt/decrypt', hide_input=decrypt)

    input_text = text  # Initialize input_text with the value of text

    try:
        if file:
            input_text = file.read()

        if algorithm == 'caesar':
            result = caesar_cipher(input_text, shift if not decrypt else -shift)
        elif algorithm == 'rot13':
            result = rot13_cipher(input_text)
        elif algorithm == 'atbash':
            result = atbash_cipher(input_text)
        elif algorithm == 'crot13':
            result = crot13(input_text, shift, 'encrypt' if not decrypt else 'decrypt')

        if output:
            output.write(result)
            output.close()
            click.echo(f'Result has been written to the file: {output.name}')
        else:
            click.echo(f'Result: {result}')
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    main()
