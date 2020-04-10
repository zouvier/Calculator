# todo: [SOLVED] Create an interface for calculator
#   ~used tkinter

# todo: [SOLVED] Work on multiplication function(figure out how to implement the function)
#   ~ created an if/elif statement that takes in a global variable that is altered depending on the function
#   ~ this allows me to keep track of which function. i.e (using button_mult func sets the attribute variable to 1
#   ~ using button_sub sets the variable to 2) the attribute value is then used in the equal func (see below)

# todo: subtraction function: issue with the final output displaying a negative sign in front of the answer

# todo: [SOLVED] figure out why my global variables are not passing through to all functions.
#  ~ the global variable needs to be called each time it is brought up in a function


from tkinter import *
root = Tk()
root.title("Calculator")

attribute = 0
holder2 = 0
# creates the entry box and prepares a grid to where the numbers will be placed
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# Buttons of the calculator


# Allows for numbers to be placed into the entry box
def button_digit(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# clear function that clears the entry box
def button_clearing():
    e.delete(0, END)


def button_div():
    global attribute
    attribute = 3
    global holder2
    holder1 = int(e.get())
    holder2 = holder1
    e.delete(0, END)


# subtraction function
def button_sub():
    global attribute
    attribute = 2
    global holder2
    holder1 = int(e.get())
    holder2 = holder1
    e.delete(0, END)


# addition function
def button_add():
    global attribute
    attribute = 0
    global holder2
    holder1 = int(e.get())
    holder2 = holder1
    e.delete(0, END)


#  multiplication function
def button_mult():
    global attribute
    attribute = 1
    global holder2
    holder1 = int(e.get())
    holder2 = holder1
    e.delete(0, END)


# the equal button.
def button_e():
    if attribute == 0:
        holder3 = int(e.get())
        holder4 = int(holder3)
        holder5 = holder4 + holder2
        e.delete(0, END)
        e.insert(0, holder5)
    elif attribute == 1:
        holder3 = int(e.get())
        holder4 = int(holder3)
        holder5 = holder4 * holder2
        e.delete(0, END)
        e.insert(0, holder5)
    elif attribute == 2:
        holder3 = int(e.get())
        holder4 = int(holder3)
        holder5 = holder4 - holder2
        e.delete(0, END)
        e.insert(0, holder5)
    elif attribute == 3:
        holder3 = int(e.get())
        holder4 = int(holder3)
        holder5 = holder4/holder2
        e.delete(0, END)
        e.insert(0, holder5)


# defined buttons (the numbers on the calculator)
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_digit(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_digit(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_digit(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_digit(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_digit(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_digit(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_digit(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_digit(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_digit(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_digit(0))
button_addition = Button(root, text='+', padx=40, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=140, pady=20, command=button_e)
button_clear = Button(root, text='Clear', padx=30, pady=20, command=button_clearing)
button_subbing = Button(root, text='-', padx=40, pady=20, command=button_sub)
button_multiply = Button(root, text='X', padx=40, pady=20, command=button_mult)
button_divide = Button(root, text='/', padx=40, pady=20, command=button_div)
# Button's being placed on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=5, column=0)
button_addition.grid(row=4, column=1)
button_subbing.grid(row=4, column=2)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_equal.grid(row=6, column=0, columnspan=3)


root.mainloop()