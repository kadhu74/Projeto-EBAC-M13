import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../dados/ecommerce_preparados.csv')
print(df.info())
print(df.describe())
print(df.columns.tolist())        # Lista de colunas
print(df.dtypes)                  # Tipo de cada coluna
print(df.head(5).to_string())     # Só as 5 primeiras linhas completas


#  Tratamento de Dados
print(df['Qtd_Vendidos'].unique())  # mostra todos os 'dados' (todos os números e palavras que continha) da coluna
vendas = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+500': 500,
    '+1000': 1000,
    '+5mil': 5000,
    '+10mil': 10000,
    '+50mil': 50000
}
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(vendas)  # Transformando a coluna em numérica
df['Marca_Cod'] = df['Marca'].astype('category').cat.codes   # converte a coluna marca para número

#  GRÁFICO DE HISTOGRAMA / Aqui vamos VISUALIZAR a QUANTIDADE (Y) de produtos com tal PREÇO (X)

plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=50, color='green', edgecolor='black', alpha=0.6) #BINS controla o número de intervalos no eixo X
plt.title('Distribuição dos Preços')
plt.xlabel('Preço')
plt.ylabel('Quantidade de Produtos')
plt.grid(True)  #Adiciona as linhas de fundo do grafico (aquele jogo da velha de fundo)
plt.show()


#   GRÁFICO DE DISPERSÃO / Vamos ver a relação entre duas variáveis numéricas preço por quantidade de vendas
plt.figure(figsize=(10, 6))
plt.scatter(df['Preço'], df['Qtd_Vendidos_Cod'], alpha=0.6, color='green')   # eixo X= PREÇO para observarmos o valor/ eixo Y= QUANTIDADE para vermos o volume de vendas
plt.title('Dispersão - Preço e Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()

# HEATMAP /
corr = df[['Marca_Cod', 'Qtd_Vendidos_Cod']].corr()   #calcula a correlação entre marca e quantidade de vendas
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm')   # annot=True mostra os números da correlação dentro de cada célula
plt.title('Correlação - Marca e Quantidade de Vendas')
plt.tight_layout()  #   Ajusta automaticamente o espaçamento entre os gráficos na figura para que os títulos, rótulos dos eixos e os próprios gráficos não fiquem sobrepostos ou cortados.
plt.show()

#   GRÁFICO DE PIZZA /
df['Tem_Desconto'] = df['Desconto'].apply(lambda x: 'Com Desconto' if x > 0 else 'Sem Desconto')  #cria uma nova coluna baseada nos produtos com e sem desconto/ e se o desconto for maior que 0 vai pra com desconto
contagem_desconto = df['Tem_Desconto'].value_counts()   # conta quantos produtos tem desconto e quantos não tem
plt.figure(figsize=(6, 6))
plt.pie(contagem_desconto.values, labels=contagem_desconto.index, autopct='%.1f%%', startangle=90, colors=['#66bb6a', '#ef5350'])  #cor verde para com desconto e vermelho para sem desconto
plt.title('Produtos com e Sem Desconto')
plt.show()

#   GRÁFICO DE DENSIDADE
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], shade=True, color='blue')
plt.title('Densidade - Distribuição dos Preços')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.grid(True)
plt.show()

#   GRÁIFICO DE BARRAS
plt.figure(figsize=(10, 6))
top_marcas = df['Marca'].value_counts().head(5).index   # conta as 5 marcas com mais produtos
total_avaliacoes_marca = df[df['Marca'].isin(top_marcas)].groupby('Marca')['N_Avaliações'].sum()    #Agrupa o total de avaliações pra essas 5 marcas
total_avaliacoes_marca = total_avaliacoes_marca.sort_values(ascending=True)    # Ordena do menor para o maior/ melhor leitura no gráfico horizontal
total_avaliacoes_marca.plot(kind='barh', color='#90ee70')
plt.title('Marca e Total de Avaliações')
plt.xlabel('Total de Avaliações', fontsize=10, labelpad=10)
plt.ylabel('Marcas', fontsize=10, labelpad=10)
plt.tight_layout()
plt.show()

#   GRÁFICO DE REGRESSÃO
plt.figure(figsize=(8, 6))
sns.regplot(x='Nota', y='Qtd_Vendidos_Cod', data=df, scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
plt.title('Relação entre Nota e Vendas')
plt.xlabel('Nota do Produto')
plt.ylabel('Quantidade Vendida')
plt.tight_layout()
plt.show()