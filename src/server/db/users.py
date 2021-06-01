import sqlite3


class Users:
    def __init__(self, db_connection):
        self.create_table = """CREATE TABLE IF NOT EXISTS users (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    auth_id text NOT NULL,
                                    access_token text,
                                    refresh_token text
                                );"""
        sqlite3.create_table(db_connection, self.create_table)
