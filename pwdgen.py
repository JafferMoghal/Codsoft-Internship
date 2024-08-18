from tkinter import *
import random
import string

root = Tk()
root.geometry('400x200')
passstr = StringVar()
pwd_len = IntVar()

def get_pass():
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = ""
    length = pwd_len.get()
    if length <= 0:
        passstr.set("Invalid length")
        return
    for _ in range(length):
        password += random.choice(pass1)
    passstr.set(password)

Label(root, text="Password Generator", font="calibri 18 bold").pack(pady=10)
Label(root, text="Enter the length of Password").pack(pady=5)
Entry(root, textvariable=pwd_len).pack(pady=5)
Button(root, text='Generate Password', command=get_pass).pack(pady=15)
Entry(root, textvariable=passstr, state='readonly').pack(pady=5)

root.mainloop()
