from re import sub
from unicodedata import normalize
import glob


files = glob.glob("*.txt")
sorted(files)

def format_text(txt):
    txt = normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
    txt = sub('[^\n\.\?\:\;\!A-Za-z0-9 -]+', '', txt).strip()
    return txt.upper()

# A expressão regular [^\n\.\?\!A-Za-z0-9 -]+ é usada como o padrão de busca.
#Trata-se de uma classe de caracteres negados ([^...]), que corresponde a qualquer caractere que não esteja presente na 
#classe de caracteres especificada.
# +: Indica que o padrão pode ocorrer uma ou mais vezes.
    

def get_text(filename):
  tese = open(filename,encoding='utf-8')
  tese_list = list(filter(lambda x: x.strip() != '',tese.readlines()))
  tese_clean_spaces = [l.strip() for l in tese_list]
  tese_text = ''.join(tese_list)
  tese_formatted_text = format_text(tese_text)
  tese.close()
  return tese_formatted_text

tese = []

for file in files:
   tese.append(get_text("C:\\data_extraction\\metadata01.txt"))


def save_variable_to_file(variable, filename):
    with open(filename, 'w') as file:
        file.write(variable)

save_variable_to_file('\n'.join(tese), 'tese.txt')

#print(tese)