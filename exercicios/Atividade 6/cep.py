import requests

def consultar_cep(cep: str) -> dict:
    """
    Consulta informações de endereço a partir de um CEP usando a API ViaCEP.

    Parâmetros:
        cep (str): CEP a ser consultado.

    Retorna:
        dict: Dicionário com logradouro, bairro, cidade e estado.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado.")
            return None
        return {
            "logradouro": dados.get("logradouro", ""),
            "bairro": dados.get("bairro", ""),
            "cidade": dados.get("localidade", ""),
            "estado": dados.get("uf", "")
        }
    except Exception as e:
        print(f"Erro ao consultar o CEP: {e}")
        return None

if __name__ == "__main__":
    while True:
        cep = input("Digite o CEP para consulta (somente números): ").strip()
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. Digite exatamente 8 números.")
            continue
        endereco = consultar_cep(cep)
        if endereco:
            print(f"Logradouro: {endereco['logradouro']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Cidade: {endereco['cidade']}")
            print(f"Estado: {endereco['estado']}")
        break