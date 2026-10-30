consultation = int(input("Enter consultation fee: "))
diagnostic = int(input("Enter diagnostic fee: "))
treatment = int(input("Enter treatment fee: "))

total = consultation + diagnostic + treatment

if total >= 5000:
    discount = total * 10 / 100
else:
    discount = 0

final_bill = total - discount

print("Total Bill =", total)
print("Discount =", discount)
print("Final Bill =", final_bill)

if final_bill >= 5000:
    print("Category: High Payment")
else:
    print("Category: Normal Payment")
