"""# UNIR TODOS OS ARQUIVOS"""

import os

# Diretório onde os arquivos estão localizados
diretorio = '/content'

# Percorre todos os arquivos no diretório
for filename in os.listdir(diretorio):
    if filename.startswith('fixtures_'):
        # Verifica se o arquivo tem a extensão desejada
        if filename.endswith('.json'):
            file_path = os.path.join(diretorio, filename)
            # Exclui o arquivo
            os.remove(file_path)
            print(f"Arquivo {filename} excluído com sucesso.")
