"""# CONVERTER EM CSV"""

from google.cloud import storage
import pandas as pd
import json
from google.oauth2 import service_account

# Definir as informações de acesso ao bucket
bucket_name = 'fut_bucket'
json_file_name = 'api_responses.json'
csv_file_name = 'fixtures.csv'

# Carregar as credenciais do arquivo no Colab
with open('/content/account_service_key.json') as credentials_file:
    credentials_data = json.load(credentials_file)

# Criar um objeto de credenciais com as credenciais carregadas
creds = service_account.Credentials.from_service_account_info(credentials_data)

# Criar uma instância do cliente do Google Cloud Storage com as credenciais
client = storage.Client(credentials=creds)

# Obter uma referência ao objeto do arquivo JSON no bucket
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(json_file_name)

# Fazer o download do arquivo JSON para o sistema de arquivos local
blob.download_to_filename(json_file_name)

# Ler o arquivo JSON
with open(json_file_name, 'r') as json_file:
    data = json.load(json_file)

# Converter os dados para um DataFrame do pandas
df = pd.DataFrame(data)

# Salvar o DataFrame como arquivo CSV
df.to_csv(csv_file_name, index=False)

# Fazer o upload do arquivo CSV para o bucket
blob = bucket.blob(csv_file_name)
blob.upload_from_filename(csv_file_name)
