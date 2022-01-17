import csv
with open('insurance.csv', newline='') as file:
    csvreader = csv.reader(file)
    count = 0
    for row in csvreader:
        count += 1
        print(row)
    print(count)

with open('insurance.csv')
