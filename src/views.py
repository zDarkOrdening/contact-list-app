def show_menu():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print("Contact List Menu\n")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Edit contact")
    print("4. Mark/unmark as favorite")
    print("5. Show favorite contacts")
    print("6. Delete contact")
    print("7. Exit")


def get_user_input():
    return input("\nChoose an option: ")


def get_contact_data():
    name = input("\nEnter the contact name: ")
    phone = input("\nEnter the contact phone: ")
    email = input("\nEnter the contact email: ")
    return name, phone, email


def display_contacts(contacts, favorite_only=False):
    counter = 0
    if not contacts:
        print("\nNo contacts to show.\n")
        return False

    for index, contact in enumerate(contacts):
        if favorite_only and not contact.favorite:
            continue
        favorite = "| ★" if contact.favorite else ""
        print(
            f"\n{index + 1}. {contact.name} | {contact.phone} | {contact.email} {favorite}\n"
        )
        counter += 1
    if counter <= 0:
        print("\nNo favorite contacts to show.\n")
        return False
    return True


def get_contact_edit_data():
    print("Just press enter to not change an information")
    name = input("Enter the new contact name: ")
    phone = input("Enter the new contact phone: ")
    email = input("Enter the new contact email: ")
    return name, phone, email


def choose_contact():
    choose = int(input("\nPlease choose the contact you want: "))
    return choose
