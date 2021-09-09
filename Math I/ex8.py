print("vamos ver em quanto tempo voce fica milionario:")
salario=float(input("\nInsira o valor do seu salario:"))
despesa=float(input("\nInsira o valor da sua despesa mensal:"))


mensal= salario-despesa
media_anual=mensal*12
resultado_1= 1000000/media_anual

print("\nEm", resultado_1, "anos")

input("Pressione Enter para sair")
