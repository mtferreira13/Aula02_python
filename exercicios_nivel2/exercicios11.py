#Conversor de Temperatura

try:

    graus_celsius = float(input("Digite a temperatura em graus Celsius: "))
    graus_fahrenheit = (graus_celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {graus_fahrenheit:.2f} °F")

except ValueError:
    print("Por favor, insira um número válido para a temperatura.")
