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

        self.bday_label = tk.Label(root, text="Date of Birth: ")
        self.bday_entry = tk.Entry(root)

        self.gender_label = tk.Label(root, text="Gender: ")
        self.gender_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone Number: ")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email Address: ")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address: ")
        self.address_entry = tk.Entry(root)

        self.date_label = tk.Label(root, text="Date of Test: ")
        self.date_entry = tk.Entry(root)

        self.result_label = tk.Label(root, text="Result: ")
        self.result_entry = tk.Entry(root)

        # Create buttons
        self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
        self.search_button = tk.Button(root, text="Search Entry", command=self.search_entry)

        # Place labels and entry fields on grid
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry.grid(row=0, column=1, pady=10, padx=5)

        self.bday_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.bday_entry.grid(row=1, column=1, pady=10, padx=5)

        self.gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.gender_entry.grid(row=2, column=1, pady=10, padx=5)

        self.phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry.grid(row=3, column=1, pady=10, padx=5)

        self.email_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry.grid(row=4, column=1, pady=10, padx=5)

        self.address_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.address_entry.grid(row=5, column=1, pady=10, padx=5)

        self.date_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        self.date_entry.grid(row=6, column=1, pady=10, padx=5)

        self.result_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        self.result_entry.grid(row=7, column=1, pady=10, padx=5)

        # Place buttons on grid
        self.add_button.grid(row=8, column=0, padx=10, pady=5)
        self.search_button.grid(row=8, column=1, padx=10, pady=5)

        # Create an instance of the contact tracing app
        self.contact_tracing = ContactTracingApp()

    def add_entry(self):
        name = self.name_entry.get()
        bday = self.bday_entry.get()
        gender = self.gender_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        date = self.date_entry.get()
        result = self.result_entry.get()

        # Call the add_entry method from the ContactTracingApp
        self.contact_tracing.add_entry(name, bday, gender, phone, email, address, date, result)

        self.clear_entries()
        print("Entry added successfully.")

    def search_entry(self):
        name = self.name_entry.get()

        # Call the search_entry method from the ContactTracingApp class
        entry = self.contact_tracing.search_entry(name)

        if entry:
            print("Entry found:")
            for item in entry:
                print(item)
        else:
            print("Entry not found")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.bday_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()

    # Create and instance of contact tracing GUI
    app = ContactTracingAppGUI(root)

    # Run the application
    root.mainloop()