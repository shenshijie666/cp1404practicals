"""
State names in a dictionary with PEP 8 compliance and enhanced functionality
Estimate: 20 minutes
Actual:   25 minutes
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

max_code_length = max(len(code) for code in CODE_TO_NAME.keys())
for code, name in CODE_TO_NAME.items():
    print(f"{code:{max_code_length}} is {name}")

state_code = input("Enter short state (or press Enter to quit): ").upper()
while state_code != "":
    try:

        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state (or press Enter to quit): ").upper()
