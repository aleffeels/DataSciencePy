with open('pmid-cancerORtu-set.txt', 'r') as arq1: 
    string1=arq1.readlines()

with open('pmid-cancerORtu-set (1).txt', 'r') as arq2: 
    string2=arq2.readlines()

with open('pmid-cancerORtu-set (2).txt', 'r') as arq3: 
    string3=arq3.readlines()

with open('pmid-cancerORtu-set (3).txt', 'r') as arq4: 
    string4=arq4.readlines()

with open('pmid-cancerORtu-set (4).txt', 'r') as arq5: 
    string5=arq5.readlines()

with open('pmid-cancerORtu-set (5).txt', 'r') as arq6: 
    string6=arq6.readlines()
completa=sorted(set(string1+string2+string3+string4+string5+string6))
with open('COMPLETA.txt', 'w') as comp: 
    comp.writelines(completa)