# ==============================================================================
# PROVA PRÁTICA AV1 - 3º BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: Lucas Coelho
# Data:28/09
# ==============================================================================

# Lista de cadastros brutos recebidos do sistema
cadastros_brutos = [
    "  joao da silva;11988887777  ",
    "  maria sousa;21977776666  ",
    "  carlos edgardo oliveira;31966665555  ",
    "  ana paula lima;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

for i in range(len(cadastros_brutos)):

    # 1. Remove os espaços extras do início e fim do cadastro atual
    cadastro = cadastros_brutos[i].strip()

    # 2. Separa o nome e o telefone
    partes = cadastro.split(";")
    nome = partes[0]
    telefone = partes[1]

    # 3. Converte o nome para letras MAIÚSCULAS
    nome = nome.upper()

    # 4. Extrai o DDD (2 primeiros dígitos do telefone) com fatiamento
    ddd = telefone[0:2]

    # 5. Exibe o resultado padronizado no terminal
    print(f"Funcionário: {nome} | DDD: {ddd} | Telefone: {telefone}")

print("\n==================================================")
print("             PROCESSAMENTO CONCLUÍDO              ")
print("==================================================")
