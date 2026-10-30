usage = int(input("Enter data usage in GB: "))
budget = int(input("Enter your budget: "))

plan1 = 199
plan2 = 299
plan3 = 399

if usage <= 2 and plan1 <= budget:
    print("Best Plan: Plan 1")
    print("Cost =", plan1)

elif usage <= 5 and plan2 <= budget:
    print("Best Plan: Plan 2")
    print("Cost =", plan2)

elif usage <= 10 and plan3 <= budget:
    print("Best Plan: Plan 3")
    print("Cost =", plan3)

else:
    print("No suitable plan available")
