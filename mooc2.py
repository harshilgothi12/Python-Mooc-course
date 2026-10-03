class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title
        title = self.name.center(30, "*")

        # Ledger entries
        items = []
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            # Description left-aligned, amount right-aligned
            items.append(f"{description:<23}{amount:>7}")

        # Total
        total = f"Total: {self.get_balance():.2f}"

        return title + "\n" + "\n".join(items) + "\n" + total


def create_spend_chart(categories):
    # Calculate total spending (withdrawals only)
    spent = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages rounded DOWN to nearest 10
    percentages = []

    for amount in spent:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((amount / total_spent) * 100)
            percentage = (percentage // 10) * 10

        percentages.append(percentage)

    # Start chart
    chart = "Percentage spent by category\n"

    # Bars from 100 to 0
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    # Remove final newline
    return chart.rstrip("\n")