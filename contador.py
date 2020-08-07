"""with open('Arquivo_StringCompleta.txt','r') as f, open('Arquivo_Parte1_Quebra.txt', 'r') as arq1, open('Arquivo_Parte2_Quebra.txt','r') as arq2,  open('Arquivo_Parte3_Quebra.txt', 'r') as arq3, open('Arquivo_Parte4_Quebra.txt','r') as arq4, open('Arquivo_Parte5_Quebra.txt','r') as arq5, open('Arquivo_Parte6_Quebra.txt','r') as arq6: 

	string=f.read()
	string1=arq1.read()
	string2=arq2.read()
	string3=arq3.read()
	string4=arq4.read()
	string5=arq5.read()
	string6=arq6.read()
	
	print(len(string))
	print(len(string1))
	print(len(string2))
	print(len(string3))
	print(len(string4))
	print(len(string5))
	print(len(string6))
	print(len(string1) + len(string2) + len(string3) + len(string4) + len(string5) + len(string6))

f.close()
arq1.close()
arq2.close()
arq3.close()
arq4.close()
arq5.close()
arq6.close()"""

"""
with open('identificandoAspas.txt','r') as arq2:
	a=arq2.readlines()
	cont=0
	for linha in a:
		cont+=1
		x=linha.count(")")
		y=linha.count("(")
		if x!=y:
			print("Errado na linha: " + linha, cont)
	
"""
"""
with open('Arquivo_Parte2_Quebra.txt','r') as arq2:
	a=arq2.read()
	print(a.count("("))
	print(a.count(")"))

"""
