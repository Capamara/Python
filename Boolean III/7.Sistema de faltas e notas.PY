print("Ola seja bem vindo ao sistema faltas e notas")
user_1=input("Digite o seu nome: ")
print("-"*90)
nota_1=float(input("Digite a primeira nota: "))
nota_2=float(input("Digite a segunda nota: "))
nota_3=float(input("Digite a terceira nota: "))
faltas=int(input("Digite o numero de faltas: "))

medias_notas=(nota_1+ nota_2 + nota_3) /3

if faltas<20:
    print("O aluno foi aprovado por presenca")
    if medias_notas>=7:
        print("O aluno(a)",user_1, "foi aprovado nas notas, tendo uma media de: ",medias_notas)
    if medias_notas<7:
        print("O aluno(a)",user_1, "foi reprovado nas notas, tendo uma media de: ",medias_notas)
else:
    print("o aluno foi reprovado por falta")
    

