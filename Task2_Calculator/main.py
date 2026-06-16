import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

root = tk.Tk()
root.title("Jashanpreet's Smart Calculator")
root.geometry("450x400")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🧮 Jashanpreet's Smart Calculator",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

tk.Label(root, text="Enter First Number", font=("Arial", 11)).pack()
entry1 = tk.Entry(root, font=("Arial", 12), justify="center")
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number", font=("Arial", 11)).pack()
entry2 = tk.Entry(root, font=("Arial", 12), justify="center")
entry2.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="+", width=8,
          command=lambda: calculate("+")).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="-", width=8,
          command=lambda: calculate("-")).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="×", width=8,
          command=lambda: calculate("*")).grid(row=0, column=2, padx=5)

tk.Button(button_frame, text="÷", width=8,
          command=lambda: calculate("/")).grid(row=0, column=3, padx=5)

tk.Button(
    root,
    text="Clear",
    width=15,
    command=clear_fields
).pack(pady=10)

result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 15, "bold")
)
result_label.pack(pady=20)

footer = tk.Label(
    root,
    text="Developed by Jashanpreet",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()
