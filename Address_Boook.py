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
    contacts =[]
    def __init__(self,contact):
        self.contacts.append(contact)

    def __str__(self):
        for contact in self.contacts:
            return f"Address Book \n Name: {contact.first_name} {contact.last_name}\n Address: {contact.address} \n City: {contact.city}\nS tate: {contact.state}\n Zip: {contact.zip}\n Phone_number: {contact.phone_number}"    

print("Welcome to Address Book ")

first_name = input("Enter the First name: ")
last_name = input("Enter the Last name: ")
address = input("Enter the address: ")
city = input("Enter the city: ")
state = input("Enter the State:")
zip = input("Enter the zip:")
phone_number = input("Enter the phone number:")

contact1 = Contact(first_name,last_name,address,city,state,zip,phone_number)
AddressBook1 = AddressBook(contact1)

print(AddressBook1)




        