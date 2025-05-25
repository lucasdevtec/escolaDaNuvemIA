# Este programa calcula o total a receber de um vendedor, considerando salário fixo e comissão de 15% sobre as vendas.

# Lê o nome do vendedor
nome = input("Digite o nome do vendedor: ")

# Lê o salário fixo
salario_fixo = float(input("Digite o salário fixo: "))

# Lê o total de vendas efetuadas no mês
total_vendas = float(input("Digite o total de vendas efetuadas no mês: "))

# Calcula a comissão (15% sobre o total de vendas)
comissao = total_vendas * 0.15

# Calcula o total a receber
total_receber = salario_fixo + comissao

# Exibe o resultado com duas casas decimais
print(f"TOTAL = R$ {total_receber:.2f}")