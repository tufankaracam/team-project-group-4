from address_book import AddressBook
from notebook import Notebook
from birthday import BirthdayFormatError, BirthdayValueError
from phone import PhoneFormatError
from record import Record
from address import AddressFormatError, AddressEmptyError
from ct_email import EmailFormatError
import os
import platform
import difflib


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
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found!"
        except IndexError:
            return "Give me name please."
        except TypeError:
            return "Give me name and phone please"
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
def delete(args, contacts: AddressBook):
    try:
        name = args[0]
        contacts.delete(name)
        contacts.save_records()
        return 'Contact removed'
    except KeyError:
            return 'Contact not found'

@input_error
def show_phone(args, contacts: AddressBook):
    contact = contacts.find(args[0])
    return f'{contact.name.value}: { ", ".join([phone.value for phone in contact.phones])}'


def show_all(contacts: AddressBook):
    return str(contacts)


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
        return 'You need to give name and birthday.'
    except KeyError:
        return 'Contact not found.'


def show_birthday(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)
        return contact.show_birthday()
    except IndexError:
        return 'You need to give name.'
    except KeyError:
        return 'Contact not found.'


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
        name, *address = args  # args[0], args[1:]
        address_str = (" ").join(address).title()
        contact = contacts.find(name)
        contact.add_address(address_str)
        contacts.save_records()
        return 'Address added.'
    except AddressFormatError as e:
        return e
    except AddressEmptyError as e:
        return e
    except IndexError:
        return 'You need to give name and address.'
    except KeyError:
        return 'Contact not found.'


def show_address(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)
        return contact.show_address()
    except IndexError:
        return 'You need to give name.'
    except KeyError:
        return 'Contact not found.'


def search(args, contacts: AddressBook):
    return contacts.search(args[0].strip())


def add_note(args, notes: Notebook):
    text = ' '.join(args)
    return notes.create_note(text)


def update_note(args, notes: Notebook):
    id, *text = args
    return notes.update_note(id, ' '.join(text))


def search_note(args, notes: Notebook):
    text = ' '.join(args)
    return notes.search_note(text)


def remove_note(args, notes: Notebook):
    id = args[0]
    return notes.remove_note(id)


def all_notes(notes: Notebook):
    return notes

def add_tags(args, notes: Notebook):
    id, *tags = args
    return notes.add_tags(id, tags)

def remove_tag(args, notes: Notebook):
    id, tag = args
    return notes.remove_tag(id, tag)

def add_email(args, contacts: AddressBook):
    try:
        name, email = args
        contact = contacts.find(name)
        contact.add_email(email)
        contacts.save_records()
        return 'Email added.'
    except EmailFormatError as e:
        return e
    except ValueError:
        return 'You need to give name and email.'
    except KeyError:
        return 'Contact not found.'


def show_email(args, contacts: AddressBook):
    try:
        name = args[0]
        contact = contacts.find(name)
        return contact.show_email()
    except IndexError:
        return 'You need to give name.'
    except KeyError:
        return 'Contact not found.'


def check_suggestion(keyword, items):
    matches = difflib.get_close_matches(keyword, items, n=3)

    if matches:
        return 'Did you mean\n'+'\n'.join([f'{match}?' for match in matches])
    else:
        return "Invalid command."


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
        'delete': {'name': delete, 'obj': contacts},
        'all': {'name': show_all, 'obj': contacts},
        'add-birthday': {'name': add_birthday, 'obj': contacts},
        'show-birthday': {'name': show_birthday, 'obj': contacts},
        'birthdays': {'name': birthdays, 'obj': contacts},
        'add-address': {'name': add_address, 'obj': contacts},
        'show-address': {'name': show_address, 'obj': contacts},
        'search': {'name': search, 'obj': contacts},
        'add-email': {'name': add_email, 'obj': contacts},
        'show-email': {'name': show_email, 'obj': contacts},

        'add-note': {'name': add_note, 'obj': notes},
        'update-note': {'name': update_note, 'obj': notes},
        'search-note': {'name': search_note, 'obj': notes},
        'remove-note': {'name': remove_note, 'obj': notes},
        'all-notes': {'name': all_notes, 'obj': notes},
        'add-tags': {'name': add_tags, 'obj': notes},
        'remove-tag': {'name': remove_tag, 'obj': notes},
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
                    try:
                        print(methods[cmd]['name'](methods[cmd]['obj']))
                    except TypeError:
                        print('Please provide full info')
            else:
                print(check_suggestion(cmd, methods.keys()))


if __name__ == '__main__':
    main()
