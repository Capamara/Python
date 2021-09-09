print("Ola!, seja bem vindo ao sistema de numeros divisiveis por 5 e 10")
numero_1=int(input("\nDigite o numero desejado: "))

resultado_1=numero_1 % 5
resultado_2=numero_1 % 10

if numero_1!=0:


    if resultado_1==0:
        print("\nO numero",numero_1,"é divisivel por 5")
    else:
        print("\nO numero",numero_1,"nao é divisivel por 5")

    if resultado_2==0:
        print("\nO numero",numero_1,"é divisivel por 10")
    else:
        print("\nO numero",numero_1,"nao é divisivel por 10")

else:
    print("0 nao eh divisivel por 10 e 5")


