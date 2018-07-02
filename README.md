# conversor-csv-to-json

Abre o arquivo csv e o salva em formato json.

O cabeçalho do csv se torna as chaves do json, como no exemplo:

Arquivo CSV: 
NOME TELEFONE 
JOAO 33333333 
(...)

Arquivo JSON: 
[{"NOME": "JOAO", "TELEFONE": "33333333"}, 
(...)
