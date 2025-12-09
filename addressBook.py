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
class AddressBook:
   def __init__(self):
      self.contacts = []
   
   def add_contact(self,contact):
      self.contacts.append(contact)
   def show_contacts(self):
      if not self.contacts:
         print("No contact")
      for contact in self.contacts:
         print(contact)
               

def main():
 print("Welcome to Address Book Program")


 book = AddressBook()
 while True:
        print("\n1. Add Contact\n2. Show Contacts\n3. Exit")
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
            book.add_contact(contact)
            print("Contact added.")
        elif choice == "2":
            book.show_contacts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

 



    
if __name__ == "__main__":
    main()