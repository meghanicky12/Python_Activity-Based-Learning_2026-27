venue = int(input("Enter venue cost: "))
equipment = int(input("Enter equipment cost: "))
food = int(input("Enter catering cost: "))
transport = int(input("Enter transport cost: "))
sponsorship = int(input("Enter sponsorship amount: "))
fee = int(input("Enter registration fee: "))

total = venue + equipment + food + transport

shortfall = total - sponsorship

participants = total / fee

print("Total Expense =", total)
print("Sponsorship Shortfall =", shortfall)
print("Minimum Participants =", int(participants) + 1)
