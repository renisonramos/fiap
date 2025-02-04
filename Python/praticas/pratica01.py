#1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura')
#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = input('Qual é o seu nome:')
idade = input('Quantos anos você tem:')
print(f'Meu nome é {nome} e tenho {idade} anos ')
#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
print('A')
print('L')
print('U')
print('R')
print('A')

print('ou')

print('A','L','U','R','A',sep='\n') 
#Para imprimir a palavra ‘ALURA’ com cada letra em cada linha com a função print utilizando o parâmetro sep para especificar o separador entre os argumentos. O separador sep é definido como \n, que representa uma quebra de linha.


#4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
pi = 3.14159
print('O valor arredondado de pi é:', round(pi, 2))

"""pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))"""
