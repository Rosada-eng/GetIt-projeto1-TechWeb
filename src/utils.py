import os
from pathlib import Path
from urllib.parse import unquote_plus

CUR_DIR = Path(__file__).parent.parent

def extract_route(request: str):
    """ 
    Recebe o request e extrai a rota do arquivo
    ex.: docs/img/logo-getit.png
    """
    commands = request.split(" ")
    route = commands[1][1:]
    print(f"route: {route}")
    return route

def read_file(path):
    """
    Lê o arquivo solicitado e devolve em texto, se for [.txt, .html, .css, .js]
    Caso contrário, devolve o arquivo em bytes
    Insira o caminho do documento a partir da pasta principal (projeto1)
    ex.: docs/getit.js
    """
    name, extension = os.path.splitext(path)
    print(f"lendo em: {os.path.join(CUR_DIR, path)}")
    if extension in ['txt', 'html', 'css', 'js']:
        # read as text
        with open(os.path.join(CUR_DIR, path), 'r', encoding='utf-8') as f:
           data = f.read()

    else:
        # read as bytes
        with open(os.path.join(CUR_DIR, path), 'rb') as f:
            data = f.read()

    return data

def load_template(path):
    # devolve a leitura do template do Card como texto (string)
    with open (os.path.join(CUR_DIR, path), 'r', encoding='utf-8') as f:
        template = f.read()

    return template

def extract_body_from_request(request):
    request = request.replace('\r', '') # Remove caracteres indesejados

    # Separa o request em Cabeçalho e Corpo
    cabecalho, corpo = request.split('\n\n')

    # Dicionário de parâmetros com as informações relevantes:
    params = {}

    # Separa as informações contidas no request
    for chave_valor in corpo.split('&'):
        k_v = chave_valor.split("=")
        params[k_v[0]] = unquote_plus(k_v[1], encoding='utf-8')

    return params

def build_response(code=200, reason='OK', headers=''):
    return f"HTTP/1.1 {code} {reason}{headers}\n\n".encode()