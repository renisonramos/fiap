'''
instrumento1 = 'Bateria'
instrumento2 = 'Violão'
instrumento3 = 'Guitarra'
'''
lista_instrumentos = ['Bateria','Violão','Guitarra']
lista_instrumentos.append(input('Adcione um novo instrumento: '))
lista_instrumentos.sort()

for instrumento in lista_instrumentos:
    print(instrumento)