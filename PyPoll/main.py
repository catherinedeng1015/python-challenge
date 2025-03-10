# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
total_votes = 0
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output

    # Print the total vote count (to terminal)
output = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")

    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage
for candidate, vote_count in candidate_votes.items():
    percentage = (vote_count / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({vote_count})\n"

        # Update the winning candidate if this one has more votes
for candidate, vote_count in candidate_votes.items():
    if vote_count > winning_count:
        winning_count = vote_count
        winning_candidate = candidate
output += (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n")

        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary
print(output)

    # Save the winning candidate summary to the text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)