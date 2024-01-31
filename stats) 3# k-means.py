# Caminho para o arquivo
file_path = "/content/drive/MyDrive/Futebol/Dados/DB Fut 1.2 - Quintil - Posicoes.xlsx"

# Número ideal de clusters para cada aba (alterado conforme sua observação)
optimal_clusters = {
    "Atacantes": 3,
    "Pontas": 2,
    "Meio Ofensivos": 2,  # Modificado conforme sua observação
    "Volantes": 3,
    "Laterais": 3,
    "Zagueiros": 3,
    "Goleiros": 3
}

# Função para plotar os clusters
def plot_clusters(data_2d, kmeans_labels, centroids_2d, title):
    plt.figure(figsize=(8, 6))

    scatter = plt.scatter(data_2d[:, 0], data_2d[:, 1], c=kmeans_labels, cmap='rainbow', edgecolors='k', s=100)
    for i, centroid in enumerate(centroids_2d):
        plt.scatter(centroid[0], centroid[1], c='black', s=200, marker='X', label=f"Centroid {i+1}")

    plt.title(title)
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.legend(handles=scatter.legend_elements()[0], title="Clusters")
    plt.show()

# Processando cada aba do arquivo
xls = pd.ExcelFile(file_path)
for sheet_name in optimal_clusters:
    data = pd.read_excel(xls, sheet_name=sheet_name)

    # Selecionando as colunas a partir de K
    data_selected = data.iloc[:, 10:]

    # Aplicando a transformação logarítmica
    data_log_transformed = np.log1p(data_selected)

    # Padronizando os dados após a transformação logarítmica
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_log_transformed)

    # Executando o KMeans com o número ótimo de clusters
    kmeans = KMeans(n_clusters=optimal_clusters[sheet_name], random_state=0)
    kmeans.fit(data_scaled)

    # Transformando os dados em 2D para a plotagem
    pca = PCA(n_components=2)
    data_2d = pca.fit_transform(data_scaled)

    # Obter os centróides e transformá-los em 2D
    centroids_2d = pca.transform(kmeans.cluster_centers_)

    # Plotando os clusters
    plot_clusters(data_2d, kmeans.labels_, centroids_2d, title=sheet_name)

    # Identificando os pontos mais próximos dos centróides
    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, data_scaled)
    print(f"Linhas do Excel mais próximas dos centróides para {sheet_name}: {closest + 2}")
