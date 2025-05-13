import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv("statusinvest-busca-avancada.csv", sep=";", decimal=",", index_col=False)

# Substituir valores nulos (NaN) por 0
df.fillna(0, inplace=True)

# Converter colunas para números para evitar erro de comparação
colunas_numericas = ["P/L", "ROE", "DY", "DIV. LIQ. / PATRI."]
for coluna in colunas_numericas:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce").fillna(0)

# Definir critérios de análise fundamentalista
def analise_fundamentalista(linha):
    score = 0
    try:
        if linha["P/L"] < 15:  # Preço/Lucro baixo pode indicar bom valor
            score += 2
        if linha["ROE"] > 15:  # Retorno sobre patrimônio líquido elevado é positivo
            score += 3
        if linha["DY"] > 5:  # Dividend Yield acima de 5% pode ser atraente
            score += 2
        if linha["DIV. LIQ. / PATRI."] < 1:  # Baixa alavancagem é um bom sinal
            score += 2
    except KeyError:
        pass  # Ignorar caso alguma coluna não exista no CSV
    return score

# Aplicar análise linha por linha e criar novo DataFrame com ranking
df["Score"] = df.apply(analise_fundamentalista, axis=1)
df_ranked = df.sort_values(by="Score", ascending=False).reset_index(drop=True)

# Exibir o DataFrame resultante
print(df_ranked)

