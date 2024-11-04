import re
from .field import Field

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number. It must be 10 digits long.")
        super().__init__(value)

    @staticmethod
    def validate_phone(value):
        return re.fullmatch(r'\d{10}', value) is not None
