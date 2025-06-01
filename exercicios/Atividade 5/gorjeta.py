def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: O valor da gorjeta calculada.
    """
    return valor_conta * (porcentagem_gorjeta / 100)

if __name__ == "__main__":
    while True:
        try:
            valor_conta = float(input("Digite o valor total da conta: R$ "))
            if valor_conta < 0:
                print("O valor da conta não pode ser negativo. Tente novamente.")
                continue
            porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
            if porcentagem_gorjeta < 0:
                print("A porcentagem da gorjeta não pode ser negativa. Tente novamente.")
                continue
            gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
            print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")