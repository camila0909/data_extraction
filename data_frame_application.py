import create_data_frame
from create_data_frame import df
import define_functions
from define_functions import format_text
from define_functions import fix_accents_bugs_in_pdf_conversion
from define_functions import encontrar_abstract
from define_functions import encontrar_resumo
from define_functions import encontrar_local
from define_functions import encontrar_ano
from define_functions import encontrar_keywords
from define_functions import encontrar_palavras_chave
from define_functions import encontrar_orientador


df['CONTEUDO'] = df['CONTEUDO'].map(lambda lines: [fix_accents_bugs_in_pdf_conversion(line) for line in lines])
df['CONTEUDO']= df['CONTEUDO'].map(lambda lines: [format_text(line) for line in lines])

df['UNIVERSIDADE'] = df['CONTEUDO'].map(lambda lines: lines[0] if lines else "")
df['ORIENTADOR'] = df['CONTEUDO'].map(lambda lines: encontrar_orientador(lines))
#df['LOCAL'] = df['CONTEUDO'].map(lambda lines: encontrar_local(lines))
df['ANO'] = df['CONTEUDO'].map(lambda lines: encontrar_ano(lines))
df['RESUMO'] = df['CONTEUDO'].map(lambda lines: encontrar_resumo(lines))
df['PALAVRAS_CHAVE'] = df['CONTEUDO'].map(lambda lines: encontrar_palavras_chave(lines))
df['ABSTRACT'] = df['CONTEUDO'].map(lambda lines: encontrar_abstract(lines))
df['KEYWORDS'] = df['CONTEUDO'].map(lambda lines: encontrar_keywords(lines))

df.to_excel("C:\\data_extraction\\dados.xlsx", index=False)

print(df['CONTEUDO'])

