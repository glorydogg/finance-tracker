from datetime import datetime, date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.incomes = []
        self.categories = ["Food", "Insurance", "Savings", "Entertainment", "Transportation", "Miscellaneous"]

    def _get_valid_date(self, date_str):
        "Helper to parse and validate date string."
        try:
            if date_str.strip() == "":
                return date.today()
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return None

    def add_expense(self):
        date_str = input("Enter date (YYYY-MM-DD), or leave blank for today: ") 
        expense_date = self._get_valid_date(date_str) #Input validation
        if expense_date is None:
            return

        category = input(f"Enter category {self.categories}: ")
        if category.lower() not in self.categories.lower():
            print("Invalid category.")
            return

        try:
            cost = float(input("Enter cost of expense: "))
        except ValueError:
            print("Cost must be a number.")
            return

        self.expenses.append({
            "date": expense_date,
            "category": category,
            "amount": cost
        })
        print(f"Expense added: {expense_date}, {category}, ${cost:.2f}")

    def add_income(self, amount, income_date):
        if not isinstance(amount, (int, float)):
            print("Amount must be a number.")
            return

        if not isinstance(income_date, date):
            print("Date must be a valid date object.")
            return

        self.incomes.append({
            "date": income_date,
            "amount": amount
        })
        print(f"Income of ${amount:.2f} added on {income_date}")
    
    def get_expense_by_category(self, category_name):
        if category_name not in self.categories:
            print("Invalid category.")

        matching_expenses = [e for e in self.expenses if  e["category"] ==category_name]

        if not matching_expenses:
            print(f"No expenses found in category: {category_name}")
            return

        print(f"Expenses in {category_name}:")
        total = 0.0
        for expense in matching_expenses:
            print(f"- {expense['date']}: ${expense['amount']:.2f}")
            total += expense["amount"]
        print(f"Total: ${total:.2f}")

    def get_expense_by_date(self, start_date, end_date):
        filtered_expenses = []
        for expense in self.expenses:
            if start_date <= expense["date"] <= end_date:
                filtered_expenses.append(expense)
            
            print("There are no expenses within this range")
                
        filtered_expenses = sorted(filtered_expenses, key=lambda e: e["date"])

        for expense in filtered_expenses:
            print(f"- {expense['date']}: ${expense['amount']:.2f}")
            total += expense['amount']
            print(f"Total: ${total:.2f}")

    def view_all_expenses(self):
        for expense in self.expenses:
            print(expense)

if __name__ == "__main__":
    tracker = ExpenseTracker()
    while True:
        print("Option: \n1 Add expense \n2 Add income \n3 View by category \n4 View by date range \n5 View all")
        choice = input("Enter 1-6")
        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            try:
                amt = float(input("Enter income amount: "))
                date_str = input("Enter income date (YYYY-MM-DD), or leave blank for today: ")
                d = tracker._get_valid_date(date_str)
                if d: tracker.add_income(amt, d)
            except ValueError:  
                print("Invalid Input")
        elif choice == "3":
            cat = input(f"Enter category {tracker.categories}: ")
            tracker.get_expense_by_category(cat)
        elif choice == "4":
            s = tracker._get_valid_date(input("Start date (YYYY-MM-DD): "))
            e = tracker._get_valid_date(input("End date (YYYY-MM-DD): "))
            if s and e:
                tracker.get_expense_by_date(s, e)
        elif choice == "5":
            tracker.view_all_expenses()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")









    
 