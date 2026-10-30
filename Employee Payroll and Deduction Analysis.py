basic = int(input("Enter basic salary: "))
allowance = int(input("Enter allowance: "))
overtime = int(input("Enter overtime amount: "))
incentive = int(input("Enter incentive: "))

gross = basic + allowance + overtime + incentive

if gross <= 20000:
    deduction = gross * 5 / 100
else:
    deduction = gross * 10 / 100

net_salary = gross - deduction

print("Gross Salary =", gross)
print("Deduction =", deduction)
print("Net Salary =", net_salary)
