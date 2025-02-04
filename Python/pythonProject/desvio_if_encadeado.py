#Faixa de Bônus
# > 1000 3GB
# > 500 1,5GB
# > 200 500MB
# < 200 nenhum bonus

pontos = int(input('Informe a quantidade de pontos do cleinte: '))
if pontos > 1000:
    print('O cliente recebe 3GB adicionais.')
else:
    if pontos > 500:
        print('O cliente recebe 1,5GB adicionais.')
    else:
        if pontos > 200:
            print('O cliente recebe 500MB adicionais')
        else:
            print('O cliente não recebe nenhum ponto.')
