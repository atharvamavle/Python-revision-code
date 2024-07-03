# import tkinter as tk

# def button_click():
#     label.config(text="Hello, " + entry.get())

# # Create the main window
# root = tk.Tk()
# root.title("Basic Tkinter Example")

# # Create a label
# label = tk.Label(root, text="Enter your name:")
# label.pack()

# # Create an entry widget
# entry = tk.Entry(root)
# entry.pack()

# # Create a button
# button = tk.Button(root, text="Click Me!", command=button_click)
# button.pack()

# # Start the Tkinter event loop
# root.mainloop()

# import tkinter as tk
# from math import pi

# def calculate_area():
#     try:
#         # Get the radius from the entry widget
#         radius = float(entry.get())
        
#         # Calculate the area of the circle
#         area = pi * radius**2
        
#         # Update the label with the result
#         result_label.config(text=f"Area of the circle: {area:.2f}")
#     except ValueError:
#         # Handle the case where the input is not a valid number
#         result_label.config(text="Please enter a valid number for the radius.")

# # Create the main window
# root = tk.Tk()
# root.title("Circle Area Calculator")

# # Create a label and an entry widget for the radius
# radius_label = tk.Label(root, text="Enter the radius:")
# radius_label.pack()

# entry = tk.Entry(root)
# entry.pack()

# # Create a button to trigger the calculation
# calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
# calculate_button.pack()

# # Create a label to display the result
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Start the Tkinter event loop
# root.mainloop()


# import tkinter as tk

# def add_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 + num2
#         result_label.config(text=f"Result: {num1} + {num2} = {result}")
#     except ValueError:
#         result_label.config(text="Please enter valid numbers")

# # Create the main window
# root = tk.Tk()
# root.title("Number Adder")

# # Create entry widgets for user input
# entry1 = tk.Entry(root, width=10)
# entry2 = tk.Entry(root, width=10)

# # Create a button to trigger the calculation
# calculate_button = tk.Button(root, text="Add Numbers", command=add_numbers)

# # Create a label to display the result
# result_label = tk.Label(root, text="Result: ")

# # Place widgets using the grid layout manager
# entry1.grid(row=0, column=0, padx=5, pady=5)
# entry2.grid(row=0, column=1, padx=5, pady=5)
# calculate_button.grid(row=1, column=0, columnspan=2, pady=5)
# result_label.grid(row=2, column=0, columnspan=2, pady=5)

# # Start the Tkinter event loop
# root.mainloop()

# create a calculator using tkinenter

# import tkinter as tk

# def calculator():
#     num1=int("Enter your first number: ",entry1.get())
#     num2=int("Enter your Second number: ",entry2.get())

#     cl


# import tkinter as tk

# def on_click(button_value):
#     current = entry_var.get()
#     if button_value == '=':
#         try:
#             result = eval(current)
#             entry_var.set(result)
#         except Exception as e:
#             entry_var.set("Error")
#     elif button_value == 'C':
#         entry_var.set('')
#     else:
#         entry_var.set(current + button_value)

# # Create the main window
# root = tk.Tk()
# root.title("Simple Calculator")

# # Entry widget to display the current expression or result
# entry_var = tk.StringVar()
# entry = tk.Entry(root, textvariable=entry_var, justify='right', font=('Arial', 14))
# entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

# # Button layout
# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+',
#     'C'
# ]

# # Create and place buttons
# row_val = 1
# col_val = 0
# for button in buttons:
#     tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12),
#               command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# # Configure row and column weights so that they expand proportionally
# for i in range(5):
#     root.grid_rowconfigure(i, weight=1)
#     root.grid_columnconfigure(i, weight=1)

# # Start the Tkinter event loop
# root.mainloop()




        