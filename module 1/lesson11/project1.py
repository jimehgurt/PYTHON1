number = int(input("Enter a number: "))
n = int(input("Enter the highest power you want to calculate: "))
print(f"\nPowers of {number} up to {n} are:")
for i in range(1, n + 1):
    result = number ** i
    print(f"{number}^{i} = {result}")