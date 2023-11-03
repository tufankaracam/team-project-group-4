from address_book import AddressBook

def change_contact_birthday(address_book):
    contact_name = input("Enter the name of the contact to modify: ")
    
    if contact_name in address_book:
        contact = address_book[contact_name]

        if "birthday" in contact:
            new_birthday = input("Enter the new birthday for {}: ".format(contact_name))
            contact["birthday"] = new_birthday
            print("Birthday for contact {} successfully modified.".format(contact_name))
        else:
            print("Contact {} does not have a birthday to modify.".format(contact_name))
    else:
        print("Contact with the name {} not found in the address book.".format(contact_name))

def delete_contact_birthday(address_book):
    contact_name = input("Enter the name of the contact to delete birthday: ")

    if contact_name in address_book:
        contact = address_book[contact_name]

        if "birthday" in contact:
            del contact["birthday"]
            print("Birthday for contact {} successfully deleted.".format(contact_name))
        else:
            print("Contact {} does not have a birthday to delete.".format(contact_name))
    else:
        print("Contact with the name {} not found in the address book.".format(contact_name))

def main():
    address_book = AddressBook()

    change_contact_birthday(address_book.contacts)
    print("Updated address book:", address_book.contacts)

    delete_contact_birthday(address_book.contacts)
    print("Updated address book:", address_book.contacts)

if __name__ == "__main__":
    main()
