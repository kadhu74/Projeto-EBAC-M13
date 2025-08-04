import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../dados/clientes-v3-preparado.csv')

print(df.head().to_string())


#  Histograma  - histograma é um gráfico de distribuição de frequências
plt.hist(df['salario'])
plt.show()


#  Histograma - Parâmetros
plt.figure(figsize=(10, 6))   # definição do tamanho da figura, aqui seria 10 * 6
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
# O argumento "bins=100" significa que o histograma será dividido em 100 faixas (intervalos) de valores de salário.
# Cada faixa representa um pedaço da escala de salários, e o gráfico vai mostrar quantos salários caem em cada faixa.
# Quanto maior o número de bins, mais detalhado fica o gráfico (mais barras e intervalos menores).
#  alpha=0.8 → Transparência das barras (0 = totalmente transparente, 1 = totalmente opaco).

plt.title('Histograma - Distribuição de Salários')  # Adicionamos um título para nosso histograma
plt.xlabel('Salário')  # atribuindo um nome para o eixo X
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
# aqui estamos definindo o tamanho/intervalo do eixo X, onde definimos que ele vai do 0 até o valor maxímimo encontrado na coluna salario com um intervalo de 2000, ou seja pula de 2000 em 2000
# Aqui estamos definindo os intervalos do eixo X (ticks), começando em 0, indo até um pouco além do maior salário (+2000 de folga), com passos de 2000 em 2000.
# Fazemos o +2000 porque o range() não inclui o número final, e assim garantimos que o último salário apareça no gráfico.
#  O RANGE É FAZ O SEGUINTE CAMINHO (INICIO, FIM, PASSO)

plt.ylabel('Frequência')  # atribuimos um nome para o eixo Y
plt.grid(True)   # O grid são aquelas linhas de fundo (horizontais e verticais) que aparecem atrás do gráfico
plt.show()   # sempre utilize este comando


#  Multiplos Graficos
plt.figure(figsize=(10, 6))  # definição do tamanho do gráfico
plt.subplot(2, 2, 1)  # 2 Linha(numero de linha na grade de subgraficos), 2 Colunas(numero de colunas na grade de subgráficos), 1 Gráfico(posição do  gráfico atual)
#  Precisa usar o subplot, pois teremos mais que um grafico
# Estamos criando uma grade de subgráficos com 2 linhas e 2 colunas (total de até 4 gráficos na mesma imagem).
# O número 1 indica que este gráfico será desenhado na primeira posição (canto superior esquerdo da grade).

#   Grafico de Dispersão  agora aqui configuramos o primeiro gráfico da imagem, como nome(titulo), e definimos os nomes dos eixos X e Y
plt.scatter(df['salario'], df['salario'])  # com ela mesma (X e Y iguais, resultando numa linha de pontos diagonais).
plt.title('Dispersão - Salario e Salario')  # criamos o título para o gráfico de dispersão
plt.xlabel('Salario')
plt.ylabel('Salario')


plt.subplot(1, 2, 2)   # 1 Linha(a grade terá uma linha só), 2 Colunas 2 Graficos
# Agora estamos criando uma grade com 1 linha e 2 colunas (total de 2 espaços lado a lado).
# O número 2 indica que vamos trabalhar no segundo espaço (coluna da direita).
# Ou seja: estamos configurando o segundo gráfico, que ficará ao lado do primeiro.

plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha=0.6, s=30)   # codigo da cor hexiadecimal
# Criando um gráfico de dispersão com 'salario' no eixo X e 'anos_experiencia' no eixo Y.
# Definimos a cor dos pontos com código hexadecimal (#5883a8), ajustamos a transparência com alpha=0.6, e o tamanho dos pontos com s=30.
#  no comando plt.scatter  está dizendo ao Python quais dados vão no eixo X e no eixo Y (ou seja, quais variáveis ele deve usar). Exemplo: "Salário vai no eixo X e Experiência no eixo Y

plt.title('Dispersão - Idade e Anos de Experiência')
plt.xlabel('Salario')
plt.ylabel('Anos de Experiência')

#  Mapa de Calor  agora iremos utilizar a biblioteca seaborn
corr = df[['salario', 'anos_experiencia']].corr()  # .corr() Esse é o método do Pandas que calcula a matriz de correlação entre as colunas selecionadas
# Calcula a correlação entre as colunas 'salario' e 'anos_experiencia'
# O resultado será uma matriz 2x2 mostrando a correlação de cada uma com a outra

plt.subplot(2, 2, 3)  # 1 Linha, 2 Colunas, 3 Gráfico(terceira posição na grade)
sns.heatmap(corr, annot=True, cmap='coolwarm')
# Cria um mapa de calor (heatmap) para mostrar visualmente a correlação.
# 'annot=True' exibe os valores numéricos dentro dos quadrados.
# 'cmap="coolwarm"' escolhe uma paleta de cores que vai de azul a vermelho.

plt.title('Correlação Salário e Idade')  # comando para o título

plt.tight_layout()
#   Ajusta automaticamente o espaçamento entre os gráficos na figura para que os títulos, rótulos dos eixos e os próprios gráficos não fiquem sobrepostos ou cortados.

plt.show()