import sqlite3 as sql3


def create_table():
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute(
        " CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, ISBN INTEGER)"
    )
    conn.commit()
    conn.close()


def insert(title, author, year, ISBN):
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (NULL,?,?,?,?)", (title, author, year, ISBN))
    conn.commit()
    conn.close()


def view():
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    data = cur.fetchall()
    conn.close()
    return data


def Serach(title="", author="", year="", ISBN=""):
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM store WHERE title=? OR author= ? OR year= ? OR ISBN= ?",
        (title, author, year, ISBN),
    )
    data = cur.fetchall()
    conn.close()
    return data


def delete(id):
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    data = cur.execute("DELETE FROM store WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return f"{data.rowcount} Deleted"


def update(id, title, author, year, ISBN):
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    data = cur.execute(
        "UPDATE store SET title=?, author=?, year=?, ISBN=? WHERE id=?",
        (title, author, year, ISBN, id),
    )
    conn.commit()
    conn.close()
    return f"{data.rowcount} Updated"


create_table()

