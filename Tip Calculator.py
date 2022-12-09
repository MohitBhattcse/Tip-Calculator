                 # welocome to the tip calculator
# Today we going to make a tip calculator
# Input total bill
Bill=int(input())
#now input what percentage of bill is paying as a tip
percentage=float(input())
# now multiply it with total bill to get the tip
tip=int(Bill//percentage)
print(tip)
# Now add the total tip with the Bill
New_Bill=int(Bill+tip)
print(New_Bill)
#Now Your final bill is ready with the tip
print(f"Your bill is {Bill},your tip is {tip}, and your final bill after adding tip is {New_Bill}")
