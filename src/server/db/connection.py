import sqlite3
import os


class Database:
    def __init__(self):
        self.db_name = os.environ.get("DATABASE_NAME")
        self.connection = sqlite3.connect(self.db_name+".db")
        print("connected to "+self.db_name)
