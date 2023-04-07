# Importa o streamlit com o apelido st
import streamlit as st

# Importa o pandas com o apelido pd
import pandas as pd

# Importa o plotly-express com o apelido px
import plotly.express as px

from utils import regioes, importar_dados, filtrar_df


# Define configurações da página
st.set_page_config(
    page_title='Dashboard Games',
    page_icon=':video-game:',
    layout='wide',
    initial_sidebar_state='expanded'
)


# Define um título para a aplicação
st.title('Dashboard Games')

# Obtém o dataframe com os dados de vendas de video games
df_vendas = importar_dados()

# Lista com os gêneros de games
generos = list(df_vendas['Genre'].unique())

# Lista com as plataformas
plataformas = list(df_vendas['Platform'].unique())

# Lista com os anos
anos = list(df_vendas['Year'].unique())


# Cria uma barra lateral
with st.sidebar:
    # Cria uma seção intitulada Filtros na barra lateral
    st.header('Filtros')

    # Cria uma subseção na qual o usuário define um intervalo de anos
    st.subheader('Intervalo')

    # Intervalo de anos para realizar a análise
    intervalo = st.slider('Selecione um intervalo', min_value=int(min(anos)), max_value=int(max(anos)), value=(1990, 2010))

    # Cria uma subseção na qual o usuário define uma região
    st.subheader('Região')

    # Menu suspenso para o usuário escolher uma região
    regiao_selecionada = st.selectbox('Selecione uma região:', options=regioes.keys())

    # Obtém um dataframe filtrado conforme as escolhas do usuário
    df = filtrar_df(df_vendas, intervalo, regiao_selecionada)

    # Obtém a coluna de vendas a ser considerada
    coluna_vendas = regioes[regiao_selecionada]

    # Número de unidades vendidas   
    unidades_vendidas = round(df[coluna_vendas].sum(),2)

    # Vendas agrupadas por gênero
    df_genero = df[['Genre', coluna_vendas]].groupby('Genre').sum()

    # Vendas agrupadas por gênero e ordenadas em ordem decrescente de total de vendas
    df_genero = df_genero.sort_values(by=coluna_vendas, ascending=False).reset_index()

    # Obtém o gênero mais popular
    genero_mais_popular = df_genero.loc[0, 'Genre']

    # Obtém o número de vendas do gênero mais popular
    vendas_genero_mais_popular = df_genero.loc[0, coluna_vendas]

    # Vendas agrupadas por plataforma
    df_plataforma = df[['Platform', coluna_vendas]].groupby('Platform').sum()

    # Vendas agrupadas por gênero e ordenadas em ordem decrescente de total de vendas
    df_plataforma = df_plataforma.sort_values(by=coluna_vendas, ascending=False).reset_index()

    # Obtém a plataforma mais popular
    plataforma_mais_popular = df_plataforma.loc[0, 'Platform']

    # Vendas de jogos para a plataforma mais popular
    vendas_plataforma_mais_popular = df_plataforma.loc[0, coluna_vendas]

    # Vendas agrupadas por ano
    df_ano = df[['Year', coluna_vendas]].groupby('Year').sum().reset_index()

    # Vendas agrupadas por nome do jogo
    df_jogo = df[['Name', coluna_vendas]].groupby('Name').sum()

    # Vendas agrupadas por nome do jogo ordenadas em ordem decrescente de total de vendas
    df_jogo = df_jogo.sort_values(by=coluna_vendas, ascending=False).reset_index()

    # Obtém o jogo mais popular
    jogo_mais_popular = df_jogo.loc[0, 'Name']

    # Vendas jogo mais popular
    vendas_jogo_mais_popular = df_jogo.loc[0, coluna_vendas]

# Cria quatro colunas
col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(label='**Unidades Vendidas (milhões)**', value=unidades_vendidas)

with col2:
    st.metric(label=f'**Gênero mais Popular**: {genero_mais_popular}', value=vendas_genero_mais_popular)

with col3:
    st.metric(label=f'**Jogo mais Popular**: {jogo_mais_popular}', value=vendas_jogo_mais_popular)

with col4:
    st.metric(label=f'**Plataforma com mais Jogos Vendidos**: {plataforma_mais_popular}', value=vendas_plataforma_mais_popular)

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(df_jogo[:5], x='Name', y=coluna_vendas, labels={'Nome', 'Unidades Vendidas'}, title='Top 5 Jogos')
    st.plotly_chart(fig)

    fig = px.bar(df_genero, x='Genre', y=coluna_vendas, labels={'Gênero', 'Unidades Vendidas'}, title='Vendas por Gênero do Jogo')
    st.plotly_chart(fig)

with col2:
    fig = px.area(df_ano, x='Year', y=coluna_vendas, labels={'Ano', 'Unidades Vendidas'}, title='Vendas por Ano')
    st.plotly_chart(fig)

    st.write()
    fig = px.bar(df_plataforma[:5], x='Platform', y=coluna_vendas, labels={'Plataforma', 'Unidades Vendidas'}, title='Top 5 Plataformas')
    st.plotly_chart(fig)
