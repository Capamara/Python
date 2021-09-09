print("Ola seja bem vindo ao sistema do triangulo")
A=int(input("Digite o primiero numero: "))
B=int(input("Digite o segundo numero: "))
C=int(input("Digite o terceiro numero: "))

if A+B>C or A+C>B or C+B>A:
    print("Com esses valores podemos formar um triagulo")
    if A==B==C:
        print("Triangulo Equilatero")
    elif (A==B) or (A==C) or (B==C):
        print("Triangulo Isoceles")
    else:
        print("TRAINGULO FDP!")

else:
    print("PASSAR BEM")




