#criando um dicionario com dados
dicionário = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o dicionário completo
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
#removendo o item cuja chave é R2-D2
dicionário.pop("R2-D2")
#exibindo o dicionário completo após a remoção
for chave, valor in dicionário.items():
    print("O personagem {} é da categoria {}".format(chave, valor))