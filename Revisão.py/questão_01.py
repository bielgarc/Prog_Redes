import random, os, sys
from função_01 import gerar_lista

try:
    quantidade = int(input('Informe a quantidade de elementos da lista: '))
    valor_mínimo = int(input('Informe o valor mínimo presente na lista: '))
    valor_máximo = int(input('Informe o valor máximo presente na lista: '))    
except ValueError:
    print('\nERRO: Por favor informe um número inteiro...\n')
    sys.exit()
except:
    print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
    sys.exit()
else:
    if (quantidade <= 0 or valor_mínimo <=0 or valor_máximo <=0):
        print(f'\nERRO: Por favor informe um número inteiro...\n')
        sys.exit()

print(gerar_lista(quantidade, valor_mínimo,valor_máximo))