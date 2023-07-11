# COVID Contact Tracing App
The provided code creates a COVID contact tracing application with a visual interface using Python's Tkinter library. The code is divided into two parts: **contact_tracing_gui.py** and contact_tracing_app.py.

The **contact_tracing_gui.py** file handles the **graphical user interface (GUI)**. It creates a window with **labels, input fields, and buttons.** Users can enter their name, phone number, and date of visit. Clicking the **"Add Entry"** button saves the entered data to a file called **contact_tracing.csv.** Clicking the **"Search Entry"** button searches for matching entries in the file and displays them on the screen.

The **contact_tracing_functionality.py** file contains the code responsible for the app's functionality. It defines a class called **ContactTracingApp**, which has methods for adding and searching entries. The **add_entry** method takes the name, phone number, and date of visit as input and saves them to the CSV file. The **search_entry** method takes a name as input, looks for matching entries in the file, and returns the results.

To run the application, execute the **contact_tracing_gui.py** file. It will open a window where users can interact with the app by adding entries or searching for existing ones.

## Features
- User-friendly GUI for easy interaction.
- Input fields for name, phone number, and date of visit.
- **"Add Entry"** button to save information to a file.
- **"Search Entry"** button to find existing entries based on the name.
- Separation of functionality into GUI and app logic files.

## Usage
1. Run the application: **contact_tracing_gui.py**
2. The GUI window will appear.
3. Enter your details in the respective fields.
4. Click the **"Add Entry"** button to save the information to the file.
5. Click the **"Search Entry"** button to find existing entries based on the name.

## File Structure
The repository contains the following files:
- **contact_tracing_gui.py**: Implements the graphical user interface (GUI) using Tkinter.
- **contact_tracing_app.py**: Provides the app's functionality for adding and searching entries.
- **contact_tracing.csv**: Stores the contact tracing data in CSV format.

## Contributing
Contributions to the COVID Contact Tracing App are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
