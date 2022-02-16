Консольное приложение выполняющее функции телефонной книги. В приведенном шаблоне кода созданы два класса:

Contact - объект списка контактов, умеющий хранить имя, фамилию и номер телефона,
PhoneBook - объект телефонной книги, хранящий объекты типа Contact, умеющий добавлять/удалять/получать/искать контакты, а так же читать список из файла и писать в файл.
Приложение реализует следующий функционал:

1. Пользователь запускает приложение и у него спрашивается номер книги из списка, либо предлагается создать новую.
2. Создется бесконечный цикл, в котором у пользователя спрашивают на выбор действия по созданию, удалению, получению, сохранению контакта. Для выхода в любой момент пользователю требуется ввести !q.
3. Реализован методы телефонной книги и контакта для получения списка контактов из книги по индексу контакта, фамилии или имени.
4. Реализован метод для удаления контакта из книги.
5. Реализован метод для создания нового контакта.
6. Реализован метод для сохранения нового контакта.
7. Контакты хранятся в текстовых файлах в любом удобном виде. 