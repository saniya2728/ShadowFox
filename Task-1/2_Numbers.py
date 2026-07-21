#  Part 1: Format Function 
result = format(145, 'o')
print(f"145 in Octal is: {result}")

#  Part 2: Circular Pond
radius = 84
pi = 3.14
area = pi * (radius ** 2)
print(f"Area of the pond: {area} sq meters")

# Bonus: Total water
water = area * 1.4
print(f"Total water: {int(water)} liters")

#  Part 3: Speed Calculation
dist = 490
time_sec = 7 * 60
speed = dist / time_sec
print(f"Speed: {int(speed)} m/s")
