from src.models import Contact, List
from src.views import (
    get_contact_data,
    display_contacts,
    get_contact_edit_data,
    choose_contact,
)

contacts_list = List()


def add_contact():
    name, phone, email = get_contact_data()
    contact = Contact(name, phone, email)
    contacts_list.contacts.append(contact)
    print(f"\nSuccess on add {name}.\n")


def show_contacts():
    return display_contacts(contacts_list.show_contacts())


def show_favorite_contacts():
    return display_contacts(contacts_list.show_contacts(), favorite_only=True)


def edit_contact():
    contacts = show_contacts()
    if contacts:
        choose = choose_contact() - 1
        contact = contacts_list.find_contact(choose)
        if contact is not None:
            name, phone, email = get_contact_edit_data()
            contact.edit_contact(name, phone, email)
            print(f"\nSucces on updating contact {choose + 1}.")


def mark_or_unmark_contact():
    contacts = show_contacts()
    if contacts:
        choose = choose_contact() - 1
        contact = contacts_list.find_contact(choose)
        if contact:
            contact.mark_or_unmark_contact()
            print(f"\nSucces on mark/unmark contact {choose + 1} as favorite.")


def delete_contact():
    contacts = show_contacts()
    if contacts:
        choose = choose_contact() - 1
        contact = contacts_list.find_contact(choose)
        if contact:
            contacts_list.delete_contact(choose)
            print(f"\nSucces on deleting contact {choose + 1}.")
