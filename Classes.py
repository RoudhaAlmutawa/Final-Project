#the code below shows a software system to manage the organizes events of the company
from datetime import datetime

class Employee:
    """a class to represent employee"""
    def __init__(self, name="", employeeID=0, department="", jobTitle="", basicSalary=0.0, age=0, dateOfBirth= datetime, passportDetails=""):
        self.name= name
        self.employeeID= employeeID
        self.department= department
        self.jobTitle= jobTitle
        self.basicSalary= basicSalary
        self.age= age
        self.dateOfBirth = dateOfBirth
        self.passportDetails = passportDetails

#method to update emplyee details
    def updateDetails(self):
        pass


#adding the setter and getter functions for the class Employee
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name= name

    def get_employeeID(self):
        return self.employeeID
    def set_employeeID(self, employeeID):
        self.employeeID = employeeID

    def get_department(self):
        return self.department
    def set_department(self, department):
        self.department = department

    def get_jobTitle(self):
        return self.jobTitle
    def set_jobTitle(self, jobTitle):
        self.jobTitle = jobTitle

    def get_basicSalary(self):
        return self.basicSalary
    def set_basicSalary(self, basicSalary):
        self.basicSalary = basicSalary

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

    def get_dateOfBirth(self):
        return self.dateOfBirth
    def set_dateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth

    def get_passportDetails(self):
        return self.passportDetails
    def set_passportDetails(self, passportDetails):
        self.passportDetails = passportDetails

class Manager(Employee):
    """a class to represent manager"""
    def __init__(self, name="", employeeID=0, department="", jobTitle="", basicSalary=0.0, age=0, dateOfBirth= datetime, passportDetails="", managerType ="", ):
        super().__init__()      # Calling the superclass constructor
        self.managerType= managerType
        self.managedEmployees=[]

#method to know the mannaged employees
    def getManagedEmployees(self):
        pass

#adding the setter and getter functions for the class Manager
    def get_ManagerType(self):
        return self.managerType
    def set_ManagerType(self, managerType):
        self.managerType = managerType

    def get_ManagedEmployees(self):
        return self.managedEmployees
    def set_ManagedEmployees(self, managedEmployees):
        self.managedEmployees = managedEmployees

class Salesperson(Employee):
    """a class to represent sales person"""
    def __init__(self, name="", employeeID=0, department="", jobTitle="", basicSalary=0.0, age=0, dateOfBirth= datetime, passportDetails="", managerID=""):
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails)        # Calling the superclass constructor
        self.managerID= managerID

#adding the setter and getter functions for the class Salesperson
    def getManagerID(self):
        return self.managerID
    def setManagerID(self, managerID):
        self.managerID = managerID


class Event:
    """a class to represent event"""
    def __init__(self, eventID=0, eventType="", theme= "", eventDate=datetime, eventTime= datetime, eventDuration= 0, venueAddress= "", clientID=0, guestList= [], cleaningCompany=None, cateringCompany= None, decorationsCompany=None, entertainmentCompany=None, furnitureSupplyCompany=None):
        self.eventID= eventID
        self.eventType= eventType
        self.theme= theme
        self.eventDate= eventDate
        self.eventTime= eventTime
        self.eventDuration= eventDuration
        self.venueAddress= venueAddress
        self.clientID= clientID
        self.guestList= guestList
        self.cateringCompany= cateringCompany
        self.cleaningCompany= cleaningCompany
        self.decorationsCompany= decorationsCompany
        self.entertainmentCompany= entertainmentCompany
        self.furnitureSupplyCompany= furnitureSupplyCompany

#method to calculate the total cost
    def calculateTotalCost(self):
        pass

#adding the setter and getter functions for the class Event
    def get_eventID(self):
        return self.eventID
    def set_eventID(self, eventID):
        self.eventID = eventID

    def get_eventType(self):
        return self.eventType
    def set_eventType(self, eventType):
        self.eventType = eventType

    def get_theme(self):
        return self.theme
    def set_theme(self, theme):
        self.theme = theme

    def get_eventDate(self):
        return self.eventDate
    def set_eventDate(self, eventDate):
        self.eventDate = eventDate

    def get_eventTime(self):
        return self.eventTime
    def set_eventTime(self, eventTime):
        self.eventTime = eventTime

    def get_eventDuration(self):
        return self.eventDuration
    def set_eventDuration(self, eventDuration):
        self.eventDuration = eventDuration

    def get_venueAddress(self):
        return self.venueAddress
    def set_venueAddress(self, venueAddress):
        self.venueAddress = venueAddress

    def get_clientID(self):
        return self.clientID
    def set_clientID(self, clientID):
        self.clientID = clientID

    def get_guestList(self):
        return self.guestList
    def set_guestList(self, guestList):
        self.guestList = guestList

    def get_cateringCompany(self):
        return self.cateringCompany
    def set_cateringCompany(self, cateringCompany):
        self.cateringCompany = cateringCompany

    def get_cleaningCompany(self):
        return self.cleaningCompany
    def set_cleaningCompany(self, cleaningCompany):
        self.cleaningCompany = cleaningCompany

    def get_decorationsCompany(self):
        return self.decorationsCompany
    def set_decorationsCompany(self, decorationsCompany):
        self.decorationsCompany = decorationsCompany

    def get_entertainmentCompany(self):
        return self.entertainmentCompany
    def set_entertainmentCompany(self, entertainmentCompany):
        self.entertainmentCompany = entertainmentCompany

    def get_furnitureSupplyCompany(self):
        return self.furnitureSupplyCompany
    def set_furnitureSupplyCompany(self, furnitureSupplyCompany):
        self.furnitureSupplyCompany = furnitureSupplyCompany

