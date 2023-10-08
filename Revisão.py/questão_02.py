import os
from função_02 import ler_arquivo, ordena_bubble, ordena_insertion, ordena_selection, ordena_quick, salvar_arquivo

def main():
    nome_arquivo = input('Digite o nome do arquivo que deseja ordenar: ')
    leitura, lista = ler_arquivo(nome_arquivo)

    if leitura:
        print('Arquivo lido.')
        print('Lista original:')
        imprimir_lista(lista)

        metodo = input('Escolha um método de ordenação:')

        if metodo == 'Bubble':
            ordenacao, lista_ordenada = ordena_bubble(lista)
        elif metodo == 'Insertion':
            ordenacao, lista_ordenada = ordena_insertion(lista)
        elif metodo == 'Selection':
            ordenacao, lista_ordenada = ordena_selection(lista)
        elif metodo == 'Quick':
            ordenacao, lista_ordenada = ordena_quick(lista)
        else:
            print('Método de ordenção inválido')
            return

        if ordenacao:
            print('Lista Ordenada')
            imprimir_lista(lista_ordenada)
            arquivo_saida = input('Digite o nome que deseja salvar o arquivo após a ordenção: ')
            salvar_arquivo(lista_ordenada, arquivo_saida)
        else:
            print('Falha ao tentar ordenar lista')
    else:
        print('Falha na leitura do arquivo original')

def imprimir_lista(lista):
    for numero in lista:
        print(numero)

if __name__ == "__main__":
    main()