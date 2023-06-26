import sys
sys.path.append('C:\\data_extraction\\')

import os
import glob
import pandas as pd
import read_and_format
from read_and_format import fix_accents_bugs_in_pdf_conversion
from read_and_format import format_text
from read_and_format import get_text


filenames = glob.glob('metadata/*.txt')
sorted(filenames)

#print(filenames)

file_contents = []

for file in filenames:
   file_contents.append(get_text(file))

file_contents_formatted = []

for file in file_contents:
   file_contents_formatted.append(format_text(file))

#print(file_contents[0])

'''
for file in filenames:
    # abrir arquivo
    f = open(file, 'r', encoding="utf8")
    # ler as linhas
    rows = f.readlines()
    # concatenar as linhas
    content = "".join(rows)
    content = content.split(r'\r\n|\n')
    content = [c.strip() for c in content]
    content = [c for c in content if c != ""]
    # anexar numa lista
    file_contents.append(content)
    # fechar o arquivo
    f.close()        

'''
df = pd.DataFrame({
    "CAMINHO_DO_ARQUIVO": filenames, 
    "CONTEUDO": file_contents,
    "CONTEUDO_FORMATADO": file_contents_formatted})

df.to_excel("C:\\data_extraction\\data_processing\\dados_tratados.xlsx", index=False)

print(df.head())
