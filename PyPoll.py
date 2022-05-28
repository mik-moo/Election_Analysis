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

#1 initialize vote counter.
total_votes= 0

#candidate options and votes
candidate_options =[]
candidate_votes = {}

#winning cadidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open and read election results
with open(file_to_load) as election_data:
     #to do: read and analyze data here.
     #Read the file object with reader function.
     file_reader = csv.reader(election_data)
     #print each row of csv file
     #for row in file_reader:
      #    print(row)
     
     #read header row
     headers = next(file_reader)
     
     #print each row in file
     for row in file_reader:
          #2 add to total vote count
          total_votes += 1

          #Print candidate names
          candidate_name = row[2]
          
          #see is candidate name unique
          if candidate_name not in candidate_options:
               #Add candidate name to list
               candidate_options.append(candidate_name)

               #track votes per candidate
               candidate_votes[candidate_name] = 0

          #add votes
          candidate_votes[candidate_name] += 1
         
#save results to text file
with open(file_to_save, "w") as txt_file:   
               
     #print final vote count to terminal
     election_results = (
          f'\nElection Results\n'
          f'-------------------------\n'
          f'Total Votes:{total_votes:,}\n'
          f'-------------------------\n')
     print(election_results, end="")
     #save the count to text file
     txt_file.write(election_results)
     
     #print(candidate_votes)

     # Determine the percentage of votes for each candidate by looping through the counts.
     # 1. Iterate through the candidate list.
     for candidate_name in candidate_votes:
          # 2. Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
          # 3. Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_votes) * 100

          #To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
          candidate_results = (
               f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          #print candidate, counts and percentage
          print(candidate_results)
          #save results to txt file
          txt_file.write(candidate_results)       
     
          # Determine winning count, percentage and candidate
          if (votes > winning_count) and (vote_percentage > winning_percentage):
         
               winning_count = votes
               winning_candidate = candidate_name
               winning_percentage = vote_percentage
               
     #Print winning results to terminal
     
     winning_candidate_summary = (
               f"-------------------------\n"
               f"Winner: {winning_candidate}\n"
               f"Winning Vote Count: {winning_count:,}\n"
               f"Winning Percentage: {winning_percentage:.1f}%\n"
               f"-------------------------\n")
     print(winning_candidate_summary)
     #save results to text file
     txt_file.write(winning_candidate_summary)