# Dependencies
import os
import csv



# Files to Load

data_file = os.path.join ("Resources","budget_data.csv")
Output_file ="Resources/budget_data_txt.txt_file"

# Variables to Track

total_months = 0
total_revenue = 0
revenue = 0
prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
revenue_changes = []



# Read Files

with open(data_file) as csvfile:
   # csvreader = csv.reader(csv,delimiter = ',')

    #csv_header = next(csvreader)

    reader = csv.DictReader(csvfile)

     # Loop through all the rows of data we collect

    for row in reader:
        #total_months.append(row[0])


              # Calculate the totals

        total_months = total_months + 1
        print(row)
        # Keep track of changes

        revenue_changes = revenue - prev_revenue
        print(revenue_changes)



        # Reset the value of prev_revenue to the row I completed my analysis

        prev_revenue = revenue

        # print(prev_revenue)



        # Determine the greatest increase

        if (revenue_change > greatest_increase[1]):

            greatest_increase[1] = revenue_change

            greatest_increase[0] = row["Date"]



        if (revenue_change < greatest_decrease[1]):

            greatest_decrease[1] = revenue_change

            greatest_decrease[0] = row["Date"]



        # Add to the revenue_changes list

       # revenue_changes.append(int(row[1]))



    # Set the Revenue average

    revenue_avg = sum(revenue_changes) / len(revenue_changes)

    

    # Show Output

    print()

    print()

    print()

    print("Financial Analysis")

    print("-------------------------")

    print("Total Months: " + str(total_months))

    print("Total Revenue: " + "$" + str(total_revenue))

    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))

    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 

    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

    
    with open(Output_file, "w") as txt_file:

        txt_file.write("Total Months: " + str(total_months))
    
        txt_file.write("\n")
    
        txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    
        txt_file.write("\n")
    
        txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    
        txt_file.write("\n")
    
        txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    
        txt_file.write("\n")
    
        txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
    
    


