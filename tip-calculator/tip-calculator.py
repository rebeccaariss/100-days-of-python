print("Welcome to the tip calculator!")
bill_total = float(input("What was the total bill? $"))
tip = int(input("How much would you like to tip? 10, 15, 18, or 20? "))
people = int(input("How many people will be splitting the bill? "))
total_with_tip = bill_total * (1 + tip / 100)
bill_per_person = total_with_tip / people
print(f"🧾 Each person should pay: ${round(bill_per_person, 2):.2f} 💸")