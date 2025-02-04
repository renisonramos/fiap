#Pedir que o usuário digite o nome do funcionário
nome_do_funcionario = input('Digite o nome do funcionário: ')
#Pedir que o usuário digite o salário do funcionário
salario_do_funcionario = float(input('Digite o salário do funcionário: '))
#Caso o salário seja negativo, alertar o usuário
if (salario_do_funcionario) < 0:
    salario_do_funcionario = salario_do_funcionario * -1
    print('O salário digitado corresponde a um número negativo, reveja as informações novamente')
#Exibir o salário armazenado
    print(f'O funcionário (a) {nome_do_funcionario} recebe R${salario_do_funcionario}')