import pandas as pd

# A expressão lambda é uma forma de escrever uma função em apenas uma linha, então não precisa definir a função, você usa a expressão lambda pra fazer a função diretamente nela


# função para calcular o cubo de um número
def eleva_cubo(x):
    return x ** 3

#expressão de lambda para calcular o cubo de um número
eleva_cubo_lambda = lambda x: x ** 3

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]})

df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)  #  a função apply serve para aplicar uma função um map, lambda, não precisa especificar o argumento, pois como ja esta dentro do dataframe não precisa criar um for
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3) # usamos lambda quanto temos operações simples
print(df)

