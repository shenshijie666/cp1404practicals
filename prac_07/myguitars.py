import csv
from guitar import Guitar

def main():
    guitars = load_guitars()

    print("Current Guitars:")
    print_guitars(guitars)

    name = input("Enter guitar name: ")
    year = input("Enter year made: ")
    cost = input("Enter cost: ")

    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

    guitars.sort(key=lambda x: x.year)

    print("Guitars:")
    print_guitars(guitars)

    save_guitars(guitars)

def load_guitars():
    guitars = []
    with open('guitars.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for row in reader:
            guitars.append(Guitar(row[0], row[1], row[2]))
    return guitars

def print_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def save_guitars(guitars):
    with open('guitars.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Name", "Year", "Cost"])
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == '__main__':
    main()
