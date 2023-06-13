import csv
with open('it.csv') as csv_file:
    rows = csv.reader(csv_file, delimiter = ',')
for row in rows:
print(row)
