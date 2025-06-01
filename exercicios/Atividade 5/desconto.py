def calcular_preco_final(preco_original: float, percentual_desconto: float) -> float:
    """
    Calcula o preço final de um produto após aplicar o desconto.

    Parâmetros:
        preco_original (float): O preço original do produto.
        percentual_desconto (float): O percentual de desconto (ex: 10 para 10%).

    Retorna:
        float: O preço final do produto após o desconto.
    """
    desconto = preco_original * (percentual_desconto / 100)
    return preco_original - desconto

if __name__ == "__main__":
    while True:
        try:
            preco_original = float(input("Digite o preço original do produto: R$ "))
            if preco_original < 0:
                print("O preço do produto não pode ser negativo. Tente novamente.")
                continue
            percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
            if percentual_desconto < 0 or percentual_desconto > 100:
                print("O percentual de desconto deve estar entre 0 e 100. Tente novamente.")
                continue
            preco_final = calcular_preco_final(preco_original, percentual_desconto)
            print(f"Preço final com desconto: R$ {preco_final:.2f}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")