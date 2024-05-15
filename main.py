total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would? Just the number not % needed. "))
people = int(input("How many people to split the bill? Make sure to count yourself! "))
tip_percentage = tip_percentage / 100
tip_amount = total_bill * tip_percentage
print("Tip amount is: $" + str(tip_amount))
total_bill = total_bill + tip_amount
print("Total bill amount is: $" + str(total_bill))
split_bill = total_bill / people
print("Each person should pay: $" + str(split_bill))