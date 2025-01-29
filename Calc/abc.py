import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Stylish Calculator")
window.configure(bg='#2c3e50')

# Create the display
display = tk.Entry(window, width=20, font=("Arial", 24), justify='right', bd=0, relief="flat", fg="#ecf0f1", bg="#34495e")
display.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky='ew')

# Button styling with black text
button_style = ttk.Style()
button_style.configure('Calculator.TButton', font=("Arial", 18, "bold"), width=5, height=2, borderwidth=0, 
                       relief="flat", background="#16a085", foreground="#000000", padding=10)
button_style.map('Calculator.TButton', background=[('active', '#1abc9c')])

# Create the buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Add the buttons to the grid
for button_text, row, column in buttons:
    button = ttk.Button(window, text=button_text, style='Calculator.TButton', 
                        command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column, pady=10, padx=10)

# Clear button styling
clear_button = ttk.Button(window, text="C", style='Calculator.TButton', 
                          command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

# Equal button styling
equal_button = ttk.Button(window, text="=", style='Calculator.TButton', 
                          command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2, pady=10, padx=10)

# Configure grid weights to make the display expandable
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(0, weight=1)

# Start the main event loop
window.mainloop()
