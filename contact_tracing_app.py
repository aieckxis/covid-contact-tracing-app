# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Import CSV to enable reading from and writing to CSV files
import csv

# Initialize ContactTracingApp class
class ContactTracingApp:
    def __init__(self):
        pass

    # Write collected information to a CSV file
    def add_entry(self, name, bday, gender, phone, email, address, date, result):
        with open("contact_tracing.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, bday, gender, phone, email, address, date, result])

    # Read entries from CSV file and search for a matching name
    def search_entry(self, name):
        entries = []
        with open("contact_tracing.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:

                # Check if the name matches and print whether the entry is found or not
                if row[0] == name:
                    entries.append(row)
        return entries