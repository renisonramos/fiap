somatoria = 0.0
for i in range (1,6, 1):
    nota = float(input('Digite a nota do aluno: '))
    somatoria = somatoria + nota
media = somatoria / 30
print(f'A média da turma é igual a {media}')
