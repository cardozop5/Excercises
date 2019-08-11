
import os
import csv


election_csv = os.path.join("Resources","election_data.csv")
election_output = ("Resources","election_data_txt.txt")

Total_Votes = 0

Khan_Votes = 0

Correy_Votes = 0

Li_Votes = 0

OTooley_Votes = 0




# Open and read csv
with open(election_csv, newline='') as election_data:
    csvreader = csv.reader(election_data, delimiter =',')

    for row in csvreader:
        Total_Votes +=1

        if row[2] == "Khan":
            Khan_Votes +=1

        elif row[2] == "Correy":
             Correy_Votes +=1

        elif row[2] == "Li":
            Li_Votes +=1

        elif row[2] =="OTooley":
            OTooley_Votes +=1

#create a list
candidates = ["Khan", "Correy", "Li","OTooley"]

votes = [Khan_Votes, Correy_Votes, Li_Votes, OTooley_Votes]

#the purpose of zip is to map the similar index of multiple containers
# so they can be used just using as single entity
#max function to return the winner

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max (dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Create percentages

khan_percent = (Khan_Votes/Total_Votes)
correy_percent = (Correy_Votes/Total_Votes)
li_percent = (Li_Votes/Total_Votes)
otooley_percent = (OTooley_Votes/Total_Votes)


print(f"Election Results")
print (f"----------------------")
print(f"Total Votes: {Total_Votes}")
print (f"----------------------")
print(f"Khan: {khan_percent:.3%} ({Khan_Votes})")
print(f"Correy: {correy_percent:.3%} ({Correy_Votes})")
print(f"Li: {li_percent:.3%} ({Li_Votes})")
print(f"OTooley: {otooley_percent:.3%} ({OTooley_Votes})")
print (f"----------------------")
print(f"Winner: {key}")
print (f"----------------------")


f = open('election_data_txt.txt','w')
print(f"Election Results", file=f)
print (f"----------------------")
print(f"Total Votes: {Total_Votes}", file=f)
print (f"----------------------")
print(f"Khan: {khan_percent:.3%} ({Khan_Votes})", file=f)
print(f"Correy: {correy_percent:.3%} ({Correy_Votes})", file=f)
print(f"Li: {li_percent:.3%} ({Li_Votes})", file=f)
print(f"OTooley: {otooley_percent:.3%} ({OTooley_Votes})", file=f)
print (f"----------------------")
print(f"Winner: {key}", file=f)
print (f"----------------------")
f.close()