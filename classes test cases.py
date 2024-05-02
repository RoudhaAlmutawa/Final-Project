# this code defines test cases to showcase the program features.
#importing the classes
from Classes import Employee, Manager, Salesperson, Event, Client, Guest, Venue, Supplier, Caterer, CleaningCompany, DecorationsCompany, EntertainmentCompany, FurnitureSupplier
from datetime import datetime #importing the date time


# Test case 1: creating and updating employee details
# Creating the employees
emp1 = Employee(name="Susan Meyers", employeeID=47899, department="Sales", jobTitle="Manager", basicSalary=37500.0)
emp2 = Employee(name="Joy Rogers", employeeID=81774, department="Sales", jobTitle="Manager", basicSalary=24000.0)
emp3 = Salesperson(name="Shyam Sundar", employeeID=11234, department="Sales", jobTitle="Salesperson", basicSalary=20000.0, managerID=47899)
emp4 = Salesperson(name="Mariam Khalid", employeeID=98394, department="Sales", jobTitle="Salesperson", basicSalary=20000.0, managerID=81774)
emp5 = Salesperson(name="Salma J Sam", employeeID=98637, department="Sales", jobTitle="Salesperson", basicSalary=20000.0, managerID=47899)

# Updating the employees' details
emp1.set_basicSalary(40000.0)
emp3.set_basicSalary(22000.0)

# Displaying the updated details
print("test case 1:")
print("Employee 1 Name:", emp1.get_name())
print("Employee 1 Basic Salary:", emp1.get_basicSalary())
print("Employee 3 Name:", emp3.get_name())
print("Employee 3 Basic Salary:", emp3.get_basicSalary())

#test case 2: creating and managing events:
#creating the event
event1 = Event(eventID=1, eventType="graduation", theme="fun", eventDate=datetime(2024, 5, 15),
               eventTime=datetime(2024, 5, 15, 18, 0), eventDuration=4, venueAddress="trade center", clientID=1,
               guestList = [Guest(guestID=1, guestName="aisha", guestAddress="Mirdf", guestContactDetails="aisha@gmail.com"),
             Guest(guestID=2, guestName="roudha", guestAddress="al khawaneej", guestContactDetails="roudha@gmail.com"),
             Guest(guestID=3, guestName="maitha", guestAddress="nad al sheeba",
                   guestContactDetails="maitha@gmail.com")])

#updating the event details
event1.set_theme("modern")
event1.set_eventDate(datetime(2024, 6, 20))

# displaying the  updated details
print("test case 2:")
print("Event Theme:", event1.get_theme())
print("Event Date:", event1.get_eventDate())
#displaying the guest list
print("Guest List:")
for guest in event1.get_guestList():
    print(guest)

#test case 3: Creating and managing clients:
#creating the client
client1= Client(clientID=1, clientName="Reem", clientAddress="skh. zayed road", clientContactDetails="reem@yahoo.com",
                 clientBudget=10000.0)

#updating the  client details
client1.set_clientName("Reem Enterprises")
client1.set_clientBudget(12000.0)

# displaying the  updated details
print("test case 3:")
print("Client Name:", client1.get_clientName())
print("Client Budget:", client1.get_clientBudget())

#test case 4:creating and viewning supplier services:
#creating the  catering company
caterer1 = Caterer(supplierID=1, supplierName="Best Catering", supplierAddress="Jumaira",
                   supplierContactDetails="05072323233", menu=["Appetizers", "Entrees", "Desserts"],
                   caterminOfGuests=50, catermaxOfGuests=200)
# viewing the catering menu
print("test case 4:")
print("Catering Menu:", caterer1.get_menu())

# creating the entertainment company
entertainment1 = EntertainmentCompany(supplierID=2, supplierName="Best Entertainment", supplierAddress="Business Bay",
                                      supplierContactDetails="050343545", typeOfEntertainment="Live music")
# View entertainment options
print("Entertainment Type:", entertainment1.get_typeOfEntertainment())

#test case 5: creating and managing  Employees with diffrent roles:
# creating the managers
manager1 = Manager(name="Susan Meyers", employeeID=47899, department="Sales", jobTitle="Manager", basicSalary=37500.0,
                   age=45, dateOfBirth=datetime(1979, 5, 15), passportDetails="ABCD1234", managerType="Senior")
manager2 = Manager(name="Joy Rogers", employeeID=81774, department="Sales", jobTitle="Manager", basicSalary=24000.0,
                   age=38, dateOfBirth=datetime(1986, 8, 22), passportDetails="EFGH5678", managerType="Junior")

# creating the salespeople
salesperson1 = Salesperson(name="Shyam Sundar", employeeID=11234, department="Sales", jobTitle="Salesperson",
                           basicSalary=20000.0, age=30, dateOfBirth=datetime(1994, 11, 10), passportDetails="IJKL9012",
                           managerID="47899")
salesperson2 = Salesperson(name="Mariam Khalid", employeeID=98394, department="Sales", jobTitle="Salesperson",
                           basicSalary=20000.0, age=28, dateOfBirth=datetime(1996, 2, 5), passportDetails="MNOP3456",
                           managerID="81774")
salesperson3 = Salesperson(name="Salma J Sam", employeeID=98637, department="Sales", jobTitle="Salesperson",
                           basicSalary=20000.0, age=29, dateOfBirth=datetime(1995, 7, 18), passportDetails="QRST7890",
                           managerID="47899")

# displaying the  managed employees for each manager
manager1.set_ManagedEmployees([salesperson1, salesperson3])
manager2.set_ManagedEmployees([salesperson2])
print("test case 5:")
print("Manager 1 Managed Employees:", [emp.get_name() for emp in manager1.get_ManagedEmployees()])
print("Manager 2 Managed Employees:", [emp.get_name() for emp in manager2.get_ManagedEmployees()])

# Test case 6: creatuing and managing events with carious services
# Creating an event with different services
event2 = Event(eventID=2, eventType="Annual collage reunion", theme="formal",
               eventDate=datetime(2024, 7, 30), eventTime=datetime(2024, 7, 30, 19, 0),
               eventDuration=5, venueAddress="Zu campus", clientID=2,
               guestList=[Guest(guestID=1, guestName="saif"), Guest(guestID=2, guestName="roudha")])

# Adding the catering company
event2.set_cateringCompany(Caterer(supplierID=3, supplierName="Dest Delights", supplierAddress="dubai mall",
                                   supplierContactDetails="05034545334", menu=["Appetizers", "Main Course", "Desserts"],
                                   caterminOfGuests=100, catermaxOfGuests=500))
# Adding the entertainment company
event2.set_entertainmentCompany(EntertainmentCompany(supplierID=4, supplierName="fun live activity",
                                                     supplierAddress="dubai", supplierContactDetails="05034344",
                                                     typeOfEntertainment="live music"))

# Displaying the event details
print("Test Case 6:")
print("Event Type:", event2.get_eventType())
print("Theme:", event2.get_theme())
print("Event Date:", event2.get_eventDate())
print("Event Time:", event2.get_eventTime())
print("Venue Address:", event2.get_venueAddress())
print("Catering Menu:", event2.get_cateringCompany().get_menu())
print("Entertainment Type:", event2.get_entertainmentCompany().get_typeOfEntertainment())