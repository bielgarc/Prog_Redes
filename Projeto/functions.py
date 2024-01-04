import requests, json

def obtendo_mensagens(update_id, url_base):
    link = f'{url_base}getUpdates?timeout=100'
    if update_id:
        link = f'{link}&offset={update_id + 1}'   
    resultado = requests.get(link)
    try:
        data = json.loads(resultado.content)
        return data.get('result', [])
    except json.JSONDecodeError:
        return []
    
def comando(mensagem, chat_id, url_base):
    try:
        texto = mensagem['message']['text']
        
        if texto == '/start':
            return 'Olá, seja bem-vindo ao bot Prog_Redes! No que posso ajudá-lo? Utilize os comandos /U, /C, /i ip, /N t, /u ip, /off c- ip ou /off -s para solucionar seus problemas. Possíveis dúvidas, utilize o nosso manual de ajuda, basta digitar /help.'
        elif texto in ['/U', '/C', '/i ip', '/N t', '/u ip', '/off -c ip', '/off -s', '/help']:
            return processar_comando(texto)
        else:
            return 'Comando desconhecido. Por favor, utilize /help para ver os comandos disponíveis.'
    except KeyError:
        return 'Desculpe, não consigo interpretar esse tipo de mídia. Por favor, selecione uma das opções informadas no início da interação ou utilize o /help'
    
def processar_comando(comando):
    if comando == '/U':
        return 'Comando em Execução:\nDescrição: Lista os usuários conectados ao servidor.'
    elif comando == '/C':
        return 'Comando em Execução:\nDescrição: Lista as configurações dos usuários conectados.'
    elif comando == '/ip i':
        return 'Comando em Execução\nDescrição: Traz os aplicativos instalados nos clientes especificados pelo IP.'
    elif comando == '/N t':
        return 'Comando em Execução:\nDescrição: Histórico de navegação da aplicação especificada.'
    elif comando == '/u ip':
        return 'Comando em Execução:\nDescrição: Traz informações detalhadas sobre o usuário especificado.'
    elif comando == '/off -c ip':
        return 'Comando em Execução:\nDesconecta de maneira manual o cliente especificado.'
    elif comando == '/off -s':
        return 'Comando em Execução:\nDesconecta de maneira manual o servidor.'
    elif comando == '/help':
        return 'Olá, bem-vindo a central de ajudas do bot Prog_Redes. O comando /U serve para listar os usuários conectados ao servidor, já o comando /C lista as configurações dos usuários conectados, o comando /i ip traz os aplicativos instalados nos clientes que foram especificados através do seu IP, o comando /N t traz o histórico de navegação, o comando /u ip traz informações gerais do usuário especificado pelo Ip, o comando /off -c ip desliga de maneira manuela o cliente especificado e por fim o comando /off -s desliga o servidor de maneira manual.'
    
def respondendo(resposta, chat_id, url_base):
    link_envio = f'{url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_envio)
    
