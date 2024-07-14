import requests
import argparse

def check_directory(url, directory):
    try:
        response = requests.get(url + directory)
        if response.status_code == 200:
            print(f'[+] Diretório encontrado: {url}{directory}')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar {url}{directory}: {e}')

def main():
    print("*************************")
    print("instagram: @rafael_cyber1")
    print("*************************")

    parser = argparse.ArgumentParser(description='GoBuster em Python')
    parser.add_argument('-u', '--url', required=True, help='URL base para enumeração de diretórios')
    parser.add_argument('-w', '--wordlist', required=True, help='Caminho para o arquivo de lista de palavras')
    args = parser.parse_args()

    url = args.url
    wordlist = args.wordlist

    try:
        with open(wordlist, 'r') as file:
            directories = file.read().splitlines()

        for directory in directories:
            check_directory(url, directory)

    except FileNotFoundError:
        print(f'Arquivo {wordlist} não encontrado.')

if __name__ == "__main__":
    main()
