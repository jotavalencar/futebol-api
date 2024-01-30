"""# GET ALL TEAMS"""

import http.client
import json
from google.cloud import storage

# Carrega as credenciais do arquivo JSON
with open('account_service_key.json') as json_file:
    credentials = json.load(json_file)

# Cria uma conexão autenticada com o Google Cloud Storage
storage_client = storage.Client.from_service_account_info(credentials)

# Cria um objeto de bucket
bucket_name = 'fut_bucket'
bucket = storage_client.get_bucket(bucket_name)

# Função para obter os jogadores de todas as páginas
def get_all_teams(teams):
    for team in teams:
        # Faz a chamada à API e obtém os dados
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "19ad2b4577msh301c3eb5c5bd419p1e9b59jsn500b7096975e",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        }
        conn.request("GET", f"/v3/teams/statistics?league=71&season=2022&team={team}", headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")

        # Define o nome do arquivo a ser salvo no bucket
        filename = f'league_teams_{team}.json'

        # Cria um objeto Blob para armazenar os dados no bucket
        blob = bucket.blob(filename)

        # Salva os dados no Blob
        blob.upload_from_string(data, content_type='application/json')

        # Imprime a URL pública do arquivo salvo
        print(f'Arquivo da página {team} salvo em: {blob.public_url}')

# Lista de 10 requisicoes
teams_list = [124]
#teams_list = [134,144,145,147,151,152,154,794,1062,1193]

# Obtém os jogadores de todas as páginas
get_all_teams(teams_list)

import http.client
import json
from google.cloud import storage

# Carrega as credenciais do arquivo JSON
with open('account_service_key.json') as json_file:
    credentials = json.load(json_file)

# Cria uma conexão autenticada com o Google Cloud Storage
storage_client = storage.Client.from_service_account_info(credentials)

# Cria um objeto de bucket
bucket_name = 'fut_bucket'
bucket = storage_client.get_bucket(bucket_name)

# Função para obter os jogadores de todas as páginas
def get_all_teams(teams):
    for team in teams:
        # Faz a chamada à API e obtém os dados
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "19ad2b4577msh301c3eb5c5bd419p1e9b59jsn500b7096975e",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        }
        conn.request("GET", f"/v3/teams/statistics?league=71&season=2022&team={team}", headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")

        # Define o nome do arquivo a ser salvo no bucket
        filename = f'league_teams_{team}.json'

        # Cria um objeto Blob para armazenar os dados no bucket
        blob = bucket.blob(filename)

        # Salva os dados no Blob
        blob.upload_from_string(data, content_type='application/json')

        # Imprime a URL pública do arquivo salvo
        print(f'Arquivo da página {team} salvo em: {blob.public_url}')

# Lista de 10 requisicoes
teams_list = [134,144,145,147,151,152,154,794,1062,1193]
#teams_list = [134,144,145,147,151,152,154,794,1062,1193]

# Obtém os jogadores de todas as páginas
get_all_teams(teams_list)

import http.client
import json
from google.cloud import storage

# Carrega as credenciais do arquivo JSON
with open('account_service_key.json') as json_file:
    credentials = json.load(json_file)

# Cria uma conexão autenticada com o Google Cloud Storage
storage_client = storage.Client.from_service_account_info(credentials)

# Cria um objeto de bucket
bucket_name = 'fut_bucket'
bucket = storage_client.get_bucket(bucket_name)

# Função para obter os jogadores de todas as páginas
def get_all_teams(teams):
    all_data = []  # Lista para armazenar os dados de todas as páginas

    for team in teams:
        # Faz a chamada à API e obtém os dados
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "19ad2b4577msh301c3eb5c5bd419p1e9b59jsn500b7096975e",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        }
        conn.request("GET", f"/v3/teams/statistics?league=71&season=2022&team={team}", headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")

        # Adiciona os dados à lista
        all_data.append(data)

        # Imprime a mensagem de progresso
        print(f'Dados da equipe {team} obtidos')

    # Combina os dados em um único objeto
    combined_data = '[' + ','.join(all_data) + ']'

    # Define o nome do arquivo a ser salvo no bucket
    filename = 'combined_teams3.json'

    # Cria um objeto Blob para armazenar os dados no bucket
    blob = bucket.blob(filename)

    # Salva os dados no Blob
    blob.upload_from_string(combined_data, content_type='application/json')

    # Imprime a URL pública do arquivo salvo
    print(f'Arquivo combinado salvo em: {blob.public_url}')

# Lista de 10 equipes
teams_list = [119,120,121,124,125,126,127,128,129,131]

# Obtém os dados de todas as equipes e combina em um único arquivo
get_all_teams(teams_list)
