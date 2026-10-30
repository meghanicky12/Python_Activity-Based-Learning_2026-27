price = int(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 5000:
    discount = total * 10 / 100
else:
    discount = total * 5 / 100

tax = total * 5 / 100

final_bill = total - discount + tax

print("Total =", total)
print("Discount =", discount)
print("Tax =", tax)
print("Final Bill =", final_bill)
