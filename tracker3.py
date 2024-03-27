class ExpenseTracker:
    def __init__(self, initial_expenses=None):
        if initial_expenses is None:
            initial_expenses = {}
        self.expenses = initial_expenses

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def total_expenses(self):
        total = 0
        for category, amount in self.expenses.items():
            total += amount
        return total

    def category_expenses(self, category):
        return self.expenses.get(category, 0)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("Expense Tracker:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")


# Example usage
def main():
    initial_expenses = {
        "Food": 50,
        "Transportation": 30,
        "Entertainment": 20,
    }
    tracker = ExpenseTracker(initial_expenses)

    print("Total expenses:", tracker.total_expenses())
    print("Food expenses:", tracker.category_expenses("Food"))
    print("Transportation expenses:", tracker.category_expenses("Transportation"))
    print("Entertainment expenses:", tracker.category_expenses("Entertainment"))
    tracker.view_expenses()


if __name__ == "__main__":
    main()
