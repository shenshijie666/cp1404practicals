"""
Hexadecimal colour code lookup program
Estimate: 30 minutes
Actual:   35 minutes
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "BabyBlue": "#89cff0",
    "Coral": "#ff7f50",
    "DarkGreen": "#006400",
    "Gold": "#ffd700",
    "HotPink": "#ff69b4",
    "Indigo": "#4b0082",
    "Lavender": "#e6e6fa",
    "Magenta": "#ff00ff",
    "Navy": "#000080"
}

max_colour_length = max(len(colour) for colour in COLOUR_TO_HEX.keys())
print("Available colours:")
for colour, hex_code in COLOUR_TO_HEX.items():
    print(f"{colour:{max_colour_length}}: {hex_code}")

colour_name = input("\nEnter a colour name (or press Enter to quit): ").title()
while colour_name != "":
    try:
        print(f"{colour_name} hex code is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name (or press Enter to quit): ").title()
