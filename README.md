# data_extraction

## [read_and_format.py](https://github.com/camila0909/data_extraction/blob/main/read_and_format.py)
Define as funções de leitura e formatação de arquivos de texto

## [define_functions.py](https://github.com/camila0909/data_extraction/blob/main/define_functions.py)
Define as funções para encontrar padrões específicos no texto (local de defesa, ano, orientador, resumo, palavras-chave, abstract e keywords)

## [execution.py](https://github.com/camila0909/data_extraction/blob/main/execution.py)
Executa as funções de [define_functions.py](https://github.com/camila0909/data_extraction/blob/main/define_functions.py) no arquivo [tese.txt](https://github.com/camila0909/data_extraction/blob/main/tese.txt) (este arquivo foi utilizado com o referência para definir os padrões)

## [create_data_frame.py](https://github.com/camila0909/data_extraction/blob/main/create_data_frame.py)
Cria um dataframe com os [metadados](https://github.com/camila0909/data_extraction/tree/main/metadata)

## [data_frame_application.py](https://github.com/camila0909/data_extraction/blob/main/data_frame_application.py)
Aplica as funções de [define_funcions.py](https://github.com/camila0909/data_extraction/blob/main/define_functions.py) no dataframe extraindo os dados desejados e salva no arquivo [dados.xlsx](https://github.com/camila0909/data_extraction/blob/main/dados.xlsx)

## [Requeriments](https://github.com/camila0909/data_extraction/blob/main/requirements.txt) 


* ﻿et-xmlfile==1.1.0
* numpy==1.25.0
* openpyxl==3.1.2
* pandas==2.0.2
* python-dateutil==2.8.2
* pytz==2023.3
* six==1.16.0
* tzdata==2023.3


## Referências:
1. https://profmat-sbm.org.br/dissertacoes/
2. https://chat.openai.com/
