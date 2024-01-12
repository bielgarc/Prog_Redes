import socket
import threading
import requests

HOST = 'localhost'
PORT_SERVER = 5678
PORT_TELEGRAM = 65000
BUFFER_SIZE = 512
CODE_PAGE = 'utf-8'

def handle_client(connection, address):
    print(f"Conexão estabelecida com {address}")

    try:
        while True:
            data = connection.recv(BUFFER_SIZE)
            if not data:
                print(f"Conexão encerrada por {address}")
                break

            message = data.decode(CODE_PAGE)
            print(f"Mensagem recebida de {address}: {message}")

            response = processar_mensagem(message)
            connection.sendall(response.encode(CODE_PAGE))

    except ConnectionResetError:
        print(f"Conexão redefinida por {address}")
    except Exception as e:
        print(f"Erro ao lidar com a conexão: {str(e)}")

    finally:
        connection.close()
        print(f"Conexão fechada por {address}")

def send_to_telegram(message):
    telegram_url = "https://api.telegram.org/bot6958977609:AAE5X1-eA9spI7dXOfal1g7WWytgwWmvXeU/sendMessage"
    params = {
        'chat_id': '6970559595',  # Seu chat_id aqui
        'text': message,
    }
    requests.post(telegram_url, params=params)

def processar_mensagem(msg):
    return f"Servidor processou a mensagem: {msg}"

def start_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp_socket.bind((HOST, PORT_SERVER))
        tcp_socket.listen()

        print(f'Aguardando conexões em {HOST}:{PORT_SERVER}\n')

        while True:
            client_connection, client_address = tcp_socket.accept()
            ip_cliente, porta_cliente = client_address
            print(f'{ip_cliente} conectado na porta {porta_cliente}')

            client_thread = threading.Thread(
                target=handle_client,
                args=(client_connection, client_address)
            )

            client_thread.start()

    except Exception as e:
        print(f"Erro ao iniciar o servidor: {str(e)}")
    finally:
        tcp_socket.close()

def enviar_comandos():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        if not conectar_ao_servidor(client):
            print('\nNão foi possível se conectar ao servidor!\n')
            return

        server_thread = threading.Thread(target=receber_respostas, args=(client,))
        server_thread.start()

def conectar_ao_servidor(client):
    try:
        client.connect((HOST, PORT_TELEGRAM))
        print("Conectado ao servidor Telegram")
        return True
    except:
        return False

def receber_respostas(client):
    while True:
        try:
            msg = client.recv(512).decode('utf-8')
            if msg is None:
                print('\nNão foi possível permanecer conectado ao servidor Telegram!\n')
                client.close()
                return
            try:
                resposta = processar_resposta(msg)
            except:
                resposta = 'Resposta inválida'
            finally:
                print('Falha ao tentar processar a resposta.')

            client.send(f'{resposta}'.encode('utf-8'))
        except socket.timeout:
            print('\nNão foi possível receber dados do servidor Telegram.\n')

def processar_resposta(resposta):
    return f"Resposta do servidor Telegram: {resposta}"

def main():
    thread_server = threading.Thread(target=start_server)
    thread_client = threading.Thread(target=enviar_comandos)

    thread_server.start()
    thread_client.start()

if __name__ == '__main__':
    main()
