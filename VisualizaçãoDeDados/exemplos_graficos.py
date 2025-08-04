import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../dados/clientes-v3-preparado.csv')

# Criando uma matriz de correlação apenas com as colunas numéricas de interesse
df_corr = df[['salario', 'idade', 'anos-experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
# .corr() calcula a correlação entre as colunas numéricas selecionadas
# Correlação mostra o quanto uma variável está relacionada com a outra (de -1 a +1)

#  Heatmap de Correlação

plt.figure(figsize=(10, 6))
sns.heatmap(df_corr, annot=True, fmt=".2f")
# Cria o mapa de calor
# annot=True mostra os números da correlação dentro de cada célula
# fmt=".2f" faz aparecer os números com 2 casas decimais
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()


# Countplot / Countplot simples (Gráfico de Contagem)

sns.countplot(x='estado_civil', hue='nivel_educacao', data=df)
# Mostra quantos clientes tem em cada categoria de 'estado_civil'
# Com o hue, as barras são divididas por 'nivel_educacao' (agrupamento por cores diferentes)
plt.title('Distribuição do Estado Cívil')
plt.xlabel('Estado Cívil')
plt.ylabel('Contagem')
plt.show()


#  Countplot com Legenda personalizada

sns.countplot(x='estado_civil', hue='nivel_educacao', data=df)
# Mesmo gráfico de contagem anterior, mostrando o Estado Civil dividido por Nível de Educação
plt.title('Distribuição do Estado Cívil')
plt.xlabel('Estado Cívil')
plt.ylabel('Contagem')
plt.legend(title='Nível de Educação')
# Adiciona um título personalizado na legenda (hue)
plt.show()

# SALVAR O GRÁFICO
#  Use `plt.savefig('nome_do_arquivo.png')` antes de `plt.show()`.