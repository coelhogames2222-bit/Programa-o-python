telefone = input("Digite o telefone no formato (XX)XXXXX-XXXX:")

ddd = telefone[1:3]
numero = telefone[4:]

print(f"DDD: {ddd}")
print(f"Número: {numero}")

data = input("Digite a data no formato DD/MM/AAAA:")

dia = data[0:2]
mes = data[3:5] 
ano = data[6:]

print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")

email = input("digite seu e-mail (nome.sobrenome@escola.com):")

primeiro_nome = emaik[0:5]
dominio = email[13:]

print(f"primeiro nome extraído: {primeiro_nome}")
print(f"Domínio extraído {dominio}")
