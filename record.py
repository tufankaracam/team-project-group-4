from birthday import Birthday
from name import Name
from phone import Phone, PhoneFormatError
from address import Address
from ct_email import Email


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def show_birthday(self):
        if hasattr(self, 'birthday') and self.birthday is not None:
            return self.birthday.value.strftime('%d.%m.%Y')
        else:
            return 'Birthday info not found.'

    def add_phone(self, phone):
        phone = Phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                return 'You already have this phone number.'
        self.phones.append(phone)
        return 'Phone number added.'

    def remove_phone(self, phone):
        phone = Phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(phone)
                return 'Phone number removed.'
        return 'Phone number not found.'

    def edit_phone(self, old_phone, new_phone):
        try:
            old_p = Phone(old_phone)
            new_p = Phone(new_phone)

            for p in self.phones:
                if p.value == old_p.value:
                    p.value = new_p.value
                    return 'Phone number updated.'
            return 'Phone number not found.'
        except PhoneFormatError as e:
            return str(e)

    def find_phone(self, phone):
        phone = Phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                return p.value
        return 'Phone number not found.'

    def add_address(self, value):
        self.address = Address(value)

    def show_address(self):
        if hasattr(self, 'address') and self.address is not None:
            return self.address.value
        else:
            return 'Address info not found.'

    def add_email(self, value):
        self.email = Email(value)

    def show_email(self):
        if hasattr(self, 'email') and self.email is not None:
            return self.email.value
        else:
            return 'Email info not found.'

    def __str__(self):
        return f'''Contact name: {self.name.value}, phones: {'; '.join([p.value for p in self.phones])}'''
