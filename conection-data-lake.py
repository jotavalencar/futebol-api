"""# CHAMADA JSON"""

from google.cloud import storage
from google.oauth2.service_account import Credentials
from google.colab import files

# Faz o upload do arquivo JSON da conta de serviço
uploaded = files.upload()

# Obtém o nome do arquivo carregado
nome_arquivo = list(uploaded.keys())[0]

# Cria uma instância do cliente do Google Cloud Storage com as credenciais
credentials = Credentials.from_service_account_file(nome_arquivo)
client = storage.Client(credentials=credentials)

# Agora você tem uma conexão autenticada com o Google Cloud Storage e pode usar o cliente para interagir com o serviço.
# Por exemplo, você pode listar os buckets existentes:
buckets = client.list_buckets()

for bucket in buckets:
    print(bucket.name)
