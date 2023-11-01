from field import Field
from datetime import datetime
import re


class BirthdayFormatError(Exception):
    def __init__(self):
        super().__init__('''Birthday format is must be DD.MM.YYYY!''')

class BirthdayValueError(Exception):
    def __init__(self):
        super().__init__('''Birthday is not valid.''')


class Birthday(Field):
    def __init__(self, value):
        super().__init__(self.validate_birthday(value))

    def validate_birthday(self, value):
        pattern = r"\d{2}\.\d{2}\.\d{4}"

        if not re.match(pattern, value):
            raise BirthdayFormatError()

        try:
            day, month, year = value.split('.')
            return datetime(int(year), int(month), int(day))
        except:
            raise BirthdayValueError()
