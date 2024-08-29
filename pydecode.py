import base64
import hashlib

# Dicionário com o alfabeto em código Morse e números
morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '/': ' '
}

def decode_morse_code(morse_code):
    words = morse_code.split(' / ')
    decoded_message = []

    for word in words:
        letters = word.split()
        decoded_word = ''
        for letter in letters:
            decoded_word += morse_code_dict.get(letter, '')
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)

def clean_input(input_string):
    return input_string.strip().upper()

def decode_binary(binary_str):
    binary_str = binary_str.replace(" ", "")
    bytes_array = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    decoded_bytes = [int(byte, 2) for byte in bytes_array]
    decoded_string = ''.join(chr(byte) for byte in decoded_bytes)
    return decoded_string

def decode_hex(hex_str):
    hex_str = hex_str.replace(" ", "")
    decoded_bytes = bytes.fromhex(hex_str)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

def decode_base32(base32_str):
    try:
        decoded_bytes = base64.b32decode(base32_str.upper(), casefold=True)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except Exception as e:
        return f"Erro: {e}"

def rot13_decode(text):
    decoded_chars = []
    for char in text:
        if char.isalpha():
            shifted = ord(char) + 13
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            decoded_chars.append(chr(shifted))
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)

def rot47_decode(text):
    decoded_chars = []
    for char in text:
        if 33 <= ord(char) <= 126:
            shifted = 33 + ((ord(char) - 33 + 47) % 94)
            decoded_chars.append(chr(shifted))
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)

def decode_leet_speak(text):
    leet_dict = {
        '4': 'A', '3': 'E', '1': 'I', '0': 'O', '7': 'T',
        '5': 'S', '2': 'Z', '8': 'B', '@': 'A', '9': 'G',
        '$': 'S', '(': 'C', ')': 'C', '|': 'I', '[': 'B',
        ']': 'B', '6': 'G', '#': 'H', '^': 'V', '<': 'L',
        '>': 'L', '+': 'T', '/': 'F', '\\': 'F',
        ':': 'I', ';': 'I', '~': 'N', '`': 'I', '£': 'S',
        '¢': 'C', '¨': 'I', '°': 'O', '?': 'C', '!': 'I',
    }
    
    decoded_chars = []
    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i:i+2] in leet_dict:
            decoded_chars.append(leet_dict[text[i:i+2]])
            i += 2
        elif text[i] in leet_dict:
            decoded_chars.append(leet_dict[text[i]])
            i += 1
        else:
            decoded_chars.append(text[i])
            i += 1

    return ''.join(decoded_chars)

def md5_hash(text):
    """Calcula o hash MD5 de uma string."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def sha224_hash(text):
    """Calcula o hash SHA-224 de uma string."""
    return hashlib.sha224(text.encode('utf-8')).hexdigest()

def sha256_hash(text):
    """Calcula o hash SHA-256 de uma string."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def sha384_hash(text):
    """Calcula o hash SHA-384 de uma string."""
    return hashlib.sha384(text.encode('utf-8')).hexdigest()

def sha512_hash(text):
    """Calcula o hash SHA-512 de uma string."""
    return hashlib.sha512(text.encode('utf-8')).hexdigest()

def break_hash(hash_to_break, wordlist_file, hash_function):
    """Tenta quebrar um hash usando uma wordlist e uma função de hash especificada."""
    hash_functions = {
        'md5': md5_hash,
        'sha224': sha224_hash,
        'sha256': sha256_hash,
        'sha384': sha384_hash,
        'sha512': sha512_hash
    }
    
    if hash_function not in hash_functions:
        return "Função de hash desconhecida."
    
    hash_func = hash_functions[hash_function]
    
    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            word = line.strip()
            hashed_word = hash_func(word)
            if hashed_word == hash_to_break:
                return f'Senha encontrada na wordlist: {word}'
    return 'Senha não encontrada na wordlist.'

def decode_ascii(ascii_string):
    """Decodifica uma string de códigos ASCII separados por espaços."""
    ascii_values = ascii_string.split()
    decoded_chars = [chr(int(value)) for value in ascii_values]
    return ''.join(decoded_chars)

