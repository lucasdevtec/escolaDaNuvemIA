def calcular_preco_cadeira(tipo, preco, qtd):
    """
    Calcula o preco de uma cadeira.
    :param tipo: Tipo da cadeira (string)
    :param preco: Preco da cadeira (float)
    :param qtd: Quantidade da cadeira (Int)
    :return: Texto descritivo do preço da cadeira (string)
    """
    return f"O preço da cadeira - {tipo} é R$ {(preco*qtd):.2f}."

if __name__ == "__main__":
    try:
        tipo = input("Digite o tipo da Cadeira: ")
        preco = float(input("Digite o preço da cadeira (em reais): "))
        qtd = int(input("Digite a quantidades de cadeiras: "))
        resultado = calcular_preco_cadeira(tipo, preco, qtd)
        print(resultado)
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")