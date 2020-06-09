#!/usr/bin/env python
# coding: utf-8

# PyBank - final; streamlined the code by moving export to within function, fixed rounding error

import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Define the function and have it accept the 'bank_data' as its sole parameter
def finance_calc(bank_data):
    # Set variable for output file
    output_file = os.path.join('.', 'Analysis',"PyAnalysisTest.txt")

    #  Open the output file using with open, assign it to variable "datafile"
    with open(output_file, "w", newline="") as datafile:
    
        # variables for data in the two columns
        #bank_month = str(bank_data[0])
        #profit_loss = int(bank_data[1])
    
        #print and calculate stuff
        print("Financial Analysis")
        print("-" * 25)
        print("Total months: " + str(len(profit_list)))
    
        print("Total: $ " + str(sum(profitloss_list)))
        print("Average change: $ " + str(round((profitloss_list[85]-profitloss_list[0]) / (len(profit_list)-1),2)))

        max_month_index = profit_list[monthly_change.index(max(monthly_change))]
        print("Greatest Increase in Profits: " + max_month_index[0] + "  $ " + str(max(monthly_change)))    
    
        min_month_index = profit_list[monthly_change.index(min(monthly_change))]
        print("Greatest Decrease in Profits: " + min_month_index[0] + "  $ " + str(min(monthly_change))) 
        
        datafile.write("Financial Analysis\n")
        datafile.write("-------------------\n")
        datafile.write("Total months: " + str(len(profit_list)) + "\n")
        datafile.write("Total: $ " + str(sum(profitloss_list)) + "\n")
        datafile.write("Average change: $ " + str(round((profitloss_list[85]-profitloss_list[0]) / (len(profit_list)-1))) + "\n")
        datafile.write("Greatest Increase in Profits: " + max_month_index[0] + "  $ " + str(max(monthly_change)) + "\n")
        datafile.write("Greatest Decrease in Profits: " + min_month_index[0] + "  $ " + str(min(monthly_change)))

with open(csvpath, 'r') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    profit_list = []
    profitloss_list = []
    monthly_change = []
    previous_month = 867884

    # Loop through the data
    for row in csvreader:

        # do the loop calculations
        # create list and append each value to profit list  
        profit_list.append(row)
        profitloss_list.append(int(row[1]))
        monthly_change.append((int(row[1])-previous_month))
        previous_month = int(row[1])
        
    finance_calc(row)       





