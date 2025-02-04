#criando um dicionario vazio
dicionário = {}
#incluindo dados no dicionario
dicionário["André David"] = "Professor"
#Pedindo para o usuário incluir dados no dicionário
nova_chave = input("Informe o nome do colaborador da FIAP")
novo_valor = input("Informe a função do colaborador da FIAP")
dicionário[nova_chave] = novo_valor
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))