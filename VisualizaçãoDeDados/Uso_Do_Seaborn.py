import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../dados/clientes-v3-preparado.csv')
print(df.head().to_string())   ## Exibe as primeiras linhas completas, sem cortar colunas(.to_string())

#  Gráfico de Dispersão com Seaborn (Jointplot = Dispersão + histogramas marginais dos eixos X e Y)
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')  # ['scatter', 'hist',  'hex', 'kde', 'reg', 'resid']
# Fazemos um gráfico de dispersão mostrando a relação entre idade e salário
# Também exibe histogramas nos eixos para mostrar a distribuição de cada variável
plt.show()

# Gráfico de Densidade (KDE = Kernel Density Estimation)

plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
# Mostra a distribuição da variável 'salario' como uma curva suave
# fill=True preenche a área embaixo da curva
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.show()


# Gráfico de Pairplot - Dispersão e Histograma

sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])  # https://seaborn.pydata.org/tutorial/color_palettes.html
# Faz vários gráficos de dispersão cruzando todas as combinações entre essas colunas
# Nos mesmos gráficos aparecem os histogramas nas diagonais
plt.show()

#  Gráfico de Regressão (Reta de tendência + Dispersão)
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
# Mostra os pontos de dispersão e também uma linha de regressão (reta de tendência)
# scatter_kws ajusta a transparência e cor dos pontos de dispersão
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

#   Gráfico de Contagem (Countplot) com agrupamento (hue)

sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
# Conta quantos clientes tem em cada categoria de estado civil
# Agrupando por nível de educação (cores diferentes dentro de cada barra)
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade de Clientes')
plt.legend(title='Nível de Educação')
plt.show()