import json
from Note import Note


class NoteManager:
    def __init__(self, file_path):
        # Конструктор класса NoteManager, инициализирует менеджер заметок с указанным путем к файлу
        self.file_path = file_path
        self.notes = self.load_notes()  # Загружаем заметки из файла при создании менеджера

    def load_notes(self):
        # Метод для выгрузки заметок из файла
        try:
            with open(self.file_path, "r") as file:
                notes_data = json.load(file)
                return [Note.from_dict(note) for note in notes_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Если файл не найден или данные не могут быть прочитаны, возвращаем пустой список

    def save_notes(self):
        # Метод для сохранения заметок в файл
        with open(self.file_path, "w") as file:
            notes_data = [note.to_dict() for note in self.notes]
            json.dump(notes_data, file, indent=4)

    def add_note(self, title, body):
        # Метод для добавления новой заметки
        new_id = len(self.notes) + 1
        new_note = Note(new_id, title, body)
        self.notes.append(new_note)
        self.save_notes()
        print(f"Заметка с ID {new_id} добавлена.")

    def delete_note(self, note_id):
        # Метод для удаления заметки по ID
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()
        print(f"Заметка с ID {note_id} удалена.")

    def edit_note_body(self, note_id, new_body):
        # Метод для редактирования заметки по ID
        for note in self.notes:
            if note.id == note_id:
                print(f"Текущий текст заметки с ID {note_id}:")
                print(note.body)
                choice = input("1. Добавить новый текст\n2. Исправить текущий текст\nВыберите действие: ")
                if choice == "1":
                    note.update_body(new_body)
                elif choice == "2":
                    note.body = new_body
                else:
                    print("Неправильный выбор. Текст заметки не изменен.")
                self.save_notes()
                print(f"Заметка с ID {note_id} отредактирована.")
                return
        print(f"Заметка с ID {note_id} не найдена.")

    def check_note_exists(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return True
        return False

    def get_all_notes(self):
        # Метод для вывода всех заметок на экран
        for note in self.notes:
            print(note)

    def get_notes_by_date(self, date):
        # Метод для вывода заметок, созданных в указанную дату
        notes_on_date = [note for note in self.notes if note.created_at.startswith(date)]
        if not notes_on_date:
            print(f"Нет заметок с указанной датой: {date}")
        else:
            for note in notes_on_date:
                print(note)
