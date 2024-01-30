# Se 20 atletas foram processados, imprime uma mensagem e pausa por 1 minuto
    if (index + 1) % 20 == 0:
        if dados_totais[nome_atleta]['Dados das Tabelas'] or dados_totais[nome_atleta]['Informações Adicionais']:
            print(f'Dados dos 20 atletas até {nome_atleta} foram armazenados.')
        else:
            print(f'Dados dos 20 atletas até {nome_atleta} estão vazios.')
        time.sleep(60)  # Pausa por 60 segundos (1 minuto)
