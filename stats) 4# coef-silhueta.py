# Suponha que os dados já foram carregados, transformados e o modelo KMeans já foi treinado.

# Dicionário com o número ótimo de clusters para cada posição (altere conforme necessário)
optimal_clusters = {
    "Atacantes": 3,
    "Pontas": 2,
    "Meio Ofensivos": 2, # Modificado conforme sua observação
    "Volantes": 3,
    "Laterais": 3,
    "Zagueiros": 3,
    "Goleiros": 3
}

for sheet_name, n_clusters in optimal_clusters.items():
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    data = data.iloc[:, 10:]

    # Transformação logarítmica e padronização
    data = np.log1p(data)
    scaled_data = StandardScaler().fit_transform(data)

    # Treinando o KMeans com o número ótimo de clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(scaled_data)

    # Calculando o coeficiente médio de silhueta para todos os pontos
    silhouette_avg = silhouette_score(scaled_data, cluster_labels)
    print(f"Para {sheet_name} com n_clusters = {n_clusters}, o coeficiente médio de silhueta é: {silhouette_avg:.2f}")

    # Calculando os coeficientes de silhueta para cada amostra
    sample_silhouette_values = silhouette_samples(scaled_data, cluster_labels)

    fig, ax = plt.subplots()
    ax.set_xlim([-0.1, 1])
    ax.set_ylim([0, len(scaled_data) + (n_clusters + 1) * 10])

    y_lower = 10
    for i in range(n_clusters):
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        ax.fill_betweenx(np.arange(y_lower, y_upper),
                         0, ith_cluster_silhouette_values,
                         facecolor=color, edgecolor=color, alpha=0.7)

        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    ax.set_title(f"Análise da Silhueta para {sheet_name} com n_clusters = {n_clusters}")
    ax.set_xlabel("Valor do coeficiente de silhueta")
    ax.set_ylabel("Cluster label")
    ax.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax.set_yticks([])
    ax.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    plt.show()
