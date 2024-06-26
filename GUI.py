#this code is done as a graphical user interface where the compay can interact with it to use the EventManagementApp
#this code also implemnts the pickle to handale the data
import tkinter as tk
from tkinter import messagebox
import pickle

class EventManagementApp:
    """a class to represent a EventManagementApp"""
    # the init function is added as a constructor to initialize the class EventManagementApp
    def __init__(self, root):
        #setting up the root window
        self.root = root
        self.root.title("Event Management System")

        # creating the  frame for the main interface
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        #creating the entry for entering ID number
        self.id_label = tk.Label(self.main_frame, text="Enter ID:")
        self.id_label.grid(row=0, column=0, padx=10, pady=5)

        self.id_entry = tk.Entry(self.main_frame)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self.main_frame, text="Search", command=self.search_details)
        self.search_button.grid(row=0, column=2, padx=10, pady=5)

        #adding the lable  to display details
        self.details_label = tk.Label(self.main_frame, text="")
        self.details_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        #adding the buttons for add, delete, modify, and display details
        self.add_button = tk.Button(self.main_frame, text="Add Details", command=self.open_add_window)
        self.add_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(self.main_frame, text="Delete Details", command=self.open_delete_window)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

        self.modify_button = tk.Button(self.main_frame, text="Modify Details", command=self.open_modify_window)
        self.modify_button.grid(row=2, column=2, padx=10, pady=5)

        self.display_button = tk.Button(self.main_frame, text="Display Details", command=self.open_display_window)
        self.display_button.grid(row=2, column=3, padx=10, pady=5)

    #a function to search and display details
    def search_details(self):
        id_number = self.id_entry.get()
        # adding an if condition to check if ID is provided
        if id_number == "":
            messagebox.showerror("Error", "Please enter an ID number.")
            return

        #determining the type of entity based on the ID
        entity_type = self.get_entity_type(id_number)
        if entity_type:
            #fetching and displaying details if entity type is found
            details = self.fetch_entity_details(entity_type, id_number)
            if details:
                self.display_details(entity_type, details)
            else:
                messagebox.showerror("Error", "No details found for the provided ID.")
        else:
            #showing an error if no entity type is found
            messagebox.showerror("Error", "No entity found with the provided ID.")

    #a function to determine entity type
    def get_entity_type(self, id_number):
        #the ID number of each class
        if id_number.startswith("E"):
            return "Employee"
        elif id_number.startswith("event"):
            return "Event"
        elif id_number.startswith("C"):
            return "Client"
        elif id_number.startswith("S"):
            return "Supplier"
        elif id_number.startswith("G"):
            return "Guest"
        elif id_number.startswith("V"):
            return "Venue"
        else:
            return None

    #a function to fetch entity details
    def fetch_entity_details(self, entity_type, id_number):
        #adding a laceholder function to fetch details of each entity based on the ID number
        if entity_type == "Employee":
            return self.get_employee_details(id_number)
        elif entity_type == "Event":
            return self.get_event_details(id_number)
        elif entity_type == "Client":
            return self.get_client_details(id_number)
        elif entity_type == "Supplier":
            return self.get_supplier_details(id_number)
        elif entity_type == "Guest":
            return self.get_guest_details(id_number)
        elif entity_type == "Venue":
            return self.get_venue_details(id_number)
        else:
            return None

    #adding a placeholder functions to fetch details from database or data source
    def get_employee_details(self, id_number):
        return f"Employee Details for ID {id_number}: Name - Susan Meyers, Position - Manager, Department - Sales"

    def get_event_details(self, id_number):
        return f"Event Details for ID {id_number}: Event Name - Exhibition, Date - 2024-06-15, Venue - Trade Center"

    def get_client_details(self, id_number):
        return f"Client Details for ID {id_number}: Client Name - ZU, Location - Duabi, Budget - $5000"

    def get_supplier_details(self, id_number):
        return f"Supplier Details for ID {id_number}: Supplier Name - Best Catering, Address - Jumaira, Contact - 05034354"

    def get_guest_details(self, id_number):
        return f"Guest Details for ID {id_number}: Guest Name - Roudha, Address - Alkhawaneej, Contact - roudha@gmail.com"

    def get_venue_details(self, id_number):
        return f"Venue Details for ID {id_number}: Venue Name - Auditorium, Address - ZU campus, Capacity - 500 guests"

    #a function to display details
    def display_details(self, entity_type, details):
        self.details_label.config(text=f"{entity_type} Details: {details}")

    #a placeholder functions for opening different windows
    def open_add_window(self):
        messagebox.showinfo("Add Details", "Placeholder for opening add window.")

    def open_delete_window(self):
        messagebox.showinfo("Delete Details", "Placeholder for opening delete window.")

    def open_modify_window(self):
        messagebox.showinfo("Modify Details", "Placeholder for opening modify window.")

    def open_display_window(self):
        messagebox.showinfo("Display Details", "Placeholder for opening display window.")

    #a function to save data to a file using pickle
    def save_data(self, data, filename):
        with open(filename, "wb") as file:
            pickle.dump(data, file)

    #a function to load data from a file using pickle
    def load_data(self, filename):
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
            return data
        except FileNotFoundError:
            return None

if __name__ == "__main__":
    #creating the Tkinter root window
    root = tk.Tk()
    #creating an instance of the EventManagementApp class
    app = EventManagementApp(root)
    #starting the Tkinter event loop
    root.mainloop()