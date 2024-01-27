# backend.py
from database_manager import DatabaseManager

class Backend:
    def __init__(self):
        self.db_manager = DatabaseManager('app_data.db')

    def save_text(self, text):
        self.db_manager.store_text(text)
        return "Text stored successfully!"