import tkinter as tk

root = tk.Tk()
root.title("Calculator")

Ent = tk.Entry(0, width=38, borderwidth=6) 
Ent.grid(row=0, column=0, columnspan=3, padx=8, pady=8)

#Functions
def button_click(number):
    current_number = Ent.get()
    Ent.delete(0, tk.END)
    Ent.insert(0, str(current_number) + str(number))

def button_clear():
    Ent.delete(0, tk.END)

def button_addition():
    fir_number = Ent.get()
    global f_numb
    global math
    math = "addition"
    f_numb = int(fir_number)
    Ent.delete(0, tk.END)

def button_subtraction():
    fir_number = Ent.get()
    global f_numb
    global math
    math = "subtraction"
    f_numb = int(fir_number)
    Ent.delete(0, tk.END)

def button_multiple():
    fir_number = Ent.get()
    global f_numb
    global math
    math = "multiplication"
    f_numb = int(fir_number)
    Ent.delete(0, tk.END)

def button_divide():
    fir_number = Ent.get()
    global f_numb
    global math
    math = "division"
    f_numb = int(fir_number)
    Ent.delete(0, tk.END)

def button_equal():
    sec_numb = Ent.get()
    Ent.delete(0, tk.END)

    if math == "addition":
        Ent.insert(0, f_numb + int(sec_numb))

    if math == "subtraction":
        Ent.insert(0, f_numb - int(sec_numb))

    if math == "multiplication":
        Ent.insert(0, f_numb * int(sec_numb))

    if math == "division":
        Ent.insert(0, f_numb / int(sec_numb))

#Buttons 
button_1 = tk.Button(text="1", padx=35, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(text="2", padx=35, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(text="3", padx=35, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(text="4", padx=35, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(text="6", padx=35, pady=20, command=lambda: button_click(6))
button_6 = tk.Button(text="6", padx=35, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(text="7", padx=35, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(text="8", padx=35, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(text="9", padx=35, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(text="0", padx=35, pady=20, command=lambda: button_click(0))
button_add = tk.Button(text="+", padx=35, pady=20, command=button_addition)
button_subtraction = tk.Button(text="-", padx=35, pady=20, command=button_subtraction)
button_multiple = tk.Button(text="*", padx=37, pady=20, command=button_multiple)
button_divide = tk.Button(text="/", padx=35, pady=20, command=button_divide)
button_equal = tk.Button(text="=", padx=75, pady=20, command=button_equal)
button_clear = tk.Button(text="Clear", padx=67, pady=20, command=button_clear)

#Label
part_label = tk.Label(root, text="")

#Showing Buttons
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
button_clear.grid(row=4, column=1, columnspan=2)

part_label.grid(row=5)

button_add.grid(row=6, column=0)
button_subtraction.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_multiple.grid(row=7, column=0)
button_equal.grid(row=7, column=1, columnspan=2)

tk.mainloop()