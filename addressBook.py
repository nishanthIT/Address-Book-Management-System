class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"{self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state}, {self.zip_code}\n"
                f"Phone: {self.phone}\nEmail: {self.email}\n")
    
    def __eq__(self, other):
        """Override equals method to check for duplicate based on person name"""
        if not isinstance(other, Contact):
            return False
        return (self.first_name.lower() == other.first_name.lower() and 
                self.last_name.lower() == other.last_name.lower())
    
    def __hash__(self):
        """Override hash method to enable use in sets and dictionaries"""
        return hash((self.first_name.lower(), self.last_name.lower()))

class AddressBook:
   def __init__(self):
      self.contacts = []
   
   def add_contact(self, contact):
      # Check for duplicate entry using collection method
      if any(existing_contact == contact for existing_contact in self.contacts):
         print(f"Duplicate Entry! Contact '{contact.first_name} {contact.last_name}' already exists in address book.")
         return False
      self.contacts.append(contact)
      return True
   
   def show_contacts(self):
      if not self.contacts:
         print("No contacts found.")
         return
      for i, contact in enumerate(self.contacts, 1):
         print(f"Contact {i}:")
         print(contact)
   
   def find_contact(self, first_name, last_name):
      for contact in self.contacts:
         if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
            return contact
      return None
   
   def edit_contact(self, first_name, last_name):
      contact = self.find_contact(first_name, last_name)
      if not contact:
         print(f"Contact '{first_name} {last_name}' not found.")
         return False
      
      print(f"Editing contact: {contact.first_name} {contact.last_name}")
      print("Press Enter to keep current value, or type new value:")
      
      new_first_name = input(f"First Name ({contact.first_name}): ").strip()
      if new_first_name:
         contact.first_name = new_first_name
      
      new_last_name = input(f"Last Name ({contact.last_name}): ").strip()
      if new_last_name:
         contact.last_name = new_last_name
      
      new_address = input(f"Address ({contact.address}): ").strip()
      if new_address:
         contact.address = new_address
      
      new_city = input(f"City ({contact.city}): ").strip()
      if new_city:
         contact.city = new_city
      
      new_state = input(f"State ({contact.state}): ").strip()
      if new_state:
         contact.state = new_state
      
      new_zip = input(f"ZIP ({contact.zip_code}): ").strip()
      if new_zip:
         contact.zip_code = new_zip
      
      new_phone = input(f"Phone ({contact.phone}): ").strip()
      if new_phone:
         contact.phone = new_phone
      
      new_email = input(f"Email ({contact.email}): ").strip()
      if new_email:
         contact.email = new_email
      
      print("Contact updated successfully!")
      return True
    
   def delete_contact(self,first_name,last_name):
      contact = self.find_contact(first_name,last_name)
      if not contact:
         print(f"Contact Not found for `{first_name} {last_name}`")
         return False
      self.contacts.remove(contact)
      print("Deleted success")
      return True


def main():
 print("Welcome to Address Book Program")

 book = AddressBook()
 while True:
        print("\n1. Add Contact\n2. Show Contacts\n3. Edit Contact\n4.Delete \n5. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("ZIP: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
            if book.add_contact(contact):
                print("Contact added successfully!")
        elif choice == "2":
            book.show_contacts()
        elif choice == "3":
            if not book.contacts:
                print("No contacts to edit.")
            else:
                first_name = input("Enter first name of contact to edit: ")
                last_name = input("Enter last name of contact to edit: ")
                book.edit_contact(first_name, last_name)
        elif choice == "4":
           if not book.contacts:
              print("NO contacts avalable")
           else:
              first_name = input(f"Enter the First name:")
              last_name = input(f"Enter the Last name")
              book.delete_contact(first_name,last_name)         
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()