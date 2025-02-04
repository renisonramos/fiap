'''2 - Observando o mercado de educação infantil, você e sua equipe decidem criar um aplicativo
por meio do qual as crianças aprendam a controlar os seus gastos.
Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o
usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na
sequência, deve informar o VALOR DE CADA UMA das transações que realizou.
Seu programa deverá exibir, ao final, o valor total gasto pelo usuário, bem como a média do valor
de cada transação.'''

# Solicitar ao usuário o número de transações realizadas
quantidade_transacoes = int(input("Quantas transações você realizou hoje? "))

# Inicializar uma variável para armazenar o total de gastos
total_gastos = 0

# Usar um loop para somar os valores de cada transação
for i in range(quantidade_transacoes):
    valor_transacao = float(input(f"Digite o valor da transação {i + 1}: "))
    total_gastos += valor_transacao

# Calcular a média das transações
media_transacoes = total_gastos / quantidade_transacoes if quantidade_transacoes > 0 else 0

# Exibir o total gasto e a média das transações
print(f"Total gasto hoje: R$ {total_gastos:.2f}")
print(f"Média por transação: R$ {media_transacoes:.2f}")
