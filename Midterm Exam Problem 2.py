import tkinter as tk

def show_full_name():
    full_name = f"{first_name_entry.get()} {middle_name_entry.get()} {last_name_entry.get()}"
    full_name_entry.delete(0, tk.END)
    full_name_entry.insert(0, full_name)

root = tk.Tk()
root.title("Midterm Exam Problem 2")
root.geometry("600x420")  # Set the size of the window


font = ("Arial", 15)
tk.Label(root, text="My Full Name",fg="red", font=font).grid(row=1, column=2,padx=10, pady=5)

font = ("Arial", 10)


tk.Label(root, text="Enter Given Name:",fg="red", font=font).grid(row=2, column=1,padx=10, pady=5)
tk.Label(root, text="Enter Middle Name:", fg="red", font=font).grid(row=3, column=1,padx=10, pady=5)
tk.Label(root, text="Enter Last Name:",fg="red", font=font).grid(row=4, column=1,padx=10, pady=5)
tk.Label(root, text="My Full Name is:",fg="red", font=font).grid(row=5, column=1,padx=10, pady=5)




first_name_entry = tk.Entry(root, font=font)
middle_name_entry = tk.Entry(root, font=font)
last_name_entry = tk.Entry(root, font=font)
full_name_entry = tk.Entry(root, font=font,fg="red")


first_name_entry.grid(row=2, column=4)
middle_name_entry.grid(row=3, column=4)
last_name_entry.grid(row=4, column=4)
full_name_entry.grid(row=5, column=4)


tk.Button(root, text="Show Full Name", font=font, command=show_full_name).grid(row=6, column=2, columnspan=2,padx=10, pady=5 )
tk.Button(root, text="Clear All",height=1, width=12, font=font, command= quit).grid(row=7, column=2, columnspan=1,padx=20, pady=5)
root.mainloop()