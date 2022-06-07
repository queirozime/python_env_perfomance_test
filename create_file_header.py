import csv
with open ('./results.csv', 'a+') as file:
    writer = csv.writer(file)
    header = ['function name', 'avg time','min time','max time', 'std dev'] 
    writer.writerow(header)

