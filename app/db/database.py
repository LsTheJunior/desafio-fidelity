from tinydb import TinyDB
from app.core.config import DB_PATH


# Singleton para TinyDB
class Database:
    _instance = None

    @classmethod
    def get_db(cls):
        if cls._instance is None:
            cls._instance = TinyDB(DB_PATH)
        return cls._instance


db = Database.get_db()
