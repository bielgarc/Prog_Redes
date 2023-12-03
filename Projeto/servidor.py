import socket
from socket_constants import *

# Mapeamento chave-descrição no servidor
mapeamento_chaves_servidor = {
    'U', 'C', 'i ip:', 'N t:', 'u ip:', 'off -c ip:', 'off -s'
}

print('Recebendo Mensagens...\n\n')

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_socket.bind((HOST_SERVER, SOCKET_PORT))
    tcp_socket.listen(MAX_LISTEN)

    while True:
        conexao, cliente = tcp_socket.accept()
        print('Conectado por: ', cliente)

        try:
            chave_servidor = input('Digite a chave do servidor: ')

            if chave_servidor in mapeamento_chaves_servidor:
                conexao.send(chave_servidor.encode(CODE_PAGE))
                descricao_cliente = conexao.recv(BUFFER_SIZE).decode(CODE_PAGE)
                print(f'Cliente concebeu a descrição da chave: {descricao_cliente}')
            else:
                print('Chave desconhecida')

        except OSError as os_err:
            print(f'Erro no socket: {os_err}')
            break
        except Exception as e:
            print(f'Erro na comunicação com o cliente: {e}')
            conexao.close()
except OSError as os_err:
    print(f'Erro no socket: {os_err}')
    


