"""K mean 2"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Montar o Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Especifique o caminho completo para o seu arquivo no Google Drive
file_path = '/content/drive/MyDrive/Futebol/Dados/Fut 1.2 - Quintil.xlsx'

# Lista de posições e suas respectivas colunas
posicoes = {
    'Goleiros': ['goals.conceded', 'goals.saves', 'passes.on', 'duels.won', 'penalty.saved'],
    'Zagueiros': ['passes.on', 'tackles', 'blocks', 'interceptions', 'duels.won', 'duels.total'],
    'Laterais': ['passes.key', 'passes.on', 'tackles', 'blocks', 'interceptions', 'duels.won', 'dribbles.success'],
    'Volantes': ['passes.key', 'passes.on', 'tackles', 'blocks', 'interceptions', 'duels.won', 'dribbles.success'],
    'Meio Ofensivos': ['shots.on', 'goals.total', 'goals.assists', 'passes.key', 'passes.on', 'tackles', 'interceptions', 'duels.won', 'dribbles.success', 'fouls.drawn'],
    'Pontas': ['shots.on', 'goals.total', 'goals.assists', 'passes.key', 'passes.on', 'tackles', 'interceptions', 'duels.won', 'dribbles.success', 'fouls.drawn'],
    'Atacantes': ['shots.on', 'goals.total', 'goals.assists', 'passes.key', 'passes.on', 'tackles', 'interceptions', 'duels.won', 'dribbles.success']
}

# Função para criar o modelo K-Means com variáveis padronizadas e plotar o gráfico de dispersão
def criar_kmeans_com_padronizacao(data, n_clusters, posicao):
    scaler = StandardScaler()
    data_std = scaler.fit_transform(data)  # Padronizar os dados

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data_std)

    # Plotar o gráfico de dispersão com os centroides
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data_std[:, 0], y=data_std[:, 1], hue=kmeans.labels_, palette='viridis', s=100, legend='full')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', s=200, label='Centroids')
    plt.xlabel('Feature 1 (Padronizada)')
    plt.ylabel('Feature 2 (Padronizada)')
    plt.title(f'K-Means Clustering para {posicao} (com Padronização)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

# Loop para carregar DataFrames e criar o modelo K-Means com padronização
for posicao, colunas in posicoes.items():
    df = pd.read_excel(file_path, sheet_name=posicao)
    df = df[colunas]

    quantidade_otima_clusters = calcular_quantidade_otima_clusters(df)  # Você já possui essa informação

    # Criar o modelo K-Means com padronização
    criar_kmeans_com_padronizacao(df, quantidade_otima_clusters, posicao)
