import socket
import threading

SERVER = 'localhost'
PORT = 5678
PROMPT = 'Digite sua mensagem, se desejar finalizar a conexão, digite /exit - '

def interacao_server(sock):
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(512)
            decoded_msg = msg.decode('utf-8')
            print("\n" + decoded_msg + "\n" + PROMPT)
            
            if decoded_msg == '/exit':
                print('Conexão encerrada pelo cliente.')
                break
        except:
            msg = b''

def interecao_user(sock):
    while True:
        try:
            msg = input(PROMPT)
            if msg != '':
                sock.send(msg.encode('utf-8'))
                if msg == '/exit':
                    print('Conexão encerrada pelo cliente.')
                    break
        except:
            print('Conexão encerrada.')
            break

def close_socket(sock):
    try:
        sock.close()
    except:
        None

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))

    print("Conectado a: ", (SERVER, PORT))

    coenection_server = threading.Thread(target=interacao_server, args=(sock,))
    conection_user = threading.Thread(target=interecao_user, args=(sock,))

    coenection_server.start()
    conection_user.start()

    conection_user.join()

except Exception as e:
    print("Falha ", e)
finally:
    close_socket(sock)
