print("Ola!, seja bem vindo ao sistema de numeros maiores")
numero_1=int(input("\nDigite o primeiro numero: "))
numero_2=int(input("\nDigite o segundo numero: "))
print("\nVoce Digitou",numero_1, "como primeiro numero e",numero_2,"como segundo numero")

if(numero_1>numero_2):
    print("\n",numero_1, ">",numero_2)

elif(numero_2>numero_1):
     print("\n",numero_2,">",numero_1)

elif(numero_1)==(numero_2):
    print("\nOs numeros sao iguais:",numero_1,"=", numero_2)

else:
    input("Pressione enter para sair")
