import pandas as pd

# Definindo URL
url = "https://sistemaswebb3-listados.b3.com.br/marketDataProxy/MarketDataCall/GetDownloadMarketData/RELATORIO_DADOS_DE_MERCADO.csv"

# Obtendo dados
df_relatorio = pd.read_csv(url,                 # URL ou caminho do arquivo .csv
					sep = ";",                # Separador de tabulação
					decimal = ",",            # Símbolo de decimal
					encoding = "ISO-8859-1",  # Codificação (específico em cada caso)
					skiprows = 4,             # Pulando as primeiras x linhas
					nrows = 10)               # Considerando apenas até a linha y

# Resultado (tabela)
print(df_relatorio)