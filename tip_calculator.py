# tip calculator

# welcome message
print("Welcome to the tip calculator! ")

# input the bill total
bill = None
while bill is None:
    try:
        bill = float(input("How much was dinner? "))
    except:
        print("Numbers only please!".format(bill))

# input the percentage you want to tip
percent_tip = None
while percent_tip is None:
    try:
        percent_tip = float(input("What percentage tip do you want to give? "))
    except:
        print("Numbers only please!".format(bill))

# calculate the tip
tip = round((percent_tip / 100 * bill), 2)

#calculate the total bill plus tip
total = round((bill + tip), 2)

print("Your tip amount is: $", tip)
print("Your total bill is: $", total)
