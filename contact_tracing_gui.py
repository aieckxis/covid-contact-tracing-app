# Import tkinter module and assign it as tk, and import ContactTracingApp from contact_tracing_app
import tkinter as tk
from contact_tracing_app import ContactTracingApp

# Create and instance of ContactTracingApp
class ContactTracingAppGUI:
    def __init__(self, root):
        self.root = root

        # Create labels and entry fields
        self.name_label = tk.Label(root, text="Name: ")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone Number: ")
        self.phone_entry = tk.Entry(root)

        self.date_label = tk.Label(root, text="Date of Visit: ")
        self.date_entry = tk.Entry(root)

        # Create buttons
        self.add_button = tk.Button(root, text="Add Entry")
        self.search_button = tk.Button(root, text="Search Entry")

        # Place labels and entry fields on grid
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry.grid(row=0, column=1, pady=10, padx=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry.grid(row=1, column=1, pady=10, padx=5)

        self.date_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.date_entry.grid(row=2, column=1, pady=10, padx=5)

        # Place buttons on grid
        self.add_button.grid(row=3, column=0, padx=10, pady=5)
        self.search_button.grid(row=3, column=1, padx=10, pady=5)

        # Create an instance of the contact tracing app
        self.contact_tracing = ContactTracingApp()

    def add_entry(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        date = self.date_entry.get()

        # Call the add_entry method from the ContactTracingApp
        self.contact_tracing.add_entry(name, phone, date)

        self.clear_entries()
        print("Entry added successfully.")

    def search_entry(self):
        name = self.name_entry.get()

        # Call the search_entry method from the ContactTracingApp class
        entry = self.contact_tracing.search_entry(name)

        if entry:
            print("Entry found:")
            print(f"Name: {entry[0]}")
            print(f"Phone Number: {entry[1]}")
            print(f"Date of Visit: {entry[2]}")
        else:
            print("Entry not found")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Create and instance of contact tracing GUI
app = ContactTracingAppGUI(root)

# Run the application
root.mainloop()