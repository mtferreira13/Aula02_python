try: 
    
    nome = input("Digite seu nome: ")

    if len(nome) == 0:
        raise ValueError("O nome não pode ser vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não pode conter números.")
    elif nome.isspace():
        raise ValueError("O nome não pode conter apenas espaços.")
    else:
        print(f"Nome válido: {nome}!")
except ValueError as e:
    print(e)
    raise

try:    
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        raise ValueError("O salário não pode ser negativo.")
except ValueError as e:
    print("Entrada inválida. Por favor, insira um número válido para o salário.")
    raise
try:
    bonus = float(input("Digite o valor do bônus: "))
    if bonus < 0:
        print("O bônus não pode ser negativo.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número válido para o bônus.")
    raise

bonus_final = salario * 1.2
kpi = (salario + bonus_final) / 1000

print(f"O valor do KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R$ {salario:.2f} e seu bônus final é R$ {bonus_final:.2f}.")