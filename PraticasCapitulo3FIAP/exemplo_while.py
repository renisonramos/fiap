'''Que tal prendermos o usuário em uma armadi-
Iha? Faremos um algoritmo para que ele seja
obrigado a provar que é um verdadeiro nerd
ao responder: "Qual é a resposta para a vida, o
universo e tudo mais?", e o programa não en-
cerrará até que ele dé a resposta correta (que,
segundo o livro O guia do mochileiro das galá-
xias, de Douglas Adams, é "42").
O que queremos é **repetir** uma pergunta ao
usuário **enquanto** ele não acertar a resposta.
'''
#Criação da variavel com um valor inicial.
resposta = '0'
#Enquanto a resposta não for 42, a repetição ocorre.
while (resposta != '42' ):
#Para cada uma das repetições, o usuário vai submeter uma resposta.
    resposta = input('Qual a resposta para a vida, o universo e tudo mais? ')
#Quando o laço terminar a resposta é exibida.
print('Parabéns, você acertou!')
