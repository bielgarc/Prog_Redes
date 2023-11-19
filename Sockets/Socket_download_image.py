import socket, os
from função_nome import nome_arquivo
PORT = 80


try:
    url_completa = input("Insira a URL da imagem que deseja baixar: ")

    # Separa o identificador do host e o identificador da imagem
    url_partes = url_completa.split('//')
    url_host = url_partes[1].split('/')[0]
    url_imagem = '/' + '/'.join(url_partes[1].split('/')[1:])

    nome = nome_arquivo(url_completa)
    
    # Cria o socket e faz a requisição
    url_request = f'GET {url_imagem} HTTP/1.1\r\nHost: {url_host}\r\n\r\n'
    sock_image = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_image.connect((url_host, PORT))
    sock_image.sendall(url_request.encode())

    content_length = None
    imagem = b''

    while True:
        dados = sock_image.recv(4096)
        if not dados:
            break
        imagem = imagem + dados
        content_length_match = imagem.split(b'Content-Length:')
        if len(content_length_match) > 1:
            content_length = int(content_length_match[1].split()[0])

        # Verifica se os dados foram recebidos
        if content_length is not None and len(imagem) >= content_length:
            break
    sock_image.close()
    print(f'\nTamanho da Imagem: {content_length} bytes')

    # Separa os cabeçalhos e os dados da imagem
    fim = '\r\n\r\n'.encode()
    posicao = imagem.find(fim)
    dados_bin = imagem[posicao + 4:]
    cabeçalhos = imagem[:posicao]

    # Salva a imagem no arquivo
    file_output = open(nome, 'wb')
    file_output.write(dados_bin)
    file_output.close()
except ConnectionError:
    print("Não foi possível estabelecer conexão.")
except TimeoutError:
    print("Espirou o tempo limite.")
except Exception as error:
    print(f"Ocorreu um erro: {error}")