class Client:
    """a class to represent clinet"""
    def __init__(self, clientID=0, clientName= "", clientAddress= "", clientContactDetails="", clientBudget=0.0 ):
        self.clientID= clientID
        self.clientName= clientName
        self.clientAddress= clientAddress
        self.clientContactDetails= clientContactDetails
        self.clientBudget= clientBudget

#method to update budget
    def updateBudget(self):
        pass

#adding the setter and getter functions for the class Client
    def get_clientID(self):
        return self.clientID
    def set_clientID(self, clientID):
        self.clientID = clientID

    def get_clientName(self):
        return self.clientName
    def set_clientName(self, clientName):
        self.clientName = clientName

    def get_clientAddress(self):
        return self.clientAddress
    def set_clientAddress(self, clientAddress):
        self.clientAddress = clientAddress

    def get_clientContactDetails(self):
        return self.clientContactDetails
    def set_clientContactDetails(self, clientContactDetails):
        self.clientContactDetails = clientContactDetails

    def get_clientBudget(self):
        return self.clientBudget
    def set_clientBudget(self, clientBudget):
        self.clientBudget = clientBudget

class Guest:
    """a class to represent a Guest"""
    def __init__(self, guestID=0, guestName="", guestAddress="", guestContactDetails=""):
        self.guestID= guestID
        self.guestName= guestName
        self.guestAddress= guestAddress
        self.guestContactDetails= guestContactDetails

        # adding __str__ method to display guest details
    def __str__(self):
        return f"Guest ID: {self.guestID}, Name: {self.guestName}, Address: {self.guestAddress}, Contact Details: {self.guestContactDetails}"

#adding the setter and getter functions for the class Guest
    def get_guestID(self):
        return self.guestID
    def set_guestID(self, guestID):
        self.guestID = guestID

    def get_guestName(self):
        return self.guestName
    def set_guestName(self, guestName):
        self.guestName = guestName

    def get_guestAddress(self):
        return self.guestAddress
    def set_guestAddress(self, guestAddress):
        self.guestAddress = guestAddress

    def get_guestContactDetails(self):
        return self.guestContactDetails
    def set_guestContactDetails(self, guestContactDetails):
        self.guestContactDetails = guestContactDetails

class Venue:
    """a class to represent Venue"""
    def __init__(self, venueID=0, venueName="", venueAddress="", venueContact="", venMinOfGuests=0, venMaxOfGuests=0):
        self.venueID= venueID
        self.venueName= venueName
        self.venueAddress= venueAddress
        self.venueContact= venueContact
        self.venMinOfGuests= venMinOfGuests
        self. venMaxOfGuests= venMaxOfGuests

#method to check availability
    def checkAvailability(self):
        pass

#adding the setter and getter functions for the class Venue
    def get_venueID(self):
        return self.venueID
    def set_venueID(self, venueID):
        self.venueID = venueID

    def get_venueName(self):
        return self.venueName
    def set_venueName(self, venueName):
        self.venueName = venueName

    def get_venueAddress(self):
        return self.venueAddress
    def set_venueAddress(self, venueAddress):
        self.venueAddress = venueAddress

    def get_venueContact(self):
        return self.venueContact
    def set_venueContact(self, venueContact):
        self.venueContact = venueContact

    def get_venMinOfGuests(self):
        return self.venMinOfGuests
    def set_venMinOfGuests(self, venMinOfGuests):
        self.venMinOfGuests = venMinOfGuests

    def get_venMaxOfGuests(self):
        return self.venMaxOfGuests
    def set_venMaxOfGuests(self, venMaxOfGuests):
        self.venMaxOfGuests = venMaxOfGuests

class Supplier:
    """a class to represent Supplier"""
    def __init__(self, supplierID=0, supplierName="", supplierAddress="", supplierContactDetails=""):
        self.supplierID= supplierID
        self.supplierName= supplierName
        self.supplierAddress= supplierAddress
        self.supplierContactDetails= supplierContactDetails

#method to view services
    def viewServices(self):
        pass

