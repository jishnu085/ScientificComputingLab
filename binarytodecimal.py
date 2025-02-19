binary_number = input("Enter an 8-bit binary number: ")
if len(binary_number) != 8:
    print("Invalid input. Please enter an 8-bit binary number.")
else:
    decimal_number = int(binary_number, 8)
    print("Decimal equivalent:", decimal_number)
