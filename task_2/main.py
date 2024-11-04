from datetime import datetime, timedelta

from models.address_book import AddressBook
from models.record import Record
from decorators.input_error import input_error


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    return "Contact not found."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return f"{name}'s birthday is {record.get_birthday()}."
    return "Contact not found."


@input_error
def birthdays(args, book: AddressBook):
    today = datetime.now().date()
    upcoming_birthdays = []

    for record in book.get_all_records():
        if record.birthday:
            birthday_this_year = record.birthday.value.replace(year=today.year)
            if today <= birthday_this_year <= today + timedelta(days=7):
                upcoming_birthdays.append(f"{record.name.value}'s birthday is {record.get_birthday()}.")

    if upcoming_birthdays:
        return "\n".join(upcoming_birthdays)
    return "No upcoming birthdays."


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        match command:
            case "close" | "exit":
                print("Good bye!")
                break

            case "hello":
                print("How can I help you?")

            case "add":
                print(add_contact(args, book))

            case "add-birthday":
                print(add_birthday(args, book))

            case "show-birthday":
                print(show_birthday(args, book))

            case "birthdays":
                print(birthdays(args, book))

            case "phone":
                name = args[0]
                record = book.find(name)
                if record:
                    print(f"{name}'s phones: {', '.join(phone.value for phone in record.phones)}")
                else:
                    print("Contact not found.")

            case "all":
                if not book.get_all_records():
                    print("No contacts found.")
                else:
                    for record in book.get_all_records():
                        print(f"{record.name.value}: {', '.join([phone.value for phone in record.phones])}")

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
