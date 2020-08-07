import csv

with open('table_chemical_terms.tsv') as csv_file, open ('identificandoAspas.txt', 'w') as identificandoAspas:
    
    csv_reader = csv.reader(csv_file, delimiter='"')

    csv_reader.__next__()

    for row in csv_reader:
        identificandoAspas.write(row[1] + '\n')
identificandoAspas.close()


