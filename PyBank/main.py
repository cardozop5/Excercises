# Dependencies
import os
import csv



# Files to Load

data_file = os.path.join ("Resources","budget_data.csv")
Output_file = ("Resources","budget_data_txt.txt_file")

# Variables to Track

total_months = []
total = []
average_change = []
# revenue = 0
#prev_revenue = 0
#revenue_change = 0
#greatest_increase = ["", 0]
#greatest_decrease = ["", 9999999999999999999999]
#revenue_changes = []



# Read Files

with open(data_file, newline ='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')

    csv_header = next(csvreader)

    #reader = csv.DictReader(csvfile)

     # Loop through all the rows of data we collect

    for row in csvreader:
        total_months.append(row[0])
        total.append(int(row[1]))

    for i in range(len(total)-1):
        average_change.append(total[i+1])
        #Use max for profit and min for losses
        max_increase_value = max(average_change)
        max_decrease_value = min(average_change)
        #count +1
        max_increase_month = average_change.index(max(average_change))+1
        max_decrease_month = average_change.index(min(average_change))+1

        #print
    print ("Financial Analysis")
    print(f"---------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total)}")
    print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
    print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
              
    
    f = open('budget_data_txt.txt','w')
    print ("Financial Analysis")
    print(f"---------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total)}")
    print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
    print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
    f.close()

    
    
    
    # Calculate the totals

        #total_months = total_months + 1
        #print(row)
        # Keep track of changes

        #revenue_changes = revenue + prev_revenue
        #print(revenue_changes)



        # Reset the value of prev_revenue to the row I completed my analysis

        #prev_revenue = revenue

        # print(prev_revenue)



        # Determine the greatest increase

        #if (revenue_change > greatest_increase[1]):

            # greatest_increase[1] = revenue_change

            # greatest_increase[0] = row["Date"]



        #if (revenue_change < greatest_decrease[1]):

            # greatest_decrease[1] = revenue_change

            # greatest_decrease[0] = row["Date"]



        # Add to the revenue_changes list

       # revenue_changes.append(int(row[1]))



    # Set the Revenue average

    #revenue_avg = revenue_changes / len

    

    # Show Output

    # print()

    # print()

    # print()

    # print("Financial Analysis")

    # print("-------------------------")

    # print("Total Months: " + str(total_months))

    # print("Total Revenue: " + "$" + str(total_revenue))

    # print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))

    # print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 

    # print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

    

        # txt_file.write("Total Months: " + str(total_months))
    
        # txt_file.write("\n")
    
        # txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    
        # txt_file.write("\n")
    
        # txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    
        # txt_file.write("\n")
    
        # txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    
        # txt_file.write("\n")
    
        # txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
    
    


