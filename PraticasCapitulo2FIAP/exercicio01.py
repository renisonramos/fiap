'''QUANDO A MÁQUINA COMEÇA A TOMAR DECISÕES
1 - Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso,
você deve solicitar ao usuário que informe o seu número de BATIMENTOS POR MINUTO (BPM) e
a IDADE. A partir disso, o script deve verificar e exibir uma mensagem informando se os batimen-
tos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO
da faixa adequada, de acordo com o site Tua Saúde (https://www.tuasaude.com/frequencia-
cardiaca/#:-:text=At%C3%A9%202%20anos%20de%20idade, Idosos%3A%2050%20a%2060%20
bpm):
IDADE BPM
Até 2 anos 120 a 140
De 8 anos até 17 anos 80 a 100
Adulto sedentário 70 a 80
Idosos 50 a 60
'''
print('VERIFICADOR DE FREQUENCIA CARDÍACAS')
idade = int(input('Digite sua idade: '))
bpm = int(input('Por favor informe a sua idade: '))
if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print('Frequencia cardiaca adequada')
    else:
        print('Frequencia cardiaca inadequada')
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print('Frequencia cardiaca adequada')
    else:
        print('Frequencia cardiaca inadequada')
elif idade >= 18 and idade <= 49:
    if bpm >= 70 and bpm <= 80:
        print('Frequencia cardiaca adequada')
    else:
        print('Frequencia cardiaca inadequada')
elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print('Frequencia cardiaca adequada')
    else:
        print('Frequencia cardiaca inadequada')
else:
    print('Não existem dados para a idade indicada.')



