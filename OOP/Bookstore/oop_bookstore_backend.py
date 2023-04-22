import sqlite3 as sql3


class Database:
    def __init__(self, db):
        self.conn = sql3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            " CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, ISBN INTEGER)"
        )
        self.conn.commit()

    def insert(self, title, author, year, ISBN):
        self.cur.execute(
            "INSERT INTO store VALUES (NULL,?,?,?,?)", (title, author, year, ISBN)
        )
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM store")
        data = self.cur.fetchall()
        return data

    def Serach(self, title="", author="", year="", ISBN=""):
        self.cur.execute(
            "SELECT * FROM store WHERE title=? OR author= ? OR year= ? OR ISBN= ?",
            (title, author, year, ISBN),
        )
        data = self.cur.fetchall()
        return data

    def delete(self, id):
        data = self.cur.execute("DELETE FROM store WHERE id=?", (id,))
        self.conn.commit()
        return f"{data.rowcount} Deleted"

    def update(self, id, title, author, year, ISBN):
        data = self.cur.execute(
            "UPDATE store SET title=?, author=?, year=?, ISBN=? WHERE id=?",
            (title, author, year, ISBN, id),
        )
        self.conn.commit()
        return f"{data.rowcount} Updated"
    
    def __del__(self):
        self.conn.close()
