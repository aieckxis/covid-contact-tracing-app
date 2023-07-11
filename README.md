# COVID Contact Tracing App
The provided code creates a COVID contact tracing application with a visual interface using Python's Tkinter library. The code is divided into two parts: **contact_tracing_gui.py** and contact_tracing_app.py.

The **contact_tracing_gui.py** file handles the **graphical user interface (GUI)**. It creates a window with **labels, input fields, and buttons.** Users can enter their name, phone number, and date of visit. Clicking the **"Add Entry"** button saves the entered data to a file called **contact_tracing.csv.** Clicking the **"Search Entry"** button searches for matching entries in the file and displays them on the screen.

The **contact_tracing_functionality.py** file contains the code responsible for the app's functionality. It defines a class called **ContactTracingApp**, which has methods for adding and searching entries. The **add_entry** method takes the name, phone number, and date of visit as input and saves them to the CSV file. The **search_entry** method takes a name as input, looks for matching entries in the file, and returns the results.

To run the application, execute the **contact_tracing_gui.py** file. It will open a window where users can interact with the app by adding entries or searching for existing ones.
