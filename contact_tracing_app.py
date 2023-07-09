# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Import CSV to enable reading from and writing to CSV files
import csv

# Initialize ContactTracingApp class
class ContactTracingApp:
    def __init__(self):
        pass

    # Write collected information to a CSV file
    def add_entry(self):
        with open("contact_tracing.csv", "a", newline="") as file:
            writer = csv.writer(file)

            # Write the entry to the CSV file and print added successfully
            writer.writerow(name, phone, date)
            print("Entry added successfully.")
# Read entries from CSV file and search for a matching name
# Check if the name matches
# Print whether the entry is found or not