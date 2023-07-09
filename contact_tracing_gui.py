# Import tkinter module and assign it as tk, and import ContactTracingApp from contact_tracing_app
import tkinter as tk
from contact_tracing_app import ContactTracingApp

# Create and instance of ContactTracingApp
class ContactTracingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        self.contact_tracing_app = ContactTracingAppGUI()

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

# Create the main window
root = tk.Tk()

# Create and instance of contact tracing GUI
app = ContactTracingAppGUI(root)

# Run the application
root.mainloop()