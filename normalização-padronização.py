import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('dados/clientes-v2-tratados.csv')

print(df.head())

#  df =df.drop(['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)
df = df[['idade', 'salario']]  # mais pratico do que a de cima para exibir somente os campos idade e salario

#  Normalização  MinMaxScaler  # O que faz: Redimensiona os dados para um intervalo entre 0 e 1 (ou outro definido por você).
#  Quando usar: Quando você quer preservar a distribuição dos dados mas ajustar os valores para uma escala comum.
scaler = MinMaxScaler()  # criamos a variavel scaler para atribuirmos o modulo que iremos utilizar
# aqui estamos normalizando os campos idade e salario no padrao entre 0 e 1
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])  # criamos um novo campo para compararmos
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])


#  Padronização  - StandartScaler  # O que faz: Padroniza os dados para que tenham média 0 e desvio padrão 1.
scaler = StandardScaler()  # variavel criada para atribuirmos o modulo que iremos usar
df['idadeStandartScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandartScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()  # O que faz: Escala os dados com base na mediana e no intervalo interquartil (IQR).
# Ou seja, reduz o impacto de outliers
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print('MinMaxScaler (De 0 a 1): ')
print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salário - Min: {:.4f} Max{:.4f} Mean{:.4f} Std{:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))


print('\nMinMaxScaler (De -1 a 1): ')
print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salário - Min: {:.4f} Max{:.4f} Mean{:.4f} Std{:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

print('\nStandartScaler (Ajuste a media a 0 e o desvio de padrão a 1): ')
print('Idade - Min{:.4f} Max{:.4f} Mean: {:.18f} Std: {:.4f}'.format(df['idadeStandartScaler'].min(), df['idadeStandartScaler'].max(), df['idadeStandartScaler'].mean(), df['idadeStandartScaler'].std()))
print('Salario - Min{:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}'.format(df['salarioStandartScaler'].min(), df['salarioStandartScaler'].max(), df['salarioStandartScaler'].mean(), df['salarioStandartScaler'].std()))

print('\nRobustScaler (Ajuste a mediana e IQR): ')
print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(df['idadeRobustScaler'].min(), df['idadeRobustScaler'].max(), df['idadeRobustScaler'].mean(), df['idadeRobustScaler'].std()))
print('Salario - Min: {:.4f} Max: {:.4f} Mean{:.4f} Std: {:.4f}'.format(df['salarioRobustScaler'].min(), df['salarioRobustScaler'].max(), df['salarioRobustScaler'].mean(), df['salarioRobustScaler'].std()))