if __name__ == '__main__':
    while True:
        print("*****************************")
        print("* 1. Decode UTF-8           *")
        print("* 2. Decode ASCII           *")
        print("* 3. Decode Código Morse    *")
        print("* 4. Decode Base64          *")
        print("* 5. Decode Binário         *")
        print("* 6. Decode Hexadecimal     *")
        print("* 7. Decode Base16          *")
        print("* 8. Decode Base32          *")
        print("* 9. Decode ROT-47          *")
        print("* 10. Decode Leet Speak     *")
        print("* 11. Decode ROT13          *")
        print("* 12. Decode MD5            *")
        print("* 13. Decode SHA-224        *")
        print("* 14. Decode SHA-256        *")
        print("* 15. Decode SHA-384        *")
        print("* 16. Decode SHA-512        *")
        print("* 0. Sair                   *")
        print("*****************************")
        print("* instagram: @rafael_cyber1 *")
        print("*****************************")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            # Opção 1: Decode UTF-8
            dados_codificados = input("Digite os dados codificados em UTF-8: ")

            dados_separados = dados_codificados.split('\\x')
            dados_bytes = bytes([int(x, 16) for x in dados_separados[1:]])
            texto_decodificado = dados_bytes.decode('utf-8')

            print("Texto decodificado:", texto_decodificado)

        elif escolha == '2':
            # Opção 2: Decode ASCII
            ascii_string = input("Digite o código em ASCII (separado por espaços): ")
            try:
                decoded_text = decode_ascii(ascii_string)
                print("Texto decodificado:", decoded_text)
            except Exception as e:
                print("Erro ao decodificar ASCII:", e)

        elif escolha == '3':
            # Opção 3: Decode Código Morse
            morse_input = clean_input(input("Digite o código Morse a ser decodificado: "))
            decoded_text = decode_morse_code(morse_input)

            print("Texto decodificado:", decoded_text)

        elif escolha == '4':
            # Opção 4: Decode Base64
            base64_encoded_string = input("Digite o código em Base64: ")

            try:
                decoded_bytes = base64.b64decode(base64_encoded_string)
                decoded_string = decoded_bytes.decode('utf-8')
                print("String decodificada:", decoded_string)
            except Exception as e:
                print("Erro ao decodificar Base64:", e)

        elif escolha == '5':
            # Opção 5: Decode Binário
            binary_string = input("Digite o código binário: ")

            try:
                decoded_text = decode_binary(binary_string)
                print("Texto decodificado:", decoded_text)
            except Exception as e:
                print("Erro ao decodificar binário:", e)

        elif escolha == '6':
            # Opção 6: Decode Hexadecimal
            hex_string = input("Digite o código em hexadecimal: ")

            try:
                decoded_text = decode_hex(hex_string)
                print("Texto decodificado:", decoded_text)
            except Exception as e:
                print("Erro ao decodificar hexadecimal:", e)

        elif escolha == '7':
            # Opção 7: Decode Base16
            base16_string = input("Digite o código em Base16: ")

            try:
                decoded_text = decode_hex(base16_string)  # Usando a mesma função que o hexadecimal
                print("Texto decodificado:", decoded_text)
            except Exception as e:
                print("Erro ao decodificar Base16:", e)

        elif escolha == '8':
            # Opção 8: Decode Base32
            base32_string = input("Digite o código em Base32: ")

            try:
                decoded_text = decode_base32(base32_string)
                print("Texto decodificado:", decoded_text)
            except Exception as e:
                print("Erro ao decodificar Base32:", e)

        elif escolha == '9':
            # Opção 9: Decode ROT-47
            rot47_string = input("Digite o texto codificado com ROT-47: ")
            decoded_text = rot47_decode(rot47_string)
            print("Texto decodificado:", decoded_text)

        elif escolha == '10':
            # Opção 10: Decode Leet Speak
            leet_string = input("Digite o texto codificado em Leet Speak: ")
            decoded_text = decode_leet_speak(leet_string)
            print("Texto decodificado:", decoded_text)

        elif escolha == '11':
            # Opção 11: Decode ROT13
            texto_codificado = input("Digite o texto codificado com ROT13: ")
            texto_decodificado = rot13_decode(texto_codificado)
            print("Texto decodificado:", texto_decodificado)

        elif escolha == '12':
            # Opção 12: Quebrar hash MD5 com wordlist
            hash_to_break = input("Digite o hash MD5 a ser quebrado: ").strip()
            wordlist_file = input("Digite o caminho para o arquivo da wordlist: ").strip()
            result = break_hash(hash_to_break, wordlist_file, 'md5')
            print(result)

        elif escolha == '13':
            # Opção 13: Quebrar hash SHA-224 com wordlist
            hash_to_break = input("Digite o hash SHA-224 a ser quebrado: ").strip()
            wordlist_file = input("Digite o caminho para o arquivo da wordlist: ").strip()
            result = break_hash(hash_to_break, wordlist_file, 'sha224')
            print(result)

        elif escolha == '14':
            # Opção 14: Quebrar hash SHA-256 com wordlist
            hash_to_break = input("Digite o hash SHA-256 a ser quebrado: ").strip()
            wordlist_file = input("Digite o caminho para o arquivo da wordlist: ").strip()
            result = break_hash(hash_to_break, wordlist_file, 'sha256')
            print(result)

        elif escolha == '15':
            # Opção 15: Quebrar hash SHA-384 com wordlist
            hash_to_break = input("Digite o hash SHA-384 a ser quebrado: ").strip()
            wordlist_file = input("Digite o caminho para o arquivo da wordlist: ").strip()
            result = break_hash(hash_to_break, wordlist_file, 'sha384')
            print(result)

        elif escolha == '16':
            # Opção 16: Quebrar hash SHA-512 com wordlist
            hash_to_break = input("Digite o hash SHA-512 a ser quebrado: ").strip()
            wordlist_file = input("Digite o caminho para o arquivo da wordlist: ").strip()
            result = break_hash(hash_to_break, wordlist_file, 'sha512')
            print(result)

        elif escolha == '0':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Escolha novamente.")

        input("Pressione Enter para continuar...")
        
