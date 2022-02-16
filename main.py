print("Welcome to the tip calculator.\n")


total = int(input("What was the total of your bill?\n"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
split = int(input("How many people are going to split the bill?\n"))

convertedPercentage = percentage / 100

billTotal = (total * convertedPercentage + total) / split

print(f"Your total is {billTotal} per person")