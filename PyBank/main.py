import os
import csv

# Path to collect data from the Resources folder
data_csv = os.path.join("Resources", "budget_data.csv")

#Declare variables necessary for calculation

#read in file
with open(data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    header = next(csvreader)
    
    
