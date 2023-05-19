#import modules
import os
import csv

#set the file path
budget_csv = os.path.join('Resources', 'budget_data.csv')

#set variables
date = []
changes_pl = []
number_months = 0
net_total = 0

#this will be used to calculate the changes in revenue from month to month
first_row = True

#this code is because the program was not able to read the file from the file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#open csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #looping through the data
    for row in csvreader:
        number_months = number_months + 1
        #to find date for greatest increase and decrease
        date.append(row[0])
        current_pl = int(row[1])
        #net total of profit/loss
        net_total = net_total + current_pl
        
        #to skip the first value as there is nothing to compare the value with
        if first_row:
            first_row = False 
        else:
            current_change_pl = current_pl - previous_pl
            #we calculated the net profit using incremental addition, we want the experience of using a list to calculate the avg change
            changes_pl.append(current_change_pl)

        #prepare for next row
        previous_pl = current_pl

#finding the average       
average_changes = sum(changes_pl) / len(changes_pl)

#find the greatest increase and decrease using the max and min function
greatest_increase = max(changes_pl)
greatest_decrease = min(changes_pl)

#using index function to find the corresponding date
date_increase = str(date[changes_pl.index(greatest_increase)+1])
date_decrease = str(date[changes_pl.index(greatest_decrease)+1])

#printing the data
print("Financial Analysis")
print("------------------------------")
print("Total months: " + str(number_months))
print("Total: " + "$" + str(net_total))
print("Average Change: " + "$" + str(round(average_changes, 2)))
print("Greatest Increase in Profits: " + str(date_increase) + " " + "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(date_decrease) + " " + "($" + str(greatest_decrease) + ")")

#exporting the result to a text file
with open("out.txt", "w") as f:
    f.write("Financial Analysis" + '\n')
    f.write("------------------------------" + '\n') 
    f.write("Total months: " + str(number_months) + '\n')
    f.write("Total: " + "$" + str(net_total) + '\n')
    f.write("Average Change: " + "$" + str(round(average_changes, 2)) + '\n') 
    f.write("Greatest Increase in Profits: " + str(date_increase) + " " + "($" + str(greatest_increase) + ")" + '\n')
    f.write("Greatest Decrease in Profits: " + str(date_decrease) + " " + "($" + str(greatest_decrease) + ")" + '\n')