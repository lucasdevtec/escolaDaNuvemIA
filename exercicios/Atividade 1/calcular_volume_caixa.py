def calcular_volume_caixa(comprimento, largura, altura):
    """
    Calcula o volume de uma caixa retangular.
    :param comprimento: Comprimento da caixa (float)
    :param largura: Largura da caixa (float)
    :param altura: Altura da caixa (float)
    :return: Volume da caixa (float)
    """
    return comprimento * largura * altura

if __name__ == "__main__":
    try:
        comprimento = float(input("Digite o comprimento da caixa (em metros): "))
        largura = float(input("Digite a largura da caixa (em metros): "))
        altura = float(input("Digite a altura da caixa (em metros): "))
        volume = calcular_volume_caixa(comprimento, largura, altura)
        print(f"O volume da caixa é {volume:.2f} metros cúbicos.")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")