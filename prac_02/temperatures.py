def C_to_F():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def F_to_C():
    global celsius
    celsius = (fahrenheit - 32) * 5 / 9

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        C_to_F()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        F_to_C()
        print(f"result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")


