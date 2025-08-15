valores = [float(input("Digite o primeiro valor: ")) , float(input("Digite o segundo valor: "))]  

soma = sum(valores)
qntd = len(valores)
media = soma / qntd

print(f"A média dos valores {valores} é: {media:.2f}")