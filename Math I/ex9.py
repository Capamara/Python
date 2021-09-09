print("Ola seja bem vindo")
candidato_a=int(input("\nInsira quantos votos o Candidato A obteve:"))
candidato_b=int(input("\nInsira quantos votos o Candidato B obteve:"))
candidato_c=int(input("\nInsira quantos votos o Candidato B obteve:"))
nulos=int(input("\nInsira o numero de votos nulos:"))
brancos=int(input("\nInsira o numero de votos em brancos:"))

total_eleitores= candidato_a+candidato_b+candidato_c+nulos+brancos
a_total=candidato_a/total_eleitores * 100
b_total=candidato_b/total_eleitores * 100
c_total=candidato_c/total_eleitores * 100
brancos_total=brancos/total_eleitores * 100
nulos_total=nulos/total_eleitores * 100

print("\nTotal de eleitores:", total_eleitores)
print("\nCandidato A", a_total,"%")
print("\nCandidato B",b_total,"%")
print("\nCandidato C", c_total,"%")
print("\nVotos Brancos", brancos_total,"%")
print("\nVotos Nulos", nulos_total,"%")




input("\nTECLE ENTER PARA SAIR")
