import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico','Engenheiro', 'Estudante','Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000','15000', '1200','1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000','2000', '500','250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0','1', '0','1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento','Solteiro', 'Solteiro','Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1','1', '0','0']
}

df = pd.DataFrame(data)
df.head(5)




#  GRÁFICO DE BARRAS SOBRE  A MÉDIA DE CRÉDITO POR PROFISSÃO

df['Limite_Credito'] = pd.to_numeric(df['Limite_Credito'])    #converter a variavel em numerica
limite_por_profissao = df.groupby('Profissão')['Limite_Credito'].mean().reset_index()

#   Criação do Gráfico
fig = px.bar(limite_por_profissao, x= 'Profissão', y= 'Limite_Credito', title= 'Média de Crédito Por Profissão', labels= {'Profissão': 'Profissão', 'Limite_Credito': 'Média do Limite'})
fig.show()

# Análise Sobre o Gráfico
#  A escolha foi uma escolha simples, porém efetiva para saber quais profissões possuem os maiores limites de créditos
#  Acredito que a profissão seja determinante para definir um limite de crédito, pois acaba mostrando uma vida financeira estável e até mesmo o banco pode ter mais confiança em algumaS das profissões


#   GRÁFICO DE DISPERSÃO SOBRE SALÁRIO VS LIMITE DE CRÉDITO
df['Salário'] = pd.to_numeric(df['Salário'])    # Convertendo  variavel em numerica


# Convertendo Salário para numérico, se ainda não estiver
df['Salário'] = pd.to_numeric(df['Salário'])

#  Criando o Gráfico
sns.scatterplot(data=df, x='Salário', y='Limite_Credito', hue='Profissão', alpha=0.7, edgecolor='black')   #hue='Profissão', faz com que cada profissão apareça com uma cor diferente no gráfico

#  Criando Linha de Tendência
sns.regplot(data=df, x='Salário', y='Limite_Credito', scatter=False, color='gray', line_kws={'linestyle': 'dashed'}, ci=None)

plt.title('Relação entre Salário e Limite de Crédito')
plt.xlabel('Salário')
plt.ylabel('Limite de Crédito')
plt.legend(title='Profissão', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

#  Analise do gráfico
#   Com esse gráfico podemos visualizar o seguinte fato: pessoas com salários mais altos tendem a ter um limite de crédito alto
#   Isso indica que o salário é um valor determinante para o limite de crédito
#   No gráfico temos duas exceções: pessoas com salário alto, porém com baixo limite de crédito, mas isso deve ser a algum problema financeiro do passado
#   A Linha de Tendência mostra a relação positiva entre salário e limite de crédito



#  Criando o Gráfico de Barras correlacionando Histórico de Inadimplência por Limite de Crédito

# Covertendo as variaveis para numerica
df['Limite_Credito'] = pd.to_numeric(df['Limite_Credito'])
df['Historico_Inadimplencia'] = df['Historico_Inadimplencia'].astype(int)

# Media do limite de crédito pelo histórico de inadimplencia
media_limite_inadimplencia = df.groupby('Historico_Inadimplencia')['Limite_Credito'].mean()


plt.figure(figsize=(8, 6))
bars = plt.bar(media_limite_inadimplencia.index.astype(str), media_limite_inadimplencia, color='skyblue')

#  Plotando os rotulos em em cima das barrs
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('Média do Limite de Crédito pelo Historico de Inadimplencia', fontsize=16)
plt.xlabel('Histórico de Inadimplência (0 = Não, 1 = Sim)', fontsize=12)
plt.ylabel('Média do Limite de Crédito', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#   Analise do gráfico
#   No gráfico podemos ver claramente que a média do limite de crédito é maior para pessoas SEM histórico de inadimplência (Grupo 0), comparado as que possuem histórico (Grupo 1 )
#   Histórico de inadimplência é definitivamente um fator importantíssimo para a definição do limite de crédito