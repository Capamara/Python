print("Ola!, seja bem vindo ao sistema de numeros descrescente")
numero_1=float(input("\nDigite o primeiro numero: "))
numero_2=float(input("\nDigite o segundo numero: "))
numero_3=float(input("\nDigite o terceiro numero: "))
print("\nVoce Digitou",numero_1, "como primeiro numero ",numero_2,"como segundo numero", numero_3,"como terceiro numero")

if(numero_1)==(numero_2)==(numero_3):
    print("Os numeros nao podem ser iguais")

elif(numero_1>numero_2 and numero_1>numero_3 and numero_2>numero_3):
    print(numero_1,numero_2, numero_3) 

elif(numero_1>numero_2 and numero_1>numero_3 and numero_3>numero_2):
    print(numero_1,numero_3, numero_2) 

elif(numero_2>numero_1 and numero_2>numero_3 and numero_1<numero_3):
    print(numero_2, numero_3, numero_1)

elif(numero_2>numero_1 and numero_2>numero_3 and numero_3<numero_1):
    print(numero_2, numero_1, numero_3)

elif(numero_3>numero_2 and numero_3>numero_1 and numero_1<numero_2):
    print(numero_3, numero_2, numero_1)

elif(numero_3>numero_2 and numero_3>numero_1 and numero_2<numero_1):
    print(numero_3, numero_1, numero_2)

