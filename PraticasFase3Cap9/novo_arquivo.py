#Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("c:\\arquivos\\novo_arquivo.txt", "a")

#Escrevendo o conteúdo da variável conteudo dentro do arquivo
arquivo.write(conteudo)

#fechando o arquivo
arquivo.close()