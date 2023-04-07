import pandas as pd


# Dicionário com os locais com dados de vendas
regioes = {
    'América do Norte': 'NA_Sales',
    'Europa': 'EU_Sales',
    'Japão': 'JP_Sales',
    'Outros': 'Other_Sales'
}


def importar_dados():
    # Lê o arquivo CSV com os dados de vendas de video games
    df = pd.read_csv('vgsales.csv')

    # Elimina toda as linhas que contém pelo menos um dado do tipo NaN
    df.dropna(axis='index', how='any', inplace=True)

    # Converte o tipo da coluna Year para inteiro
    df['Year'] = df['Year'].astype('int64')

    # Seleciona somente as linhas em que o ano é menor do que 2016
    df = df[df['Year'] < 2016]

    # Retorna o dataframe para a análise
    return df


def filtrar_df(df_vendas, intervalo, regiao):
    # Desempacotamento da tupla
    menor_ano, maior_ano = intervalo

    # Filtra os dados de vendas para o intervalor de anos selecionado
    df_vendas = df_vendas[(df_vendas['Year'] >= menor_ano) & (df_vendas['Year'] <= maior_ano)]

    if regiao == 'América do Norte':
        df_vendas = df_vendas.drop(['EU_Sales', 'JP_Sales', 'Other_Sales'], axis=1)
    elif regiao == 'Europa':
        df_vendas = df_vendas.drop(['NA_Sales', 'JP_Sales', 'Other_Sales'], axis=1)
    elif regiao == 'Japão':
        df_vendas = df_vendas.drop(['NA_Sales', 'EU_Sales', 'Other_Sales'], axis=1)
    else:
        df_vendas = df_vendas.drop(['NA_Sales', 'EU_Sales', 'JP_Sales'], axis=1)

    # Retorna o df filtrado
    return df_vendas
