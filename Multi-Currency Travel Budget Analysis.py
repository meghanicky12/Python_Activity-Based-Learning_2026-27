rate = float(input("Enter exchange rate: "))
hotel = float(input("Enter hotel expense: "))
food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))

total = hotel + food + travel

conversion_fee = total * 2 / 100

final_amount = total * rate + conversion_fee * rate

print("Hotel Cost =", hotel * rate)
print("Food Cost =", food * rate)
print("Travel Cost =", travel * rate)
print("Total INR =", final_amount)

if final_amount <= 50000:
    print("Within Budget")
else:
    print("Over Budget")
