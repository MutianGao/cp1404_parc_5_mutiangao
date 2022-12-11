def main():

    email_to_name = {}
    email = input("Enter the Email: ")

    while email != "":
        name = email_name_get(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def email_name_get(email):
    get_name_part = email.split('@')[0]
    name_except_point = get_name_part.split('.')
    name = " ".join(name_except_point).title()
    return name


main()