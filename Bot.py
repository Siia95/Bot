import pickle
import re
from collections import UserDict
from datetime import datetime



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, batch_size):
        records = list(self.data.values())
        for i in range(0, len(records), batch_size):
            yield records[i:i+batch_size]

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self, filename):
        with open(filename, 'rb') as file:
            self.data = pickle.load(file)

    def search(self, query):
        results = []
        for record in self.data. values():
            if re.search(query, record.name.value, re.IGNORECASE):
                results.append(record)
            else:
                for phone in record.phone:
                    if re.search(query, phone.value):
                        results.append(record)
                        break
        return results


class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = Name(name)
        self.phone = []
        for num in phone:
            self.phone.append(Phone(num))
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phone.append(Phone(phone))

    def remove_phone(self, phone):
        self.phone.remove(phone)

    def change_phone(self, old_phone, new_phone):
        try:
            old_index = self.phone.index(old_phone)
            self.phone[old_index] = Phone(new_phone)
        except ValueError:
            print(f"{old_phone} not found in phone list")

    def days_to_birthday(self):
        if not self.birthday:
            return None
        now = datetime.now()
        bday = datetime(now.year, self.birthday.month, self.birthday.day)
        if bday < now:
            bday = datetime(now.year + 1, self.birthday.month, self.birthday.day)
        delta = bday - now
        return delta.days

    @property
    def phones(self):
        return [phone.value for phone in self.phone]

    @property
    def birthday_date(self):
        return self.birthday.value if self.birthday else None

    @birthday_date.setter
    def birthday_date(self, value):
        self.birthday = Birthday(value)



class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        self._value = None
        self.value = phone

    @Field.value.setter
    def value(self, phone):
        if not isinstance(phone, str):
            raise ValueError("Invalid phone number")
        phone = phone.replace(' ', '').replace('-', '')
        if not phone.isdigit():
            raise ValueError("Invalid phone number")
        if len(phone) != 10:
            raise ValueError("Phone number must contain 10 digits")
        self._value = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]

class Birthday(Field):
    def __init__(self, birthday):
        self.value = birthday

    @Field.value.setter
    def value(self, birthday):
        try:
            dt = datetime.strptime(birthday, '%d.%m.%Y')
        except (ValueError, TypeError):
            raise Exception("Invalid birthday. Only string format dd.mm.yyyy")
        self._value = dt.date()



