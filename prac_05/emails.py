"""
Email and name management program
Estimate: 45 minutes
Actual:   50 minutes
"""


def extract_name_from_email(email):
    username = email.split("@")[0]
    if "." in username:
        name_parts = username.split(".")
        return " ".join(part.title() for part in name_parts)
    else:
        return username.title()


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ").upper()
        if confirm != "N" and confirm != "NO":
            email_to_name[email] = name
        else:
            correct_name = input("Name: ")
            email_to_name[email] = correct_name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()