import os
import glob
import pandas as pd

filenames = glob.glob('metadata/*.txt')

file_contents = []
for file in filenames:
    # abrir arquivo
    f = open(file, 'r', encoding="utf8")
    # ler as linhas
    rows = f.readlines()
    # concatenar as linhas
    content = "".join(rows)
    content = content.split("\n")
    content = [c.strip() for c in content]
    content = [c for c in content if c != ""]
    # anexar numa lista
    file_contents.append(content)
    # fechar o arquivo
    f.close()        

df = pd.DataFrame({
    "NOME_ARQUIVO": filenames, 
    "CONTEUDO": file_contents})

print(df)