import json

def escrever_json(caminho_arquivo: str, pessoa: dict):
    """
    Escreve os dados de uma pessoa em um arquivo JSON.

    Parâmetros:
        caminho_arquivo (str): Caminho do arquivo JSON.
        pessoa (dict): Dicionário com os campos 'nome', 'idade' e 'cidade'.
    """
    with open(caminho_arquivo, mode='w', encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

def ler_json(caminho_arquivo: str) -> dict:
    """
    Lê os dados de uma pessoa de um arquivo JSON.

    Parâmetros:
        caminho_arquivo (str): Caminho do arquivo JSON.

    Retorna:
        dict: Dicionário com os campos 'nome', 'idade' e 'cidade'.
    """
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

if __name__ == "__main__":
    pessoa = {
        "nome": "Lucas",
        "idade": 30,
        "cidade": "Porto Alegre"
    }
    caminho = "exercicios/Atividade 7/leitura-e-escrita-JSON-arquivo.json"
    escrever_json(caminho, pessoa)
    print("Dados escritos no JSON.")

    dados_lidos = ler_json(caminho)
    print("Dados lidos do JSON:")
    print(f"Nome: {dados_lidos['nome']}, Idade: {dados_lidos['idade']}, Cidade: {dados_lidos['cidade']}")