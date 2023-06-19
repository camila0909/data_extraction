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

print(universidade)
print(orientador)
print(co_orientador)
print(local)
print(ano)
print(resumo)
print(palavras_chave)
print(abstract)
print(keywords)