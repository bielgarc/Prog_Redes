import socket, sys, os
from função_porta import verificar_porta

try:
    # Obter nome do host
    host = input("Informe o host: ")
    # Obter endereço IP
    ip = socket.gethostbyname(host)
except Exception as e:
    print(f"Erro ao obter o nome do host ou endereço IP: {e}")
    sys.exit(1)

# Manipulação do arquivo
dir_atual = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(dir_atual, 'protocolos.csv')

try:
    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = [linha.strip().strip('"').split('", "') for linha in arquivo]
except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo} não foi encontrado.")
    sys.exit(1)
except Exception as e:
    print(f"Erro ao abrir o arquivo: {e}")
    sys.exit(1)

# Extação de portas e protocolos
TCP, UDP, TCP_UDP = [], [], []

for linha in linhas:
    porta, protocolo, nome = int(linha[0]), linha[1], linha[2]
    
    if protocolo == "TCP,UDP":
        TCP_UDP.append(porta)
    elif protocolo == "TCP":
        TCP.append(porta)
    elif protocolo == "UDP":
        UDP.append(porta)

# Verificando as portas
try:
    for porta in linhas:
        port, protocolo, nome = int(porta[0]), porta[1], porta[2]
        
        try:
            if port in TCP or (port in TCP_UDP and protocolo == 'TCP'):
                verificar_porta(ip, port, 'TCP', nome)
            if port in UDP or (port in TCP_UDP and protocolo == 'UDP'):
                verificar_porta(ip, port, 'UDP', nome)
        except Exception as e:
            print(f"Erro ao verificar a porta {port}: {e}")
except KeyboardInterrupt:
    print("\nVerificação de portas interrompida por meio do teclado.")
    sys.exit(0)
