#Data we need to retrieve
#1. Total votes cast
#2. List of candidates that received votes
#3. Total votes per candidate
#4. Percent votes per candidate
#5. Winner by popular vote

# #Assign a vairable fo the file to load and the path
# file_to_load = 'Resources/election_results.csv'

# # Open election results and read the file
# with open(file_to_load) as election_data:


#      #To do: perform analysis.
#      print(election_data)

# Add dependencies
import csv
import os

# Assign a vairable for the file to laod from path.
file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open and read election results
with open(file_to_load) as election_data:
     #to do: read and analyze data here.
     #Read the file object with reader function.
     file_reader = csv.reader(election_data)
     #print each row of csv file
     #for row in file_reader:
      #    print(row)
     
     #print header row
     headers = next(file_reader)
     print(headers)
