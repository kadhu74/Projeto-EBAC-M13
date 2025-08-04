#  aplicar técnicas de engenharia de features, como transformação logarítmica, normalização e contagem de frequência, para melhorar o desempenho dos modelos analíticos

import pandas as pd
import numpy as np
from scipy import stats


pd.set_option('display.width', None)

df = pd.read_csv('dados/clientes-v2-tratados.csv')

print(df.head())

#  Transformação Logarítimica

df['salario_log'] = np.log1p(df['salario'])  # log1p é usado para evitar problemas com valores zero


print('\n DataFrame após a transformação logarítimica no salario:\n', df.head())


#  Transformação Box-Cox

df['salario_boxcox'],_ = stats.boxcox(df['salario'] + 1)  # o + 1 e para caso tenha um valor negativo como -1 ira somar e transformalo em um numero inteiro

print('\nDataFrame após a transformação BoxCox no salario:\n', df.head())


#  Codificação de frequencia nos estados


estado_freq = df['estado'].value_counts() / len(df)  # trabalha com porcentagem
df['estado_freq'] = df['estado'].map(estado_freq)

print('\nDataFrame após a codificação de frequencia para estado:\n', df.head())


# Interações

df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']

print('\nDataFrame após a criação de interações entre idade e numero filho'
      's:\n', df.head())