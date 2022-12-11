# Find below some pseudocode for this project:

# find the:

# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

import os
import csv
dir(csv)
# there is a function called reader which we will be using to read the csv file that contains our data
# the dir function returns all the functions available in the csv module

# opens the file
election_data = open('election_results.csv', "r")
# closes the file, important to close the file after reading and writing data to a file
election_data.close()

# also opens the data
with open('Resources/election_results.csv') as election_data:
    print(election_data)

# sometimes we won't know the direct path to the file on our computer, so can use the os module!!
dir(os)
# very extensive list, but it has a path submodule
# there is a join() function which joins our file path components together when they are provided as separate strings then it returns a direct path
# this is called Chaining
file_to_load = os.path.join("Resources", "election_results.csv")
# this will return the path to our file
file_to_load
with open(file_to_load) as election_data:
    print(election_data)

# writing to files, after performing analysis write results to a text file

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")
# the above will throw an error because there is no folder named analysis...
# so what we can do is create an empty folder in the Election_Analysis folder
# now when the folder is created when the code is run again an empty txt file is created
outfile = open(file_to_save, "w")
outfile.write("Hello World")
# then close the file
outfile.close()

# can also do the following:
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Testing")
# we can continue to write data to this file using the .write() function
    txt_file.write("More text")
    txt_file.write("More text here too")
# but when this is run we will see that there is no space between the text added

# so to get around that write the following:
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Hello, ")
    txt_file.write("More text, ")
    txt_file.write("More text here too")
# can also put it all on one line:
    txt_file.write("Hello, Hello Again, Once more hello")
# can also use \n to get them on separate lines:
    txt_file.write("Hello \nHello on a new line")


file_to_save = os.path.join("analysis", "election_analysis.txt")

file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)
# can use the reader function now, make sure its indented  after the with open statement
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)
# this will print each row in the file as a list
        print(row[0])
# the above prints the first column, each value

# for our analysis we don't need the column headers, so can skip it with the next() method
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
# this will print the headers aka row 1!!!

# to count all the votes, we will need to initialize a variable which is called an accumulator that will increment by 1 as we read each row in the for loop
# total_votes has to be placed above the with open statement

file_to_load = os.path.join("Resources", "election_results.csv")

total_votes = 0
candidate_options = []

with open(file_to_load) as election_data:
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        candidate_options.append(candidate_name)
    print(candidate_options)
    print(total_votes)

# this will return 369,711 if i say print total_votes
# if i print candidate_options it will give all the names back, but we don't want every single instance of the name...so use an if statement

file_to_load = os.path.join("Resources", "election_results.csv")

total_votes = 0
candidate_options = []

with open(file_to_load) as election_data:
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:

        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
    print(candidate_options)

# now this code will JUST PRINT THE UNIQUE NAMES !!!!


file_to_load = os.path.join("Resources", "election_results.csv")

total_votes = 0
candidate_options = []
candidate_votes = {}

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:

        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    print(candidate_votes)
# this gives us how many votes each candidate got

file_to_load = os.path.join("Resources", "election_results.csv")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:

        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            
                
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)

   

election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
print(election_results, end="")

candidate_results = "Charles Casper Stockham: 23.0% (85,213)\nDiana DeGette: 73.8% (272,892)\nRaymon Anthony Doane: 3.1% (11,606)\n"
candidate_results

winning_candidate_summary

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
   
    txt_file.write(election_results)
    txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary)



    