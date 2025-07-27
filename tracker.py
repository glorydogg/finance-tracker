from datetime import datetime, date


def add_expense():
        categories = ["Food", "Insurance", "Savings", "Entertainment", "Transportation", "Miscellaneous"]
        
        date_str = input("Enter date(YYYY-MM-DD):")
        try:
                if date_str.strip() == "":
                        expense.date = date.today()
                else:
                        expense_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        