import tkinter as tk
from oop_bookstore_backend import Database

database = Database("bookstore.db")


class Bookstore_fornt(object):
    def __init__(self, window):
        self.window = window
        self.window.title("BOOK DATABASE")

        frame = tk.Frame(self.window, padx=10, pady=10)
        frame.pack()

        label_title = tk.Label(frame, text="Title:")
        self.title_value = tk.StringVar()
        self.title = tk.Entry(frame, textvariable=self.title_value)
        label_title.grid(row=0, padx=10, pady=5, column=0)
        self.title.grid(row=0, padx=10, pady=5, column=1)

        label_author = tk.Label(frame, text="Author:")
        self.author_value = tk.StringVar()
        self.author = tk.Entry(frame, textvariable=self.author_value)
        label_author.grid(row=0, padx=10, pady=5, column=2)
        self.author.grid(row=0, padx=10, pady=5, column=3)

        lable_year = tk.Label(frame, text="Year")
        self.year_value = tk.StringVar()
        self.year = tk.Entry(frame, textvariable=self.year_value)
        lable_year.grid(row=1, padx=10, pady=5, column=0)
        self.year.grid(row=1, padx=10, pady=5, column=1, rowspan=2)

        lable_isbn = tk.Label(frame, text="ISBN")
        self.isbn_value = tk.StringVar()
        self.isbn = tk.Entry(frame, textvariable=self.isbn_value)
        lable_isbn.grid(row=1, padx=10, pady=5, column=2)
        self.isbn.grid(row=1, padx=10, pady=5, column=3)

        self.result_list = tk.Listbox(frame, width=35, height=6)
        scrollbar = tk.Scrollbar(frame)
        self.result_list.grid(row=3, rowspan=5, column=0, columnspan=2, sticky="NSEW")
        scrollbar.grid(row=3, rowspan=5, column=2, sticky="NS")
        scrollbar.config(width=15, command=self.result_list.yview)

        self.result_list.bind("<<ListboxSelect>>", self.get_selected_row)

        viewAll = tk.Button(frame, text="view All", width=20, command=self.showData)
        searchEntry = tk.Button(
            frame, text="Search Entry", width=20, command=self.serachData
        )
        addData = tk.Button(frame, text="Add Data", width=20, command=self.send_data)
        updateSelected = tk.Button(
            frame, text="Update Selected", width=20, command=self.updateData
        )
        deleteSelected = tk.Button(
            frame, text="Delete Selected", width=20, command=self.deleteData
        )
        close = tk.Button(frame, text="Close", width=20, command=self.window.destroy)

        viewAll.grid(row=3, padx=10, column=3)
        searchEntry.grid(row=4, padx=10, column=3)
        addData.grid(row=5, padx=10, column=3)
        updateSelected.grid(row=6, padx=10, column=3)
        deleteSelected.grid(row=7, padx=10, column=3)
        close.grid(row=8, padx=10, column=3)

    def send_data(self):
        if self.title.get():
            database.insert(
                self.title_value.get(),
                self.author_value.get(),
                self.year_value.get(),
                self.isbn_value.get(),
            )
            self.result_list.insert(
                tk.END,
                (
                    f"ADDED: { self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get(),}"
                ),
            )
            self.clear_entry()

    def clear_entry(self):
        self.title.delete(0, tk.END)
        self.author.delete(0, tk.END)
        self.isbn.delete(0, tk.END)
        self.year.delete(0, tk.END)

    def showData(self):
        self.result_list.delete(0, tk.END)
        for row in database.view():
            self.result_list.insert(tk.END, row)

    def serachData(self):
        self.result_list.delete(0, tk.END)
        for row in database.Serach(
            self.title_value.get(),
            self.author_value.get(),
            self.year_value.get(),
            self.isbn_value.get(),
        ):
            self.result_list.insert(tk.END, row)

    def get_selected_row(self, event=""):
        try:
            global selected_tuple
            index = self.result_list.curselection()[0]
            selected_tuple = self.result_list.get(index)
            self.clear_entry()
            self.title.insert(tk.END, selected_tuple[1])
            self.author.insert(tk.END, selected_tuple[2])
            self.year.insert(tk.END, selected_tuple[3])
            self.isbn.insert(tk.END, selected_tuple[4])
        except Exception:
            return

    def deleteData(self):
        database.delete(selected_tuple[0])
        self.clear_entry()
        self.showData()

    def updateData(self):
        database.update(
            selected_tuple[0],
            self.title_value.get(),
            self.author_value.get(),
            self.year_value.get(),
            self.isbn_value.get(),
        )
        self.showData()


wind = tk.Tk()
Bookstore_fornt(wind)
wind.mainloop()
