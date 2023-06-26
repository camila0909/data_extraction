import re
from re import sub
from unicodedata import normalize
import glob

'''
files = glob.glob("*.txt")
sorted(files)
'''

def fix_accents_bugs_in_pdf_conversion(txt):
  to_replace = {
      '¸c': 'ç',
      '˜a': 'ã',
      '~a': 'ã',
      '´a': 'á',
      'ˆa': 'â',
      'a~': 'ã',
      '˜a': 'ã',
      '^a': 'â',
      '´e': 'é',
      '˜e': 'e',
      '~e': 'e',
      'ˆe': 'ê',
      '^e': 'ê',
      '´ı': 'í',
      '´o': 'ó',
      'ˆo': 'ô',
      '^o': 'ô',
      '˜o': 'õ',
      '~o': 'õ',
      '´u': 'ú',
      '˜a': 'ã',
      '´a': 'á',
      '^a':'â',
      '¸C':'Ç',
      '˜A': 'Ã',
      '~A': 'Ã',
      '´A': 'Á',
      'ˆA': 'Â', 
      'ˆA': 'Â',
      '´E': 'É',
      '˜E': 'E',
      '~E': 'E',
      'ˆE': 'Ê',#Verificar porque o uso do acento ^ no lugar de ˆ, alterou caracteres que não precisavam ser alterados.
      '´I': 'Í',
      '´O': 'Ó',
      'ˆO': 'Ô',
      '˜O': 'Õ',
      '~O': 'Õ',
      '´U': 'Ú',
      '˜A': 'Ã',
      '´A': 'Á',
}
  for key in to_replace:
    txt = re.sub(key, to_replace[key], txt)
  return txt

def format_text(txt):
    txt = fix_accents_bugs_in_pdf_conversion(txt)
    txt = normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
    #txt = re.sub(r"[\x00-\x1F\x7F-\x9F]", " ", txt) Esta linha de código está substituindo também "\n", o que não é desejado.
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
  tese.close()
  return tese_text

'''
tese = []

for file in files:
   tese.append(get_text("C:\\data_extraction\\data_processing\\metadata01.txt"))

'''
def save_variable_to_file(variable, filename):
    with open(filename, 'w') as file:
        file.write(variable)

#save_variable_to_file('\n'.join(tese), 'tese.txt')

#print(tese)
#print(files)