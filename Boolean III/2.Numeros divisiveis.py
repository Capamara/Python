print("Ola seja bem vindo ao sistema de numeros inteiros e divisiveis")
numero_1=int(input("Digite o primiero numero desejado: "))
numero_2=int(input("Digite o segundo numero desejado: "))

divisao=numero_1 % numero_2

if divisao==0:
    print("O numero 1 Eh divisivel pelo segundo!")
else:
    print("o numero nao eh divisivel pelo segundo")