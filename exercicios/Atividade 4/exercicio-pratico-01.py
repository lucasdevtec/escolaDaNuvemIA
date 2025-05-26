# Calculadora que realiza as quatro operações básicas com tratamento de erros

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, * ou /): ").strip()

        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida. Tente novamente.")
            continue

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                continue
            resultado = num1 / num2

        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        break

    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")