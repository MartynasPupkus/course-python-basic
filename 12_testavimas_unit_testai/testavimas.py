

def add_income(income, amount): 
    income += amount
    print(f"Income added: {amount}") 
    return income 

def add_expense(expenses, amount):
    expenses += amount 
    print(f"Expense added: {amount}")
    return expenses 

def calculate_balance(income, expenses): 
    balance = income - expenses 
    print(f"Current balance: {balance}") 


income = 0 
expenses = 0 

while True: 
    print("\nOptions:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Calculate Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ") 

    if choice == '1': 
        amount = float(input("Enter the income amount: ")) 
        income = add_income(income, amount) 
    elif choice == '2':
        amount = float(input("Enter the expense amount: ")) 
        expenses = add_expense(expenses, amount) 
    elif choice == '3': 
        calculate_balance(income, expenses) 
    elif choice == '4': 
        print("Exiting the budget calculator. Goodbye!") 
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")