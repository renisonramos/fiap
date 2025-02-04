import json
#Indicando onde ta o meu arquivo Json
arquivo = open("c:\\arquivos\\agenda.json" , "r", encoding="utf-8")

#colocando o arquivo em uma variavel do tipo string
conteudo = arquivo.read()

#fechando o arquivo
arquivo.close()

#usando o método loads para converter uma string no formato json em um dicionário.
agenda = json.loads(conteudo)

#agenda agora é do tipo dicionario
print(type(agenda))
