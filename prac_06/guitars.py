from guitar import Guitar
print("My guitars!")
guitars = []

while True:
    name = input("Name: ")
    if name:
     year = int(input("Year: "))
     cost = input("Cost: $")
     print(f"{name} ({year}) : ${cost} added.")
     guitar=Guitar(name=name, year=year, cost=cost)
     guitars.append(guitar)

    if not name:
        break
print(guitars)


print("----- snip -----")
for index, guitar in enumerate(guitars):
    if guitar.is_vintage():
        print(f"{index + 1}: {guitar.name:>14} ({guitar.year}), worth ${guitar.cost:>} (vintage)")
    else:
        print(f"{index + 1}: {guitar.name:>14} ({guitar.year}), worth ${guitar.cost:>}")
