import pandas as pd

# Ler os dados de reserva
df = pd.read_csv("reservas.csv")

# Calcular a distribuição de receitas
for index, row in df.iterrows():
    receita_proprietario = (1 - row["porcentagem_comissao"]) * row["receita"]
    receita_anfitriao = row["porcentagem_comissao"] * row["receita"]

    df.loc[index, "receita_proprietario"] = receita_proprietario
    df.loc[index, "receita_anfitriao"] = receita_anfitriao

# Gerar a distribuição de receita calculada
df.to_csv("receitas.csv")