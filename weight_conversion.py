#Python weight converter

weight = float(input("Enter weight: "))
unit = input("Enter unit (kg, lb, g): ")

if unit == "kg":
    converted_weight = weight * 2.20462
    print(f"{weight} kg is equal to {round(converted_weight, 2)} lb.")
elif unit == "lb":
    converted_weight = weight * 0.453592
    print(f"{weight} lb is equal to {round(converted_weight, 2)} kg.")
elif unit == "g":
    converted_weight = weight * 0.001
    print(f"{weight} g is equal to {round(converted_weight, 2)} kg.")
else:
    print("Error: Invalid unit.")