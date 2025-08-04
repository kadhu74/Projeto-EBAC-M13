import pandas as pd

df = pd.read_csv('dados/clientes.csv')

#verificar os primeiros registros
print(df.head().to_string())

#verificar os ultimos registros
print(df.tail().to_string())

#verificar a quantidade de linhas e colunas
print('Quantidade: ', df.shape)

#verificar a tipagem dos dados
print('Tipagem: \n', df.dtypes)

#checar os valores nulos
print('Valores Nulos: \n', df.isnull().sum())
