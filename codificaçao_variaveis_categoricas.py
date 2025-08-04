#  implementar a codificação de variáveis categóricas, transformando dados textuais em dados numéricos para uso em algoritmos de aprendizado de máquina
#  transformamos os dados de textos em números, suponhamos que tu queira fazer um calculo matematico de um campo, mas se contem um texto nao tem como fazer esse calculo




import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('dados/clientes-v2-tratados.csv')

print(df.head())


#  Codificação one-hot para 'estado-civil' = transforma as variaveis categoricas em valores numéricos para que possam ser usadas em modelos de Machine Learning
#  A ideia é transformar cada categoria em uma coluna biária (0 ou 1), onde 1 indica a PRESENÇA e 0 a AUSÊNCIA

df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)  #axis=1 é coluna linha seria axis=0
#  pd.get_dummies(df['estado_civil'], prefix='estado_civil')
# Essa parte transforma a coluna estado_civil em várias colunas binárias (0 ou 1), uma para cada valor diferente encontrado
#  pd.concat([...], axis=1)
# O pd.concat junta (concatena) o DataFrame original df com o resultado da codificação.
# O axis=1 indica que a junção será feita por colunas (lado a lado), não por linhas.
# df = ...
# Atualiza o próprio DataFrame df com a versão modificada.

print('\nDataFrame após codificação one-hot para estado_civil:\n', df.head())

# Codificação Ordinal para 'nivel_educação'
#  A codificação ordinal converte valores categóricos em números inteiros, preservando a ordem natural entre as categorias.
# diferença entra One-Hot para Ordinal: One-Hot transforma cada categoria em uma COLUNA SEPARADA(sem ordem)
#  Ordinal transforma cada categoria em um NUMERO INTEIRO, respeitando a ordem
#  Importante: só use Ordinal Encoding quando a ordem fizer sentido lógico
#  Se não houver ordem lógica (como nomes de cidades, cores, etc.), não use codificação ordinal — use One-Hot.

educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-Graduação': 4}  # Essa ordem faz sentido lógico e hierárquico, o que é essencial em codificação ordinal
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)  # O método .map() substitui cada valor da coluna original pelo número correspondente no dicionário.
#  Cria uma nova coluna chamada nivel_educacao_ordinal com os valores numéricos codificados

print('\n DataFrame após codificação ordinal para nivel_educação: \n', df.head())


# Transformar 'area_atuacao' em categorias codificadas usando o método .cat.codes
#  o método .cat.codes, que é mais uma forma de fazer codificação ordinal automática usando o tipo category do pandas.
#  É um método do pandas que converte uma coluna categórica (category) em números inteiros, atribuindo um código numérico para cada categoria automaticamente.
#  Se você não definir a ordem das categorias, o pandas usa ordem alfabética, que pode não representar a ordem lógica correta.

df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print('\n DataFrame após transformar area_atuacao em códigos numéricos:\n', df.head())


#  LabelEncorder para 'estado'
#  LabelEncorder converte cada valor unico em numeros de 0 a n_classes-1
#  O LabelEncoder converte valores categóricos (strings) em valores numéricos (inteiros).
#  Use quando você tem uma coluna com rótulos (labels) e precisa transformá-los em números para treinar modelos
#  Importante: o LabelEncoder não preserva uma ordem lógica, apenas atribui um número para cada categoria com base na ordem em que aparecem (ou ordem alfabética).
#  O modelo pode interpretar essas categorias como se tivessem ordem ou distância (ex: "masculino = 2" > "outro = 1"), mesmo que não tenha.
#  Por isso, não use LabelEncoder em variáveis categóricas nominais (sem ordem), como cor, cidade, sexo — nesses casos prefira One-Hot
#Mas ele pode ser útil para variáveis como rótulos de classes em problemas de classificação (ex: bom, médio, ruim → 2, 1, 0).


label_encorder = LabelEncoder()  # um método da biblioteca scikit-learn usado para transformar variáveis categóricas em números
df['estado_cod'] = label_encorder.fit_transform(df['estado'])

print('\nDataFrame após aplicar LabelEncorder em estado:\n', df.head())

