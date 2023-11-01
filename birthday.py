from field import Field
from datetime import datetime
import re


class BirthdayFormatError(Exception):
    def __init__(self):
        super().__init__('''Birthday format is must be DD.MM.YYYY!''')


class Birthday(Field):
    def __init__(self, value):
        self.validate_birthday(value)

        day, month, year = value.split('.')
        super().__init__(datetime(int(year), int(month), int(day)))

    def validate_birthday(self, value):
        pattern = r"\d{2}\.\d{2}\.\d{4}"

        if not re.match(pattern, value):
            raise BirthdayFormatError()
