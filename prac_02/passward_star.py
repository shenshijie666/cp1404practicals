def main():
    pwd = get_password()
    the_password(pwd)


def the_password(pwd):
    print("*" * len(pwd))


def get_password():
    pwd = input("Enter your password:")
    while len(pwd) < 8:
        print("Too short!")
        pwd = input("Enter your password:")
    return pwd


main()