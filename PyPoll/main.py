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

            vote_totals[newCandidate] = 1

        elif i[2] in candidate_list:
            vote_totals[i[2]] += 1


winner = max(vote_totals, key=vote_totals.get)     
def print_Lines():
    print("-------------------------")


print("Election Results")
print_Lines()
print(f"Total Votes: {total_votes}")
print_Lines()
print()
for i in candidate_list:
    vote_percentage = vote_totals[i]/total_votes
    percentage = f"{vote_percentage:.3%}"
    print(f"{i}: {percentage} ({vote_totals[i]})")
print_Lines()
print(f"Winner {winner}")
print_Lines()



   

        


# print(total_votes)
# print(vote_totals)
# #print(candidate_list)
# print(vote_totals)



