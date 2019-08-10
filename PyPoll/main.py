
import os
import csv

from collections import OrderedDict

from operator import itemgetter

election_csv = os.path.join("Resources","election_data.csv")
election_output = "Resources","election_data_txt.txt"

Votes = 0

winner_votes = 0

total_candidates = 0

greatest_votes = ["",0]

candidate_options = []

candidate_votes = {}



# Open and read csv
with open(election_csv) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
            
        votes = Votes + 1

        total_candidates = row["Candidate"]   

        if row["Candidate"] not in candidate_options:
    
     
            candidate_options.append(row["Candidate"])


            candidate_votes[row["Candidate"]] = 1

            

    else:

         candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1



#----------------------------------------------------------------------------------------

    # Determine the Winner:

    #if (votes > winner_votes[2]):

     #   greatest_increase[1] = revenue_change

      #  greatest_increase[0] = row["Candidate"]

#----------------------------------------------------------------------------------------

    

print()

print()

print()

print("Election Results")

print("-------------------------")

print("Total Votes " + str(votes))

print("-------------------------")

#results

for candidate in candidate_votes:

    print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 

    candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 

    

    candidate_votes





#results

print("-------------------------")

print("-------------------------")

# Output Files

with open(election_output, "w") as txt_file:

    

    txt_file.write("Election Results")

    txt_file.write("\n")

    txt_file.write("-------------------------")

    txt_file.write("\n")

    #txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")

    txt_file.write(str(winner))

    txt_file.write("\n")

    txt_file.write("-------------------------")

    txt_file.write("\n")

    txt_file.write("Winner: " + str(winner[0]))

    txt_file.write("\n")

    txt_file.write("Total Votes " + str(votes))