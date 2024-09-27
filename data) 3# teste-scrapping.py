"""# Scrapping Teste"""

import requests
from bs4 import BeautifulSoup
import json

# Função para extrair informações da div
def extrair_info_div(soup):
    meta_div = soup.find('div', id='meta')
    if not meta_div:
        return {}

    # Extrair texto de cada tag <p> dentro da div
    paragrafos = meta_div.find_all('p')
    dados_paragrafos = {f'Parágrafo {i+1}': p.get_text(strip=True) for i, p in enumerate(paragrafos)}

    # Extrair URLs de imagens dentro da div
    imagens = meta_div.find_all('img')
    urls_imagens = [img['src'] for img in imagens if 'src' in img.attrs] if imagens else None

    # Combina os dados dos parágrafos e URLs de imagens em um único dicionário
    dados_div = {**dados_paragrafos, 'URLs de Imagens': urls_imagens}

    return dados_div

# Função para extrair dados das tabelas
def extrair_dados_tabelas(soup):
    tabelas = soup.find_all('table')
    dados_tabelas = []
    for tabela in tabelas:
        linhas = tabela.find_all('tr')
        for linha in linhas:
            celulas = linha.find_all('td')
            dados_linha = [celula.text for celula in celulas]
            dados_tabelas.append(dados_linha)
    return dados_tabelas

# Base da URL
url_base = 'https://fbref.com/pt/jogadores/7f9c5d2d/partidas/2022/c24/'

# Sufixos de URL
sufixos = [
    'passing/Abner-Historicos-dos-Jogos',
    # Adicione outros sufixos conforme necessário
]

# Dicionário para armazenar todos os dados
dados_totais = {}

# Iterando sobre cada sufixo de URL
for sufixo in sufixos:
    url = url_base + sufixo
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraindo informações da div
    info_adicionais = extrair_info_div(soup)

    # Extraindo e imprimindo dados das tabelas
    dados_tabelas = extrair_dados_tabelas(soup)

    # Adicionando dados ao dicionário
    dados_totais[sufixo] = {
        'Informações Adicionais': info_adicionais,
        'Dados das Tabelas': dados_tabelas
    }

# Salvando dados em um arquivo JSON
with open('dados_extraidos.json', 'w', encoding='utf-8') as f:
    json.dump(dados_totais, f, ensure_ascii=False, indent=4)
