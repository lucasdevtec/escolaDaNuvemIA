numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"NÚMERO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")