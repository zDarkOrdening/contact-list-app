# Contact List App

A simple command-line contact list application built with Python for a Rocketseat challenge. It allows you to manage your contacts efficiently.

## Features

- **Add contact:** Store contact information including name, phone number, email, and favorite status.
- **View contacts:** Display a list of all saved contacts.
- **Edit contact:** Update existing contact details.
- **Mark/Unmark as favorite:** Easily mark and unmark contacts as favorites.
- **View favorite contacts:** Quickly access a list of your favorite contacts.
- **Delete contact:** Remove unwanted contacts from the list.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/contact-list-app.git
   cd contact-list-app
   ```

2. **Run the application:**

   ```bash
   python main.py
   ```

## Usage

Upon running the application, you will be presented with a menu-driven interface like this:

```
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Contact List Menu

1. Add contact
2. Show contacts
3. Edit contact
4. Mark/unmark as favorite
5. Show favorite contacts
6. Delete contact
7. Exit

Choose an option: 
```

Follow the on-screen prompts to interact with the application.

## File Structure

```
contact-list-app/
├── src/
│   ├── controllers.py
│   ├── models.py
│   └── views.py
└── main.py
```

- **`main.py`:** The entry point of the application. Handles the main program loop and user interaction.
- **`src/controllers.py`:** Contains the logic for handling user actions and updating the contact list.
- **`src/models.py`:** Defines the data structures for representing contacts and the contact list.
- **`src/views.py`:** Handles the display of information to the user, including menus and contact details.

## Notes:

- This project was developed for educational purposes and to demonstrate basic Python concepts.
- Data persistence has not been implemented in this project, meaning contacts will be lost when you close the program.