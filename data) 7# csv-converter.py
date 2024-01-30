import pandas as pd
import json

# Carregar o arquivo JSON
with open('/content/fbref_summary_2023.json', 'r') as f:
    data = json.load(f)

# Lista para armazenar os dados processados
processed_data = []

for player, player_data in data.items():
    # Informações básicas
    player_info = {
        'NomeDoAtleta': player,
        **player_data.get('Informações Adicionais', {})
    }

    # Dados das tabelas
    if 'Dados das Tabelas' in player_data and 'Dados' in player_data['Dados das Tabelas']:
        table_data = player_data['Dados das Tabelas']['Dados']

        for row in table_data:
            # Crie um dicionário para cada linha da tabela
            row_data = {f'Coluna {i+1}': value for i, value in enumerate(row)}
            processed_data.append({**player_info, **row_data})

# Convertendo a lista processada em um DataFrame
final_df = pd.DataFrame(processed_data)

# Mostrar os primeiros registros do DataFrame final
print(final_df.head())

# Salvar o DataFrame em um arquivo CSV
final_df.to_csv('fbref_summary_2023.csv', index=False)
