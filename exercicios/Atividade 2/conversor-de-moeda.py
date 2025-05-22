def converter_moeda(valor_reais, taxa):
    """
    Converte o valor em reais para outra moeda usando a taxa informada.
    :param valor_reais: Valor em reais (float)
    :param taxa: Taxa de conversão (float)
    :return: Valor convertido (float)
    """
    return round(valor_reais / taxa, 2)

if __name__ == "__main__":
    valor_reais = 100.00
    taxa_dolar = 5.20
    taxa_euro = 6.15

    valor_dolar = converter_moeda(valor_reais, taxa_dolar)
    valor_euro = converter_moeda(valor_reais, taxa_euro)

    print(f"Valor em reais: R$ {valor_reais:.2f}")
    print(f"Valor em dólares: US$ {valor_dolar:.2f}")
    print(f"Valor em euros: € {valor_euro:.2f}")