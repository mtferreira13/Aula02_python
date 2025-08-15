# Verificador de Palíndromo

palindromo = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
if isinstance(palindromo, str):
    # Remove espaços e converte para minúsculas
    palindromo_limpo = ''.join(palindromo.split()).lower()
    # Verifica se é um palíndromo
    if palindromo_limpo == palindromo_limpo[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")