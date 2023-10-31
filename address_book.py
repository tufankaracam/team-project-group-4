from collections import UserDict
from datetime import datetime, timedelta
from name import Name
from record import Record
import os
import pickle

class AddressBook(UserDict):

    def __init__(self):
        self.filename = 'data'
        super().__init__()
        if os.path.exists('data'):
            self.load_records()
        else:
            self.data = {}

    def add_record(self, record: Record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
            return 'New contact with number added.'
        else:
            contact: Record = self.find(record.name.value)
            contact.add_phone(record.phones[0].value)
            return 'Phone number added.'

    def save_records(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)

    def load_records(self):
        if (os.path.getsize(self.filename) > 0):
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)
        else:
            self.data = {}

    def find(self, name: Name):
        return self.data[name]

    def delete(self, name: Name):
        del self.data[name]

    def get_birthdays_per_week(self):
        now = datetime.now().date()
        delta_next_week = 7 - now.weekday()
        next_week_start = now + timedelta(days=delta_next_week)
        next_week_end = next_week_start + timedelta(days=6)

        birthdays = {}

        current_date = next_week_start

        while (current_date <= next_week_end):
            birthdays[current_date.strftime('%A')] = []
            current_date += timedelta(days=1)

        for user in self.data:
            if hasattr(self.data[user], 'birthday'):
                if self.data[user].birthday is not None:
                    birthday = datetime(
                        now.year, self.data[user].birthday.value.month, self.data[user].birthday.value.day).date()
                    if next_week_start <= birthday <= next_week_end:
                        birthdays[birthday.strftime('%A')].append(
                            self.data[user].name.value)
        return "\n".join([f'{k}: {", ".join(v)}' for k, v in birthdays.items() if len(v) > 0])