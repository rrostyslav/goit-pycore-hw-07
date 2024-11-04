from .field import Field

class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number. It must consist of 10 digits.")

    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10
