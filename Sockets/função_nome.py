# Função para obter o nome do arquivo a partir da url
def nome_arquivo(url):
    partes = url.split('/')
    return partes[-1]