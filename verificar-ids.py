# Verifique se há IDs que não tiveram dados armazenados
if ids_sem_dados:
    print("Os seguintes IDs não tiveram informações populadas:")
    for id_atleta, nome_atleta in ids_sem_dados:
        print(f"ID: {id_atleta}, Nome: {nome_atleta}")

# Salve os dados totais e os IDs sem dados em arquivos JSON separados
with open('fbref_misc_2023.json', 'w', encoding='utf-8') as f:
    json.dump(dados_totais, f, ensure_ascii=False, indent=4)

if ids_sem_dados:  # Se houver IDs sem dados, salve-os em um arquivo separado
    with open('ids_sem_dados_misc_2023.json', 'w', encoding='utf-8') as f:
        json.dump(ids_sem_dados, f, ensure_ascii=False, indent=4)
