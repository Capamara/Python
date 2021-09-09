print("BEM VINDO A PREFEITURA DE RECIFE")
salario_bruto=float(input("Digite o valor do seu salario: "))
valor_prestacao=float(input("Digite o valor da prestacao: "))


if valor_prestacao>0 or salario_bruto>0:
    if valor_prestacao<=(salario_bruto)*30/100*10:
        print("Valor concedido")
    if valor_prestacao>(salario_bruto)*30/100*10:
        print("valor nao concedido")
else:
    print("O valor nao pode ser calculado ")

