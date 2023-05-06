from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = [phone]

    def add_phone(self, phone):
        self.phone.append(phone)

    def remove_phone(self, phone):
        self.phone.remove(phone)

    def change_phone(self, old_phone, new_phone):
        old_index = self.phone.index(old_phone)
        self.phone[old_index] = new_phone


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, name: str):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

