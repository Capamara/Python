print("bem vindo ao sistema de Media do Colegio Python")
trabalho_laboratorio=float(input("Digite a Nota do trabalho de laboratorio: "))
avaliacao_semestral=float(input("Digite a Nota da Avaliacao Semestral: "))
exame_final=float(input("Digite a Nota do Exame Final: "))

media=((trabalho_laboratorio)*2 + (avaliacao_semestral)*3 + (exame_final)* 5)/10

print("A sua media eh:", media)
if(media>=8<=10):
    print("Conceito A")
elif(media>=7<=7.9):
    print("Conceito B")
elif(media>=6<=6.9):
    print("Conceito C")
elif(media>=5<=5.9):
    print("Conceito D")
elif(media>=0<=4.9):
    print("Conceito E")