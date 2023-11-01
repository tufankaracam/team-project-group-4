from field import Field
import re


class EmailFormatError(Exception):
    def __init__(self):
        super().__init__('''Invalid email format. Please use the following format: <local-part>@<domain>.''')


class Email(Field):
    def __init__(self, value):
        super().__init__(self.validate_email(value))

    def validate_email(self, value):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, value):
            raise EmailFormatError()
        else:
            return value
