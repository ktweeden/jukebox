import sqlite3


class Rfid_tags:
    def __init__(self, db_connection):
        self.create_table = """CREATE TABLE IF NOT EXISTS RFID_TAGS (
                                    ID integer PRIMARY KEY,
                                    TAG_VALUE text NOT NULL,
                                    SPOTIFY_URI text
                                );"""
        self.db_connection = db_connection
        sqlite3.create_table(db_connection, self.create_table)

    def save_new_tag(self, rfid_value):
        sql = """INSERT INTO RFID_TAGS (TAG_VALUE)
                VALUES (?)"""
        self.db_connection.execute(sql, (rfid_value))
        self.db_connection.commit()

    def add_spotify_resource_to_tag(self, rfid_value, spotify_uri):
        sql = """UPDATE RFID_TAGS
              SET SPOTIFY_URI = ?,
              WHERE TAG_VALUE = ?"""
        self.db_connection.execute(sql, (spotify_uri, rfid_value))
        self.db_connection.commit()

    def get_spotify_resource_for_tag(self, rfid_value):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "SELECT * FROM RFID_TAGS WHERE TAG_VALUE=?", (rfid_value))
        self.db_connection.commit()
        rows = cursor.fetchall()
