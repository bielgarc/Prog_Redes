import socket
import threading
import functions from *

SERVER = '0.0.0.0'
PORT = 5678

def interacao_client(conexao, cliente):
    try:
        while True:
            mensagem_cliente = conexao.recv(512).decode('utf-8')
            
            if not mensagem_cliente:
                break
            
            print(f'Mensagem do cliente {cliente}: {mensagem_cliente}')
            if mensagem_cliente == '/exit':
                break

    except Exception as e:
        print(f'Erro na comunicação com o cliente {cliente}: {e}')
    finally:
        conexao.close()
        print(f'Conexão com {cliente} encerrada.')


def main():
    print('Recebendo Mensagens...\n\n')

   def main():
    bot_thread = threading.Thread(target=iniciar)
    bot_thread.start()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp_socket.bind((SERVER, PORT))
        tcp_socket.listen(5)

        while True:
            conexao, cliente = tcp_socket.accept()
            print('Conectado por: ', cliente)
            client_thread = threading.Thread(target=interacao_client, args=(conexao, cliente))
            client_thread.start()

    except OSError as os_err:
        print(f'Erro no socket: {os_err}')
    finally:
        tcp_socket.close()

def iniciar():
    update_id = None
    token = 'Substitua pelo seu TOKEN'
    url_base = f'https://api.telegram.org/bot{token}/'

    while True:
        atualizacao = obtendo_mensagens(update_id, url_base)
        mensagens = atualizacao
        if mensagens:
            for mensagem in mensagens:
                update_id = mensagem.get('update_id', update_id)
                chat_id = mensagem['message']['from']['id']

                resposta = comando(mensagem, chat_id, url_base)
                respondendo(resposta, chat_id, url_base)
    iniciar()

main()
