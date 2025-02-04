'''1 - Você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos
alimentos consumiu naquele dia e depois possa informar o número de calorias de cada um dos
alimentos. Como não estudamos listas neste capítulo, você não deve se preocupar em armazenar
todas as calorias digitadas, mas deve exibir o total de calorias no final. '''

# Solicitar ao usuário o número de alimentos consumidos
quantidade_alimentos = int(input("Quantos alimentos você consumiu hoje? "))

# Inicializar uma variável para armazenar o total de calorias
total_calorias = 0

# Usar um loop para somar as calorias de cada alimento
for i in range(quantidade_alimentos):
    calorias = float(input(f"Digite o número de calorias do alimento {i + 1}: "))
    total_calorias += calorias

# Exibir o total de calorias consumidas
print(f"Total de calorias consumidas hoje: {total_calorias:.2f}")
