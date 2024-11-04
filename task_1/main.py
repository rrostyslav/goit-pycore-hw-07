from address_book import AddressBook
from models.record import Record

if __name__ == "__main__":
    book = AddressBook()

    mike_record = Record("Mike")
    mike_record.add_phone("9876543210")
    mike_record.add_birthday("11.02.1977")
    book.add_record(mike_record)

    emily_record = Record("Emily")
    emily_record.add_phone("9900093210")
    emily_record.add_birthday("06.05.1986")
    book.add_record(emily_record)

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("09.11.1990")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("08.11.2000")
    book.add_record(jane_record)


    for name, record in book.data.items():
        print(record)

    upcoming_birthdays = book.get_upcoming_birthdays()
    print("Upcoming birthdays next week:")
    for record in upcoming_birthdays:
        print(record)
