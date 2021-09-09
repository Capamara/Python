print("\nBem-vindo ao setor financeiro:")
valorb=float(input("\nDigite o valor do boleto:"))
juros=float(input("\nDigite o valor de juros em %:"))
dias=int(input("\nDigite os dias apos a data de vencimento do boleto:"))

resultado_1= valorb+(valorb*(juros/100))*dias

print("\nO novo do boleto com juros sera","R$", resultado_1)

input("pressione Enter para sair")