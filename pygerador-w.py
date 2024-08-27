import random
import string

def obter_informacao(prompt):
    return input(prompt).strip()

def gerar_combinacoes_unicas(informacoes, num_combinacoes, min_len=5, max_len=20):
    combinacoes_geradas = set()
    
    while len(combinacoes_geradas) < num_combinacoes:
        comprimento = random.randint(min_len, max_len)  # Comprimento aleatório entre min_len e max_len
        # Cria uma combinação com comprimento aleatório usando as informações fornecidas
        combinacao = ''.join(random.choices(informacoes, k=comprimento))
        if min_len <= len(combinacao) <= max_len:  # Verifica se a combinação está no intervalo de comprimento desejado
            combinacoes_geradas.add(combinacao)
    
    return combinacoes_geradas

print("****************************")
print("* Instagram: rafael_cyber1 *")
print("****************************")

def criar_wordlist_combinacoes():
    # Solicitar as 10 informações do usuário
    info1 = obter_informacao("INFO 1: ")
    info2 = obter_informacao("INFO 2: ")
    info3 = obter_informacao("INFO 3: ")
    info4 = obter_informacao("INFO 4: ")
    info5 = obter_informacao("INFO 5: ")
    info6 = obter_informacao("INFO 6: ")
    info7 = obter_informacao("INFO 7: ")
    info8 = obter_informacao("INFO 8: ")
    info9 = obter_informacao("INFO 9: ")
    info10 = obter_informacao("INFO 10: ")

    informacoes = [info1, info2, info3, info4, info5, info6, info7, info8, info9, info10]

    # Número de combinações desejado
    num_combinacoes = 5000  # Ajuste conforme necessário

    # Gerar combinações únicas
    combinacoes = gerar_combinacoes_unicas(informacoes, num_combinacoes, min_len=5, max_len=20)

    # Criar e abrir o arquivo de texto para escrita
    with open("combinacoes_wordlist.txt", "w") as arquivo:
        for combinacao in combinacoes:
            arquivo.write(f"{combinacao}\n")

    print(f"Wordlist com {len(combinacoes)} combinações únicas criada com sucesso em 'combinacoes_wordlist.txt'.")

# Executar a função para criar a wordlist com combinações
criar_wordlist_combinacoes()
