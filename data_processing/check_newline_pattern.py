path = 'metadata\\dissertacao_0001.txt'

def check_newline_pattern(path):
    with open(path, 'rb') as file:
        conteudo = file.read()

    if b'\r\n' in conteudo:
        print("O arquivo segue o padrão CRLF (Carriage Return + Line Feed)")
    elif b'\n' in conteudo:
        print("O arquivo segue o padrão LF (Line Feed)")
    else:
        print("O arquivo não contém quebras de linha")

check_newline_pattern(path)
