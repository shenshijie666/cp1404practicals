"""
Wimbledon champions data analysis
Estimate: 60 minutes
Actual:   70 minutes
"""

import csv


def read_wimbledon_data(filename):
    champions = []
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for row in reader:
            champions.append(row[2])
            countries.add(row[1])
    return champions, countries


def count_championships(champions):
    champ_count = {}
    for champ in champions:
        champ_count[champ] = champ_count.get(champ, 0) + 1
    return champ_count


def display_results(champ_count, countries):
    print("Wimbledon Champions:")
    sorted_champs = sorted(champ_count.items())
    for champ, count in sorted_champs:
        print(f"{champ} {count}")

    sorted_countries = sorted(countries)
    countries_str = ", ".join(sorted_countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(countries_str)


def main():
    filename = "wimbledon.csv"
    champions, countries = read_wimbledon_data(filename)
    champ_count = count_championships(champions)
    display_results(champ_count, countries)


if __name__ == "__main__":
    main()