prices = []

print("Enter prices of 6 items:")

for i in range(6):
    price = float(input(f"Item {i + 1}: "))
    prices.append(price)

budget = float(input("\nEnter total budget: "))

bought_items = []
total_spent = 0

for i in range(len(prices)):
    price = prices[i]

    if total_spent + price <= budget:
        bought_items.append(price)
        total_spent += price
        print(f"\nItem {i + 1} = {price:g} -> buy")
    else:
        print(f"\nItem {i + 1} = {price:g} -> cannot buy")

    print(f"Current total = {total_spent:g}")

remaining_budget = budget - total_spent

print(f"\nBought items: {bought_items}")
print(f"Total spent: {total_spent:g}")
print(f"Remaining budget: {remaining_budget:g}")
