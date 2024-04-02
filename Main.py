from NoteManager import NoteManager


def main():
    file_path = "notes.json"  # Путь к файлу для сохранения заметок
    note_manager = NoteManager(file_path)  # Создаем объект NoteManager

    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Удалить заметку")
        print("3. Редактировать заметку")
        print("4. Показать все заметки")
        print("5. Показать заметки по дате (YYYY-MM-DD):")
        print("6. Выход")

        choice = input("Введите цифру меню: ")  # Получаем выбор пользователя

        if choice == "1":
            title = input("Введите заголовок заметки: ")  # Получаем заголовок заметки
            body = input("Введите тело заметки: ")  # Получаем тело заметки
            note_manager.add_note(title, body)  # Вызываем метод добавления заметки
        elif choice == "2":
            note_id = int(input("Введите ID заметки для удаления: "))  # Получаем id заметки для удаления
            note_manager.delete_note(note_id)  # Вызываем метод удаления заметки
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))  # Получаем id заметки для редактирования
            if note_manager.check_note_exists(note_id):  # Проверяем существование заметки по ID
                new_body = input("Введите новое тело заметки: ")  # Получаем новое тело заметки
                note_manager.edit_note_body(note_id, new_body)  # Вызываем метод редактирования заметки
            else:
                print("Ошибка: Заметка с ID {} не существует.".format(note_id))
        elif choice == "4":
            note_manager.get_all_notes()  # Вызываем метод вывода всех заметок
        elif choice == "5":
            date = input("Введите дату в формате (YYYY-MM-DD) для вывода заметки: ")  # Получаем дату для поиска заметок
            note_manager.get_notes_by_date(date)  # Вызываем метод вывода заметок по дате
        elif choice == "6":
            print("Good luck!")  # Выводим сообщение о выходе
            break  # Завершаем выполнение цикла и приложения
        else:
            print("Неправильный выбор меню. Попытайтесь снова.")  # Выводим сообщение об ошибке в случае некорректного выбора

if __name__ == "__main__":
    main()  # Вызываем основную функцию main() для запуска приложения
