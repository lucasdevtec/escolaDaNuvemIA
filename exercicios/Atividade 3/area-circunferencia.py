# Este programa calcula a área de uma circunferência a partir do valor do raio informado pelo usuário.
# A fórmula utilizada é: área = π * raio^2
# Para este cálculo, vamos considerar π como 3.14159265

# Solicita ao usuário que informe o valor do raio da circunferência
raio = float(input("Informe o valor do raio da circunferência: "))

# Define o valor de π conforme especificado no enunciado
pi = 3.14159265

# Calcula a área elevando o raio ao quadrado e multiplicando por π
area = pi * (raio ** 2)

# Exibe o resultado formatado com 4 casas decimais, conforme solicitado
print(f"A={area:.4f}")
