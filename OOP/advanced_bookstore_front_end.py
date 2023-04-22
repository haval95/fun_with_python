import tkinter as tk
from oop_bookstore_backend import Database


class Bookstore_fornt(Database):
    def __init__(self):
        super(Database, self).__init__()
        window = tk.Tk()
        window.title("BOOK DATABASE")

        frame = tk.Frame(window, padx=10, pady=10)
        frame.pack()

        label_title = tk.Label(frame, text="Title:")
        title_value = tk.StringVar()
        title = tk.Entry(frame, textvariable=title_value)
        label_title.grid(row=0, padx=10, pady=5, column=0)
        title.grid(row=0, padx=10, pady=5, column=1)

        label_author = tk.Label(frame, text="Author:")
        author_value = tk.StringVar()
        author = tk.Entry(frame, textvariable=author_value)
        label_author.grid(row=0, padx=10, pady=5, column=2)
        author.grid(row=0, padx=10, pady=5, column=3)

        lable_year = tk.Label(frame, text="Year")
        year_value = tk.StringVar()
        year = tk.Entry(frame, textvariable=year_value)
        lable_year.grid(row=1, padx=10, pady=5, column=0)
        year.grid(row=1, padx=10, pady=5, column=1, rowspan=2)

        lable_isbn = tk.Label(frame, text="ISBN")
        isbn_value = tk.StringVar()
        isbn = tk.Entry(frame, textvariable=isbn_value)
        lable_isbn.grid(row=1, padx=10, pady=5, column=2)
        isbn.grid(row=1, padx=10, pady=5, column=3)

        result_list = tk.Listbox(frame, width=35, height=6)
        scrollbar = tk.Scrollbar(frame)
        result_list.grid(row=3, rowspan=5, column=0, columnspan=2, sticky="NSEW")
        scrollbar.grid(row=3, rowspan=5, column=2, sticky="NS")
        scrollbar.config(width=15, command=result_list.yview)

        result_list.bind("<<ListboxSelect>>", get_selected_row)

        viewAll = tk.Button(frame, text="view All", width=20, command=showData)
        searchEntry = tk.Button(frame, text="Search Entry", width=20, command=serachData)
        addData = tk.Button(frame, text="Add Data", width=20, command=send_data)
        updateSelected = tk.Button(
            frame, text="Update Selected", width=20, command=updateData
        )
        deleteSelected = tk.Button(
            frame, text="Delete Selected", width=20, command=deleteData
        )
        close = tk.Button(frame, text="Close", width=20, command=window.destroy)

        viewAll.grid(row=3, padx=10, column=3)
        searchEntry.grid(row=4, padx=10, column=3)
        addData.grid(row=5, padx=10, column=3)
        updateSelected.grid(row=6, padx=10, column=3)
        deleteSelected.grid(row=7, padx=10, column=3)
        close.grid(row=8, padx=10, column=3)
        window.mainloop()

    def send_data(self):
        if title.get():
            database.insert(
                title_value.get(),
                author_value.get(),
                year_value.get(),
                isbn_value.get(),
            )
            result_list.insert(
                tk.END,
                (
                    f"ADDED: { title_value.get(), author_value.get(), year_value.get(), isbn_value.get(),}"
                ),
            )
            clear_entry()

    def clear_entry(self):
        title.delete(0, tk.END)
        author.delete(0, tk.END)
        isbn.delete(0, tk.END)
        year.delete(0, tk.END)

    def showData(self):
        result_list.delete(0, tk.END)
        for row in database.view():
            result_list.insert(tk.END, row)

    def serachData(self):
        result_list.delete(0, tk.END)
        for row in database.Serach(
            title_value.get(), author_value.get(), year_value.get(), isbn_value.get()
        ):
            result_list.insert(tk.END, row)

    def get_selected_row(self, event=""):
        try:
            global selected_tuple
            index = result_list.curselection()[0]
            selected_tuple = result_list.get(index)
            clear_entry()
            title.insert(tk.END, selected_tuple[1])
            author.insert(tk.END, selected_tuple[2])
            year.insert(tk.END, selected_tuple[3])
            isbn.insert(tk.END, selected_tuple[4])
        except Exception:
            return

    def deleteData(self):
        database.delete(selected_tuple[0])
        clear_entry()
        showData()

    def updateData(self):
        database.update(
            selected_tuple[0],
            title_value.get(),
            author_value.get(),
            year_value.get(),
            isbn_value.get(),
        )
        showData()

    


