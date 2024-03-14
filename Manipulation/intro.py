import pandas as pd

# Lendo os dados da Tabela.
dados = pd.read_csv("../Data/ratings.csv")

# Dados da Tabela.
user_id = dados["userId"]
movie_id = dados["movieId"]
rating = dados["rating"]
timestamp = dados["timestamp"]

print(dados)
