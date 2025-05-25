# Este programa classifica a idade do usuário em categorias: Criança, Adolescente, Adulto ou Idoso.

# Solicita ao usuário que informe sua idade
idade = int(input("Informe sua idade: "))

# Verifica em qual faixa etária a idade se encaixa e exibe a categoria correspondente
if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade inválida. Por favor, informe um valor positivo.")

idade = int(input("Informe sua idade: "))

# Utilizando o novo recurso de pattern matching do Python 3.10+
match idade:
    case idade if 0 <= idade <= 12:
        print("Criança")
    case idade if 13 <= idade <= 17:
        print("Adolescente")
    case idade if 18 <= idade <= 59:
        print("Adulto")
    case idade if idade >= 60:
        print("Idoso")
    case _:
        print("Idade inválida. Por favor, informe um valor positivo.")