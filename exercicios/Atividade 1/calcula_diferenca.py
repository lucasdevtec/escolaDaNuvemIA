def calcula_diferenca(num1, num2, num3, num4):
    """
    Calcula a diferença entre dois números produtos de 4 numeros.
    :param num1: Primeiro número (float)
    :param num2: Segundo número (float)
    :param num3: Terceiro número (float)
    :param num4: Quarto número (float)
    :return: Diferença entre o produto de num1 * num2 e o produto de num3 e num4 (float)
    """
    return num1 * num2 - num3 * num4

if __name__ == "__main__":
    try:
        print("A formula é a * b - c * d")
        num1 = float(input("Digite o número a: "))
        num2 = float(input("Digite o número b: "))
        num3 = float(input("Digite o número c: "))
        num4 = float(input("Digite o número d: "))
        print(f"A formula com os valores fornecidos é {num1} * {num2} - {num3} * {num4}")
        diferenca = calcula_diferenca(num1, num2, num3, num4)
        print(f"A diferença entre os números é {diferenca:.2f}")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")