# Python compund interest calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

# Convert rate from percentage to decimal
rate = rate / 100

# Calculate compound interest
amount = principal * (1 + rate) ** time
compound_interest = amount - principal

# Display the results
print(f"Compound Interest: {round(compound_interest, 2)}")
print(f"Total Amount: {round(amount, 2)}")