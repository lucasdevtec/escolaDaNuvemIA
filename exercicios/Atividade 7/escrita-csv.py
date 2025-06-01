import csv
from pathlib import Path

def escrever_csv(caminho_arquivo: str, dados: list):
    """
    Escreve dados pessoais em um arquivo CSV.

    Parâmetros:
        caminho_arquivo (str): Caminho do arquivo CSV.
        dados (list): Lista de dicionários com as chaves 'Nome', 'Idade' e 'Cidade'.
    """
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ['Nome', 'Idade', 'Cidade']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for pessoa in dados:
            escritor.writerow(pessoa)

if __name__ == "__main__":
    pessoas = [
        {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
        {"Nome": "Lucas", "Idade": 34, "Cidade": "Belo Horizonte"},
        {"Nome": "Marina", "Idade": 22, "Cidade": "Curitiba"}
    ]
    caminho = Path("exercicios/Atividade 7/escrita-csv-arquivo.csv")
    caminho.parent.mkdir(parents=True, exist_ok=True)
    escrever_csv(str(caminho), pessoas)
    print(f"Arquivo '{caminho}' criado com sucesso!")