# importing dependencies
import csv
import os

# setting up variables
count = 0
total = 0
mydict = {}
avg = 0
minval = 0
maxval = 0
truth = False

# pull in external data (Atom location is relative to project base not file)
bank_csv = os.path.join("./PyBank/budget_data.csv")

# use os module to read in csv file
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

# iterate though csv to get prep answers
    for row in csvreader:
        count += 1  # get total number of months
        total = total + int(row[1])  # get total revenues
        mydict[row[0]] = int(row[1])

# iterate through keys and values in dictionary
    for date, amount in mydict.items():
        if truth is False:  # setting up first value comparisons
            prevkey = date
            prevamt = amount
            truth = True
        elif (amount - prevamt) > maxval:  # compare curr and prev vals
            maxval = amount - prevamt  # setting max val to max num
            maxdate = date  # curr date not prev date
            prevkey = date  # resetting prev vals for next compare
            prevamt = amount
            avg = avg + maxval  # building total for Average
        elif (amount - prevamt) < minval:  # basic repeat of maxval chk
            minval = amount - prevamt
            mindate = date
            prevkey = date
            prevamt = amount
            avg = avg + minval
        else:  # when chg is less then max and more than min
            avg = avg + (amount - prevamt)
            prevkey = date
            prevamt = amount

avg = avg / (count - 1)  # get average change

# Yuuumm! Here are the answers!
print("         Financial Analysis        ")
print("___________________________________")
print(f"Total Months  : {count} ")
print(f"Total Revenue : ${total} ")
print(f"Average Change: ${round(avg, 2)} ")
print(f"Greatest Increase in Profits: ${maxval} on {maxdate}")
print(f"Greatest Decrease in Profits: ${minval} on {mindate}")

# create text file to write answers
with open("./PyBank/Finances.txt", "w") as file:
    file.write("         Financial Analysis        \n")
    file.write("___________________________________\n")
    file.write(f"Total Months  : {count} \n")
    file.write(f"Total Revenue : ${total} \n")
    file.write(f"Average Change: ${round(avg, 2)} \n")
    file.write(f"Greatest Increase in Profits: ${maxval} on {maxdate}\n")
    file.write(f"Greatest Decrease in Profits: ${minval} on {mindate}\n")

    file.close
