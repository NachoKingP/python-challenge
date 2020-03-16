#Brian Remite python-challenge, PyBank scenario
import os
import csv

#-------------------------------------------
# Declarations
#-------------------------------------------

#Declare variables necessary for calculation
TotMonths = 0
TotPL = 0.00
MaxPL = 0.00
MaxMonth = ""
MinPL = 0.00
MinMonth = ""
PLChange = 0.00
LastMonthPL = 0.00
PLAvg = 0.00

#List declaration to track average P/L changes
PLChanges = []

#-------------------------------------------
# Code to process file
#-------------------------------------------

#Path to collect data from the Resources folder
data_csv = os.path.join("Resources", "budget_data.csv")

#read in file
with open(data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    header = next(csvreader)
    
    #Parse the data in the file
    for row in csvreader:
        
        #Update totals
        TotMonths += 1
        TotPL += int(row[1])
        
        #Subtract previous PL total from current to get change
        PLChange = int(row[1]) - LastMonthPL
        
        #Update LastMonthPL value for next calculation
        LastMonthPL = int(row[1])
        
        #Add current P/L changes to running list of total P/L changes
        PLChanges.append(int(row[1]))
        
        #Check to see if current revenue change is greatest
        if (PLChange > MaxPL):
            MaxPL = PLChange
            MaxMonth = row[0]
        
        #Check to see if current revenue change is lowest
        if (PLChange < MinPL):
            MinPL = PLChange
            MinMonth = row[0]
    
    #Calculate the average P/L change
    PLAvg = sum(PLChanges) / len(PLChanges)

#-------------------------------------------
# Output results to screen
#-------------------------------------------

print("\n \n \n")
print("```text")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(TotMonths))
print("Total: $" + str(TotPL))
print("Average Change: $" + str(PLAvg))
print("Greatest Increase in Profits: $" + str(MaxPL) + " in " + str(MaxMonth))
print("Greatest Decrease in Profits: $" + str(MinPL) + " in " + str(MinMonth))
print("```")
    
    
    
    
