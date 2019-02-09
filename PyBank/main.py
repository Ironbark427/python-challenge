# Dependencies
import csv
import os

# Specify the file to write to
bank_csv = os.path.join("budget_data.csv")

with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)

    count = 0
    total = 0
    
    
    for row in csvreader:
        count += 1
        total = total + int(row[1])
              
    print (count)
    print (total)