from address_book import AddressBook

def change_contact_email(address_book):
    contact_name = input("Enter the name of the contact to modify: ")

    if contact_name in address_book.contacts:
        new_email = input("Enter the new email address for {}: ".format(contact_name))
        address_book.modify_email(contact_name, new_email)
        print("Email address for contact {} successfully modified.".format(contact_name))
    else:
        print("Contact with the name {} not found in the address book.".format(contact_name))

def delete_contact_email(address_book):
    contact_name = input("Enter the name of the contact to delete email: ")

    if contact_name in address_book.contacts:
        address_book.delete_email(contact_name)
        print("Email address for contact {} successfully deleted.".format(contact_name))
    else:
        print("Contact with the name {} not found in the address book.".format(contact_name))

def main():
    address_book = AddressBook()

    change_contact_email(address_book)
    print("Updated address book:", address_book.contacts)

    delete_contact_email(address_book)
    print("Updated address book:", address_book.contacts)

if __name__ == "__main__":
    main()
