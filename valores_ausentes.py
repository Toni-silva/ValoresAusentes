import pandas as pd

# Nome do seu arquivo Excel
nome_do_arquivo = 'indicadores.csv'

# Lê o arquivo Excel
try:
    df = pd.read_csv(nome_do_arquivo)
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
    exit()

# Identifica os valores ausentes
valores_ausentes = df.isna()

# Conta os valores ausentes por coluna
contagem_ausentes_por_coluna = valores_ausentes.sum()
print("Contagem de valores ausentes por coluna:\n", contagem_ausentes_por_coluna)

# Filtra as linhas com valores ausentes
linhas_com_ausentes = df[df.isna().any(axis=1)]
print("\nLinhas com valores ausentes:\n", linhas_com_ausentes)

# Identifica as colunas com valores ausentes
colunas_com_ausentes = df.columns[df.isna().any()].tolist()
print("\nColunas com valores ausentes:", colunas_com_ausentes)