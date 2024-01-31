# Método de Cotovelo
"""
def process_excel(file_path):
    # Lendo o arquivo Excel
    xls = pd.ExcelFile(file_path)

    for sheet_name in xls.sheet_names:
        print(f"Processando a aba: {sheet_name}")

        # Lendo a aba específica
        data = xls.parse(sheet_name)

        # Selecionando as colunas a partir de K
        data = data.iloc[:, 10:]

        # Identificando colunas que contêm 'accuracy'
        accuracy_cols = [col for col in data.columns if 'accuracy' in col]

        # Normalizar as colunas de accuracy para escala [0,1]
        if accuracy_cols:
            min_max_scaler = MinMaxScaler()
            data[accuracy_cols] = min_max_scaler.fit_transform(data[accuracy_cols])

        # Padronizar o restante das colunas
        scaler = StandardScaler()
        data = scaler.fit_transform(data)

        # Método de Cotovelo para determinar o número ideal de clusters
        distortions = []
        K = range(1, 10)
        for k in K:
            kmeanModel = KMeans(n_clusters=k)
            kmeanModel.fit(data)
            distortions.append(kmeanModel.inertia_)

        # Cálculo da distância euclidiana
        x1, y1 = 1, distortions[0]
        x2, y2 = len(K), distortions[-1]

        distances = []
        for i in range(len(distortions)):
            x0 = i+1
            y0 = distortions[i]
            numerator = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
            denominator = ((y2 - y1)**2 + (x2 - x1)**2)**0.5
            distances.append(numerator/denominator)

        optimal_clusters = distances.index(max(distances)) + 1

        # Plotando o gráfico de cotovelo
        plt.figure(figsize=(10,5))
        plt.plot(K, distortions, 'bx-')
        plt.xlabel('Número de clusters')
        plt.ylabel('Distortion')
        plt.title(f'Método de Cotovelo para a aba {sheet_name}')
        plt.show()

        print(f"Número ótimo de clusters para {sheet_name}: {optimal_clusters}\n")

# Coloque aqui o caminho do seu arquivo
file_path = '/content/drive/MyDrive/Futebol/Dados/DB Fut 1.2 - Quintil - Posicoes.xlsx'
process_excel(file_path)
