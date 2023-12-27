import tkinter as tk
from tkinter import messagebox

def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
app = tk.Tk()
app.title("Multiply Calculator")
app.configure(bg="#13EAC9")  # Set background color

# Define a custom font with a larger size
custom_font = ("Arial", 16, "bold")

# Create and place widgets with reduced spacing
label_num1 = tk.Label(app, text="Enter the first number:", bg="#13EAC9", font=custom_font)
label_num1.pack(pady=0)

entry_num1 = tk.Entry(app, font=custom_font)
entry_num1.pack(pady=0)

label_num2 = tk.Label(app, text="Enter the second number:", bg="#13EAC9", font=custom_font)
label_num2.pack(pady=0)

entry_num2 = tk.Entry(app, font=custom_font)
entry_num2.pack(pady=0)

multiply_button = tk.Button(app, text="Multiply", command=multiply, bg="#13EAC9", font=custom_font)
multiply_button.pack(pady=0)

result_label = tk.Label(app, text="Result: ", bg="#13EAC9", font=custom_font)
result_label.pack(pady=0)

# Start the GUI application
app.mainloop()
