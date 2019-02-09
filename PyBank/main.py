import csv
import os

bank_csv = os.path.join("./PyBank/budget_data.csv")

with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    count = 0
    total = 0
    valuelist = []
    mydict = {}

    for row in csvreader:
        count += 1
        total = total + int(row[1])
        valuelist.append(int(row[1]))
        mydict[row[0]] = int(row[1])

    maxvalue = max(valuelist)
    minvalue = min(valuelist)

    for date, amount in mydict.items():
        if amount == maxvalue:
            maxdate = date
        elif amount == minvalue:
            mindate = date

    print(maxdate)
    print(mindate)
    print(count)
    print(total)
    print(max(valuelist))
    print(min(valuelist))
    # print(valuelist)
