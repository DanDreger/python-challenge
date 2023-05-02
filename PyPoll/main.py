import os

import csv

voting_csv = os.path.join(".", "Resources", "election_data.csv")

with open(voting_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    candidate_list = []
   
 
    vote_totals = {}
    number_of_candidates = 0

    total_votes = 0
    for i in csvreader:
        total_votes = total_votes + 1
        votes = 0
        
     
        if i[2] not in candidate_list:
            newCandidate = i[2]
            candidate_list.append(newCandidate)
            number_of_candidates = number_of_candidates +1
         
        
            key=str(newCandidate)
            vote_totals[key]= 0
            print(vote_totals)
            vote_totals.update({f"{newCandidate}: {int(1)}"})
        # elif i[2] in candidate_list:
        #     print("candidate is already in the list")
        






   

        


# print(total_votes)
print(candidate_list)
# print(vote_totals['Charles Casper Stockham'])



