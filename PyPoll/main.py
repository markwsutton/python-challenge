#!/usr/bin/env python
# coding: utf-8

# In[3]:


#this is PyPoll - final code

import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Define the function and have it accept the 'election_data' as its sole parameter
def votes_calc(election_data):
    
    # Set variable for output file
    output_file = os.path.join('.', 'Analysis',"ElectionTally.txt")
    
    # Open the output file using with open, assign content to variable "datafile", init winner
    with open(output_file, "w", newline="") as datafile:
        winner = ""
   
        #print title and total votes
        print("Election Results")
        print("-" * 25)
        print("Total votes: " + str(len(voter_list)))
        print("-" * 25)
        
        #export that data
        datafile.write("Election Results\n")
        datafile.write("-" * 25 + "\n")
        datafile.write("Total votes: " + str(len(voter_list)) + "\n")
        datafile.write("-" * 25 + "\n")
    
        #loop to get index then print, export all candidates and name, percent, votes received
        candidateindex = -1
        for i in uniquecandidate_list:
            candidateindex += 1
            percent_votes = str(round(unique_counts_list[candidateindex]/(len(voter_list)) * 100,4))
            print(uniquecandidate_list[candidateindex] + ": " + str(percent_votes) + "%  (" + str(unique_counts_list[candidateindex]) + ")")
            datafile.write(uniquecandidate_list[candidateindex] + ": " + str(percent_votes) + "%  (" + str(unique_counts_list[candidateindex]) + ")\n")
 
        # calculate, print, and export winner
        winner_index = unique_counts_list.index(max(unique_counts_list))
        winner = uniquecandidate_list[winner_index]
    
        print("-" * 25)
        print("Winner: " + winner)
        datafile.write("-" * 25 + "\n")
        datafile.write("Winner: " + winner + "\n")
    
with open(csvpath, 'r') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents, account for header, init lists
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    voter_list = []
    votegetter_list = []
    uniquecandidate_list = []
    unique_counts_list = []
    
    # Loop through the data
    for row in csvreader:
        voter_list.append(row[0])
        votegetter_list.append(row[2])      
      
    # get list of unique candidates, put them in list uniquecandidate_list
    for x in votegetter_list: 
        # check if exists in uniquecandidate_list or not 
        if x not in uniquecandidate_list: 
            uniquecandidate_list.append(x)
        
    # count the votes for how ever many unique candidates exist
    for y in uniquecandidate_list:
        votes = votegetter_list.count(y)
        unique_counts_list.append(votes)
        
    #run the function 
    votes_calc(row)


# In[ ]:




