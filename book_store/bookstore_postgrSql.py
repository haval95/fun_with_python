import tkinter as tk
import psycopg2


def create_table():
    conn = psycopg2.connect(
        "dbname='bookstore' user='postgres' password='root' port='5432'"
    )
    cur = conn.cursor()
    cur.execute(
        " CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"
    )
    conn.commit()
    conn.close()


def insert(item: str, quantity: int, price: float):
    conn = psycopg2.connect(
        "dbname='bookstore' user='postgres' password='root' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname='bookstore' user='postgres' password='root' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    data = cur.fetchall()
    conn.close()
    return data


def delete(item):
    conn = psycopg2.connect(
        "dbname='bookstore' user='postgres' password='root' port='5432'"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(oldItem, item, quantity, price):
    conn = psycopg2.connect(
        "dbname='bookstore' user='postgres' password='root' port='5432'"
    )
    cur = conn.cursor()
    cur.execute(
        "UPDATE store SET item=%s, quantity=%s , price=%s WHERE item=%s",
        (item, quantity, price, oldItem),
    )
    conn.commit()
    conn.close()


create_table()
update("oop", "object orianted programming", 10, 22.60)
delete("clean code")
print(view())

window = tk.Tk()


def send_data():
    if item_value.get():
        insert(item_value.get(), int(quantity_value.get()), float(price_value.get()))
        clear_entry()


def clear_entry():
    item.delete(0, tk.END)
    price.delete(0, tk.END)
    quantity.delete(0, tk.END)


b1 = tk.Button(window, text="Excute", command=send_data)

label_item = tk.Label(window, text="Book Name:")
item_value = tk.StringVar()
item = tk.Entry(window, textvariable=item_value)

label_quantity = tk.Label(window, text="Quantity:")
quantity_value = tk.StringVar()
quantity = tk.Entry(window, textvariable=quantity_value)

lable_price = tk.Label(window, text="Price")
price_value = tk.StringVar()
price = tk.Entry(window, textvariable=price_value)

label_quantity.grid(row=0, column=0)
quantity.grid(row=0, column=1)
lable_price.grid(row=0, column=2)
price.grid(row=0, column=3)
label_item.grid(row=1, column=0)
item.grid(row=1, column=1, rowspan=2)
b1.grid(row=2, column=0, rowspan=3)


window.mainloop()
