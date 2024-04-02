import json
from datetime import datetime

class Note:
    def __init__(self, id, title, body):
        # Конструктор класса Note, инициализирует заметку с указанными атрибутами
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def update_body(self, new_body):
        # Метод для корректировки тела заметки и установки новой даты обновления
        if self.body:  # Проверяем, что у заметки уже есть текст
            if new_body:
                self.body += "\n" + new_body  # Добавляем новый текст к старому с новой строки
                self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                print("Текст заметки не был обновлен.")
        else:
            print("Не удается обновить текст для заметки, текста не существует.")

    def to_dict(self):
        # Метод для преобразования заметки в словарь для сохранения в JSON
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(note_dict):
        # Статический метод для создания объекта Note из словаря (для загрузки из JSON)
        return Note(
            note_dict["id"],
            note_dict["title"],
            note_dict["body"]
        )

    def __str__(self):
        # Метод для форматированного вывода информации о заметке
        return f"ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\nCreated At: {self.created_at}\nUpdated At: {self.updated_at}"