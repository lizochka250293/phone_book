import string
import os  # Библиотека, необходимаяя для получения списка файлов и папок
import json  # Можно применять в качестве формата для хранения книги
import csv  # Так же можно применять в качестве формата хранения


class Contact:
    """
    Класс описывает контакт для телефонной книги
    """
    first_name = ''
    last_name = ''
    __phone = ''

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.__phone = phone


    @property
    def phone(self):
        """
        Свойство возвращающее телефонный номер
        :return:
        """
        return self.__phone
    @staticmethod
    def is_include_digit(phone):
        ph: str = phone[1:]
        if ph.isdigit():
            return True
        return False

    @phone.setter
    def phone(self, phone):
        if not Contact.is_include_digit(phone):
            raise ValueError("Телефон должен состоять из цифр")
        self.__phone = phone

        """
        Метод задающий номер телефона и проверяющий его валидность
        """



class PhoneBook:
    book_filename = ''
    contact_list = []
    book_data = None

    def __init__(self, book_filename):
        # Check if file exists
        self.book_filename = book_filename
        self.load_book(book_filename)


    def add_contact(self, contact):
        """
        Метод добавляющий экземпляр класса Contact в contact_list
        :param contact: Экземпляр класса Contact например: c = Contact('Алексей', 'Иванов')
        """
        self.contact_list.append(contact)




    def get_contact(self, **kwargs):
        """
        Метод возвращающий объект Contact или их список, удовлетворяющий критериям поиска
        :param kwargs: любые свойства класса Contact.
        Например:
            book.get_contact(first_name='Олег') -> [<class Contact: Олег Иванов>, <class Contact: Олег Петров>]
        """
        contacts = []
        for item in self.contact_list:
            result = []
            for key, value in kwargs.items():
                try:
                    result.append(item.__getattribute__(key) == value)
                except:
                    print('Такого атрибута нет')
            if len(result) and all(result):
                contacts.append(item)
        return contacts

    def get_contact_index(self, contact):
        return self.contact_list.index(contact)

    def remove_contact(self, index):
        """
        Удаляет контакт из списка contact_list по его индексу и возвращает его
        :param index: индекс элемента в списке contact_list
        :return: Contact
        """

        return self.contact_list.pop(index)

    def save_changes(self):
        """
        Сохраняет изменения в файл
        """
        self.book_data = []
        for item in self.contact_list:
            self.book_data.append({
                'first_name': item.first_name,
                'last_name': item.last_name,
                'phone': item.phone
            })

        with open(self.book_filename, "w", encoding="UTF-8") as f:
            json.dump(self.book_data, f)

    def load_book(self, book_filename):
        """
        Загружает список контактов из файла телефонной книги. Если файл отсутствует, то создает его
        """
        with open(book_filename, 'r', encoding="UTF-8") as f:
            self.book_data = json.load(f)
        if self.book_data:
            for item in self.book_data:
                self.add_contact(Contact(**item))


def touch(path):
    # Функция создает пустой текстовый файл. Аналог команды touch в Unix
    with open(path, 'a', encoding='utf-8'):
        os.utime(path, None)

# book = PhoneBook('books/book1.json')

def start():
    # Проверяем папку с телефонными книгами и если ее нет, то создаем
    if not os.path.exists('books'):
        os.mkdir('books')
    books = os.listdir('books')  # Получаем список телефонных книг из папки

    no_books = True
    if len(books):
        no_books = False
        print('Выберите телефонную книгу из списка:')
        for i, book in enumerate(books):
            print(f'{i + 1}. {book}')
        print('0: Создать новую')
    else:

        print('Введите название для новой телефонной книги')

    answer = input('Введите ответ: ')
    book_filename = None
    create_book = False

    if no_books:
        # Если пока нету ни одной книги
        create_book = True
        book_filename = os.path.join('books', answer)
    elif answer == '0' and not no_books:
        # Если ответ 0, то создаем новую
        create_book = True
        book_filename = os.path.join('books', input('Введите имя файла: '))
    elif answer.isdigit() and not no_books:
        # Если ответ - цифра и книги есть
        book_filename = os.path.join('books', books[int(answer) - 1])
    else:
        print('Вы что-то ввели не так!')

    if create_book:
        # Создаем пустой файл для книги
        touch(book_filename)

    phone_book = PhoneBook(book_filename)

    print(phone_book)

    while True:
        answers = '0: Создать контакт\n1: Удалить контакт\n' \
                  '2: Получить контакт\n3: Сохранить изменения\n' \
                  '4: Напечатать список контаков\n!q: Выход\n'
        answer = input(answers)
        if answer == '0':
            # Add contact
            contact_data = {
                'first_name': input('Введите имя: '),
                'last_name': input('Введите фамилию: '),
                'phone': input('Введите телефон: ')
            }
            phone_book.add_contact(Contact(**contact_data))

        elif answer == '1':
            # Delete contact
            try:
                index = int(input('Введите номер контакта из списка'))
                phone_book.remove_contact(index)
            except:
                print('Произошла ошибка!\n')
            pass
        elif answer == '2':
            # Get contact
            contact_data = {
                'first_name': input('Введите имя: '),
                'last_name': input('Введите фамилию: '),
                'phone': input('Введите телефон: ')
            }
            kwargs = {}
            for key in contact_data.keys():
                if contact_data[key] != '':
                    kwargs[key] = contact_data[key]
            contacts = phone_book.get_contact(**kwargs)
            for index, contact in enumerate(contacts):
                print(f'{index}: {contact.first_name} {contact.last_name} {contact.phone}')
            print('\n')
        elif answer == '3':
            # Save changes
            phone_book.save_changes()
            print('Saved!')
        elif answer == '4':
            # Get contact list
            for index, contact in enumerate(phone_book.contact_list):
                print(f'{index}: {contact.first_name} {contact.last_name} {contact.phone}')
            print('\n')

        elif answer == '!q':
            # Exit
            break

    print('До свидания!')


start()
