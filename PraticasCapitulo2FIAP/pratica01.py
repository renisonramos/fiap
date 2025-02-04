#Nosso programa deve solicitar o e-mail e a nota do aluno, exibindo a mensagem "ENVIANDO CONVITE" caso a nota do aluno satisfaça a condição proposta.
#solicitando o emial do aluno
email = input('Digite o seu e-mail: ')
#solicitando a nota do aluno
nota = int(input('Agora digite sua nota: '))
#realizando o teste de condição
if nota > 8.5:
    print('ENVIANDO CONVITE, PARABÉNS, VOCÊ ESTÁ SENDO CONVIDADO PARA UMA VISITA DE CAMPO NA AMERICA DO SUL.')