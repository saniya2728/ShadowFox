# 1.BMI
meters = float(input("Enter height in meters: "))
kilo = float(input("Enter weight in kilograms: "))

BMI = kilo / (meters ** 2)

print("BMI =", BMI)

if BMI >= 30:
    print("Obesity")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
else:
    print("Underweight")



#  2.List of cities
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Get input from user
city = input("Enter a city name: ")

# Check the country
if city in Australia:
    print("The city belongs to Australia.")
elif city in UAE:
    print("The city belongs to UAE.")
elif city in India:
    print("The city belongs to India.")
else:
    print("City not found in the list.")

# 3.list of cities for each country
Australia = ["Sydney", "Melbourne", "Brisbane"]
India = ["Mumbai", "Delhi", "Bangalore", "Chennai"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah"]

# Get input from the user
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check if both cities belong to the same country
if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in India and city2 in India:
    print("Both cities are in India")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
else:
    print("They don't belong to the same country")
