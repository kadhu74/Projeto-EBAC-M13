import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../dados/clientes-v3-preparado.csv')
# Lê o arquivo CSV com os dados dos clientes
print(df.head(20).to_string())
# Exibe as primeiras 20 linhas do DataFrame no terminal

# O termo PLOTAR significa VISUALIZAR

#  Gráfico de Barras - Modo 1 (usando o plot do Pandas direto)
plt.figure(figsize=(10, 6))  #  Define o tamanho da figura (largura 10, altura 6)
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')   # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas
# Aqui contamos quantas vezes aparece cada nível de educação(VALUE_COUNTS)
# e criamos um gráfico de barras (kind='bar') com a cor verde claro

plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)  # Mantém os rótulos do eixo X na horizontal (0 graus)
plt.show()  # Exibe o gráfico na tela

# GRÁFICO DE BARRAS - Modo 2 (usando plt.bar manualmente)
x = df['nivel_educacao'].value_counts().index   # # Aqui pegamos os nomes das categorias (ex: Ensino Médio, Superior, etc) (.INDEX)
y = df['nivel_educacao'].value_counts.values   # # Aqui pegamos as quantidades de cada categoria (.VALUES)

plt.figure(figsize=(10, 6))   # Define o tamanho da figura
plt.bar(x, y, color='#60aa65')  # este comando faz a mesma coisa do de cima, mas precisamos definir o que é o eixo X e Y, se são indices/valores...
# Cria um gráfico de barras passando manualmente os valores de X e Y
plt.title('Divisão de Escolaridade - 2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.show()

#  Gráfico de Pizza - Melhor para ver a PORCENTAGEM

plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)  #autopct e para mostrar com a porcentagem aparecera, nesse caaso com 1 casa decimal

#   Cria o grafico de pizza
# - y são os valores
# - labels=x são os nomes das categorias
# - autopct mostra as porcentagens com 1 casa decimal
# - startangle=90 faz o gráfico começar a desenhar a partir do ângulo de 90 graus (fica mais bonito)
plt.title('Distribuição de Nível de Educação')
plt.show()


#  Gráfico de Dispersão - HEXBIN (Dispersão com densidade de pontos)

plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')  #  https://matplotlib.org/stable/users/explain/colors/colormaps.html
# Cria um gráfico de dispersão em formato de hexágonos (Hexbin)
# - Eixo X: Idade
# - Eixo Y: Salário
# - gridsize=40 → define o tamanho das células hexagonais
# - cmap='Blues' → define a paleta de cor (tons de azul, mais pontos = mais escuro)

plt.colorbar(label='Contagem dentro do bin')  # # Adiciona uma barra de cores mostrando a quantidade de pontos por área
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()