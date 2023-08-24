def calculate_bonus(salary, grade):
    if salary < 10000:
        bonus_percentage = 0.1  # 10% base bonus
        bonus_percentage += 0.02  # Extra 2% for salary < $10,000
    else:
        bonus_percentage = 0.05 if grade == 'A' else 0.1
    
    bonus_amount = salary * bonus_percentage
    total_salary = salary + bonus_amount
    return bonus_amount, total_salary

# Get input from the user
salary = float(input("Enter the employee's salary: "))
grade = input("Enter the employee's grade (A/B): ").upper()

bonus_amount, total_salary = calculate_bonus(salary, grade)

print(f"Bonus amount: ${bonus_amount:.2f}")
print(f"Total salary: ${total_salary:.2f}")




