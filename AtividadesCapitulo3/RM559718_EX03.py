# Mensagem inicial para deixar o usuário ciente para que serve o programa.
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
mensagem = f"{BOLD}{CYAN}Este programa calcula o valor da dívida, juros e parcelas para um empréstimo.{RESET}"
print(mensagem)

# Entrada do usuário
valor_divida = float(input("Digite o valor da dívida: "))

# Exibir a tabela de valores
for parcelas in [1, 3, 6, 9, 12]:
    # Definindo os juros com base na quantidade de parcelas
    if parcelas == 1:
        taxa_juros = 0.00
    elif parcelas == 3:
        taxa_juros = 0.10
    elif parcelas == 6:
        taxa_juros = 0.15
    elif parcelas == 9:
        taxa_juros = 0.20
    elif parcelas == 12:
        taxa_juros = 0.25

    # Cálculo dos juros
    valor_juros = valor_divida * taxa_juros
    # Cálculo do valor total da dívida
    total_divida = valor_divida + valor_juros
    # Cálculo do valor da parcela
    valor_parcela = total_divida / parcelas

    # Exibir os resultados
    print(f"Total: R$ {total_divida:,.2f} Juros: R$ {valor_juros:,.2f} Número de parcelas: {parcelas} Valor da Parcela: R$ {valor_parcela:,.2f}")
