from guitar import Guitar
guitars = [
    Guitar("Gibson L-5 CES", 1922, 16035.40),
    Guitar("Another Guitar", 2013)
]
for obj in guitars:
    print(f"{obj.name} get_age() - Expect {2024-obj.year}. Got {obj.get_age()}")

for obj in guitars:
    print(f"{obj.name} is_vintage - Expect {(2024-obj.year) >= 50}. Got {obj.is_vintage()}")