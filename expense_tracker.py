print("===== PERSONAL EXPENSE TRACKER =====")

expenses = []

while True:
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expenses.append({
        "amount": amount,
        "category": category
    })

    choice = input("Add another expense? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\n===== EXPENSE REPORT =====")

total = 0

for expense in expenses:
    print(expense["category"], ":", expense["amount"])
    total += expense["amount"]

print("Total Expense:", total)
