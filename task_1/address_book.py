from collections import UserDict
from datetime import timedelta, datetime

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.now()
        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value
                if today <= birthday_date.replace(year=today.year) < today + timedelta(days=7):
                    upcoming_birthdays.append(record)
        return upcoming_birthdays
