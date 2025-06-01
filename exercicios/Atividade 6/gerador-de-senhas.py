import random
import string

def gerar_senha_aleatoria(tamanho: int) -> str:
    """
    Gera uma senha aleatória com pelo menos uma letra minúscula, uma maiúscula,
    um número e um caractere especial.

    Parâmetros:
        tamanho (int): Quantidade de caracteres da senha.

    Retorna:
        str: Senha aleatória gerada.
    """
    if tamanho < 12:
        raise ValueError("O tamanho mínimo da senha deve ser 12.")

    # Garante pelo menos um de cada tipo
    senha = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    # Preenche o restante
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha += [random.choice(caracteres) for _ in range(tamanho - 4)]
    random.shuffle(senha)
    return ''.join(senha)

def validar_senha(senha: str) -> list:
    faltando = []
    if not any(c.islower() for c in senha):
        faltando.append("uma letra minúscula")
    if not any(c.isupper() for c in senha):
        faltando.append("uma letra maiúscula")
    if not any(c.isdigit() for c in senha):
        faltando.append("um número")
    if not any(c in string.punctuation for c in senha):
        faltando.append("um caractere especial")
    if len(senha) < 12:
        faltando.append("tamanho mínimo de 12 caracteres")
    return faltando

if __name__ == "__main__":
    while True:
        try:
            tamanho = int(input("Informe a quantidade de caracteres da senha aleatória (mínimo 12): "))
            if tamanho < 12:
                print("A quantidade de caracteres deve ser pelo menos 12. Tente novamente.")
                continue
            senha = gerar_senha_aleatoria(tamanho)
            faltando = validar_senha(senha)
            print(f"Senha aleatória gerada: {senha}")
            if faltando:
                print("A senha gerada não atende aos seguintes requisitos:")
                for item in faltando:
                    print(f"- Falta {item}")
            else:
                print("A senha atende a todos os requisitos de segurança.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")