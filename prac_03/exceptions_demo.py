#ValueError Appears when either of the two inputs is not an integer
#ZeroDivisionError Appears when denominator is zero
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Add conditional checks to ensure that the denominator is not zero
    if denominator == 0:
        raise ValueError("Denominator cannot be zero!")

    fraction = numerator / denominator
    print(fraction)
except ValueError as ve:
    if "cannot be zero" in str(ve):
        print(ve)
    else:
        print("Numerator and denominator must be valid numbers!")

print("Finished.")

