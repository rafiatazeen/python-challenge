#importing modules
import os
import csv

#setting the file path
poll_csv = os.path.join('Resources', 'election_data.csv')

#setting variables
ballot_id = []
count = []
candidate = []
unique_list = []
total_votes = 0
#using dictionary to the unique candidates, number of votes and percentage of votes
number_votes = {}
each_candidate = []
winner_votes = 0

#this code is because the program was not able to read the file from the file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#opening the csv file
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #looping through the data
    for row in csvreader:
        ballot_id = row[0]
        candidate = row[2]
        total_votes = total_votes + 1

        #appending the unique candidates to a list and also calculating corresponding number of votes
        if candidate not in unique_list:
            unique_list.append(candidate)
            number_votes[candidate] = 0
        number_votes[candidate] = number_votes[candidate] + 1
    
    #printing first part of the results
    print("Election Results")
    print("------------------------------")
    print("Total Votes: " + str(total_votes))
    print("------------------------------")

#exporting the result to a text file
with open("out.txt", "w") as f:
    f.write("Election Results" + '\n')
    f.write("------------------------------" + '\n')
    f.write("Total Votes: " + str(total_votes) + '\n')
    f.write("------------------------------" + '\n')

    #finding the values of percentage of votes for each unique candidate
    for candidate in unique_list:
        if candidate in unique_list:
            can_votes = number_votes[candidate]
            percent_votes = can_votes / total_votes * 100
            voter_percent = f"{candidate}: {percent_votes:.3f}% ({can_votes})"
            
            #including the print and write command here as it was not printing all three candidates info otherwise
            print(voter_percent)
            f.write(voter_percent + '\n')
            
            #tried using max function and index function but was not working so used an if statement
            if (can_votes > winner_votes):
                winner_votes = can_votes
                winning_candidate = candidate
    
    #including the write command here as it was not displaying correctly otherwise
    f.write("------------------------------" + '\n')
    f.write("Winner: " + winning_candidate + '\n')

#printing the winner name
print("------------------------------")
print("Winner: " + winning_candidate)



