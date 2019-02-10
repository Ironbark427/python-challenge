# importing dependencies
import csv
import os

# setting up variables

count = 0
maxamt = 0
candidates = {}


# pull in external data (Atom location is relative to project base not file)
elect_csv = os.path.join("./PyPoll/election_data.csv")

with open(elect_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    # iterate though csv to get prep answers
    for row in csvreader:
        count += 1  # get total number of votes
        if row[2] not in candidates:
            candidates[row[2]] = 1  # Add them to dictionary
        else:
            candidates[row[2]] += 1  # mmmm...more votes!

# Greetings! Here are the results:
print("    Election Results")
print("---------------------------")
print(f"Total Votes: {count}")
print("---------------------------")

for vote, amount in candidates.items():
    pct_vote = round((amount / count)*100, 2)
    print(f"{vote}: {pct_vote}% ({amount})")
    if(amount > maxamt):
        maxamt = amount
        winner = vote

print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# create text file to write answers
with open("./PyPoll/results.txt", "w") as file:
    file.write("         Election Results       \n")
    file.write("-----------------------------------\n")
    file.write(f"Total Votes  : {count} \n")
    file.write("-----------------------------------\n")

# Yes, I know it is redundant. A function or done above would have been
# better but, it works.
    for vote, amount in candidates.items():
        pct_vote = round((amount / count)*100, 2)
        file.write(f"{vote}: {pct_vote}% ({amount})\n")

    file.write("-----------------------------------\n")
    file.write(f"Winner: {winner}")

    file.close
