class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number

    def __str__(self):
         return f"{self.first_name} {self.last_name} | {self.city} | {self.phone_number} | {self.state} | {self.zip}" 


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

    def sort_by_name(self):
        return sorted(self.contacts,key=lambda c: c.first_name.lower())
    
    def sort_by_city(self):
        return sorted(self.contacts,key=lambda c: c.city.lower())
    def sort_by_state(self):
        return sorted(self.contacts,key=lambda c: c.state.lower())
    def sort_by_zip(self):
        return sorted(self.contacts,key=lambda c: c.zip.lower())
   
   

address_books = {}

while True:
    print("\n--- Address Book System ---")
    print("1. Create Address Book")
    print("2. Add Contact")
    print("3. View Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. search by City")
    print("7. sort by name")
    print("8. sort by city")
    print("9. sort by state")
    print("10. sort by zip")
    print("11. Exit")

    choice = input("Enter your choice: ")

   
    if choice == "1":
        name = input("Enter Address Book Name: ")
        if name in address_books:
            print("Address Book already exists")
        else:
            address_books[name] = AddressBook()
            print(f"Address Book '{name}' created")

    
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

    elif choice == "3":
        name = input("Enter Address Book Name: ")
        if name not in address_books:
            print("Address Book not found")
            continue
        address_books[name].desplay_contact()

    elif choice == "4":
        name = input("Enter Address Book Name: ")
        if name not in address_books:
            print("Address Book not found")
            continue

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address_books[name].edit_contact(first_name, last_name)


    elif choice == "5":
        name = input("Enter Address Book Name: ")
        if name not in address_books:
            print("Address Book not found")
            continue

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address_books[name].delete_contact(first_name, last_name)

    elif choice =="6":
        found = False
        count =0
        
        city =input("Enter the City name:")
        for bk_name,i in address_books.items():
            for j in i.contacts:
                if j.city.lower() == city.lower():
                    print(f"[{bk_name}] {j}")
                    count +=1
                    found = True
        print(f"Total Count by City:{count}")            
        if not found:
            print("No COntacts")            
        


    elif choice =="7":
        name = input("Enter the Address Book:")
        if name not in address_books:
            print("Address Bokk Not present")
        sorted_list = address_books[name].sort_by_name()
        for i in sorted_list:
            print(i)


    elif choice =="8":
        name = input("Enter the Address Book:")
        if name not in address_books:
            print("Address Bokk Not present")
        sorted_list = address_books[name].sort_by_city()
        for i in sorted_list:
            print(i)


    elif choice =="9":
        name = input("Enter the Address Book:")
        if name not in address_books:
            print("Address Bokk Not present")
        sorted_list = address_books[name].sort_by_state()
        for i in sorted_list:
            print(i)


    elif choice =="10":
        name = input("Enter the Address Book:")
        if name not in address_books:
            print("Address Bokk Not present")
        sorted_list = address_books[name].sort_by_zip()
        for i in sorted_list:
            print(i)

    
    elif choice == "8":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
