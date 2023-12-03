import socket
from socket_constants import *

# Mapeamento chave-descrição no cliente
mapeamento_chaves = {
    'U': 'Lista os usuários conectados ao servidor',
    'C': 'Lista as configurações dos usuários conectados',
    'i ip:': 'Traz os aplicativos instalados nos clientes especificados pelo IP',
    'N t:': 'Histórico de navegação da aplicação especificada',
    'u ip:': 'Traz informações detalhadas sobre o usuário especificado',
    'off -c ip:': 'Desconecta de maneira manual o cliente especificado',
    'off -s': 'Desconecta de maneira manual o servidor'
}

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

    while True:
        chave = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)

        if chave in mapeamento_chaves:
            descricao = mapeamento_chaves[chave]
            print(f'Recebido: {chave}')

            tcp_socket.send(descricao.encode(CODE_PAGE))
            
        tcp_socket.close()
        break

except OSError as os_err:
    print(f'Erro no socket: {os_err}')

except ConnectionRefusedError:
    print('Conexão recusada pelo servidor. Verifique se existe algum servidor em execução')

except Exception as x:
    print(f'Erro durante a comunicação com o servidor: {x}')

print('Cliente encerrado.')
