import time
from src.controllers import (
    add_contact,
    show_contacts,
    edit_contact,
    mark_or_unmark_contact,
    show_favorite_contacts,
    delete_contact,
)
from src.views import show_menu, get_user_input


def main():
    while True:
        time.sleep(1)
        show_menu()
        choice = get_user_input()

        match choice:
            case "1":
                add_contact()

            case "2":
                show_contacts()

            case "3":
                edit_contact()

            case "4":
                mark_or_unmark_contact()

            case "5":
                show_favorite_contacts()

            case "6":
                delete_contact()

            case "7":
                print("Exiting contact list...")
                return

            case _:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
