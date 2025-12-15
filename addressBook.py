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
   def __init__(self, name):
      self.name = name
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
      print(f"\n--- Contacts in '{self.name}' ---")
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


class AddressBookManager:
   def __init__(self):
      self.address_books = {}
   
   def create_address_book(self, name):
      if name in self.address_books:
         print(f"Address book '{name}' already exists!")
         return False
      self.address_books[name] = AddressBook(name)
      print(f"Address book '{name}' created successfully!")
      return True
   
   def get_address_book(self, name):
      return self.address_books.get(name)
   
   def list_address_books(self):
      if not self.address_books:
         print("No address books available.")
         return
      print("\nAvailable Address Books:")
      for i, name in enumerate(self.address_books.keys(), 1):
         book = self.address_books[name]
         print(f"{i}. {name} ({len(book.contacts)} contacts)")
   
   def select_address_book(self):
      if not self.address_books:
         print("No address books available. Please create one first.")
         return None
      
      self.list_address_books()
      book_name = input("\nEnter address book name: ").strip()
      book = self.get_address_book(book_name)
      if not book:
         print(f"Address book '{book_name}' not found.")
         return None
      return book
   
   def search_by_city(self, city):
      """Search for persons in a city across all address books"""
      results = []
      for book_name, book in self.address_books.items():
         for contact in book.contacts:
            if contact.city.lower() == city.lower():
               results.append((book_name, contact))
      return results
   
   def search_by_state(self, state):
      """Search for persons in a state across all address books"""
      results = []
      for book_name, book in self.address_books.items():
         for contact in book.contacts:
            if contact.state.lower() == state.lower():
               results.append((book_name, contact))
      return results
   
   def display_search_results(self, results, search_type, search_term):
      if not results:
         print(f"No contacts found in {search_type}: {search_term}")
         return
      
      print(f"\n========== Search Results for {search_type}: {search_term} ==========")
      print(f"Found {len(results)} contact(s):\n")
      
      for book_name, contact in results:
         print(f"Address Book: {book_name}")
         print(contact)


def main():
 print("Welcome to Address Book Program")

 manager = AddressBookManager()
 current_book = None
 
 while True:
        print("\n========== Main Menu ==========")
        print("1. Create New Address Book")
        print("2. Select Address Book")
        print("3. List All Address Books")
        if current_book:
           print(f"\n--- Working with: '{current_book.name}' ---")
           print("4. Add Contact")
           print("5. Show Contacts")
           print("6. Edit Contact")
           print("7. Delete Contact")
        print("8. Search by City")
        print("9. Search by State")
        print("10. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
           book_name = input("Enter new address book name: ").strip()
           if book_name:
              manager.create_address_book(book_name)
        
        elif choice == "2":
           current_book = manager.select_address_book()
           if current_book:
              print(f"Now working with address book: '{current_book.name}'")
        
        elif choice == "3":
           manager.list_address_books()
        
        elif choice == "4":
           if not current_book:
              print("Please select an address book first!")
           else:
              first_name = input("First Name: ")
              last_name = input("Last Name: ")
              address = input("Address: ")
              city = input("City: ")
              state = input("State: ")
              zip_code = input("ZIP: ")
              phone = input("Phone: ")
              email = input("Email: ")
              contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
              if current_book.add_contact(contact):
                 print("Contact added successfully!")
        
        elif choice == "5":
           if not current_book:
              print("Please select an address book first!")
           else:
              current_book.show_contacts()
        
        elif choice == "6":
           if not current_book:
              print("Please select an address book first!")
           elif not current_book.contacts:
              print("No contacts to edit.")
           else:
              first_name = input("Enter first name of contact to edit: ")
              last_name = input("Enter last name of contact to edit: ")
              current_book.edit_contact(first_name, last_name)
        
        elif choice == "7":
           if not current_book:
              print("Please select an address book first!")
           elif not current_book.contacts:
              print("NO contacts available")
           else:
              first_name = input(f"Enter the First name: ")
              last_name = input(f"Enter the Last name: ")
              current_book.delete_contact(first_name, last_name)
        
        elif choice == "8":
           city = input("Enter city name to search: ").strip()
           if city:
              results = manager.search_by_city(city)
              manager.display_search_results(results, "City", city)
        
        elif choice == "9":
           state = input("Enter state name to search: ").strip()
           if state:
              results = manager.search_by_state(state)
              manager.display_search_results(results, "State", state)
        
        elif choice == "10":
           print("Goodbye!")
           break
        
        else:
           print("Invalid option.")

if __name__ == "__main__":
    main()