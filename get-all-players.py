"""# GET ALL PLAYERS"""

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

# Faz a chamada à API e obtém os dados
conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
headers = {
    'X-RapidAPI-Key': "19ad2b4577msh301c3eb5c5bd419p1e9b59jsn500b7096975e",
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
}
conn.request("GET", "/v3/players?league=71&season=2022&page=1", headers=headers)
res = conn.getresponse()
data = res.read().decode("utf-8")

# Define o nome do arquivo a ser salvo no bucket
filename = 'players.json'

# Cria um objeto Blob para armazenar os dados no bucket
blob = bucket.blob(filename)

# Salva os dados no Blob
blob.upload_from_string(data, content_type='application/json')

# Imprime a URL pública do arquivo salvo
print(f'Arquivo salvo em: {blob.public_url}')
