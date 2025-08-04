import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)  # aqui colocamos o display com o maximo da largura da COLUNA

df = pd.read_csv('dados/clientes_remove_outliers.csv')  # Leitura do arquivo

print(df.head())

#  Mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')  # criamos um novo campo no dataframe chamado cpf_mascara onde aplicamos a função lambda mostrando apenas os 3 primeiros e os 2 ultimos digitos, aqui trabalhamos o cpf como uma string


#  Corrigir Datas
df['data'] = pd.to_datetime(df['data'], format= '%Y-%m-%d', errors= 'coerce')
   # Aqui estamos convertendo a coluna 'data' para o tipo datetime para que o computador possa entender os valores como datas. Usamos o parâmetro format='%Y-%m-%d' para indicar o padrão ano-mês-dia. Com errors='coerce', qualquer valor que não conseguir ser convertido corretamente será substituído por NaT (Not a Time), que representa um valor nulo para datas.

data_atual = pd.to_datetime('today')   # criamos a variavel data_atual e com a função pd.to_datetime('today') obtém a data atual do sistema e a converte para o tipo datetime.
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
#Aqui criamos um novo campo no DataFrame chamado data_atualizada. Usamos um filtro com where para manter as datas que são menores ou iguais à data atual.
#Se a data for maior que a data atual (ou seja, estiver no futuro), ela será substituída por 1900-01-01.
#df['data'] <= data_atual: retorna True para todas as datas que são menores ou iguais à data atual (ou seja, estão no passado ou são hoje).

#where(condição, valor_substituto):
#Mantém os valores da coluna 'data' onde a condição é verdadeira.
#Substitui com o valor indicado (1900-01-01) onde a condição é falsa (ou seja, quando a data está no futuro).

df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
# data_atual.year: pega apenas o ano da data atual(do dia de hoje)
# df['data_atualizada'].dt.year: extrai o ano de cada data na coluna data_atualizada
# A subtração calcula a diferença de anos, ou seja, uma idade aproximada (não leva em conta mês e dia).
# Aqui estamos criando a coluna 'idade_ajustada', que calcula a idade aproximada com base no ano da data atual e o ano da data na coluna 'data_atualizada'
# Essa forma de calcular a idade ignora mês e dia, então a idade pode estar errada por até 1 ano dependendo da data de aniversário

df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
# verifica se a data de aniversário ainda não chegou neste ano
# O mês de nascimento é maior que o mês atual, ou
# O mês é igual, mas o dia ainda não chegou.
# O resultado dessa verificação é um valor booleano (True ou False) por linha.
# O -= subtrai 1 da idade onde a pessoa ainda não fez aniversário neste ano,
# Esse comando ajusta a idade calculada anteriormente, verificando se a pessoa já fez aniversário neste ano. Se ainda não fez (com base no mês e no dia), subtraímos 1 da idade.
# O resultado é uma idade mais precisa.
# A conversão booleana para inteiro (True vira 1, False vira 0) permite fazer a subtração diretamente.

df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan
# df['idade_ajustada'] > 100: identifica as linhas onde a idade calculada ultrapassa 100 anos
# df.loc[condição, coluna] = valor: aplica a substituição somente onde a condição for verdadeira.
# np.nan: atribui um valor nulo (NaN) à célula — útil para sinalizar que os dados são inválidos ou suspeitos.
# qui, verificamos se a idade ajustada é maior que 100 anos. Se for, substituímos o valor por NaN (valor nulo), assumindo que provavelmente há um erro ou inconsistência nos dados.


# Corrigir a Formatação de Endereço
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
# f['endereco']: Seleciona a coluna chamada "endereco" do DataFrame.
# .apply(lambda x: ...): Aplica uma função a cada valor da coluna (cada linha da coluna "endereco" é passada como x)
# x.split('\n'): Divide o texto da célula em uma lista, usando a quebra de linha (\n) como separador.
# [0]: Pega o primeiro item da lista, ou seja, a primeira linha antes da quebra \n.
# .strip(): Remove espaços em branco no início e no fim dessa linha.
# Criamos uma nova coluna chamada endereco_curto, que recebe apenas a primeira linha do conteúdo da coluna endereco
# , separando pelo caractere de quebra de linha (\n) e removendo espaços em branco no início e fim da string.

