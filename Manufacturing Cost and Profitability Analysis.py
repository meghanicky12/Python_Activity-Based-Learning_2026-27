material = int(input("Enter material cost: "))
labour = int(input("Enter labour cost: "))
machine = int(input("Enter machine cost: "))
selling = int(input("Enter selling price: "))

total_cost = material + labour + machine

profit = selling - total_cost

print("Total Cost =", total_cost)
print("Profit =", profit)

if profit >= 1000:
    print("Target Achieved")
else:
    print("Target Not Achieved")
