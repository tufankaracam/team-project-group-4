from address_book import AddressBook
from notebook import Notebook
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


def birthdays(args, contacts: AddressBook):
    try:
        count_days = int(args[0])
        return contacts.get_birthdays_for_days(count_days)
    except ValueError:
        return 'You need to give number of days.'
    except IndexError:
        return 'You need to give number of days.'


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


def add_note(args, notes: Notebook):
    text = ' '.join(args)
    return notes.create_note(text)


def update_note(args, notes: Notebook):
    *text, id = args
    return notes.update_note(' '.join(text), id)


def search_note(args, notes: Notebook):
    text = ' '.join(args)
    return notes.search_note(text)


def remove_note(args, notes: Notebook):
    id = args[0]
    return notes.remove_note(id)


def all_notes(notes: Notebook):
    return notes


def parseCommands(input):
    if input == '':
        return '', []

    cmd, *args = input.strip().lower().split()
    return cmd, args


def main():
    print('Welcome to the Contact Assistant!')

    contacts = AddressBook()
    notes = Notebook()

    methods = {
        'phone': {'name': show_phone, 'obj': contacts},
        'add': {'name': add_contact, 'obj': contacts},
        'change': {'name': change_contact, 'obj': contacts},
        'all': {'name': show_all, 'obj': contacts},
        'add-birthday': {'name': add_birthday, 'obj': contacts},
        'show-birthday': {'name': show_birthday, 'obj': contacts},
        'birthdays': {'name': birthdays, 'obj': contacts},
        'add-address': {'name': add_address, 'obj': contacts},
        'show-address': {'name': show_address, 'obj': contacts},
        'search': { 'name': search, 'obj': contacts},
      
        'add-note': {'name': add_note, 'obj': notes},
        'update-note': {'name': update_note, 'obj': notes},
        'search-note': {'name': search_note, 'obj': notes},
        'remove-note': {'name': remove_note, 'obj': notes},
        'all-notes': {'name': all_notes, 'obj': notes}
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
                if len(args) > 0:
                    print(methods[cmd]['name'](
                        args, methods[cmd]['obj']))
                else:
                    print(methods[cmd]['name'](methods[cmd]['obj']))
            else:
                print('Invalid command.')


if __name__ == '__main__':
    main()
