#lista que gere um arquivo aleatório e salve 
import random 

try:
 numeros = int(input('digite a quantidade de números que desejar:')) 

 lista = []
  

 for i in range(numeros): 
    lista.append(random.randint(1,1000000)) 
except ValueError:
    print('erro, o valor informado não corresponde a um número inteiro')
except TypeError:
    print('erro, o valor informado não corresponde a um número inteiro')
except Exception as a:
    print(f'Erro{a}')
else:    
 arq = open('lista_nao_ordenada.txt', 'w') 
 for i in lista: 
  arq.write(f'{i}\n')  
  
arq.close()