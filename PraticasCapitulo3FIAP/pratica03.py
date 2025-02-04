'''3 - Uma grande empresa de jogos deseja tornar seus games mais desafiadores. Por isso ela con-
tratou você para desenvolver um algoritmo que será aplicado futuramente em diversos outros ga-
mes: o algoritmo da sorte de Fibonacci.

A ideia dessa empresa, é claro, é fazer com que seja mais difícil os jogadores terem sucesso nas
ações que realizam nos games. Por isso o seu algoritmo deverá funcionar da seguinte forma: o
usuário deve digitar um valor numérico inteiro e o algoritmo deverá verificar se esse valor encon-
tra-se na sequência de Fibonacci. Caso o número esteja na sequência, o algoritmo deve exibir a
mensagem "Ação bem-sucedida!", e caso não esteja, deve exibir a mensagem "A ação falhou...".

A sequência de Fibonacci é muito simples e possui uma lógica de fácil compreensão: ela se inicia
em 1 e cada novo elemento da sequência é a soma dos dois elementos anteriores. Portanto: 1, 1, 2,
3, 5, 8, 13, 21, e assim por diante.

Logo, se o usuário digitar o número 55 o programa deverá informar que a ação foi bem-sucedida,
afinal 55 está entre os números da sequência.

Mas, se o usuário digitar o número 6, por exemplo, a ação não será bem-sucedida, pois o número
6 não está na sequência.
'''

# Função para verificar se um número está na sequência de Fibonacci
def eh_fibonacci(numero):
    # Iniciando os dois primeiros números da sequência
    a, b = 1, 1
    # Continuar gerando a sequência até encontrar ou passar o número
    while b < numero:
        a, b = b, a + b
    # Se o número for igual a 'b', ele pertence à sequência de Fibonacci
    return b == numero or numero == 1

# Solicitar ao usuário que insira um valor numérico
numero = int(input("Digite um número inteiro: "))

# Verificar se o número está na sequência de Fibonacci
if eh_fibonacci(numero):
    print("Ação bem-sucedida!")
else:
    print("A ação falhou...")
