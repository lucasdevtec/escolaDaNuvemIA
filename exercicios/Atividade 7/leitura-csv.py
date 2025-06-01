import csv

def ler_csv(caminho_arquivo: str):
    """
    Lê um arquivo CSV e exibe os dados na tela.

    Parâmetros:
        caminho_arquivo (str): Caminho do arquivo CSV.
    """
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            nome = linha.get('Nome', '')
            idade = linha.get('Idade', '')
            cidade = linha.get('Cidade', '')
            print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

if __name__ == "__main__":
    caminho = "exercicios/Atividade 7/escrita-csv-arquivo.csv"
    ler_csv(caminho)