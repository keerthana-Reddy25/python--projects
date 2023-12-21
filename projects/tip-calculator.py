
print("Welcome to the tip calculator.")
initialBill = float(input("What was the total bill? $"))
tipPercentage = float(input("What percentage tip would you like to give> 10, 12, or 15? "))
totalPeople = int(input("How many people to split the bill? "))
calculatedTotalBill = ((initialBill * tipPercentage/100) + initialBill) / totalPeople
roundedCalculation = round(calculatedTotalBill, 2)
print("Each person should pay : $",roundedCalculation)