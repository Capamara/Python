print("Ola!, seja bem vindo ao sistema de par ou impar")
numero_1=int(input("\nDigite o numero desejado: "))
resultado=numero_1 % 2

if resultado == 1:
    print("O numero",numero_1,"é impar")
else:
    print("O numero",numero_1,"é par")
