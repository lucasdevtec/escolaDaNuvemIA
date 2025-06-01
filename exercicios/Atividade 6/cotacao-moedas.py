import requests

def consultar_cotacao(moeda: str) -> dict:
    """
    Consulta a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL)
    usando a API AwesomeAPI.

    Parâmetros:
        moeda (str): Código da moeda estrangeira (ex: USD, EUR, GBP).

    Retorna:
        dict: Dicionário com valor atual, máximo, mínimo, data e hora da última atualização.
    """
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada ou código inválido.")
            return None
        info = dados[chave]
        return {
            "valor_atual": info.get("bid"),
            "maximo": info.get("high"),
            "minimo": info.get("low"),
            "data_hora": f"{info.get('create_date')}"
        }
    except Exception as e:
        print(f"Erro ao consultar a cotação: {e}")
        return None

if __name__ == "__main__":
    while True:
        moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()
        if not moeda.isalpha() or len(moeda) != 3:
            print("Código de moeda inválido. Digite um código com 3 letras.")
            continue
        cotacao = consultar_cotacao(moeda)
        if cotacao:
            print(f"Valor atual: R$ {cotacao['valor_atual']}")
            print(f"Valor máximo: R$ {cotacao['maximo']}")
            print(f"Valor mínimo: R$ {cotacao['minimo']}")
            print(f"Data e hora da última atualização: {cotacao['data_hora']}")
        break