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
# Place labels and entry fields on grid
# Place buttons on grid
# Create the main window
# Create and instance of contact tracing GUI
# Run the application