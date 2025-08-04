import pandas as pd

df = pd.read_csv('dados/clientes.csv')

pd.set_option('display.width', None)
print(df.head())

#  Remover DADOS/ primeiramente removemos o dado pais, pq todas as pessoas nesse banco de dados são brasileiras, então acaba sendo um dado insignificante para nossa coleta
df.drop('pais', axis=1, inplace=True)   #axis=1 é referente a Coluna
df.drop(2, axis=0, inplace= True)  # axis=0 é referente a Linha
#  o inplace é para fazer a substituição direta no nosso dataframe, no primeiro lugar do parenteses colocamos o campo que queremos remover

#  Normalizar Campos de Textos/ O padrão é sempre deixar todas as linhas iguais
df['nome'] = df['nome'].str.title()  #colocando a primeira letra de cadsa palavra em maiusculo por ser um nome
df['endereço'] = df['endereço'].str.lowe()  #colocando todo o endereço em minusculo
df['estado'] = df['estado'].str.strip().upper()  #tiramos os espaços e colocamos em maiusculo


#  Converter Tipos de Dados
df['idade'] = df['idade'].astype(int)  #usamos o comando astype para a conversão que queremos


#  Tratar Valores Nulos
df_fillna = df.fillna(0)  # Substitui os valores nulos (NaN) por 0
df_dropna = df.dropna()  # Remove o registro com valores nulos (NaN)
df_dropna4 = df.dropna(thresh=4)  # Definir o minino de valores não nulos que cada registro deve ter/ a linha será mantida se tiver pelo menos 4 valores não nulos
df = df.dropna(subset=['cpf'])  # Remover registros que tem o campo cpf nulo, fazendo diretamente no arquivo do dataframe


print('Valores Nulos:\n', df.isnull().sum().sum())
print('Qnt de registros nulos com fillna: ', df_fillna.isnull().sum().sum())
print('Qnt de registros nulos com dropna: ', df_dropna.isnull().sum().sum())
print('Qnt de registros nulos com dropna4: ', df_dropna4.isnull().sum().sum())
print('Qnt de registros nulos com cpf: ', df.insull().sum().sum())


#   Jeitos diferentes de usar o fillna

df.fillna({'estado': 'Desconhecido'}, inplace=True)  #após as chaves colocamos o campo que queremos substituir, apo´s os : colocamos o que queremos substituir, e o inplace pra ja fazer direto no dataframe
df['endereço'] = df['endereço'].fillna('Endereço não informado')  # fazendo a substituição do valor original na variavel
df['idade_corrigidaa'] = df['idade'].fillna(df['idade'].mean())   #aqui criamos um novo campo no nosso dataframe onde o campo idade que tiver valor nulo será substituido pela média (.mean()) de idade do 'grupo'


#   Tratar formato dos Dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d%m%Y', errors='coerce')  # errors=coerce é o que fazer se aconversão falhar o coerce faz com que caso a conversão falhe os valores nulos serão substituidos por NaT (Not a Time)


# Tratar Valores Duplicados
print('Qnt de registros atual: ', df.shape[0])
df.drop_duplicate()
df.drop_duplicate(subset='cpf', inplace=True)
print('Qnt de registros removendo as duplicadas: ', len(df))

print('Dados limpos:\n', df)


#   Salvar DataFrame
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereço', 'estado']]
df_salvar.to_csv('dados/clientes_limpeza.csv', inplace=True)

print('Novo dataframe: \n', pd.read_csv('dados/clientes_limpeza.csv'))



