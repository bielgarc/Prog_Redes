import socket, sys

# Parâmetros de definição do funcionamento
PORT = 80
CODE_PAGE = 'utf-8'
BUFFER_SIZE = 256
TIMEOUT = 5

# Solicita ao usuário que informe o HOST ou URL do site
host = input('\nInforme o nome do HOST ou URL do site: ')

try:
    # Cria um socket e estabelece a conexão, setando um timeout na resposta do servidor
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.settimeout(TIMEOUT)
    tcp_socket.connect((host, PORT))

    # Envia a requisição HTTP para o servidor
    requisicao = f'GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
    tcp_socket.sendall(requisicao.encode(CODE_PAGE))

    total_length = 0

    while True:
        resposta = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
        if not resposta:
            break
        total_length += len(resposta)
        print(resposta)

    if total_length == 0:
        print('O Content-Length do servidor é 0')
    else:
        print(f'O total de bytes da requisição foi de: {total_length}')

except socket.error as e:
    print(f'Erro de socket: {e}')

except Exception as e:
    print(f'Erro inesperado: {e}')

tcp_socket.close()

