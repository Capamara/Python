print("Ola seja bem vindo ao sistema de transporte")
regiao=input("\nPor favor, digite a regiao onde quer ir: NORTE, NORDESTE E CENTRO-OESTE: ")
caminho=input("\nIsira tambem se quer ida ou ida e volta: ")

if (regiao=="Norte"):
    print("Voce escolheu viajar para a regiao Norte")
    
    if caminho=="ida":
        print("R$280")
    if caminho=="ida e volta":
        print("R$400")
else:
    print("Escolha a opcao correta")

if regiao=="Nordeste":
    print("Voce escolheu viajar para a regiao Nordeste")
    
    if caminho=="ida":
        print("R$380 ")
    if caminho=="ida e volta":
        print("R$628")

if regiao=="Centro oeste":
    print("Voce escolheu viajar para a regiao Centro Oeste")
    
    if caminho=="ida":
        print("R$620")
    if caminho=="ida e volta":
        print("R$1100")
    
