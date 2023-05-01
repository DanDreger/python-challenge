import os

import csv

from statistics import mean 
import locale
locale.setlocale( locale.LC_ALL, '' )


budget_csv = os.path.join(".", "Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    month_number = 0
    total = 0
    current_income = 0
    greatest_Increase = 0
    greatest_Decrease = 0
    previous_income=0
    greatest_profit_decrease=["", 0]
    greatest_profit_increase=["", 0]
    all_profit_changes=[]
    average_change = 0
   

    for i in csvreader:

        #store curent income and current month in variables
        current_income = int(i[1])
        current_month = str(i[0])

        # Track the number of months in a month_number variable and add 1 to it each loop
        month_number = month_number + 1

        #calculate running total and store it in total variable
        total = total + current_income
        

        # month >1 because there is no previous income value for month 0
        if month_number > 1:
            income_difference = current_income - previous_income
        
            #calculate the profit change from previous month to this month and put that difference in all_profit_changes
            profit_change = current_income-previous_income
            all_profit_changes.append(profit_change)

            if (current_income > 0) and (previous_income < 0) and (income_difference > greatest_Increase):
                greatest_Increase = income_difference
                greatest_profit_increase = [current_month, income_difference]
            elif current_income < 0 and previous_income > 0 and income_difference < greatest_Decrease:
                greatest_Decrease = income_difference
                greatest_profit_decrease = [current_month, income_difference]

        previous_income = int(i[1])

average_change = mean(all_profit_changes)

output_lines = [f"Total months: {month_number}", f"Total: ${total}", f"Average Change: $ {locale.currency( average_change, grouping=True )}", f"Greatest Increase in Profits: {greatest_profit_increase[0]} (${greatest_profit_increase[1]})", f"Greatest Decrease in Profits: {greatest_profit_decrease[0]} (${greatest_profit_decrease[1]})" ]

for line in output_lines:
    print(line)

with open('PyBank_Results.txt', 'w') as f:
    for line in output_lines:
        f.write(line)
        f.write('\n')

