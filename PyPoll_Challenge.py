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

# Create a county list and county votes dictionary.
county_options = []
county_votes = {}

#winning cadidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
turnout_county = ""
turnout_votes = 0
turnout_percentage = 0

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

          # Extract the county name from each row.
          county_name = row[1]
          #print(county_name)

          #see is candidate name unique
          if candidate_name not in candidate_options:
               #Add candidate name to list
               candidate_options.append(candidate_name)

               #track votes per candidate
               candidate_votes[candidate_name] = 0

          #add votes
          candidate_votes[candidate_name] += 1

          # 4a: Write an if statement that checks that the
           # county does not match any existing county in the county list.
          if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
          county_votes[county_name] += 1
         
#save results to text file
with open(file_to_save, "w") as txt_file:   
               
     #print final vote count to terminal
     election_results = (
          f'\nElection Results\n'
          f'-------------------------\n'
          f'Total Votes:{total_votes:,}\n'
          f'-------------------------\n'
          f"\nCounty Votes:\n")
     print(election_results, end="")
     #save the count to text file
     txt_file.write(election_results)
     
     # 6a: Write a for loop to get the county from the county dictionary.
     for county_name in county_votes:
        # 6b: Retrieve the county vote count.
          turnout = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
          county_percentage = float(turnout) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
          county_results = (                        
               f"{county_name}: {county_percentage:.1f}% ({turnout:,})\n")
        
         # 6e: Save the county votes to a text file.
          print(county_results, end="")
          txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
          if (turnout > turnout_votes) and (county_percentage > turnout_percentage):
               turnout_votes = turnout
               turnout_county = county_name
               turnout_percentage = county_percentage

    # 7: Print the county with the largest turnout to the terminal.
     turnout_county_summary = (
          f"\n-------------------------\n"
          f"Largest County Turnout: {turnout_county}\n"
          #f"Voters: {turnout_votes}\n"
          #f"Voter Percentage: {turnout_percentage:.1f}%\n"
          f"-------------------------\n")
     print(turnout_county_summary)

    # 8: Save the county with the largest turnout to a text file.
     txt_file.write(turnout_county_summary)

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