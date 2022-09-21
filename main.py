from tkinter import *


def Press_of_Button(value):
    global equation
    equation = equation + str(value)
    Screen_Text.set(equation)


def equal():
    global equation
    total = str(eval(equation))
    Screen_Text.set(total)


def clear():
    global equation
    equation = ""
    Screen_Text.set(equation)


# Create GUI
Calculator_GUI = Tk()
Calculator_GUI.title("Calculator")
Calculator_GUI.geometry("400x600")
Calculator_GUI.configure(bg='black')

# Screen Text
equation = ""
Screen_Text = StringVar()

# Create Screen
label = Label(Calculator_GUI, textvariable=Screen_Text, font=('Times New Roman', 48), bg="white", width=200, height=3)
label.pack()

# Create Buttons
Button_frame = Frame(Calculator_GUI)
Button_frame.pack()

# Top Row Buttons
Clear_Button = Button(Button_frame, text="Clear", height=4, width=10, font=35, command=clear)
Clear_Button.grid(row=0, column=2)

Mult_Button = Button(Button_frame, text="X", height=4, width=10, font=35, command=lambda: Press_of_Button('*'))
Mult_Button.grid(row=0, column=3)

# Second Row Buttons
Seven_Button = Button(Button_frame, text="7", height=4, width=10, font=35, command=lambda: Press_of_Button(7))
Seven_Button.grid(row=1, column=0)

Eight_Button = Button(Button_frame, text="8", height=4, width=10, font=35, command=lambda: Press_of_Button(8))
Eight_Button.grid(row=1, column=1)

Nine_Button = Button(Button_frame, text="9", height=4, width=10, font=35, command=lambda: Press_of_Button(9))
Nine_Button.grid(row=1, column=2)

Div_Button = Button(Button_frame, text="/", height=4, width=10, font=35, command=lambda: Press_of_Button('/'))
Div_Button.grid(row=1, column=3)

# Third Row Buttons
Four_Button = Button(Button_frame, text="4", height=4, width=10, font=35, command=lambda: Press_of_Button(4))
Four_Button.grid(row=2, column=0)

Five_Button = Button(Button_frame, text="5", height=4, width=10, font=35, command=lambda: Press_of_Button(5))
Five_Button.grid(row=2, column=1)

Six_Button = Button(Button_frame, text="6", height=4, width=10, font=35, command=lambda: Press_of_Button(6))
Six_Button.grid(row=2, column=2)

Sub_Button = Button(Button_frame, text="-", height=4, width=10, font=35, command=lambda: Press_of_Button('-'))
Sub_Button.grid(row=2, column=3)

# Fourth Row Buttons
One_Button = Button(Button_frame, text="1", height=4, width=10, font=35, command=lambda: Press_of_Button(1))
One_Button.grid(row=3, column=0)

Two_Button = Button(Button_frame, text="2", height=4, width=10, font=35, command=lambda: Press_of_Button(2))
Two_Button.grid(row=3, column=1)

Three_Button = Button(Button_frame, text="3", height=4, width=10, font=35, command=lambda: Press_of_Button(3))
Three_Button.grid(row=3, column=2)

Add_Button = Button(Button_frame, text="+", height=4, width=10, font=35, command=lambda: Press_of_Button('+'))
Add_Button.grid(row=3, column=3)

# Fifth Row Buttons
Zero_Button = Button(Button_frame, text="0", height=4, width=10, font=35, command=lambda: Press_of_Button(0))
Zero_Button.grid(row=4, column=1)

Dec_Button = Button(Button_frame, text=".", height=4, width=10, font=35, command=lambda: Press_of_Button('.'))
Dec_Button.grid(row=4, column=2)

Equal_Button = Button(Button_frame, text="=", height=4, width=10, font=35, command=equal)
Equal_Button.grid(row=4, column=3)

Calculator_GUI.mainloop()
