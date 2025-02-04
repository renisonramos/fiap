#importando o módulo sys para conseguirmos usar o getsizeof
import sys
#criando uma lista e uma tupla vazias, respectivamente
lista_vazia = []
tupla_vazia = ()
#printando o tipo e tamanho de cada estrutura
print("O objeto lista_vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))