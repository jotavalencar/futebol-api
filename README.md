## WebScrapping site FBREF 

<p>O site foi escolhido por dispor de informações públicas relevantes e confiáveis a título de comparação com outras alterativas no mercado e pertence ao grupo Sports Reference.</p>

  <p>O fator determinante foi a parceria do site com outros grandes veículos do mercado de dados esportivos, destacam-se os dados do projeto Opa da Stats Perform para dados avançados.</p>
  
---
#### Data Engeneering (data) - Processo para recuperar os dados e salvar como um arquivo excel.

O sistema completo de scrapping foi divido em vários pequenos códigos para facilitar a leitura e sua sequencia será listada abaixo:

  1. import.py --> bibliotecas que foram utilizadas para esse projeto.
  2. lista-ids-fbref.py --> recuperar os ids dos atletas que é utilizado para identificar as informações de cada atleta individualmente.
  3. teste-scrapping.py --> código construído para testar o scrapping dos dados para um atleta.
  4. sleep.py --> função construída por respeito a política do site.
  5. scrapping-passing.py --> exemplo de uma pagina que foi recuperada de forma independente em um json.
  6. verificar-ids.py --> função construída para verificar se algum id voltou vazio.
  7. csv-converter.py - código para transformar os arquivos json em csv.

--- Data Science (stats) - Análise estatistica construída para 


