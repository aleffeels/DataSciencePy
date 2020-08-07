import csv

with open('table_chemical_terms.tsv') as csv_file, open ('Arquivo_StringCompleta.txt', 'w') as completa:
    
    csv_reader = csv.reader(csv_file, delimiter='"')

    csv_reader.__next__()

    completa.write('(cancer OR tumor) AND (')

    for row in csv_reader:
        completa.write('"'+ row[1] + '" OR ')
completa.close()

with open('Arquivo_StringCompleta.txt', 'a') as completa:
	completa.write(')')
	completa.close()

