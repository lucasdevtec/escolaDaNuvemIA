# Programa para verificar se uma senha é forte

import string

def senha_forte(senha):
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False
    if not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
        return False
    if not any(char.isalpha() for char in senha):
        print("A senha deve conter pelo menos uma letra.")
        return False
    if not any(char.isupper() for char in senha):
        print("A senha deve conter pelo menos uma letra maiúscula.")
        return False
    if not any(char in string.punctuation for char in senha):
        print("A senha deve conter pelo menos um caractere especial.")
        return False
    return True

while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ").strip()
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break
    if not senha:
        print("Senha vazia. Digite uma senha válida ou 'sair'.")
        continue
    try:
        if senha_forte(senha):
            print("Senha forte cadastrada com sucesso!")
            break
    except Exception as e:
        print(f"Ocorreu um erro: {e}")