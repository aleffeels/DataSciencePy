#Copiando a String que será utilizada na busca do site PubMed para quebra-la em seguida.

with open('Arquivo_StringCompleta.txt', 'r') as arq: 
    string=arq.read()				#Passando o texto completo pra uma string

string2=string[:50000]				#Copiando toda informação de 0 a 50000 caracteres
string3=string[50000:100000]		#Copiando toda informação de 50000 a 100000 caracteres
string4=string[100000:150000]		#Copiando toda informação de 100000 a 150000 caracteres
string5=string[150000:200000]		#Copiando toda informação de 150000 a 200000 caracteres
string6=string[200000:250000]		#Copiando toda informação de 200000 a 250000 caracteres
string7=string[250000:]				#Copiando toda informação de 250000 ao resto de caracteres

with open('Arquivo_Parte1_Quebra.txt','w') as part1: 
	part1.write(string2 + ')')								#Escrevendo a parte 1 em Arquivo_Parte1_Quebra 

with open('Arquivo_Parte2_Quebra.txt','w') as part2:
	part2.write('(cancer OR tumor) AND ('+ string3 + ')')		#Escrevendo a parte 2 em Arquivo_Parte2_Quebra

with open('Arquivo_Parte3_Quebra.txt','w') as part3:
	part3.write('(cancer OR tumor) AND ('+ string4 + ')')		#Escrevendo a parte 3 em Arquivo_Parte3_Quebra

with open('Arquivo_Parte4_Quebra.txt','w') as part4:
	part4.write('(cancer OR tumor) AND ('+ string5 + ')')		#Escrevendo a parte 4 em Arquivo_Parte4_Quebra

with open('Arquivo_Parte5_Quebra.txt','w') as part5:
	part5.write('(cancer OR tumor) AND ('+ string6 + ')')		#Escrevendo a parte 5 em Arquivo_Parte5_Quebra

with open('Arquivo_Parte6_Quebra.txt','w') as part6:
	part6.write('(cancer OR tumor) AND ('+ string7)		#Escrevendo a parte 6 em Arquivo_Parte6_Quebra

#Não posso esquecer de fechar os arquivos pois senão da merda.
arq.close()
part1.close()
part2.close()
part3.close()
part4.close()
part5.close()
part6.close()

#No final desse processo as alterações podem ser feitas manualmente.
