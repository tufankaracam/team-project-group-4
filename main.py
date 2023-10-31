from address_book import AddressBook
from birthday import BirthdayFormatError
from phone import Phone, PhoneFormatError
from record import Record
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
        contact.edit_phone(phone1, phone2)
        for phone in contact.phones:
            phone1 = Phone(phone1)
            if phone1.value == phone.value:
                phone.value = phone2
                contacts.save_records()
                return "Phone number updated."
            return "Phone number not found."
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
    except ValueError:
        return 'You need to give name and birthday #dd.mm.yyyy'


def show_birthday(args, contacts: AddressBook):
    name = args[0]
    contact = contacts.find(name)
    return contact.show_birthday()


def birthdays(contacts: AddressBook):
    return contacts.get_birthdays_per_week()


def parseCommands(input):
    if input == '':
        return '', []

    cmd, *args = input.strip().lower().split()
    return cmd, args


def main():
    print('Welcome to the Contact Assistant!')

    contacts = AddressBook()

    methods = {
        'phone': show_phone,
        'add': add_contact,
        'change': change_contact,
        'all': show_all,
        'add-birthday': add_birthday,
        'show-birthday': show_birthday,
        'birthdays': birthdays,

    }

    while (True):
        cmd, args = parseCommands(input('> '))
        clear_console()
        if cmd == 'hello':
            print('How can I help you?')
        elif (cmd == 'close' or cmd == 'exit'):
            print('Good bye!')
            break
        elif cmd in methods:
            if args:
                print(methods[cmd](args, contacts))
            else:
                print(methods[cmd](contacts))
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()