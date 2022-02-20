print("Welcome to the tip calaculator.")
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

tip = (total_bill * (percent_tip/100))
pay = total_bill + tip
pay_per_person = pay/split
pay_per_person = round(float(pay_per_person), 2)

print(f"Each person should pay: ${pay_per_person}")