## GET API-FOOTBALL 

#### Site: https://www.api-football.com/
#### Documentation v3: https://www.api-football.com/documentation-v3
#### Site api key: [https://www.api-football.com/documentation-v3](https://api-football-v1.p.rapidapi.com/v3/)

O código api-football.py é o arquivo completo com todas as etapas de conexão de dados. 

As etapas abordam a construição de uma conexão do código com a api do site para puxar os dados do Campeonato BR22.

Os demais códigos .py são etapas avulsas que podem ser testadas de forma individual, na seguinte ordem:

  1. import.py --> arquivo com as bibliotecas que foram instaladas e utilizadas para construição do código.
  2. conection-data-lake.py --> conecta a api do repositório de dados escolhido para esse estudo.
  3. get-all-players.py --> função que retorna todas as informações de atletas do BR22, também apresenta a conexão com a api-football.org.
  4. get-all-teams.py --> função que retorna todas as informações de times do BR22.
  5. get-all-fixtures.py --> retorna as informações de cada partida do BR22.
  6. unir-arquivos-json.py --> uni todos os arquivos de get-all-fixtures que foram importados.
  7. converter-csv.py --> converte todos os arquivos json para csv.
