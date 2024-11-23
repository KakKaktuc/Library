import json
import uuid

class Library:

    def add_book():
        "добавить книгу"

        try:
            with open('Books.json','r',encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, FileExistsError):
            books = []
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")

        books_id = str(uuid.uuid4())
        
        book = {
            "id":books_id,
            "title": title,
            "author": author,
            "year": year,
            "status":"в наличии"
        }
        books.append(book)
        with open('Books.json', 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

        print("Книга успешно добавлена!")



    def delete_books():
        "удалить книгу"
        try:
            with open('Books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл не найден или пуст.")
            return

        # Просим пользователя ввести id книги
        book_id = input("Введите id книги, которую нужно удалить: ")

        # Ищем книгу с указанным id
        filtered_books = [book for book in books if book['id'] != book_id]

        # Проверяем, была ли удалена книга
        if len(books) == len(filtered_books):
            print("Книга с указанным id не найдена.")
        else:
            # Сохраняем обновленный список в файл
            with open('Books.json', 'w', encoding='utf-8') as file:
                json.dump(filtered_books, file, ensure_ascii=False, indent=4)
            print("Книга успешно удалена!")    
    

    def find_books():
        "найти книгу"
        try:
            with open('Books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл не найден или пуст.")
            return

        # Просим пользователя выбрать критерий поиска
        print("Выберите критерий поиска:")
        print("1. Название книги (title)")
        print("2. Автор (author)")
        print("3. Год издания (year)")
        choice = input("Введите номер критерия: ")

        if choice == "1":
            query = input("Введите название книги: ").strip().lower()
            found_books = [book for book in books if query in book['title'].lower()]
        elif choice == "2":
            query = input("Введите имя автора: ").strip().lower()
            found_books = [book for book in books if query in book['author'].lower()]
        elif choice == "3":
            query = input("Введите год издания: ").strip()
            found_books = [book for book in books if book['year'] == query]
        else:
            print("Неверный выбор.")
            return

        # Выводим результаты поиска
        if found_books:
            print("Найденные книги:")
            for book in found_books:
                print(f"- ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")
        else:
            print("Книги по заданному критерию не найдены.")


    def display_books():
        "отобразить все книги"
        try:
            with open('Books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл не найден или пуст.")
            return

        # Проверяем, есть ли книги в списке
        if not books:
            print("Список книг пуст.")
            return

        # Отображаем список книг
        print("Список всех книг:")
        for book in books:
            print(f"- ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")

    def change_status():
        "изменить статус книги"
        try:
            with open('Books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл не найден или пуст.")
            return
        
        book_id = input("Введите ID книги, статус которой нужно изменить: ")

        # Ищем книгу с указанным ID
        for book in books:
            if book['id'] == book_id:
                # Если книга найдена, запросим новый статус
                new_status = input("Введите новый статус (в наличии/выдана): ").strip().lower()
                if new_status not in ["в наличии", "выдана"]:
                    print("Неверный статус. Статус должен быть 'в наличии' или 'выдана'.")
                    return
            
                # Обновляем статус книги
                book['status'] = new_status

        # Сохраняем изменения в файл
        with open('Books.json', 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

            print("Статус книги успешно обновлён!")
            return

    # Если книга с указанным ID не найдена
        print("Книга с указанным ID не найдена.")

class Main():
    
    def working():
        work = True
        while work == True:
            print("Выбери нужный пункт")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Найти книгу")
            print("4. Отобразить список книг")
            print("5. Изменить статус книги")
            
            choice = input("")

            if choice == "1":
                return Library.add_book()
            elif choice == "2":
                Library.delete_books()
            elif choice == "3":
                Library.find_books()
            elif choice == "4":
                Library.display_books()
            elif choice == "5":
                Library.change_status()
            else:
                print("Такого пункта нет. Попробуй ещё раз.")
                
Main.working()