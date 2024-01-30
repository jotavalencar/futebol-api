# Função para calcular a quantidade ótima de clusters usando o método do cotovelo
def calcular_quantidade_otima_clusters(data):
    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)

    # Calcular a diferença entre os valores SSE
    diff = np.diff(sse)

    # Encontrar o ponto de "cotovelo" onde a diferença começa a nivelar
    for i in range(1, len(diff)):
        if diff[i] < 0.2 * diff[i - 1]:  # Ajuste o valor 0.2 conforme necessário
            quantidade_otima_clusters = i + 1  # Adicione 1 para compensar a indexação
            break
    else:
        quantidade_otima_clusters = 1

    # Plotar o gráfico do cotovelo para análise visual
    plt.figure(figsize=(8, 6))
    sns.lineplot(x=range(1, 11), y=sse, marker='o', linestyle='--')
    plt.xlabel('Número de Clusters (K)')
    plt.ylabel('SSE')
    plt.title('Método do Cotovelo')
    plt.grid(True)
    plt.show()

    return quantidade_otima_clusters

# Loop para carregar DataFrames e calcular a quantidade ótima de clusters para cada posição
for posicao, colunas in posicoes.items():
    df = pd.read_excel(file_path, sheet_name=posicao)
    df = df[colunas]

    quantidade_otima_clusters = calcular_quantidade_otima_clusters(df)
    print(f'Quantidade ótima de clusters para {posicao}: {quantidade_otima_clusters}')
