# Mensagem inicial
print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

# Entrada do usuário
tipo_investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

# Verifica se o tipo de investimento é válido
if tipo_investimento not in [1, 2, 3]:
    print("Tipo de investimento inválido! Por favor, escolha 1, 2 ou 3.")
else:
    valor_resgate = float(input("Digite o valor a ser resgatado: "))
    dias_investido = int(input("Digite o número de dias que o valor permaneceu investido: "))

    # Inicializa a variável do imposto de renda
    imposto_renda = 0

    # Calcula o imposto de renda se o investimento for CDB (tipo 1)
    if tipo_investimento == 1:
        if dias_investido <= 180:
            imposto_renda = valor_resgate * 0.225
        elif 181 <= dias_investido <= 360:
            imposto_renda = valor_resgate * 0.20
        elif 361 <= dias_investido <= 720:
            imposto_renda = valor_resgate * 0.175
        else:
            imposto_renda = valor_resgate * 0.15
    # Para LCI e LCA (tipos 2 e 3), o imposto é zero
    else:
        imposto_renda = 0

    # Exibe o resultado
    print(f"O valor do imposto de renda a ser pago é: R$ {imposto_renda:.2f}")
