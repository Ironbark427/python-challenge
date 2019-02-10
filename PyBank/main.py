# importing dependencies
import csv
import os

# setting up variables
count = 0
total = 0
valuelist = []
mydict = {}
avg = 0

# pull in external data
bank_csv = os.path.join("./PyBank/budget_data.csv")

# use os module to read in csv file
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

# iterate though csv to get prep answers
    for row in csvreader:
        count += 1  # get total number of months
        total = total + int(row[1])  # get total revenues
        valuelist.append(int(row[1]))  # create list for evaluation
        mydict[row[0]] = int(row[1])  # turn csv into dictionary for comparison

# get min and max values
    maxvalue = max(valuelist)
    minvalue = min(valuelist)

    for date, amount in mydict.items():  # iterate through dict
        if amount == maxvalue:  # to find the maximum maxdate
            maxdate = date
        elif amount == minvalue:  # and the mindate
            mindate = date

    for i in range(count):  # use count for loop through values
        if(i == 0):
            pass  # must pass as the first value can't subtract nothing
        else:
            avg = avg + (valuelist[i] - valuelist[i-1])  # sum changes

    avg = avg / (count - 1)

# Yuuumm! Here are the answers!
print("         Financial Analysis        ")
print("___________________________________")
print(f"Total Months  : {count} ")
print(f"Total Revenue : ${total} ")
print(f"Average Change: ${round(avg, 2)} ")
print(f"Greatest Increase in Profits: {maxvalue} on {maxdate}")
print(f"Greatest Decrease in Profits: {minvalue} on {mindate}")

# create text file to write answers
