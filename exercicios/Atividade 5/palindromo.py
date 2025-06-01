import string

def eh_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    Parâmetros:
        texto (str): Palavra ou frase a ser verificada.

    Retorna:
        str: "Sim" se for palíndromo, "Não" caso contrário.
    """
    texto_limpo = ''.join(
        c.lower() for c in texto if c.isalnum()
    )
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

if __name__ == "__main__":
    while True:
        texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
        if not texto.strip():
            print("Entrada vazia. Por favor, digite uma palavra ou frase.")
            continue
        resultado = eh_palindromo(texto)
        print(f"É palíndromo? {resultado}")
        break