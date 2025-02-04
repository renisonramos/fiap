'''4 - Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software
malicioso que criptografou todos os discos e pede a digitação de uma senha para a liberação da
máquina. E é claro que os criminosos exigem um pagamento para informar a senha.

Ao analisar o código do programa deles, porém, você descobre que a senha é composta pela pa-
lavra "LIBERDADE" seguida do fatorial dos minutos que a máquina estiver marcando no momento
da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120).
Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária
para desbloqueio. ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do
fatorial. Ele deve obrigatoriamente utilizar loop.'''

# Função para calcular o fatorial usando loop
def calcular_fatorial(minutos):
    fatorial = 1
    for i in range(1, minutos + 1):
        fatorial *= i
    return fatorial

# Solicitar ao usuário que insira os minutos atuais
minutos = int(input("Digite os minutos atuais da máquina: "))

# Calcular o fatorial dos minutos
fatorial_minutos = calcular_fatorial(minutos)

# Gerar a senha necessária
senha = f"LIBERDADE{fatorial_minutos}"

# Exibir a senha
print(f"A senha para desbloqueio é: {senha}")
