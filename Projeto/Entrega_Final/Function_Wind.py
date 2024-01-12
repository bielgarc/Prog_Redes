import platform, subprocess, socket, datetime
from browser_history.browsers import Chrome, Edge, Firefox
import os, sqlite3

def hardware_Wind():
    try:
        def memoria_wind():
            resultado = subprocess.run(['systeminfo'], capture_output=True, text=True)
            systeminfo = resultado.stdout
            memoria_total = [linha for linha in systeminfo.split('\n') if 'Memória física total:' in linha]
            total = memoria_total[0].split(':')[-1].strip()
            memoria_dis = [linha for linha in systeminfo.split('\n') if 'Memória física disponível:' in linha]
            disponivel = memoria_dis[0].split(':')[-1].strip()

            final = f"Memória Total: {total}\nMemória Disponível: {disponivel}"
            return final
    except Exception as e:
            return f"Erro ao obter informações de memória: {str(e)}"

    def disco_wind():
            resultado = subprocess.run(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'], capture_output=True, text=True)
            linhas = resultado.stdout.strip().split('\n')
            dados = linhas[2].split()
            vazio = int(dados[1]) / (1024 ** 3)
            total = int(dados[2]) / (1024 ** 3)

            informacoes_discos = f"Espaço livre em disco: {vazio:.2f} GB\nEspaço total em disco: {total:.2f} GB"
            return informacoes_discos
    try:
        sistema_operacional = platform.system()
        processador = platform.processor()
        arquitetura = platform.architecture()
    except Exception as e:
        return f'Não foi possível obter as informações de Hardware: {str(e)}'

    informacoes = [
        f"Sistema Operacional: {sistema_operacional}\n"
        f"Processador: {processador}\n"
        f"Arquitetura: {arquitetura[0]} {arquitetura[1]}\n"
        f"\n----- INFORMAÇÕES DE DISCO -----\n{disco_wind()}\n"
        f"\n----- INFORMAÇÕES DE MEMÓRIA -----\n{memoria_wind()}"
    ]

    return informacoes

def programs_Wind():
    try:
        resultado = subprocess.run(['wmic', 'product', 'get', 'name'], capture_output=True, text=True)
        linhas = resultado.stdout.splitlines()
        
        if len(linhas) < 3:
            raise Exception("Nenhum programa instalado encontrado.")
        
        informacoes = "\n---------- INFORMAÇÕES DE PROGRAMAS INSTALADOS ----------\n\n"
        for linha in linhas[2:-3]:
            informacoes += linha + "\n"

        return informacoes
    except Exception as e:
        return f'Não foi possível obter as informações de programas instalados: {str(e)}'

def google_Wind():
    try:
        b = Chrome()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except Exception as e:
        return f"Erro ao tentar receber histórico de navegação do Google!!! {str(e)}"

def edge_Wind():
    try:
        b = Edge()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except Exception as e:
        return f"Erro ao tentar receber histórico de navegação do Microsoft Edge!!! {str(e)}"

def firefox_Wind():
    try:
        b = Firefox()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except Exception as e:
        return f"Erro ao tentar receber histórico de navegação do Mozila Firefox!!! {str(e)}"

def opera_Wind():
    try:
        final = ''
        con = sqlite3.connect(fr'C:\Users\{os.getlogin()}\AppData\Roaming\Opera Software\Opera Stable\Default\History')
        cur = con.cursor()
        cur.execute("select url, title, visit_count from urls")
        results = cur.fetchall()
        for result in results:
            final += (result)

        return final
    except Exception as e:
        return f"Erro ao tentar receber histórico de navegação do Opera!!! {str(e)}"