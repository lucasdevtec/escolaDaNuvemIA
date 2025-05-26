# Programa para registrar notas de uma turma e calcular a média

def ler_nota():
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ").strip()
        if entrada.lower() == 'fim':
            return 'fim'
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número válido ou 'fim'.")

notas = []

while True:
    resultado = ler_nota()
    if resultado == 'fim':
        break
    else:
        notas.append(resultado)

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")