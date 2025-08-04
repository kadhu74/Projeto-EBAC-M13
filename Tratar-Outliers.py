#  Tratar Outliers- Outliers é todo valor que são extremamente alto ou extremamente baixo. É de extrema importância saber o que se deve fazer com um outlier
import pandas as pd
from scipy import stats


pd.set_option('display.width', None)

df = pd.read_csv('dados/clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]  #aqui criamos um novo dataframe, sem excluir o original, onde nos mostrará todas as linhas que contem a idade maior do que 100


print('Filtro Básico:\n', df_filtro_basico[['nome', 'idade']])  # aqui estamos exibindo ele na tela, mas apenas pedindo para mostrar o nome e a idade, e não todas as colunas da linha


#Identificar Outliers com Z-score(z-score: é uma medida estatisca que diz quantos desvios padrão um valor está acima ou abaixo da média, obs se for maior que +3 ou menor que -3 é considerado um outlier)

z_scores = stats.zscore(df['idade'].dropna())  # aqui a variavel z_scores vai mostar um novo dataframe, sem excluir o original, mostrando apenas as linhas que contém uma idade 'válida', aqui o dropna ele não exclui a linha por completo e sim cria uma cópia da coluna sem os valores nulos
outliers_z = df[z_scores >= 3]   # aqui estamos criando um novo dataframe onde apenas as linhas do dataframe onde o z-score é maior ou igual a 3 (nos mostrando os outliers)
print('Outliers pelo Z-Score:\n', outliers_z)


#Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)]  # aqui o stats.zscore(df['idade']) calcula o Z-score no nosso dataframe original na coluna 'idade', ou seja mede o desvio de padrão cada idade está da media e os valores menores que 3 (< 3) serão impimidos na tela
#   Um detalhe muito importante é que nesse calculo do Z-score ele só irá mostrar os valores menores do que 3, só exclui os outliers ACIMA da média, os Z-score muito negativos entrarão dentro  do dataframe


# Identificar Outliers com IQR/ é a faixa interquartílica, uma medida estatística que mostra a dispersão central dos dados
# Q1 (1º quartil) → 25% dos dados menores que este valor.

# Q2 (2º quartil ou mediana) → o valor do meio (50%).

# Q3 (3º quartil) → 75% dos dados são menores que este valor.

# Ideal quando seus dados não seguem uma distribuição normal (não simétrica).

# Mais robusto que o Z-score porque não depende da média nem do desvio padrão.

# Mediana = valor central quando os dados estão ordenados

Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('Limites IQR: ', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('Outliers pelo IQR:\n', outliers_iqr)

#  Filtrar Outliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]


#  Filtrar endereços inválidos com IQR
df['endereço'] = df['endereço'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)


#  Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print('Qnt de registros com nomes grandes: \n', (df['nome'] == 'Nome inválido').sum())

print('Dados com Outliers tratados:\n ', df)


#   Salvar dataframe
df.to_csv('dados/clientes_remove_outliers.csv', index=False)


