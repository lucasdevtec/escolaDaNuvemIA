import re
import statistics

def extrair_tempos_execucao(caminho_arquivo: str) -> list:
    """
    Lê um arquivo de log e extrai os tempos de execução dos treinamentos.

    Parâmetros:
        caminho_arquivo (str): Caminho para o arquivo de log.

    Retorna:
        list: Lista de tempos de execução em segundos (float).
    """
    tempos = []
    padrao = re.compile(r"tempo de execução\s*[:=]\s*([\d.,]+)", re.IGNORECASE)
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            match = padrao.search(linha)
            if match:
                tempo_str = match.group(1).replace(",", ".")
                try:
                    tempos.append(float(tempo_str))
                except ValueError:
                    continue
    return tempos

def calcular_media_desvio(tempos: list) -> tuple:
    """
    Calcula a média e o desvio padrão de uma lista de tempos.

    Parâmetros:
        tempos (list): Lista de tempos (float).

    Retorna:
        tuple: (média, desvio padrão)
    """
    if not tempos:
        return (0, 0)
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0
    return (media, desvio)

if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo de log: ").strip()
    tempos = extrair_tempos_execucao(caminho)
    if tempos:
        media, desvio = calcular_media_desvio(tempos)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio:.2f} segundos")
    else:
        print("Nenhum tempo de execução encontrado no arquivo.")