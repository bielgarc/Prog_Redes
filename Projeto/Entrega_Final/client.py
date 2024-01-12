import threading, platform, subprocess
import socket, os, time
from Function_Linux import *
from Function_Wind import *
from browser_history.browsers import Chrome, Edge, Firefox
import os
import sqlite3

SERVER = 'localhost'
PORT = 5678
SO = platform.system()

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        if not connect_server(client):
            print('\nNão foi possível se conectar ao servidor!\n')
            return

        server_thread = threading.Thread(target=recebe_comandos, args=(client,))
        server_thread.start()
        
def connect_server(client):
    try:
        client.connect((SERVER, PORT))
        print("Conectado")
        return True
    except:
        return False

def recebe_comandos(client):
    while True:
        try:
            msg = client.recv(512).decode('utf-8')
            if msg is None:
                print('\nNão foi possível permanecer conectado no servidor!\n')
                client.close()
                return
            try:
                resposta = resposta(msg)
            except: 
                resposta = 'Comando Inválido'
            finally:
                print('Falha ao tentar digitar um comando.')
            
            client.send(f'{resposta}'.encode('utf-8'))
        except socket.timeout:
            print('\nNão foi possível receber dados do servidor.\n')

def resposta(comando):
    if SO == 'Windows':
        return resposta_Wind(comando)
    elif SO == 'Linux':
        return resposta_Linux(comando)
    else:
        return 'Sistema operacional não suportado'

def resposta_Wind(comando):
    if comando == '/start':
        return 'Olá, seja bem-vindo ao bot Prog_Redes! No que posso ajudá-lo? Utilize os comandos /U, /C, /i ip, /N t, /u ip, /off c- ip ou /off -s para solucionar seus problemas. Possíveis dúvidas, utilize o nosso manual de ajuda, basta digitar /help.'
    elif comando == '/U':
        return ''
    elif comando == '/C':
        return ''
    elif comando == '/ip i':
        return ''
    elif comando == '/N t':
        return ''
    elif comando == '/u ip':
        return ''
    elif comando == '/off -c ip':
        return ''
    elif comando == '/off -s':
        return ''
    elif comando == '/help':
        return 'Olá, bem-vindo à central de ajudas do bot Prog_Redes. /U: Lista usuários conectados, /C: Lista configurações de usuários, /ip i: Apps instalados (IP), /N t: Histórico de navegação (App), /u ip: Info usuário (IP), /off -c ip: Desconectar cliente (IP), /off -s: Desconectar servidor.'
    else:
        return 'Comando não reconhecido. Use /help para obter a lista de comandos disponíveis.'
    
def resposta_Linux(comando):
    if comando == '/start':
        return 'Olá, seja bem-vindo ao bot Prog_Redes! No que posso ajudá-lo? Utilize os comandos /U, /C, /i ip, /N t, /u ip, /off c- ip ou /off -s para solucionar seus problemas. Possíveis dúvidas, utilize o nosso manual de ajuda, basta digitar /help.'
    elif comando == '/U':
        return ''
    elif comando == '/C':
        return ''
    elif comando == '/ip i':
        return ''
    elif comando == '/N t':
        return ''
    elif comando == '/u ip':
        return ''
    elif comando == '/off -c ip':
        return ''
    elif comando == '/off -s':
        return ''
    elif comando == '/help':
        return 'Olá, bem-vindo à central de ajudas do bot Prog_Redes. /U: Lista usuários conectados, /C: Lista configurações de usuários, /ip i: Apps instalados (IP), /N t: Histórico de navegação (App), /u ip: Info usuário (IP), /off -c ip: Desconectar cliente (IP), /off -s: Desconectar servidor.'
    else:
        return 'Comando não reconhecido. Use /help para obter a lista de comandos disponíveis.'


def processar_mensagem(msg):
    if msg.startswith('/start'):
        return resposta_Wind(msg)
    elif msg.lower() == '/N t':
        return historico_navegacaoL()
    elif msg.lower() == '/C':
        return informacoes_hardwareL()
    elif msg.lower() == '/ip i':
        return lista_programas_instaladosL()    
    elif msg.lower() == '/help':
        return 'Olá, bem-vindo à central de ajudas do bot Prog_Redes. /U: Lista usuários conectados, /C: Lista configurações de usuários, /ip i: Apps instalados (IP), /N t: Histórico de navegação (App), /u ip: Info usuário (IP), /off -c ip: Desconectar cliente (IP), /off -s: Desconectar servidor.'
    else:
        return 'Comando não reconhecido. Use /help para obter a lista de comandos disponíveis.'

def informacoes_hardwareW():
    return hardware_Wind()

def lista_programas_instaladosW():
    return programs_Wind()

def informacoes_hardwareL():
    informacoes = hardware()
    return informacoes 

def informacoes_usuario_logadoL():
    informacoes = agentes_IP()
    return informacoes
def lista_programas_instaladosL():
    informacoes = programas()
    return informacoes

def historico_navegacaoL():
    return "Histórico de navegação em diferentes navegadores."

main()