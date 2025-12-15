class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number


class AddressBook:
    def __init__(self):
        self.contacts = []

    def find_contact(self, first_name, last_name, silent=False):
        for c in self.contacts:
            if c.first_name.lower() == first_name.lower() and \
               c.last_name.lower() == last_name.lower():
                return c
        if not silent:
            print("Contact Not Found")
        return None

    def addContact(self, contact):
        if self.find_contact(contact.first_name, contact.last_name, silent=True):
            print("Contact already exists")
            return
        self.contacts.append(contact)
        print("Contact added successfully")

    def desplay_contact(self):
        if not self.contacts:
            print("Enter contacts first")
            return

        for i, contact in enumerate(self.contacts, start=1):
            print(f"\nContact Number {i}")
            print(f"Name: {contact.first_name} {contact.last_name}")
            print(f"Address: {contact.address}")
            print(f"City: {contact.city}")
            print(f"State: {contact.state}")
            print(f"Zip: {contact.zip}")
            print(f"Phone Number: {contact.phone_number}")

    def edit_contact(self, first_name, last_name):
        contact = self.find_contact(first_name, last_name)
        if not contact:
            return

        contact.first_name = input("Enter First Name: ")
        contact.last_name = input("Enter Last Name: ")
        contact.address = input("Enter Address: ")
        contact.city = input("Enter City: ")
        contact.state = input("Enter State: ")
        contact.zip = input("Enter Zip: ")
        contact.phone_number = input("Enter Phone Number: ")
        print("Contact updated successfully")

    def delete_contact(self, first_name, last_name):
        contact = self.find_contact(first_name, last_name)
        if not contact:
            return
        self.contacts.remove(contact)
        print("Contact removed successfully")


# Dictionary to store multiple address books
address_books = {}

while True:
    print("\n--- Address Book System ---")
    print("1. Create Address Book")
    print("2. Add Contact")
    print("3. View Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Create Address Book
    if choice == "1":
        name = input("Enter Address Book Name: ")
        if name in address_books:
            print("Address Book already exists")
        else:
            address_books[name] = AddressBook()
            print(f"Address Book '{name}' created")

    # Add Contact
    elif choice == "2":
        name = input("Enter Address Book Name: ")
        if name not in address_books:
            print("Address Book not found")
            continue

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = input("Enter Zip: ")
        phone_number = input("Enter Phone Number: ")

        contact = Contact(first_name, last_name, address, city, state, zip, phone_number)
        address_books[name].addContact(contact)

    # View Contacts
    elif choice == "3":
        name = input("Enter Address Book Name: ")
        if name not in address_books:
            print("Address Book not found")
            continue
        address_books[name].desplay_contact()

    # Edit Contact
    elif choice == "4":
        name = input("Enter Address Book Name: ")
        if name not in address_books:
            print("Address Book not found")
            continue

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address_books[name].edit_contact(first_name, last_name)

    # Delete Contact
    elif choice == "5":
        name = input("Enter Address Book Name: ")
        if name not in address_books:
            print("Address Book not found")
            continue

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address_books[name].delete_contact(first_name, last_name)

    # Exit
    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
