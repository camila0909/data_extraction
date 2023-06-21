import os
import glob
from pdfminer.high_level import extract_text
#from pdfminer.pdfparser import PDFSyntaxError
from pdfminer.pdfdocument import PDFSyntaxError, PDFPasswordIncorrect
import struct

# Obter a lista de arquivos PDF no diretório
pdf_files = glob.glob(os.path.join("C:\\Users\\Camila\\Documents\\TCC\\ambiente\\dissertacoes_copia", "*.pdf"))

# Converter cada arquivo PDF em TXT
i = 0
for pdf in pdf_files:
    i = i + 1
    if i >=6162:
        # Definir o nome do arquivo TXT de saída
        txt_file = os.path.splitext(pdf)[0] + ".txt"

        try:
        
            # Extrair o texto do arquivo PDF
            text = extract_text(pdf)
            
            # Salvar o texto extraído em um arquivo TXT
            with open(txt_file, "w", encoding="utf-8") as file:
                file.write(text)

            print(f"Arquivo convertido: {txt_file}")

        except (PDFSyntaxError,KeyError, struct.error, PDFPasswordIncorrect, ValueError) as e:
            print(f"Erro ao converter o arquivo {pdf}: {e}")
    else:
        print(i)
