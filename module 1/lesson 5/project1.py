temperature = float(input("Enter the current temperature in: "))

if temperature >= 25:
    print("It's warm, Rohan can wear light and soft clothes")
elif 15 <= temperature < 25:
    print("Its a bit cool, Rohan can wear a light jacket")
else:
    print("Its cold, Rohan should wear a jacket")