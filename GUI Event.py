import tkinter as tk
from Classes import Event, Client, Guest, Venue, Caterer, CleaningCompany, DecorationsCompany, EntertainmentCompany, FurnitureSupplier

class EventManagementGUI:
    """class to represent GUI for managing event information"""
    def __init__(self, master):
        self.master=master
        self.master.title("Event Management System")
        self.master.geometry("800x600")

        #adding the labels
        self.event_label = tk.Label(self.master, text="Event Details")
        self.event_label.pack()

        #adding the entry fields for event details
        self.event_id_label = tk.Label(self.master, text="Event ID:")
        self.event_id_label.pack()
        self.event_id_entry = tk.Entry(self.master)
        self.event_id_entry.pack()

        #adding the submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_event)
        self.submit_button.pack()

    def submit_event(self):
        """Method to handle submission of event details"""
        # getting the input values from entry fields
        event_id = self.event_id_entry.get()

        #creating the  event object using input values
        event = Event(eventID=event_id)


# creating the main window and start GUI
root = tk.Tk()
app = EventManagementGUI(root)
root.mainloop()