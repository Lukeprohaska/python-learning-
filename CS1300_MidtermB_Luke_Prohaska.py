weight = float(input("Enter weight: "))
unit_system = input("Enter unit system (M/I): ")

if unit_system == 'M':
    height = float(input("Enter height (meters): "))

    bmi = weight / (height ** 2)


elif unit_system == 'I':
    height = float(input("Enter height (inches): "))
    
    bmi = (weight * 703) / (height ** 2)


else:
    print("Invalid unit system.")

    exit()

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal weight"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")




password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

Length_pass = len(password) >= 8

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True


results = [Length_pass, has_upper, has_lower, has_digit, has_special]
criteria_met = sum(results)


print(f"\nLength >= 8:  {'PASS' if Length_pass else 'FAIL'}")
print(f"Uppercase:    {'PASS' if has_upper else 'FAIL'}")
print(f"Lowercase:    {'PASS' if has_lower else 'FAIL'}")
print(f"Digit:        {'PASS' if has_digit else 'FAIL'}")
print(f"Special char: {'PASS' if has_special else 'FAIL'} ")

print(f"\nCriteria met: {criteria_met} / 5")


if criteria_met == 5:
    rating = "Strong"
elif criteria_met >= 3:
    rating = "Moderate"
elif criteria_met >= 1:
    rating = "weak"
else:
    rating = "No password entered"
    
print(f"Strength: {rating}")





