with open('Completo.txt','r') as arq1, open ('COMPLETA.txt','r') as arq2:
	a=arq1.readlines()
	b=arq2.readlines()
	print (len(a), len(b))
