from .name import Name
from .phone import Phone
from .birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_birthday(self):
        return str(self.birthday) if self.birthday else "No birthday set."

