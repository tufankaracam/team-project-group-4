from address_book import AddressBook

def modify_contact_address(address_book):
    contact_name = input("Enter the name of the contact to modify: ")
    if contact_name in address_book.contacts:
        new_address = input("Enter the new address for {}: ".format(contact_name))
        address_book.modify_address(contact_name, new_address)
        print("Address for contact {} successfully modified.".format(contact_name))
    else:
        print("Contact with the name {} not found in the address book.".format(contact_name))

def delete_contact_address(address_book):
    contact_name = input("Enter the name of the contact to delete: ")
    if contact_name in address_book.contacts:
        address_book.delete_contact(contact_name)
        print("Contact {} successfully deleted.".format(contact_name))
    else:
        print("Contact with the name {} not found in the address book.".format(contact_name))

def main():
    address_book = AddressBook()
    
    modify_contact_address(address_book)
    print("Updated address book:", address_book.contacts)

    delete_contact_address(address_book)
    print("Updated address book:", address_book.contacts)

if __name__ == "__main__":
    main()
