import define_functions as df
from define_functions import encontrar_abstract
from define_functions import encontrar_resumo
from define_functions import encontrar_local
from define_functions import encontrar_ano
from define_functions import encontrar_keywords
from define_functions import encontrar_palavras_chave
from define_functions import encontrar_orientador

from define_functions import lines

universidade = lines[0]
orientador = df.encontrar_orientador(lines)
co_orientador = df.encontrar_local(lines)[0]
local = df.encontrar_local(lines)[1]
ano = df.encontrar_ano(lines)
resumo = df.encontrar_resumo(lines)
palavras_chave = df.encontrar_palavras_chave(lines)
abstract = df.encontrar_abstract(lines)
keywords = df.encontrar_keywords(lines)


# Criar arquivo e escrever as variáveis em linhas separadas
with open("variaveis_tese.txt", "w") as arquivo:
    arquivo.write(universidade + '\n'+'\n')
    arquivo.write(orientador + '\n'+'\n')
    for x in co_orientador:
        arquivo.write(x + '\n'+'\n')
    for y in local:
        arquivo.write(y + '\n'+'\n')
    arquivo.write(ano + '\n'+'\n')
    arquivo.write(resumo + '\n'+'\n')
    arquivo.write(palavras_chave + '\n'+'\n')
    arquivo.write(abstract + '\n'+'\n')
    arquivo.write(keywords + '\n'+'\n')
    arquivo.close()
print("Arquivo 'variaveis_tese.txt' criado com sucesso.")
