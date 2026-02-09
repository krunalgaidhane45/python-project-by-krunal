import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("Tkinter Calculator App")
root.geometry("400x300")

def show_message():
    messagebox.showinfo("Welcome", "Let's perform a calculation!")
    num1 = simpledialog.askfloat("Input", "Enter the first number:")
    if num1 is None:
        return
    num2 = simpledialog.askfloat("Input", "Enter the second number:")
    if num2 is None:
        return
    operation = simpledialog.askstring(
        "Operation",
        "Choose operation:\n+ for Add\n- for Subtract\n* for Multiply\n/ for Divide"
    )
    if operation is None:
        return
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return
        messagebox.showinfo("Result", f"The result of {num1} {operation} {num2} is {result}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

label = tk.Label(root, text="My Calculator App!", font=("Arial", 18))
label.pack(pady=20)
button = tk.Button(root, text="Click Me!", command=show_message)
button.pack(pady=10)
root.mainloop()
