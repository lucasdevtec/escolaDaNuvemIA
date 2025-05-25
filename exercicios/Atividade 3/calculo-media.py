# Este programa calcula a média ponderada de quatro notas e determina a situação do aluno.
# As notas são lidas do usuário, e a média é calculada com pesos específicos.
# O programa também verifica se o aluno está aprovado, reprovado ou em exame,
# e, se necessário, lê a nota do exame para calcular a média final.
# O programa utiliza tratamento de exceções para garantir que as entradas sejam válidas
# e que as notas estejam dentro do intervalo permitido (0.0 a 10.0).

# Função de leitura das quatro notas do aluno, cada uma com uma casa decimal 
# e com validação para garantir que estejam entre 0.0 e 10.0
# e tratamento de exceções para entradas inválidas
def ler_notas():
    while True:
        try:
            notas = input("Digite as 4 notas do aluno em ordem separadas por espaço: ").split()
            if len(notas) != 4:
                print("Por favor, digite exatamente 4 notas.")
                continue
            N1, N2, N3, N4 = map(float, notas)
            # Verifica se todas as notas estão no intervalo de 0.0 a 10.0 usando uma lista de compreensão(list comprehension) = Apanhei para aprender isso lkkkk fazer normalmente ficaria grande d+
            if not all(0.0 <= n <= 10.0 for n in [N1, N2, N3, N4]):
                print("As notas devem estar entre 0.0 e 10.0.")
                continue
            return N1, N2, N3, N4
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números válidos.")

# Função de leitura da nota do exame, com validação para garantir que esteja entre 0.0 e 10.0
# e tratamento de exceções para entradas inválidas
def ler_nota_exame():
    while True:
        try:
            nota = float(input())
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print("A nota do exame deve estar entre 0.0 e 10.0.")
        except ValueError:
            print("Entrada inválida. Digite um número válido para a nota do exame.")

N1, N2, N3, N4 = ler_notas()

# Calcula a média ponderada - {2, 3, 4, 1} são os pesos das notas
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    print("Informe a nota do exame: ")
    nota_exame = ler_nota_exame()
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")