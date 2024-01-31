import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Dicionário para o número ideal de clusters por posição
clusters_dict = {
    "Atacantes": 2,
    "Pontas": 2,
    "Meio Ofensivos": 2,
    "Volantes": 2,
    "Laterais": 2,
    "Zagueiros": 2,
    "Goleiros": 2
}

# Carregar o arquivo Excel
file_path = '/content/drive/MyDrive/Futebol/Dados/DB Fut 1.2 - Quintil - Posicoes.xlsx'

# Defina uma lista de cores. Aumente esta lista se você espera ter mais clusters.
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan', 'magenta']

for sheet_name, n_clusters in clusters_dict.items():
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Separar colunas numéricas
    data = df.select_dtypes(include=[np.number])

    # Transformação logarítmica para reduzir a dispersão
    data = np.log1p(data)

    # Padronizar os dados
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Redução de dimensionalidade para 3 componentes
    pca = PCA(n_components=3)
    principal_components = pca.fit_transform(data_scaled)

    # Aplicação do KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(principal_components)
    df['Cluster'] = kmeans.labels_

    # Visualização 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    for cluster_num in range(n_clusters):
        mask = df['Cluster'] == cluster_num
        ax.scatter(principal_components[mask, 0],
                   principal_components[mask, 1],
                   principal_components[mask, 2],
                   s=60, label=f'Cluster {cluster_num+1}', c=colors[cluster_num])

        # Plotando o centróide na cor preta
        centroid = kmeans.cluster_centers_[cluster_num]
        ax.scatter(centroid[0], centroid[1], centroid[2], s=120, c='black', marker='x')

        # Identificar linha de dados mais próxima do centróide
        closest, _ = min(enumerate(principal_components), key=lambda x: np.linalg.norm(x[1]-centroid))
        print(f"Centróide {cluster_num+1} da aba {sheet_name} está mais próximo da linha {closest+2} do Excel e é representado pela cor {colors[cluster_num]}.")

    ax.set_title(sheet_name)
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_zlabel('PC3')
    ax.legend()
    plt.show()
