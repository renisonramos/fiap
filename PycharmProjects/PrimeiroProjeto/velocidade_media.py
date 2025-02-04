#Pedir a distância de uma viagem
distancia = float(input('Qual foi a distância da viagem?'))

#Pedir o tempo da viagem
tempo = float(input('Qual foi o tempo da viagem?'))

#Dividir a distância pelo tempo
velocidade_media = distancia / tempo

#Exibir o resultado para o usuário
print(f'A velocidade média foi de {velocidade_media:.2f} km/h')