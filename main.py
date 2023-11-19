from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): # реалізація класу
    ...

class Phone(Field):
    def __init__(self, phone):
        self.validate_phone(phone)
        super().__init__(phone)

    def validate_phone(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number format.")

class Record: # реалізація класу
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))            

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def remove_phone(self, phone):
        self.phones.remove(self.find_phone(phone))

    def edit_phone(self, phone, new_phone):
        existing_phone = self.find_phone(phone)
        if existing_phone:
            existing_phone.value = new_phone
        else:
            raise ValueError("Phone not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict): # реалізація класу
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record

    def find(self, name):
        key = Name(name).value
        return self.data.get(key)

    def delete(self, name):
        key = Name(name).value
        
        if self.find(key):
            del self.data[key]
            
        
if __name__ == '__main__':
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
