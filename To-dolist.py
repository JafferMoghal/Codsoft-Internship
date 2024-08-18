from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is empty.')
    else:
        tasks.append(task_string)
        cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task_string,))
        connection.commit()
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            cursor.execute('DELETE FROM tasks WHERE title=?', (the_value,))
            connection.commit()
            list_update()
    except:
        messagebox.showinfo('Error', 'No task selected. Cannot delete.')

def delete_all_tasks():
    if messagebox.askyesno('Confirm', 'Are you sure you want to delete all tasks?'):
        tasks.clear()
        cursor.execute('DELETE FROM tasks')
        connection.commit()
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    connection.close()
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do LIST")
    guiWindow.geometry("665x400+550+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#B5E5CF")

    connection = sql.connect('listofTasks.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

    tasks = []
    functions_frame = Frame(guiWindow, bg="#850309")
    functions_frame.pack(side="top", expand=True, fill="both")

    task_label = Label(functions_frame, text="To-do LIST\n ENTER THE TASK:",
                       font=("Arial", "14", "bold"),
                       background="#850309",
                       foreground="#ffffff")
    task_label.place(x=20, y=30)

    task_field = Entry(functions_frame,
                       font=("Arial", "14"),
                       width=42,
                       foreground="black",
                       background="white")
    task_field.place(x=180, y=30)

    add_button = Button(functions_frame,
                        text="Add",
                        width=15,
                        bg='#0dd460',
                        font=("Arial", "14", "bold"),
                        command=add_task)
    add_button.place(x=18, y=80)

    del_button = Button(functions_frame,
                        text="Remove",
                        width=15,
                        bg='#0dd460',
                        font=("Arial", "14", "bold"),
                        command=delete_task)
    del_button.place(x=240, y=80)

    del_all_button = Button(functions_frame,
                            text="Delete all",
                            width=15,
                            bg='#0dd460',
                            font=("Arial", "14", "bold"),
                            command=delete_all_tasks)
    del_all_button.place(x=460, y=80)

    exit_button = Button(functions_frame,
                         text="Exit/Close",
                         width=52,
                         bg='#0dd460',
                         font=("Arial", "14", "bold"),
                         command=close)
    exit_button.place(x=17, y=330)

    task_listbox = Listbox(functions_frame,
                           width=70,
                           height=9,
                           font="bold",
                           selectmode="SINGLE",
                           background="WHITE",
                           foreground="BLACK",
                           selectbackground="#41ee33",
                           selectforeground="BLACK")
    task_listbox.place(x=17, y=140)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
