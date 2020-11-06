from tkinter import *
from tkinter import messagebox
from db import Database
root = Tk()

root.title("Student Info")
root.geometry('750x400')
db = Database('students.db')


def populate_all():
    list_box.delete(0, END)
    for row in db.fetch():
        list_box.insert(END, row)


def add_item():
    if name_text.get() == "" or class_text.get() == '' or email_text.get() == '' or address_text.get() == '':
        messagebox.showerror("Requires Fields", "All Field must be include.")
    else:
        db.add(name_text.get(), class_text.get(),
               email_text.get(), address_text.get())
        clear_text()
        populate_all()


def select_item(event):
    try:
        global selected_item
        index = list_box.curselection()
        selected_item = list_box.get(index)

        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])

        class_entry.delete(0, END)
        class_entry.insert(END, selected_item[2])

        email_entry.delete(0, END)
        email_entry.insert(END, selected_item[3])

        address_entry.delete(0, END)
        address_entry.insert(END, selected_item[4])
    except EXCEPTION as e:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_all()


def update_item():
    try:
        db.update(selected_item[0], name_text.get(
        ), class_text.get(), email_text.get(), address_text.get())
        clear_text()
        populate_all()
    except:
        pass


def clear_text():
    name_entry.delete(0, END)

    class_entry.delete(0, END)

    email_entry.delete(0, END)

    address_entry.delete(0, END)


# Name
name_text = StringVar()
name_label = Label(root, text="Name", font=(
    'bold', 14), bg='#4b7bec', fg='white')
name_label.grid(row=0, column=0, sticky=W, pady=20)
name_entry = Entry(root, textvariable=name_text, font=('lucida 12'))
name_entry.grid(row=0, column=1)

class_text = StringVar()
class_label = Label(root, text="Class", font=(
    'bold', 14), bg='#4b7bec', fg='white')
class_label.grid(row=0, column=3, sticky=W)
class_entry = Entry(root, textvariable=class_text, font=('lucida 12'))
class_entry.grid(row=0, column=4)

email_text = StringVar()
email_label = Label(root, text="Email", font=(
    'bold', 14), bg='#4b7bec', fg='white')
email_label.grid(row=1, column=0, sticky=W)
email_entry = Entry(root, textvariable=email_text, font=('lucida 12'))
email_entry.grid(row=1, column=1)

address_text = StringVar()
address_label = Label(root, text="Address", font=(
    'bold', 14), bg='#4b7bec', fg='white')
address_label.grid(row=1, column=3, sticky=W)
address_entry = Entry(root, textvariable=address_text, font=('lucida 12'))
address_entry.grid(row=1, column=4)

# Buttons
add_btn = Button(root, text="Add Item", command=add_item,
                 bg='#3867d6', fg='white', font=("lucida", 10))
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(root, text="Remove Item",
                    command=remove_item,  bg='#3867d6', fg='white', font=("lucida", 10))
remove_btn.grid(row=2, column=1)

update_btn = Button(root, text="Update Item",
                    command=update_item, bg='#3867d6', fg='white', font=("lucida", 10))
update_btn.grid(row=2, column=2)

clear_btn = Button(root, text="Clear Text",
                   command=clear_text,  bg='#3867d6', fg='white', font=("lucida", 10))
clear_btn.grid(row=2, column=3)

# ListBox
list_box = Listbox(root, width=60, height=8, font=(
    'lucida 10 '), bg='white', borderwidth=0)
list_box.grid(row=3, column=0, columnspan=3, rowspan=10, padx=20, pady=20)
list_box.bind('<<ListboxSelect>>', select_item)

populate_all()
root.config(bg='#4b7bec')
root.mainloop()
