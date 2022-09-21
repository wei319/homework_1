# this file is to calculate the length of the gene
import csv

line = 1

with open('test_data/brca_cnvs_tcga-1.csv', 'r') as TCGA_data:
    reader = csv.reader(TCGA_data, delimiter = ',')
    for row in reader:
        #   print(row)
        #   print (type(row[2]))

        if line == 1:
            row.append("seq_length")
        else:
            GeneLength = int(row[3]) - int(row[2])
            row.append(GeneLength)

        # print(row)

        with open('test_data/brca_cnvs_tcga-1_new.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
            line += 1
        

        # if line > 10:
        #     break

"""
['ID', 'chrom', 'loc.start', 'loc.end']
['TCGA-LQ-A4E4-01', '1', '3218610', '34123298']
"""