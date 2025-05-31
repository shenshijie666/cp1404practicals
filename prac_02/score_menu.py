def get_valid_score():
    while True:
        score = int(input("Enter a valid score (0-100 inclusive): "))
        if 0 <= score <= 100:
            return score
        else:
            print("Score must be between 0 and 100, please try again.")

def print_results(s):
    if s < 0 or s > 100:
        return "Invalid score"
    elif s >= 90:
        return "Excellent"
    elif s >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * score)

def main():
    while True:
        print("(G)et""\n""(P)rint""\n""(S)how stars""\n""(Q)uit""")
        choice = input("Enter").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = print_results(score)
            print("Result:", result)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main()