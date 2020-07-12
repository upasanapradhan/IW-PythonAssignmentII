import csv
with open('file.csv', mode = 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    list_dict = []
    for row in reader:
        list_dict.append(dict(row))
    print(list_dict)