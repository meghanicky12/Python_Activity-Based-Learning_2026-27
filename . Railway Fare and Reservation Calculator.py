distance = int(input("Enter distance: "))
age = int(input("Enter age: "))

if distance <= 100:
    fare = distance * 2
elif distance <= 500:
    fare = distance * 3
else:
    fare = distance * 4

if age >= 60:
    fare = fare * 50 / 100

reservation = 50
total = fare + reservation

print("Ticket Fare =", fare)
print("Reservation Fee =", reservation)
print("Total Fare =", total)
