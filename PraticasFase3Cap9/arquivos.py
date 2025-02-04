arquivo = open("c:\\arquivos\\arquivo_de_texto.txt", encoding="UTF-8")


for linha in arquivo.readlines():
    print(linha)


arquivo.close()