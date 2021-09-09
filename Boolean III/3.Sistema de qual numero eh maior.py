print("Ola seja bem vindo ao sistema de qual numero eh maior")
numero_1=int(input("Digite o primiero numero desejado: "))
numero_2=int(input("Digite o segundo numero desejado: "))

if numero_1==numero_2:
    print("\nOs numeros nao podem ser iguais")

elif numero_1>numero_2:
    print("\nO Primeiro numero eh maior que o Segundo")

elif numero_2>numero_1:
    print("\nO Segundo numero eh maior que o Primeiro ")
