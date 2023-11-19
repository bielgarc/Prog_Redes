import socket
# Função para fazer a verificação da porta
def verificar_porta(ip, porta, protocolo, nome):
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocolo == 'TCP' else socket.SOCK_DGRAM)
        if sock.connect_ex((ip, porta)) == 0:
            print(f'Porta {porta}: Protocolo: {protocolo}: {nome}/ Status: Responde (Aberta)')
        else:
            print(f'Porta {porta}: Protocolo: {protocolo}: {nome}/ Status: Não Responde (Fechada)')
    except Exception as e:
        print(f"Erro ao verificar a porta {porta}: {e}")
    finally:
        if sock:
            sock.close()