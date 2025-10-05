# BMI Calculator

# Step 1: Get input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Step 2: Calculate BMI
bmi = weight / (height ** 2)

# Step 3: Determine the category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Step 4: Display the result
print(f"\nYour BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")
