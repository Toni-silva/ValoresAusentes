# Análise de Valores Ausentes em Arquivo CSV

Este script Python (`valores_ausentes.py`) utiliza a biblioteca Pandas para analisar valores ausentes em um arquivo CSV.

## Pré-requisitos

* **Python 3.9** instalado.
* **Pandas** instalado. Você pode instalar usando o pip:

    ```bash
    pip install pandas
    ```

## Como Usar

1.  **Prepare o arquivo CSV:**
    * Certifique-se de que você tem um arquivo CSV chamado `indicadores.csv` (ou altere o nome da variável `nome_do_arquivo` no script para o nome do seu arquivo).
    * Coloque o arquivo CSV no mesmo diretório do script Python ou forneça o caminho completo para o arquivo.

2.  **Execute o script:**
    ```bash
    python valores_ausentes.py
    ```

## Funcionalidades

O script realiza as seguintes operações:

1.  **Lê o arquivo CSV:**
    * Tenta ler o arquivo CSV especificado usando `pd.read_csv()`.
    * Se o arquivo não for encontrado, exibe uma mensagem de erro e encerra a execução.

2.  **Identifica os valores ausentes:**
    * Utiliza `df.isna()` para criar um DataFrame booleano onde `True` indica um valor ausente e `False` indica um valor presente.

3.  **Conta os valores ausentes por coluna:**
    * Calcula a soma dos valores `True` (ausentes) em cada coluna usando `valores_ausentes.sum()` e exibe a contagem.

4.  **Filtra as linhas com valores ausentes:**
    * Seleciona e exibe todas as linhas que contêm pelo menos um valor ausente usando `df[df.isna().any(axis=1)]`.

5.  **Identifica as colunas com valores ausentes:**
    * Determina e exibe a lista de nomes das colunas que possuem pelo menos um valor ausente.

## Saída

O script imprime no console:

* A contagem de valores ausentes por coluna.
* As linhas que contêm valores ausentes.
* As colunas que possuem valores ausentes.

