class Contact:
    def __init__(self, name, phone, email, favorite=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite

    def edit_contact(self, name=None, phone=None, email=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email

    def mark_or_unmark_contact(self):
        if self.favorite:
            self.favorite = False
        else:
            self.favorite = True


class List:
    def __init__(self):
        self.contacts = []

    def show_contacts(self):
        return self.contacts

    def find_contact(self, index):
        if 0 <= index < len(self.contacts):
            return self.contacts[index]
        else:
            print("\nContact not found.")
            return None

    def delete_contact(self, index):
        del self.contacts[index]
