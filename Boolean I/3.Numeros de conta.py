conta = int(input("Informe o número da sua conta: "))
digito1 = conta//100
digito2 = (conta%100)//10
digito3 = (conta%100)%10
inverso = str(digito3)+str(digito2)+str(digito1)
print("O inverso da conta é: ",inverso)
soma = conta + int(inverso)
print("Soma da conta com o inverso dela:", soma)
digito2 = soma // 100
digito3 = (soma % 100) // 10
digito4 = (soma % 100) % 10
if soma > 999:
 digito1 = soma // 1000
 mult = digito1 * 1 + digito2 * 2 + digito3 * 3 + digito4 * 4
else:
 mult = digito2 * 1 + digito3 * 2 + digito4 * 3
print("Código verificador é: " + str(mult%10))
