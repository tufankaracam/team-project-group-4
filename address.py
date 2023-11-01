from field import Field
import re


class AddressFormatError(Exception):
    def __init__(self):
        super().__init__('''The address can contain only Latin letters, numbers, spaces and the following characters: . , - ' /''')


class Address(Field):
    def __init__(self, value):
        address = value.strip()
        self.validate_address(address)

        super().__init__(address)

    def validate_address(self, address):
        pattern = r'^[0-9A-Za-z\s.,-\/\']+$'
        if not re.match(pattern, address):
            raise AddressFormatError()
