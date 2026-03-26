# app.py Simple Tax Calculator [cite: 22]
def calculate_tax(income):
    if income <= 150000:
        return 0 [cite: 24, 25]
    elif income <= 300000:
        return (income - 150000) * 0.05 [cite: 26, 27]
    elif income <= 500000:
        return 7500 + (income - 300000) * 0.10 [cite: 28, 29, 30]
    elif income <= 750000:
        return 27500 + (income - 500000) * 0.15 [cite: 31, 32, 33]
    else:
        return 65000 + (income - 750000) * 0.20 [cite: 34, 35, 36]

if __name__ == "__main__": [cite: 37, 38]
    test_incomes = [100000, 250000, 400000, 600000, 1000000] [cite: 39]
    for income in test_incomes:
        tax = calculate_tax(income) [cite: 40]
        print(f"Income: {income:>10,} THB | Tax: {tax:>10,.2f} THB") [cite: 41]
