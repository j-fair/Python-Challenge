import os
import csv

#Declaration of variables
total_months = 0
net_total = 0
monthly_change = []
month_counter = []
greatest_increase = 0
greatest_inc_month = 0
greatest_decrease = 0
greatest_dec_month = 0

path = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')

with open(path) as pybank:
    csvreader = csv.reader(pybank, delimiter= ',')

    header = next(csvreader)
    row = next(csvreader)

    #variable here for determing change from previous row
    previous_row = int(row[1])

    total_months += 1
    net_total += int(row[1])
    greatest_increase = int(row[1])
    greatest_inc_month = row[0]

    for row in csvreader:
        total_months += 1

        net_total += int(row[1])
        dollar_difference = int(row[1]) - previous_row
        monthly_change.append(dollar_difference)
        previous_row = int(row[1])
        month_counter.append(row[0])

        #Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_inc_month = row[0]

        #Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_dec_month = row[0]
    
    #Average and date calculation
    average_change = sum(monthly_change) / len(monthly_change)

    most = max(monthly_change)
    least = min(monthly_change)

#Printing Summary
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_inc_month}, (${most})")
print(f"Greatest Decrease in Profits:, {greatest_dec_month}, (${least})")

#File we are writing to
output_file = os.path.join('.', 'Resources', 'budget_data_analysis.text')

#Writing to text file
with open(output_file, 'w+') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_inc_month}, (${most})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_dec_month}, (${least})\n")