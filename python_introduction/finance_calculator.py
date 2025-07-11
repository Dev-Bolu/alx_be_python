monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
Projected_savings = monthly_savings * 12 +(monthly_savings * 12 * 0.05)  # Adding 5% interest on savings
print("monthly savings is:", monthly_savings)
print("Projected savings after one year, with interest, is:", Projected_savings)