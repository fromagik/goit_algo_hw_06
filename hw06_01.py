from collections import UserDict #імпортуємо модуль


class Field(UserDict):  #Клас що використовується для базовий клас для зберігання та обробки імя та номеру
    def __init__(self, value):
        self.value = value
    
    
    def __str__(self):
        return str(self.value)
        

class Name(Field): # Клас що використовується для сберігання та обробки імені контакта
    def __init__(self, value):
        self.value = value
        super().__init__(value)


class Phone(Field): # Клас що використовується для сберігання та обробки номеру контакта
    def __init__(self, phone_number:str):
        if not phone_number.isdigit() or len(phone_number) != 10: # Перевірка на правельний запис номеру, викликає виняток 
            raise ValueError("Номер телефону має складатися з 10 цифр і містити лише цифри.")
        super().__init__(phone_number)


class Record: # Клас що використовується для роботи з контактом
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone: str) -> None:  #Метод для додавання номеру контакта 
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None: #Метод для видалення номеру контакта
        for numer in self.phones:
            if numer.value == phone:
                self.phones.remove(numer)
                break

    def edit_phone(self, phone: str, new_phone:str) -> None: # Метод для зміни номеру контакта
        for numer in self.phones: # Ітеруємось по списку номерів для контакту
            if numer.value == phone: # Якщо значення відповідає вказаному номеру то присвоюється новий номер
                numer.value = new_phone
                break


    def find_phone(self, phone: str) -> str: # Метод для пошуку контакта за номером
        for numer in self.phones:
            if numer.value == phone: # Якщо значення відповідає вказаному номеру то повертається номер
                return phone 
            else: # Або викликається вийняток який вказує що номер не знайжено
                raise ValueError(f'Номер контакту "{phone}" не знайдено.')

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict): # Клас для зберігання всіх контатів 
    def __init__(self):
        self.data = {}
        super().__init__()

    def add_record(self, contact): # Метод що використовується для добавлення нового контакту
        self.data[contact.name.value] = contact

    def find(self, contact): # Метод що використовується для знаходження контакта та повертає інформацію про його
        return self.data.get(contact)
    
    def delete(self, contact): # Метод для видалення контакту з контактонї книги
        del self.data[contact.name.value]


    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
