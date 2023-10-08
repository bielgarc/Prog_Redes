import os, sys

DIRATUAL = os.path.dirname(os.path.abspath(__file__))

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            lista = [int(line.strip()) for line in file]
        return True, lista
    except FileNotFoundError:
        return False, None
    except Exception as x:
        print(f'\nErro não indentificado: {x}')
        sys.exit()

def ordena_bubble(lista):
    x = len(lista)
    for n in range(x):
        for p in range(0, x - n - 1):
            if lista[p] > lista[p + 1]:
                lista [p], lista[p + 1] = lista[p + 1], lista[p]
    return True, lista

def ordena_insertion(lista):
    for w in range(1 ,len(lista)):
        chave = lista[w]
        q = w - 1
        while q >= 0 and chave < lista[q]:
            lista[q + 1] = lista[q]
            q -= 1
        lista[q + 1] = chave
    return True, lista

def ordena_selection(lista):
    x = len(lista)
    for p in range(x):
        menos = p
        for m in range(p + 1, x):
            if lista[m] < lista[menos]:
                menos = m
                
        lista[p], lista[menos] = lista[menos], lista[p] 
    return True, lista

def ordena_quick(lista):
    if len(lista) <= 1:
        return True, lista
    
    central = lista[len(lista) // 2 ]
    esquerdo = [w for w in lista if w < central]
    meio = [w for w in lista if w == central]
    direito = [w for w in lista if w > central]
    
    return True, ordena_quick(esquerdo)[1] + meio + ordena_quick(direito)[1]

def salvar_arquivo(lista, nome_arquivo):
    try: 
        with open(f'{nome_arquivo}.txt', 'w') as arquivo:
            for numero in lista:
                arquivo.write(str(numero) + '\n')
        print(f'Lista salva em: {nome_arquivo}')
    except Exception as x:
        print(f'Erro ao tentar salvar o arquivo:{x}')