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
        if category not in self.categories:
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
    
    def get_expense_by_category(category_name, self):
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







    
 