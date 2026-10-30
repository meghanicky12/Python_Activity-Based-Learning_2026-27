name = input("Enter student name: ")
marks = int(input("Enter aggregate marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))
maths = int(input("Enter Maths marks: "))

if marks >= 75 and maths >= 50 and attendance >= 75 and income <= 200000:
    print(name, "Eligible for Scholarship")
else:
    print(name, "Not Eligible")
