# Este programa converte temperaturas entre Celsius, Fahrenheit e Kelvin.

def converter_temperatura(valor, origem, destino):
    # Converte a temperatura para Celsius primeiro
    if origem == "C":
        temp_c = valor
    elif origem == "F":
        temp_c = (valor - 32) * 5/9
    elif origem == "K":
        temp_c = valor - 273.15
    else:
        raise ValueError("Unidade de origem inválida.")

    # Converte de Celsius para a unidade de destino
    if destino == "C":
        return temp_c
    elif destino == "F":
        return temp_c * 9/5 + 32
    elif destino == "K":
        return temp_c + 273.15
    else:
        raise ValueError("Unidade de destino inválida.")

try:
    valor = float(input("Informe a temperatura: "))
    origem = input("Informe a unidade de origem (C, F ou K): ").strip().upper()
    destino = input("Informe a unidade de destino (C, F ou K): ").strip().upper()

    resultado = converter_temperatura(valor, origem, destino)
    print(f"{valor:.2f} {origem} equivalem a {resultado:.2f} {destino}")
except ValueError as e:
    print(f"Erro: {e}")