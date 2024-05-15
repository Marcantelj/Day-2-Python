total_bill = float(input("What was the total bill? $")) # Collect Total Bill in US Dollars
tip_percentage = int(input("What percentage tip would? Just the number not % needed. ")) # Collect Tip %
people = int(input("How many people to split the bill? Make sure to count yourself! ")) # Collect amount of people to split bill
tip_percentage = tip_percentage / 100 # Calculation of % 
tip_amount = total_bill * tip_percentage # Calculation of tip amount to add to total bill 
print("Tip amount is: $" + str(tip_amount)) 
total_bill = total_bill + tip_amount # Sum of total bill and tip amount
print("Total bill amount is: $" + str(total_bill))
split_bill = total_bill / people # finding the split bill amount
split_bill = round(split_bill, 2) # Added rounding to split _bill  
split_bill = "{:.2f}".format(split_bill) #Added formatting to split_bill to show hundredths place
print("Each person should pay: $" + str(split_bill))
