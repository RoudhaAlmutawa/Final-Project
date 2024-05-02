import tkinter as tk
from tkinter import messagebox

class EventManagementApp:
    """a class to represent event managment app"""
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")

        # Create a frame for the main interface
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        # Entry for entering ID number
        self.id_label = tk.Label(self.main_frame, text="Enter ID:")
        self.id_label.grid(row=0, column=0, padx=10, pady=5)

        self.id_entry = tk.Entry(self.main_frame)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self.main_frame, text="Search", command=self.search_details)
        self.search_button.grid(row=0, column=2, padx=10, pady=5)

        # Label to display details
        self.details_label = tk.Label(self.main_frame, text="")
        self.details_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

    def search_details(self):
        id_number = self.id_entry.get()
        if id_number == "":
            messagebox.showerror("Error", "Please enter an ID number.")
            return

        entity_type = self.get_entity_type(id_number)
        if entity_type:
            details = self.fetch_entity_details(entity_type, id_number)
            if details:
                self.display_details(details)
            else:
                messagebox.showerror("Error", "No details found for the provided ID.")
        else:
            messagebox.showerror("Error", "No entity found with the provided ID.")

    def get_entity_type(self, id_number):
        # Simplified logic to determine the entity type based on the ID number
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

    def fetch_entity_details(self, entity_type, id_number):
        # Placeholder function to fetch details of each entity based on the ID number
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

    # Placeholder functions to fetch details from database or data source
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

    def display_details(self, details):
        self.details_label.config(text=details)

if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementApp(root)
    root.mainloop()