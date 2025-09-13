decimal_number = int(input("Enter a decimal number: "))
binary = ""
if decimal_number == 0:
    binary = "0"
else:
     while decimal_number > 0:
        remainder = decimal_number % 2
        binary = str(remainder) + binary
        decimal_number = decimal_number // 2
print("Binary number is:", binary)