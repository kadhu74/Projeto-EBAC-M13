#  Analise Preparatória de Dados
import pandas as pd

df = pd.read_csv('dados/clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')
print(df['data'].isnull().sum())

print('Verificação inicial: ')
print(df.info()) #mostra as informações do DataFrame, quantos campos nulos


print('Analise de dados nulos \n', df.isnull().sum())
print('% de dados nulos:\n', df.isnull().mean() * 100)  # é interessante a gente fazer a porcentagem dos campos nulos, a media (mean() * 100) pra saber a porcentagem dos dados nulos
df.dropna(inplace=True)  # aqui estamos excluindo os dados nulos
print('Confirmar remoção de dados nulos:\n', df.isnull().sum().sum())

print('Analise de dados duplicados:\n', df.duplicated().sum())

print('Analise de dados únicos:\n', df.nunique())

print('Estatísticas dos dados:\n', df.describe())  # mostra as estatisticas basicas dos dados

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]  # aqui estamos tirando esses campos que são dados sensiveis dos clientes e pedindo para exibir apenas os outros dados
print(df.head().to_string())

df.to_csv('dados/clientes-v2-tratados.csv', index=False)