df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
# x.split('\n'): Divide o texto da célula em uma lista de strings, separadas por quebras de linha (\n).
# [1]: Pega o segundo item da lista (índice 1), que normalmente corresponde ao bairro, se ele existir
# if len(x.split('\n')) > 1: Garante que existe pelo menos uma segunda linha na string (ou seja, que o índice 1 existe na lista).
# .strip(): Remove espaços em branco do início e fim do bairro.
# else 'Desconhecido': Se não houver segunda linha (ou seja, não tem bairro informado), insere a string "Desconhecido"
# Criamos uma nova coluna chamada 'bairro', onde aplicamos uma função lambda que divide o texto da coluna 'endereco' por quebras de linha (\n).
# Se existir uma segunda linha (índice 1), ela será usada como o bairro, com espaços removidos. Caso contrário, será inserido o valor 'Desconhecido'

df['estado_sigla'] = df['endereco'].apply(lambda x: x.split(' / ')[-1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
# x.split('\n') dentro do if: Está checando se o endereço tem ao menos duas linhas (como vimos antes).Ou seja, só vamos tentar extrair o estado se houver mais de uma linha no endereço
# x.split(' / ')[-1]: x.split(' / '): divide a string sempre que encontrar " / " (espaço + barra + espaço), que geralmente separa cidade e estado.
# [-1]: em Python, o índice -1 significa “último item da lista”.
# .strip(): Remove espaços em branco antes ou depois do texto — por exemplo, " SP" vira "SP".
# else 'Desconhecido': Se o endereço não tiver pelo menos duas linhas, consideramos a informação incompleta e marcamos como 'Desconhecido'.
#  Criamos uma nova coluna chamada 'estado_sigla'. Verificamos se o endereço tem mais de uma linha usando x.split('\n').
#  Se tiver, usamos x.split(' / ')[-1] para pegar a última parte da string após o separador ' / ', que geralmente representa a sigla do estado. Removemos espaços extras com .strip(). Se não houver múltiplas linhas, retornamos 'Desconhecido'


#  Verificando a formatação do endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço Inválido' if len(x) > 50 or len(x) < 5 else x)
# O comando verifica o comprimento do endereço curto(coluna que criamos anteriormente), verificamos o comprimento dele com len(x) e se ele for muito curto (< 5) ou muito longo (> 50) , assume que é provavelmente inválido e substitui por 'Endereço Inválido'.


#  Corrigir Dados Erroneos
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'CPF inválido')
# estamos verificando o comprimento do campo cpf com o len com a condição de que se for igual a 14 caracteres(contando pontos, hifen e tudo mais) mantem o cpf caso contrario substitui por cpf invalido

estados_br = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estados_sigla'] = df['estados_sigla'].str.upper().apply(lambda x: x if x in estados_br else 'Desconhecido')
# estados_br: é a lista com todas as siglas válidas dos estados brasileiros.
# df['estados_sigla'].str.upper(): Converte todas as siglas da coluna para letras maiúsculas, garantindo a comparação correta, caso haja algum escrito em minusculo
# .apply(lambda x: x if x in estados_br else 'Desconhecido'): Aplica uma função a cada valor da coluna.
# Se o valor estiver dentro da lista estados_br, ele é mantido.
# Caso contrário, é substituído por 'Desconhecido'.
#  primeiro criamos a variavel contendo as siglas dos estados br e depois pegamos a coluna estados_sigla no nosso DF, que recebe o nome da mesma coluna e aplicamos a função nas linhas dessa coluna que é: caso o estado sigla estiver com o valor atribuido com algum valor da lista estados br é verdadeiro e mantem caso contrario sera substituido por desconhecido

# Renomeando os campos com os novos campos criados
df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']
df_salvar = df[['nome', 'cpf', 'idade', 'endereco', 'bairro', 'estado']]
df_salvar.to_csv('dados/clientes_tratados', index=False)




