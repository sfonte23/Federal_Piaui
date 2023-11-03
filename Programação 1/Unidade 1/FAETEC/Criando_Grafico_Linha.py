# Carregando pacotes
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definindo abreviação (ticker)
ticker = ["PETR4.SA"]  # Petrobras SA

# Obtendo dados
df_acao = yf.download(ticker,                # Ação
                      start="2023-01-01",    # Data inicial AAAA-MM-DD
                      end="2023-04-01")      # Data final AAAA-MM-DD

# Selecionando a coluna `Adj Close` pelo rótulo
df_acao = df_acao.loc[:, ['Adj Close']]

# Renomeando coluna
df_acao.columns = ['PETR4.SA']

# Criando o gráfico
df_acao.plot(marker='x', linestyle='--', color='green')

# Adicionando:
plt.title('Valores de fechamento') # Título
plt.xlabel('Data')                 # Rótulo do eixo horizontal (x)
plt.ylabel('Valor (R$)')           # Rótulo do eixo vertical (y)

# Exibindo o gráfico
plt.show()