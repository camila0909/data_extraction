import re
from re import sub
import unicodedata
from unicodedata import normalize

#Abre arquivo convertendo o texto em uma lista de strings, variável lines recebe a lista

file = "C:\\data_extraction\\tese.txt"
lines = []

with open(file, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

#Define função de formtação de texto

def format_text(txt):
    txt = normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
    txt = sub('[^\n\.\?\:\;\!A-Za-z0-9 -]+', '', txt).strip()
    return txt.upper()

# Define função encontrar_abstract

def encontrar_abstract(lista):
    strings_encontradas = []
    encontrou_abstract = False

    for string in lista:
        if string.startswith("ABSTRACT"):
            encontrou_abstract = True
            continue

        if encontrou_abstract:
            if string.startswith("KEYWORD"):
                break
            else:
                strings_encontradas.append(string)

    resultado = " ".join(strings_encontradas)
    return resultado

#Define função encontrar_resumo

def encontrar_resumo(lista):
    strings_encontradas = []
    encontrou_resumo = False

    for string in lista:
        if string.startswith("RESUMO"):
            encontrou_resumo = True
            continue

        if encontrou_resumo:
            if string.startswith("PALAVRA"):
                break
            else:
                strings_encontradas.append(string)

    resultado = " ".join(strings_encontradas)
    return resultado


#Define função para encontrar local defesa e caso tenha, também retorna o nome do orientador

def encontrar_local(lista):
    #exit = número inteiro sendo 0 ou 1, se 0 retornará o nome do local, se 1 retornará o co_orientador
    local_encontrado = []
    co_orientador = []
    encontrou_string = False

    for i in range(len(lista)):
        if re.match(r'^ORIENTAD[ORA\(\)\:]{2,7}.*', lista[i]):
            encontrou_string = True
        
        if encontrou_string:
            if re.match(r'^CO[- ]{0,1}ORIENTAD[ORA\(\)\:]{2,7}.*', lista[i+1]):
                co_orientador.append(lista[i+1])   
                local_encontrado.append(lista[i+2]) 
            else:
                local_encontrado.append(lista[i+1])            
            break
        
    if len(co_orientador) == 0:
        co_orientador.append("NAO POSSUI")
        co_orientador = (co_orientador[0])
    else:        
        co_orientador = lines[lines.index(co_orientador[0])]
    if local_encontrado:
        local_encontrado = lines[lines.index(local_encontrado[0])]

    return local_encontrado, co_orientador

#Define função que retorna o ano da defesa

def encontrar_ano(lista):
    ano = []
    encontrou_string = False

    for i in range(len(lista)):
        #if re.match(r'^(\d{2}|\d{4})',lista[i]):
        if re.match(r'^(\d{4})',lista[i]):
            ano.append(lista[i])
            encontrou_string = True
        if encontrou_string:
            break
    return ano[0]

#Busca Keywords

def encontrar_keywords(lista):
    keywords = []
    encontrou_string = False

    for i in range(len(lista)):
        if re.match(r'^KEYWORD.*',lista[i]):
            keywords.append(lista[i])
            encontrou_string = True
        if encontrou_string:
            break
    keywords = "".join(keywords)
    return keywords

def encontrar_palavras_chave(lista):
    palavras_chave = []
    encontrou_string = False

    for i in range(len(lista)):
        if re.match(r'^PALAVRA.*',lista[i]):
            palavras_chave.append(lista[i])
            encontrou_string = True
        if encontrou_string:
            if not re.match(r'^(ABSTRACT.*|\d).*',lista[i+1]):
                palavras_chave.append(lista[i+1])
            else:
                break
    if len(palavras_chave) >= 2:
        palavras_chave = palavras_chave[0] + palavras_chave[1]
        return palavras_chave
    else:
        return palavras_chave[0]

#Define função que retorna o nome do orientador

def encontrar_orientador(lista):
    orientador = []
    encontrou_string = False

    for i in range(len(lista)):
        if re.match(r'^ORIENTAD[ORA\(\)\:]{2,7}.*',lista[i]):
            orientador.append(lista[i])
            encontrou_string = True
            if encontrou_string:
                break
    orientador = ' '.join(orientador)
    return orientador

      