#adding the setter and getter functions for the class Supplier
    def get_supplierID(self):
        return self.supplierID
    def set_supplierID(self, supplierID):
        self.supplierID = supplierID

    def get_supplierName(self):
        return self.supplierName
    def set_supplierName(self, supplierName):
        self.supplierName = supplierName

    def get_supplierAddress(self):
        return self.supplierAddress
    def set_supplierAddress(self, supplierAddress):
        self.supplierAddress = supplierAddress

    def get_supplierContactDetails(self):
        return self.supplierContactDetails
    def set_supplierContactDetails(self, supplierContactDetails):
        self.supplierContactDetails = supplierContactDetails


class Caterer(Supplier):
    """a class to represent Caterer"""
    def __init__(self, supplierID, supplierName, supplierAddress, supplierContactDetails, menu="", caterminOfGuests=0,
                 catermaxOfGuests=0):
        super().__init__()
        self.menu = menu
        self.caterminOfGuests = caterminOfGuests
        self.catermaxOfGuests = catermaxOfGuests

# method to view the menu
    def viewMenu(self):
        pass

    # adding the setter and getter functions for the class Caterer
    def get_menu(self):
        return self.menu
    def set_menu(self, menu):
        self.menu = menu

    def get_caterminOfGuests(self):
        return self.caterminOfGuests
    def set_caterminOfGuests(self, caterminOfGuests):
        self.caterminOfGuests = caterminOfGuests

    def get_catermaxOfGuests(self):
        return self.catermaxOfGuests
    def set_catermaxOfGuests(self, catermaxOfGuests):
        self.catermaxOfGuests = catermaxOfGuests


class CleaningCompany(Supplier):
    """a class to represent CleaningCompany"""
    def __init__(self, supplierID, supplierName, supplierAddress, supplierContactDetails, cleaningHours=0,
                 typeOfCleaning=""):
        super().__init__(supplierID, supplierName, supplierAddress, supplierContactDetails)
        self.cleaningHours = cleaningHours
        self.typeOfCleaning = typeOfCleaning

    # method to manage cleaning packages
    def manageCleaningPackages(self):
        pass

    # adding the setter and getter functions for the class CleaningCompany
    def get_cleaningHours(self):
        return self.cleaningHours
    def set_cleaningHours(self, cleaningHours):
        self.cleaningHours = cleaningHours

    def get_typeOfCleaning(self):
        return self.typeOfCleaning
    def set_typeOfCleaning(self, typeOfCleaning):
        self.typeOfCleaning = typeOfCleaning


class DecorationsCompany(Supplier):
    """a class to represent DecorationsCompany"""
    def __init__(self, supplierID, supplierName, supplierAddress, supplierContactDetails, arrangementsType="", cost=0.0,
                 decorationsColor=""):
        super().__init__(supplierID, supplierName, supplierAddress, supplierContactDetails)
        self.arrangementsType = arrangementsType
        self.cost = cost
        self.decorationsColor = decorationsColor

    # method to design decoration packages
    def designDecorationPackages(self):
        pass

    # adding the setter and getter functions for the class DecorationsCompany
    def get_arrangementsType(self):
        return self.arrangementsType
    def set_arrangementsType(self, arrangementsType):
        self.arrangementsType = arrangementsType

    def get_cost(self):
        return self.cost
    def set_cost(self, cost):
        self.cost = cost

    def get_decorationsColor(self):
        return self.decorationsColor
    def set_decorationsColor(self, decorationsColor):
        self.decorationsColor = decorationsColor

class EntertainmentCompany(Supplier):
    """a class to represent EntertainmentCompany"""
    def __init__(self, supplierID, supplierName, supplierAddress, supplierContactDetails, typeOfEntertainment=""):
        super().__init__(supplierID, supplierName, supplierAddress, supplierContactDetails)
        self.typeOfEntertainment = typeOfEntertainment

#method to view entertainers
    def viewEntertainers(self):
      pass

# adding the setter and getter functions for the class EntertainmentCompany
    def get_typeOfEntertainment(self):
        return self.typeOfEntertainment
    def set_typeOfEntertainment(self, typeOfEntertainment):
        self.typeOfEntertainment = typeOfEntertainment

class FurnitureSupplier(Supplier):
    """a class to represent FurnitureSupplier"""
    def __init__(self, supplierID, supplierName, supplierAddress, supplierContactDetails, typeOfFurniture= "", furnitureColor=""):
        super().__init__(supplierID, supplierName, supplierAddress, supplierContactDetails)
        self.typeOfFurniture = typeOfFurniture
        self.furnitureColor = furnitureColor

# adding the setter and getter functions for the class FurnitureSupplier
    def get_typeOfFurniture(self):
        return self.typeOfFurniture
    def set_typeOfFurniture(self, typeOfFurniture):
        self.typeOfFurniture = typeOfFurniture
    def get_furnitureColor(self):
        return self.furnitureColor
    def set_furnitureColor(self, furnitureColor):
        self.furnitureColor = furnitureColor