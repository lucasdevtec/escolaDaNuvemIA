# Este programa calcula o Índice de Massa Corporal (IMC) de uma pessoa e informa a classificação correspondente.

# Solicita ao usuário o peso em quilogramas
peso = float(input("Informe seu peso em kg: "))

# Solicita ao usuário a altura em metros
altura = float(input("Informe sua altura em metros: "))

# Calcula o IMC usando a fórmula: IMC = peso / (altura * altura)
imc = peso / (altura ** 2)

# Classifica o IMC de acordo com a tabela padrão
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibe o resultado com duas casas decimais e a classificação
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")