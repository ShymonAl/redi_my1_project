# створюємо базу книг
database = {
    1: "Книги для відпочинку",
    2: "Мотиваційні",
    3: "Детектив",
    4: "Триллери",
    5: "Історичні",
    6: "Психологічні"
}

books = {
    "Книги для відпочинку": [
        "Зелене світло",
        "Кульбабове вино",
        "Пляжне чтиво",
        "Чоловік на ім'я Уве",
        "Кафе на краю світу"
    ],
    "Мотиваційні": [
        "Як стати успішним за 30 днів",
        "Щурині перегони",
        "Їж, молись, кохай",
        "Генрі Марш. Історія успішного нейрохірурга",
        "Ідеальний код без зусиль"
    ],
    "Детектив": [
        "Шерлок Холмс і Доктор Ватсон",
        "Агата Крісті. Смерть на Нілі",
        "Випадкова вакансія",
        "Людина яка померла двічи",
        "Клуб загадкових вбивств по четвергам"
    ],
    "Триллери": [
        "Моє життя",
        "Сніговик",
        "Привид",
        "Темний ліс",
        "Дім, в якому..."
    ],
    "Історичні": [
        "І будуть люди..",
        "Сад Гетсиманський",
        "Імя рози",
        "Ярмарок марнославства",
        "Знедолені"
    ],
    "Психологічні": [
        "1984",
        "Маленькі жінки",
        "І всюди тліють пожежі",
        "Несказане",
        "Тривожні люди"
    ],
}

# Функція для додавання книги до бази даних
def add_book(genre, book):
    if genre in books:
        if book not in books[genre]:
            books[genre].append(book)
            print(f"Книга '{book}' додана у жанр '{genre}'.")
        else:
            print(f"Книга '{book}' вже присутня у жанрі '{genre}'.")
    else:
        print(f"Жанр '{genre}' не знайдений у базі даних.")

# Функція для видалення книги з бази даних
def delete_book(genre, book):
    if genre in books and book in books[genre]:
        books[genre].remove(book)
        print(f"Книга '{book}' видалена з жанру '{genre}'.")
    else:
        print(f"Книга '{book}' не знайдена у жанрі '{genre}'.")

# Функція для виведення списку книг у жанрі
def print_books(genre):
    if genre in books:
        print("Список книг у жанрі", genre, ":")
        for i, book in enumerate(books[genre], start=1):
            print(f"{i}. {book}")
    else:
        print("Жанр", genre, "не знайдений у базі даних.")

# Функція для отримання жанру за назвою або номером
def get_genre(choice):
    if choice.isdigit():
        genre_num = int(choice)
        if genre_num in database:
            return database[genre_num]
    else:
        for genre_num, genre_name in database.items():
            if genre_name.lower() == choice.lower():
                return genre_name
    return None

# Головний цикл програми
while True:
    # Виводимо доступні дії
    print("Виберіть дію:")
    print("1. Вивести список всіх доступних книг")
    print("2. Додати книгу")
    print("3. Видалити книгу")
    print("4. Вийти")

    # Користувач вводить номер дії
    choice = input("Ваш вибір: ")

    if choice == '1':  # Якщо обрана дія - вивести список всіх доступних книг
        print("Список всіх доступних книг:")
        for genre_num, genre_name in database.items():
            print(f"{genre_num}. {genre_name}:")
            print_books(genre_name)
            print()
    elif choice == '2':  # Якщо обрана дія - додати книгу
        genre_choice = input("Введіть назву або номер жанру: ")
        genre = get_genre(genre_choice)
        if genre:
            book = input("Введіть назву книги: ")
            add_book(genre, book)  # Викликаємо функцію для додавання книги до бази
        else:
            print("Некоректний жанр.")
    elif choice == '3':  # Якщо обрана дія - видалити книгу
        genre_choice = input("Введіть назву або номер жанру: ")
        genre = get_genre(genre_choice)
        if genre:
            book = input("Введіть назву книги: ")
            delete_book(genre, book)  # Викликаємо функцію для видалення книги з бази
        else:
            print("Некоректний жанр.")
    elif choice == '4':  # Якщо обрана дія - вийти
        print("До побачення!")
        break
    else:
        print("Некоректний вибір дії.")

    print()  # Розділюємо вивід дій від наступного виводу
