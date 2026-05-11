#Temperature Conversion

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("Temperature Conversion")
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

if unit.upper() == "C":
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp} °C is equal to {round(converted_temp, 2)} °F.")
elif unit.upper() == "F":
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp} °F is equal to {round(converted_temp, 2)} °C.")
else:
    print("Error: Invalid unit.")