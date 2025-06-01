from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade de uma pessoa em dias, baseada no ano de nascimento.

    Parâmetros:
        ano_nascimento (int): O ano de nascimento da pessoa.

    Retorna:
        int: A idade aproximada em dias.
    """
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação, não considera anos bissextos
    return idade_dias

if __name__ == "__main__":
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (ex: 1990): "))
            ano_atual = date.today().year
            if ano_nascimento < 0 or ano_nascimento > ano_atual:
                print(f"O ano de nascimento deve ser entre 0 e {ano_atual}. Tente novamente.")
                continue
            idade_dias = calcular_idade_em_dias(ano_nascimento)
            print(f"Idade aproximada em dias: {idade_dias}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um ano válido.")