import platform, subprocess, socket
from browser_history.browsers import Chrome, Edge, Firefox
import os, sqlite3

def hardware():
    def memoria():
        try:
            cabeçalho = subprocess.run('free | grep "total"', capture_output=True, text=True, shell=True)
            memoria = subprocess.run('free -m | grep "Mem:"', capture_output=True, text=True, shell=True)

            inform = f"\nInformações sobre a memória:\n{cabeçalho.stdout}\n{memoria.stdout}"

            return inform
        except Exception as e:
            return f"Erro ao obter informações de memória: {str(e)}"

    def disco():
        try:
            cabeçalho = subprocess.run('df -h | grep -i "File"', shell=True, capture_output=True, text=True)
            discos = ["/dev/sda", "/dev/root", "/dev/mapper", "/dev/nvme0n1p1"]

            for disco in discos:
                try:
                    armazenamento = subprocess.run(f'df -h | grep -i "{disco}"', capture_output=True, text=True, shell=True)
                    break
                except: continue 

            inform = f"\nInformações do disco:\n\n{cabeçalho.stdout}{armazenamento.stdout}"

            return inform
        except Exception as e:
            return f"Erro ao obter informações de disco: {str(e)}"

    try:
        sistema_operacional = platform.system()
        processador = platform.processor()
        arquitetura = platform.architecture()
    except Exception as e:
        return f'Não foi possível obter as informações de Hardware: {str(e)}'

    informacoes = [
        f"Sistema Operacional: {sistema_operacional}\n",
        f"Processador: {processador}\n",
        f"Arquitetura: {arquitetura[0]} {arquitetura[1]}\n",
        f"Informações do Disco: {disco()}\n",
        f"Informações da Memória:{memoria()}"
    ]

    return informacoes

def programas():
    try:
        resultado = subprocess.run(['apt', 'list', '--installed'], capture_output=True, text=True, shell=True)
        linhas = resultado.stdout.splitlines()

        informacoes = "\n---------- INFORMAÇÕES DE PROGRAMAS INSTALADOS ----------\n\n"
        for linha in linhas[2:-3]:
            informacoes += linha + "\n"

        return informacoes
    except Exception as e:
        return f'Não foi possível obter as informações de programas instalados: {str(e)}'

def info_user_Linux():
    def grups():
        try:
            usuario = os.getlogin()
            resultado = subprocess.run(['groups', usuario], capture_output=True, text=True, shell=True)
            primario = resultado.stdout.strip().split()
            secundario = ('\n'.join(primario[3:]))

            saida = f"\n--- Grupo Principal ---\n{primario[2]}\n\n--- Grupos Secundários ---\n{secundario}"
            return saida
        except Exception as e:
            return f'Não foi possível obter as informações de grupos do usuário: {str(e)}'

    try:
        return (
            f"Usuário: {os.getlogin()}\n"
            f"Diretório Inicial: {os.path.expanduser('~')}\n"
            f"Identificação de usuário: UID = {os.getuid()}\n"
            f"Os grupos do usuário são: {grups()}\n"
            f"\nO Shell padrão do Usuário é: {os.environ.get('SHELL', 'N/A')}"
        )
    except Exception as e:
        return f'Não foi possível obter informações do usuário: {str(e)}'

def agentes_IP():
    try:
        informacoes = [
            f"Nome do host: {socket.gethostname()}\n"
            f"Usuário logado: {os.getlogin()}\n"
            f"IP do Host: {socket.gethostbyname(socket.gethostname())}\n"
        ]
        return informacoes
    except Exception as e:
        return f'Não foi possível obter as informações do Agente: {str(e)}'

def history_google():
    try:
        con = sqlite3.connect(f"/home/{os.getlogin()}/.config/google-chrome/Default/History")
        cur = con.cursor()
        cur.execute("select url, title, visit_count from urls")
        results = cur.fetchall()
        for result in results:
            print(result)
    except Exception as e:
        print(f'Erro ao obter histórico do Google Chrome: {str(e)}')

def history_edge():
    try:
        con = sqlite3.connect(f"/home/{os.getlogin()}/.config/microsoft-edge/Default/History")
        cur = con.cursor()
        cur.execute("select url, title, visit_count from urls")
        results = cur.fetchall()
        for result in results:
            print(result)
    except Exception as e:
        print(f'Erro ao obter histórico do Microsoft Edge: {str(e)}')

def history_opera():
    try:
        con = sqlite3.connect(f"/home/{os.getlogin()}/.config/opera/Default/History")
        cur = con.cursor()
        cur.execute("select url, title, visit_count from urls")
        results = cur.fetchall()
        for result in results:
            print(result)
    except Exception as e:
        print(f'Erro ao obter histórico do Opera: {str(e)}')