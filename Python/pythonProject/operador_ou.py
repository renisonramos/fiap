#Uma loja concede descontos para compras pagas com cartão de crédito ou com valores acima de 1000.

valor_compra = float(input('Por favor informe o valor da compra: '))

forma_pagamento = int(input('FORMA DE PAGAMENTO\n1 - Cartão de crédito\n2 - Dinheiro\nInforme a forma adotada:  '))

if valor_compra > 1000 or forma_pagamento == 1:
    valor_compra = valor_compra * 0.9
    print('O cliente tem direito a descontos')
print(f'O valor da compra é de {valor_compra}')