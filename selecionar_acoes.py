import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv("statusinvest-busca-avancada.csv", sep=";", decimal=",", index_col=False)

# Substituir valores nulos (NaN) por 0
df.fillna(0, inplace=True)

# Exibir as primeiras linhas do DataFrame para inspeção
print(df.head())