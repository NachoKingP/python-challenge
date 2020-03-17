#Brian Remite python-challenge, PyPoll scenario
import os
import csv
#
#-------------------------------------------
# Declarations
#-------------------------------------------

#Declare variables necessary for calculation
TotVotes = 0
MaxVotes = 0
MaxCan = ""
NumCan = 0
CandidateList = []
Votes = {}

#Specify the file to write to
output_path = os.path.join("output", "results.txt")

#-------------------------------------------
# Code to process file
#-------------------------------------------

#Path to collect data from the Resources folder
data_csv = os.path.join("Resources", "election_data.csv")

#read in file
with open(data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    header = next(csvreader)
    
    #Parse the data in the file
    for row in csvreader:
        TotVotes += 1
        
        if row[2] in CandidateList:
            Votes[row[2]] += 1
        
        else:
            CandidateList.append(row[2])
            Votes[row[2]] = 1
        
        #Check to see if current candidate has the most votes
        if (Votes[row[2]] > MaxVotes):
            MaxVotes = Votes[row[2]]
            MaxCan = row[2]


#-------------------------------------------
# Output results to screen
#-------------------------------------------

print("\n \n \n")
print("```")
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(TotVotes))
print("----------------------------")
for candidate in Votes:
    print(candidate + " " + str(round(((Votes[candidate] / TotVotes) * 100))) + "% (" + str(Votes[candidate]) + ")")

print("------------------------------------")
print("Winner: " + MaxCan + " with " + str(MaxVotes) + " votes.")
print("------------------------------------")

#-------------------------------------------
# Output results to text file
#-------------------------------------------

with open(output_path, "w") as txt_file:
    #Write the results
    txt_file.write("Election Results \n")
    txt_file.write("---------------------------- \n")
    txt_file.write("Total Votes: " + str(TotVotes) + " \n")
    txt_file.write("---------------------------- \n")
    for candidate in Votes:
        txt_file.write(candidate + " " + str(round(((Votes[candidate] / TotVotes) * 100))) + "% (" + str(Votes[candidate]) + ") \n")
    
    txt_file.write("------------------------------------ \n")
    txt_file.write("Winner: " + MaxCan + " with " + str(MaxVotes) + " votes. \n")
    
    txt_file.write("------------------------------------ \n")






