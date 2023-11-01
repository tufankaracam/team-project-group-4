from address_book import AddressBook
from birthday import BirthdayFormatError, BirthdayValueError
from phone import Phone, PhoneFormatError
from record import Record
from address import Address, AddressFormatError
import os
import platform


def clear_console():

    system = platform.system()

    if system == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found!"
        except IndexError:
            return "Give me name please."
    return inner


@input_error
def add_contact(args, contacts: AddressBook):
    try:
        name, phone = args
        contact = Record(name)
        contact.add_phone(phone)
        result = contacts.add_record(contact)
        contacts.save_records()
        return result
    except PhoneFormatError as e:
        return e


@input_error
def change_contact(args, contacts: AddressBook):
    try:
        name, phone1, phone2 = args
        contact = contacts.find(name)
        result = contact.edit_phone(phone1, phone2)
        contacts.save_records()
        return result
    except PhoneFormatError as e:
        return e


@input_error
def show_phone(args, contacts: AddressBook):
    contact = contacts.find(args[0])
    return f'{contact.name.value}: { ", ".join([phone.value for phone in contact.phones])}'


def show_all(contacts: AddressBook):
    return '\n'.join([f'{k} ({v.birthday.value.strftime("%d.%m.%Y") if hasattr(v,"birthday") else "No Birthday"}): { ", ".join([phone.value for phone in v.phones])}' for k, v in contacts.items()])


def add_birthday(args, contacts: AddressBook):
    try:
        name, birthday = args
        contact = contacts.find(name)
        contact.add_birthday(birthday)
        contacts.save_records()
        return 'Birthday added.'
    except BirthdayFormatError as e:
        return e
    except BirthdayValueError as e:
        return e
    except ValueError:
        return 'You need to give name and birthday #dd.mm.yyyy'


def show_birthday(args, contacts: AddressBook):
    name = args[0]
    contact = contacts.find(name)
    return contact.show_birthday()


def birthdays(contacts: AddressBook):
    return contacts.get_birthdays_per_week()


def add_address(args, contacts: AddressBook):
    try:
        name = args[0]
        address = (" ").join(args[1:]).title()
        contact = contacts.find(name)
        contact.add_address(address)
        contacts.save_records()
        return 'Address added.'
    except AddressFormatError as e:
        return e
    except ValueError:
        return 'You need to give name and address.'


def show_address(args, contacts: AddressBook):
    name = args[0]
    contact = contacts.find(name)
    return contact.show_address()

def search(args, contacts: AddressBook):
    return contacts.search(args[0].strip())


def parseCommands(input):
    if input == '':
        return '', []

    cmd, *args = input.strip().lower().split()
    return cmd, args


def main():
    print('Welcome to the Contact Assistant!')

    contacts = AddressBook()

    methods = {
        'phone': {'name': show_phone, 'args': True},
        'add': {'name': add_contact, 'args': True},
        'change': {'name': change_contact, 'args': True},
        'all': {'name': show_all, 'args': False},
        'add-birthday': {'name': add_birthday, 'args': True},
        'show-birthday': {'name': show_birthday, 'args': True},
        'birthdays': {'name': birthdays, 'args': False},
        'add-address': { 'name': add_address, 'args': True},
        'show-address': { 'name': show_address, 'args': True},
        'search': { 'name': search, 'args': True},
    }

    while (True):
        cmd, args = parseCommands(input('> '))
        # clear_console()
        if cmd == 'hello':
            print('How can I help you?')
        elif (cmd == 'close' or cmd == 'exit'):
            print('Good bye!')
            break
        else:

            if cmd in methods:
                if methods[cmd]['args'] == True:
                    print(methods[cmd]['name'](args, contacts))
                else:
                    print(methods[cmd]['name'](contacts))
            else:
                print('Invalid command.')


if __name__ == '__main__':
    main()
