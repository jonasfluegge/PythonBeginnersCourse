initial_stock = int(input("Please enter an initial stock level: "))
num_months = int(input("Please enter the number of month to plan: "))
i = 0
months_planned_production = []

while i <= num_months - 1:
    months_planned_production.append(int(input("Please enter the planned sales quantity: ")))
    i += 1

i = 0
print("The resulting production quantities are:")

while i <= num_months - 1:
    if initial_stock - months_planned_production[i] > 0:
        initial_stock = initial_stock - months_planned_production[i]
        print("Production quantity month ", i, "- 0")
        i += 1
    else:
        break
