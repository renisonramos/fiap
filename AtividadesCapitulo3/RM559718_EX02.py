'''2– A compra de um veículo pode ser realizada parcelada. Crie um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
a) O preço final para compra à vista tem um desconto de 20%:
b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60: '''
# Mensagem inicial para deixar o usuário ciente para que serve o programa.
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"

mensagem = f"{BOLD}{CYAN}Este programa calcula o preço final de um carro e as opções de parcelamento.{RESET}"
print(mensagem)
# Entrada do usuário
valor_carro = float(input("Informe o valor do carro: "))

# Preço final à vista com desconto
preco_vista = valor_carro * 0.8

# Exibir tabela de parcelas e acréscimos
print(f"{'Parcelas':<10}{'Acréscimo':<15}{'Preço Final':<20}{'Valor da Parcela'}")
print("-" * 50)

# Exibir o preço final à vista com desconto
print(f'O preço final á vista com desconto de 20% é: R$ {preco_vista:.2f}')

# Exibir os resultados com o formato desejado
for parcelas in [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]:
    if parcelas == 6:
        acrescimo = 0.03
    elif parcelas == 12:
        acrescimo = 0.06
    elif parcelas == 18:
        acrescimo = 0.09
    elif parcelas == 24:
        acrescimo = 0.12
    elif parcelas == 30:
        acrescimo = 0.15
    elif parcelas == 36:
        acrescimo = 0.18
    elif parcelas == 42:
        acrescimo = 0.21
    elif parcelas == 48:
        acrescimo = 0.24
    elif parcelas == 54:
        acrescimo = 0.27
    elif parcelas == 60:
        acrescimo = 0.30

    # Calcula o preço final e o valor da parcela
    preco_final = valor_carro * (1 + acrescimo)  # Preço final com acréscimo
    valor_parcela = preco_final / parcelas  # Valor de cada parcela

    # Exibir os resultados formatados conforme solicitado
    print(f'O preço final parcelado em {parcelas} X é de R$ {preco_final:,.2f} com parcelas de R$ {valor_parcela:,.2f}')




