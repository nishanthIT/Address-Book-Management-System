class Contact:
    def __init__(self,first_name,last_name,address,city,state,zip,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
class AddressBook:
    def __init__(self):
        self.contacts=[]

    def addContact(self,contact):
        self.contacts.append(contact)
    def desplay_contact(self):
        if not self.contacts:
            print("ENter th contacts Firsr")
            return
        
        for i,contact in enumerate(self.contacts):
            print(f"Contact Number {i}")
            print(f"Name: {contact.first_name} {contact.last_name}")
            print(f"Address: {contact.address}")
            print(f"city: {contact.city}")
            print(f"state: {contact.state}")
            print(f"zip: {contact.zip}")
            print(f"phone_number: {contact.phone_number}")
    def find_contact(self,first_name,last_name):
        for i in self.contacts:
            if (i.first_name.lower() == first_name.lower() and i.last_name.lower() == last_name.lower()):
                return i
        print("Contact Not Found")    
        return None    
       

    def edit_contact(self,first_name,last_name):
        contact = self.find_contact(first_name,last_name)
        contact.first_name = input("Enter the First Name: ")
        contact.last_name = input("Enter the Last Name: ")
        contact.address = input("Enter the Address: ")
        contact.city = input("Enter the City: ")
        contact.state = input("Enter the State: ")
        contact.zip = input("Enter the First Zip: ")
        contact.phone_number = input("Enter the Phone Number: ")
    def delete_contact(self,first_name,last_name):
        contact = self.find_contact(first_name,last_name)
        if not contact:
            print("No contact found")
            return
        self.contacts.remove(contact)
        print("Removed Success")


address_books ={
}

while True:
    print("Welcome to Address Book ")
    print("1. Create a Address Book")
    print("2. Add Contact")
    print("3. View Contacts")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Enter Your choice: ")
    if choice == "1":
        name = input("Enter the name of the address Book")
        if name in address_books:
            print("Addres book Already Exist")
        else:
            address_books[name] = AddressBook()


    elif choice == "2":   
        name = input("Enter the Address book name")

        if name not in address_books:
            print("Name not in the address Book")


        first_name = input("Enter the First name: ")
        last_name = input("Enter the Last name: ")
        address = input("Enter the address: ")
        city = input("Enter the city: ")
        state = input("Enter the State:")
        zip = input("Enter the zip:")
        phone_number = input("Enter the phone number:")
        
        contact = Contact(first_name,last_name,address,city,state,zip,phone_number)
        address_books[name].addContact(contact)
    elif choice =="3":
         name = input("Enter the address Book Name: ")
         if name not in address_books:
             print("name Not found")
         address_books[name].desplay_contact()
    elif choice =="4":
        name = input("Enter the address Book Name: ")
        if name not in address_books:
             print("name Not found")

        first_name = input("Enter the first Name: ")     
        last_name = input("Enter the last Name: ")
        address_books[name].edit_contact(first_name,last_name)

    elif choice =="5":
        name = input("Enter the address Book Name: ")
        if name not in address_books:
             print("name Not found")
        first_name = input("Enter the first Name: ")     
        last_name = input("Enter the last Name: ")
        address_books[name].delete_contact(first_name,last_name)

    elif choice =="6":
        print("exiting...")
        break
    else:
        print("in Valied")     





    






        