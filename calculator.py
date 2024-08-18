from tkinter import *
exp = ''

def press(number):
    """Update the expression when a button is pressed."""
    global exp
    exp += str(number)
    equation.set(exp)

def equalpress():
    """Evaluate the expression and display the result."""
    global exp
    try:
        total = str(eval(exp))
        equation.set(total)
        exp = ""
    except:
        equation.set("Syntax error")
        exp = ""

def clear():
    """Clear the expression."""
    global exp
    exp = ''
    equation.set('')

tk = Tk()
tk.configure(background="yellow2")
tk.title('Basic Calculator')
tk.geometry('280x280')  
equation = StringVar()
Text_Entry_Box = Entry(tk, textvariable=equation, width=20)
Text_Entry_Box.grid(columnspan=4, ipadx=8, pady=10)

buttons = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('0', 5, 0),
    ('+', 2, 3), ('-', 3, 3), ('*', 4, 3), ('/', 5, 3),
    ('=', 5, 2), ('Clear', 5, 1)
]

for (text, row, col) in buttons:
    if text == 'Clear':
        Button(tk, text=text, fg='white', bg='brown', command=clear, height=2, width=7).grid(row=row, column=col)
    elif text == '=':
        Button(tk, text=text, fg='white', bg='brown', command=equalpress, height=2, width=7).grid(row=row, column=col)
    else:
        Button(tk, text=text, fg='white', bg='brown', command=lambda t=text: press(t), height=2, width=7).grid(row=row, column=col)

tk.mainloop()