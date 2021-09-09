print("Ola seja bem vindo ao sistema de compra e venda")
compra_1=float(input("Digite por quanto voce comprou o produto: "))

lucro_1=(compra_1<=20) * 45/100*10
lucro_2=(compra_1>20)* 30/100*10

if lucro_1:
    print(lucro_1 + compra_1)
elif compra_1>20:
    print(lucro_2 + compra_1)



