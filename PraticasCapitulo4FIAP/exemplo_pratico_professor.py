#Estrutura de menu
opcao = -1
notas = []
while opcao != 4:
    print('1 - Cadastrar nota\n2 - Exibir notas\n3 - Calcular média\n4 - Sair')
    opcao = int(input('Informe a opção desejada: '))

    if opcao == 1:
        notas.append(float(input('Por favor, informe a nota do aluno: ')))

    elif opcao == 2:
        print('As notas da turma são:')
        for i in notas:
            print(i)

    elif opcao == 3:
        media = sum(notas) / len(notas)
        print(media)
    elif opcao == 4:
        print('SAINDO ...')

    else:
        print('Opção inválida!')