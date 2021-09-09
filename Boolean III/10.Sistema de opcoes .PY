print("Ola seja bem vindo ao sistema de opcoes")
escolha=int(input("Digite as seguintes opcoes:\n"
"(1)Soma\n"
"(2)Raiz\n"))


if escolha>=3:
    print("Opcao nao valida")

elif escolha==1:
    print("Sistema de Soma:")
    numero_1=int(input("\nDigite o primeiro numero para ser feito a soma: "))
    numero_2=int(input("\nDigite o segundo numero para ser feito a soma a soma: "))
    print("Resultado:",numero_2+numero_1)

elif escolha==2:
    print("Sistem de Raiz quadrada:")
    numero_3=int(input("\nDigite o numero para ser feito a raiz quadrada:"))
    print("Resultado:",numero_3*numero_3)
















