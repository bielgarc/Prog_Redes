import random, os, sys

DIRATUAL = os.path.dirname(os.path.abspath(__file__)) 

conteudo = input("Informe o nome do que é para colocar no conteúdo a ser gerado: ")

def gerar_lista(quantidade:int, valor_minimo:int, valor_maximo:int):
    boolSucesso = False
    lstRetorno  = None

    lista = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade)]

    if lista != []:
        boolSucesso, lstRetorno = True, lista
        salvar_lista(lista, conteudo)
        return (f"{boolSucesso} \n{lstRetorno}")
    else:
        return (f"{boolSucesso} \n{lstRetorno}")

def salvar_lista(nome_lista: list, nome_arquivo: str):
    boolSucesso  = False
    Nome_Conteudo = DIRATUAL + '\\' + nome_arquivo
    try:
        arquivo_output = open(f'{nome_arquivo}.txt', 'w')
    except:
        print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
        sys.exit()
    else:
        for _ in nome_lista: arquivo_output.write(f'{_}\n')
        arquivo_output.close()

    return boolSucesso


