import tkinter as tk
import sqlite3 as sql3


def create_table():
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute(
        " CREATE TABLE IF NOT EXISTS store (title TEXT, author TEXT, year TEXT, ISBN TEXT)"
    )
    conn.commit()
    conn.close()


def insert(title: str, author: str, year: str, ISBN: str):
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?,?)", (title, author, year, ISBN))
    conn.commit()
    conn.close()


def view():
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    data = cur.fetchall()
    conn.close()
    return data


def delete(item):
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    data = cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()
    return f"{data.rowcount} Deleted"


def update(oldItem, item, quantity, price):
    conn = sql3.connect("bookstore.db")
    cur = conn.cursor()
    data = cur.execute(
        "UPDATE store SET item=?, quantity=? , price=? WHERE item=?",
        (item, quantity, price, oldItem),
    )
    conn.commit()
    conn.close()
    return f"{data.rowcount} Updated"


create_table()


def send_data():
    if title.get():
        insert(
            title.get(), author.get(), year.get(), isbn.get(),
        )
        clear_entry()


def clear_entry():
    title.delete(0, tk.END)
    author.delete(0, tk.END)
    isbn.delete(0, tk.END)
    year.delete(0, tk.END)


def showData():
    for idx, row in enumerate(view()):
        views.insert(tk.END, (f"{idx+1}: {row[0]} - {row[1]} - {row[2]} - {row[3]}\n"))
        
   
window = tk.Tk()


frame = tk.Frame(window, padx=10, pady=10)
frame.pack()

label_title = tk.Label(frame, text="Title:")
title_value = tk.StringVar()
title = tk.Entry(frame, textvariable=title_value)

label_author = tk.Label(frame, text="Author:")
author_value = tk.StringVar()
author = tk.Entry(frame, textvariable=author_value)

lable_year = tk.Label(frame, text="Year")
year_value = tk.StringVar()
year = tk.Entry(frame, textvariable=year_value)

lable_isbn = tk.Label(frame, text="ISBN")
isbn_value = tk.StringVar()
isbn = tk.Entry(frame, textvariable=isbn_value)

scrollbar = tk.Scrollbar(frame)


views = tk.Text(frame, width=2, height=10, yscrollcommand=scrollbar.set, wrap="none")

viewAll = tk.Button(frame, text="view All", width=20, command=showData)
searchEntry = tk.Button(frame, text="Search Entry", width=20, command=send_data)
addData = tk.Button(frame, text="Add Data", width=20, command=send_data)
updateSelected = tk.Button(frame, text="Update Selected", width=20, command=send_data)
deleteSelected = tk.Button(frame, text="Delete Selected", width=20, command=send_data)
close = tk.Button(frame, text="Close", width=20, command=send_data)

label_title.grid(row=0, padx=10, pady=5, column=0)
title.grid(row=0, padx=10, pady=5, column=1)
label_author.grid(row=0, padx=10, pady=5, column=2)
author.grid(row=0, padx=10, pady=5, column=3)
lable_year.grid(row=1, padx=10, pady=5, column=0)
year.grid(row=1, padx=10, pady=5, column=1, rowspan=2)
lable_isbn.grid(row=1, padx=10, pady=5, column=2)
isbn.grid(row=1, padx=10, pady=5, column=3)

views.grid(row=3, rowspan=5, column=0, columnspan=2, sticky="NSEW")
scrollbar.grid(row=3, rowspan=5, column=2, sticky="NS")
scrollbar.config(width=20, command=views.yview)

viewAll.grid(row=3, padx=10, column=3)
searchEntry.grid(row=4, padx=10, column=3)
addData.grid(row=5, padx=10, column=3)
updateSelected.grid(row=6, padx=10, column=3)
deleteSelected.grid(row=7, padx=10, column=3)
close.grid(row=8, padx=10, column=3)



window.mainloop()
