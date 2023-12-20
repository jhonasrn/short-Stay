from flask import Flask

app = Flask(__name__)

@app.route("/receitas/<propriedade_id>", methods=["GET"])
def get_receitas(propriedade_id):
    # Ler os dados de reserva
    df = pd.read_csv("reservas.csv")

    # Filtrar os dados pela propriedade especificada
    df = df[df["id_propriedade"] == propriedade_id]

    # Calcular a distribuição de receitas
    receita_proprietario = (1 - df["porcentagem_comissao"]) * df["receita"]
    receita_anfitriao = df["porcentagem_comissao"] * df["receita"]

    # Retornar a distribuição de receitas
    return {
        "propriedade_id": propriedade_id,
        "receita_proprietario": receita_proprietario,
        "receita_anfitriao": receita_anfitriao,
    }