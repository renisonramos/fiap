'''1 – A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a controlar suas fontes de receitas, gastos, dívidas e investimentos.  Ela precisa realizar uma votação para escolher qual dia da semana é o melhor para a realização das lives com o time da mentoria financeira. Desenvolva um programa em que os colaboradores informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) da sua preferência para participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.
Observação: Verifique o número de colaboradores que irão participar da votação para programar sua estrutura de repetição.
É importante o programa validar a possibilidade de empate.'''


#Mensagem para deixar o usuário ciente para que serve o programa.
# Códigos ANSI para cores e estilo
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
# Mensagem estilizada
mensagem = f"{BOLD}{CYAN}Este programa coleta a preferência dos colaboradores\npara escolher o melhor dia da semana para as lives de mentoria financeira.{RESET}"
# Exibe a mensagem no terminal
print(mensagem)
numero_colaboradores = int(input("Informe o número de colaboradores: "))

# Inicializar contadores para os dias da semana
segunda_feira = 0
terca_feira = 0
quarta_feira = 0
quinta_feira = 0
sexta_feira = 0

# Laço para registrar os votos de cada colaborador
for i in range(numero_colaboradores):
    dia_valido = False
    while not dia_valido:
# Exibir opções e solicitar o voto
        print("\nEscolha o dia da sua preferência:")
        print("1 - Segunda-feira")
        print("2 - Terça-feira")
        print("3 - Quarta-feira")
        print("4 - Quinta-feira")
        print("5 - Sexta-feira")

        try:
            voto = int(input("Digite o número correspondente ao dia: "))

# Verificar o voto usando match case
            match voto:
                case 1:
                    segunda_feira += 1
                    dia_valido = True
                case 2:
                    terca_feira += 1
                    dia_valido = True
                case 3:
                    quarta_feira += 1
                    dia_valido = True
                case 4:
                    quinta_feira += 1
                    dia_valido = True
                case 5:
                    sexta_feira += 1
                    dia_valido = True
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número entre 1 e 5.")

# Exibir a contagem de votos
print(f"\nVotos para segunda-feira: {segunda_feira}")
print(f"Votos para terça-feira: {terca_feira}")
print(f"Votos para quarta-feira: {quarta_feira}")
print(f"Votos para quinta-feira: {quinta_feira}")
print(f"Votos para sexta-feira: {sexta_feira}")

# Verificar qual dia tem o maior número de votos
maior_voto = max(segunda_feira, terca_feira, quarta_feira, quinta_feira, sexta_feira)

# Verificar se houve empate
dias_empate = []
if segunda_feira == maior_voto:
    dias_empate.append("segunda-feira")
if terca_feira == maior_voto:
    dias_empate.append("terça-feira")
if quarta_feira == maior_voto:
    dias_empate.append("quarta-feira")
if quinta_feira == maior_voto:
    dias_empate.append("quinta-feira")
if sexta_feira == maior_voto:
    dias_empate.append("sexta-feira")

# Exibir o resultado
if len(dias_empate) > 1:
    print("Houve um empate entre os dias: " + ", ".join(dias_empate))
else:
    print(f"O dia escolhido pelos colaboradores é: {dias_empate[0]}.")
