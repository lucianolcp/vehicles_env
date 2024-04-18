import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar os dados do CSV
df = pd.read_csv('vehicles_us.csv')

# Criar caixas de seleção para escolher o tipo de gráfico
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')
build_bar_chart = st.checkbox('Criar um gráfico de Tipos por Fabricantes')

if build_histogram:  # se a caixa de seleção do histograma for selecionada
    # Escrever uma mensagem
    st.write('Criando um histograma para a coluna odometer')

    # Criar um histograma
    fig_hist = px.histogram(df, x="odometer")

    # Exibir o histograma
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:  # se a caixa de seleção do gráfico de dispersão for selecionada
    # Escrever uma mensagem
    st.write('Criando um gráfico de dispersão para as colunas odometer e price')

    # Criar um gráfico de dispersão
    fig_scatter = px.scatter(df, x="odometer", y="price")

    # Exibir o gráfico de dispersão
    st.plotly_chart(fig_scatter, use_container_width=True)

if build_bar_chart:  # se a caixa de seleção do gráfico de barras for selecionada
    # Escrever uma mensagem
    st.write(
        'Criando um gráfico de barras para a contagem de tipos de veículos por fabricante')

    # Extrair o fabricante do modelo
    df['manufacturer'] = df['model'].str.split(n=1, expand=True)[0]

    # Agrupar os dados por fabricante e tipo de veículo e contar o número de ocorrências
    df_grouped = df.groupby(['manufacturer', 'type']
                            ).size().reset_index(name='count')

    # Criar o gráfico de barras iterativo
    fig_bar = px.bar(df_grouped, x='manufacturer', y='count', color='type',
                     labels={'manufacturer': 'Fabricante',
                             'count': 'Contagem', 'type': 'Tipo de Veículo'},
                     title='Contagem de Tipos de Veículos por Fabricante')

    # Exibir o gráfico de barras
    st.plotly_chart(fig_bar, use_container_width=True)
