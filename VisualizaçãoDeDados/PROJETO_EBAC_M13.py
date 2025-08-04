import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import numpy as np


df = pd.read_csv('../dados/MODULO7_PROJETOFINAL_BASE_SUPERMERCADO.csv', delimiter=',')
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

print(df.head(10))

# 1° - Traga a média e a mediana dos preços - coluna Preco_Normal - por categoria de produto.

# MÉDIA
media_por_categoria = df.groupby('Categoria')['Preco_Normal'].mean()
print(f'Média:', media_por_categoria)

# MEDIANA
mediana_por_categoria = df.groupby('Categoria')['Preco_Normal'].median()
print(f'Mediana:', mediana_por_categoria)

# Identifique as categorias que parecem ter um valor de média abaixo ou acima da mediana.

comparativo = pd.DataFrame({
                            'Média': media_por_categoria,
                            'Mediana': mediana_por_categoria
})

comparativo = comparativo.sort_values('Média', ascending=False)
print(comparativo)

# Categorias com valor de Média ABAIXO da Mediana:
# comidas-preparadas

# Categorias com valor de Média ACIMA da Mediana:
# lacteos, congelados, belleza-y-cuidado-personal, frutas, verduras, instantaneos-y-sopas


# 2° - Traga o desvio padrão por categoria de produto.

desvio_por_categoria = df.groupby('Categoria')['Preco_Normal'].std()
print(f'Desvio Padrão:', desvio_por_categoria)


# Qual o comportamento da média e mediana nas categorias com maior desvio?

comparacao = pd.DataFrame({
                            'Média': media_por_categoria,
                            'Mediana': mediana_por_categoria,
                            'Desvio Padrão': desvio_por_categoria
})
comparacao = comparacao.sort_values('Desvio Padrão', ascending=False)
print(comparacao)

#  RESPOSTA: nas categorias lacteos, belleza-y-cuidado-personal e congelados tiveram o desvio padrão é altíssimo, nos mostrando a grande variação de preço.
#  Isso significa que existem produtos com preços muito altos ou muito baixos, o que eleva o desvio padrão
# As categorias: comidas-preparas, verduras e frutas tem o desvio padrão ABAIXO da média. Isso nos mostra que não há grande dispersão nos preços



# 3° - Plot um boxplot da distribuição do Preco_Normal para a categoria que você identificou que tem o maior desvio padrão.

df_lacteos = df.loc[df['Categoria'] == 'lacteos']
fig = px.box(df_lacteos, y='Preco_Normal', title='Distribuição dos Preços - Categoria Lacteos')
fig.show()


# Como é a distribuição desses dados segundo o boxplot? Você identifica muitos outliers?
#  RESPOSTA: A distribuição dos dados nos mostra que a maior parte dos preços está concentrada entre o Q1 e o Q3. Porém, observamos uma grande quantidade de outliers acima do limite superior, indicando uma ampla dispersão nos preços — provavelmente causada por produtos importados ou considerados “premium”. Também é possível notar que não há outliers abaixo do valor mínimo, o que evidencia que os produtos de preço mais baixo estão dentro do esperado.


# 4° - Plote um gráfico de barras onde temos a média de descontos por categoria.

# Substitui zeros por NaN para limpeza
df.loc[df['Preco_Normal'] == 0, 'Preco_Normal'] = np.nan

# Filtra apenas os produtos com desconto (independente do preço normal)
produtos_com_desconto = df[df['Desconto'] > 0]

print(f'Total de produtos com desconto: {len(produtos_com_desconto)}')
print(produtos_com_desconto[['Categoria', 'Desconto', 'Preco_Normal']].head(10))

# Calcula média de desconto absoluto por categoria
media_desconto_reais = produtos_com_desconto.groupby('Categoria')['Desconto'].mean().sort_values(ascending=False)

print('Média de desconto (CLP) por categoria:\n', media_desconto_reais)


# criando o grafico de barras
fig = px.bar(
    media_desconto_reais,
    x=media_desconto_reais.index,
    y=media_desconto_reais.values,
    labels={'x': 'Categoria', 'y': 'Média do Desconto (CLP)'},
    title='Média de Desconto (Pesos Chilenos) por Categoria'
)

fig.update_layout(xaxis_tickangle=-45)
fig.show()


# 5° - Plote um gráfico de mapa interativo agrupando os dados por categoria, marca e trazendo a média de desconto.

# Agrupa por Categoria e Marca, calcula a média do desconto
df_grouped = df.groupby(['Categoria', 'Marca'])['Desconto'].mean().reset_index()

# Cria o treemap
fig = px.treemap(
    df_grouped,
    path=['Categoria', 'Marca'],
    values='Desconto',
    title='Média de Desconto por Categoria e Marca'
)

fig.show()
