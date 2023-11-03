# Carregando pacote
import yfinance as yf

# Definindo abreviação (ticker)
acao_ticker = ["PETR4.SA"]  # Petrobras

# Obtendo dados
df_acao = yf.download(acao_ticker,           # Ação
                      start="2023-01-01",    # Data inicial AAAA-MM-DD
                      end="2023-08-01")      # Data final AAAA-MM-DD

# Resultado (tabela)
print(df_acao)