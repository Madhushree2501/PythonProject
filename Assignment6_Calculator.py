#Calculator program using Tkinter
import tkinter as tk
from tkinter import messagebox

# Functions used for performing different actions
expression = ""

def click(value):
    global expression
    expression += str(value)
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set("")

def calculate():
    global expression
    try:
        if expression.strip() == "":
            raise ValueError("Please enter an expression.")

        result = eval(expression)

        entry_var.set(result)
        expression = str(result)

    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        clear()

    except SyntaxError:
        messagebox.showerror("Error", "Invalid mathematical expression.")
        clear()

    except NameError:
        messagebox.showerror("Error", "Only numbers and operators are allowed.")
        clear()

    except TypeError:
        messagebox.showerror("Error", "Invalid operation.")
        clear()

    except ValueError as e:
        messagebox.showerror("Error", str(e))
        clear()

    except OverflowError:
        messagebox.showerror("Error", "Number is too large.")
        clear()

    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))
        clear()


# Creating the main window of our application
root = tk.Tk()
root.title("Calculator")
root.geometry("340x450")
root.resizable(False, False)

#Create the StringVar and link it to the entry widget
entry_var = tk.StringVar()

entry = tk.Entry(root,
                 textvariable=entry_var,
                 font=("Arial", 22),
                 bd=8,
                 relief="sunken",
                 justify="right")
entry.place(x=10, y=10, width=320, height=50)

# Defining the buttons and place them dynamically

buttons = [
    ('7', 10, 80), ('8', 90, 80), ('9', 170, 80), ('/', 250, 80),
    ('4', 10, 140), ('5', 90, 140), ('6', 170, 140), ('*', 250, 140),
    ('1', 10, 200), ('2', 90, 200), ('3', 170, 200), ('-', 250, 200),
    ('0', 10, 260), ('.', 90, 260), ('=', 170, 260), ('+', 250, 260)
]

for (text, x, y) in buttons:
    if text == '=':
        tk.Button(root,
                  text=text,
                  font=("Arial", 16),
                  command=calculate).place(x=x, y=y, width=70, height=50)
    else:
        tk.Button(root,
                  text=text,
                  font=("Arial", 16),
                  command=lambda t=text: click(t)).place(x=x, y=y, width=70, height=50)

# Clear Button
tk.Button(root,
          text="C",
          font=("Arial", 16),
          bg="red",
          fg="white",
          command=clear).place(x=10, y=330, width=310, height=50)

#Start the event loop
root.mainloop()