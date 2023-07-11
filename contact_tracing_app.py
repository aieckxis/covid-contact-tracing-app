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
            writer.writerow("name", "phone", "date")
            print("Entry added successfully.")

    # Read entries from CSV file and search for a matching name
    def search_entry(self):
        with open("contact_tracing.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:

                # Check if the name matches and print whether the entry is found or not
                if row[0] == name:
                    print("Entry found:")
                    print(f"Name: {row[0]}")
                    print(f"Phone Number: {row[1]}")
                    print(f"Date of Visit: {row[2]}")

        print("Entry not found")