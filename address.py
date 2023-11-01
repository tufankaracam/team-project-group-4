from field import Field
import re


class AddressFormatError(Exception):
    def __init__(self):
        super().__init__('''The address can contain only Latin letters, numbers, spaces and the following characters: . , - ' /''')


class AddressEmptyError(Exception):
    def __init__(self):
        super().__init__('''The address cannot be empty!''')


class Address(Field):
    def __init__(self, value):
        super().__init__(self.validate_address(value))

    def validate_address(self, value):
        pattern = r'^[0-9A-Za-z\s.,-\/\']+$'
        if not value:
            raise AddressEmptyError()
        elif not re.match(pattern, value):
            raise AddressFormatError()
        else:
            return value
