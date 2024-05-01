#the code below shows a software system to manage the organizes events of the company
import pickle
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
        return self.jobTitle
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
    def __init__(self, name="", employeeID=0, department="", jobTitle="", basicSalary=0.0, age=0, dateOfBirth= datetime, passportDetails="", managerType ="", ):
        super().__init__()      # Calling the superclass constructor
        self.managerType= managerType
        self.managedEmployees=[]

#method to know the mannaged employees
    def getManagedEmployees(self):
        pass

#adding the setter and getter functions for the class Manager
    def getManagerType(self):
        return self.managerType
    def setManagerType(self, managerType):
        self.managerType = managerType

    def getManagedEmployees(self):
        return self.managedEmployees

    def setManagedEmployees(self, managedEmployees):
        self.managedEmployees = managedEmployees

class Salesperson(Employee):
    def __init__(self, name="", employeeID=0, department="", jobTitle="", basicSalary=0.0, age=0, dateOfBirth= datetime, passportDetails="", managerID=""):
        super().__init()      # Calling the superclass constructor
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
    def getEventID(self):
        return self.eventID
    def setEventID(self, eventID):
        self.eventID = eventID

    def getEventType(self):
        return self.eventType
    def setEventType(self, eventType):
        self.eventType = eventType

    def getTheme(self):
        return self.theme
    def setTheme(self, theme):
        self.theme = theme

    def getEventDate(self):
        return self.eventDate
    def setEventDate(self, eventDate):
        self.eventDate = eventDate

    def getEventTime(self):
        return self.eventTime
    def setEventTime(self, eventTime):
        self.eventTime = eventTime

    def getEventDuration(self):
        return self.eventDuration
    def setEventDuration(self, eventDuration):
        self.eventDuration = eventDuration

    def getVenueAddress(self):
        return self.venueAddress
    def setVenueAddress(self, venueAddress):
        self.venueAddress = venueAddress

    def getClientID(self):
        return self.clientID
    def setClientID(self, clientID):
        self.clientID = clientID

    def getGuestList(self):
        return self.guestList
    def setGuestList(self, guestList):
        self.guestList = guestList

    def getCateringCompany(self):
        return self.cateringCompany
    def setCateringCompany(self, cateringCompany):
        self.cateringCompany = cateringCompany

    def getCleaningCompany(self):
        return self.cleaningCompany
    def setCleaningCompany(self, cleaningCompany):
        self.cleaningCompany = cleaningCompany

    def getDecorationsCompany(self):
        return self.decorationsCompany
    def setDecorationsCompany(self, decorationsCompany):
        self.decorationsCompany = decorationsCompany

    def getEntertainmentCompany(self):
        return self.entertainmentCompany
    def setEntertainmentCompany(self, entertainmentCompany):
        self.entertainmentCompany = entertainmentCompany

    def getFurnitureSupplyCompany(self):
        return self.furnitureSupplyCompany
    def setFurnitureSupplyCompany(self, furnitureSupplyCompany):
        self.furnitureSupplyCompany = furnitureSupplyCompany

class Client:
    """a class to represent clinet"""
    def __inin__(self, clientID=0, clientName= "", clientAddress= "", clientContactDetails="", clientBudget=0.0 ):
        self.clientID= clientID
        self.clientName= clientName
        self.clientAddress= clientAddress
        self.clientContactDetails= clientContactDetails
        self.clientBudget= clientBudget

#method to update budget
    def updateBudget(self):
        pass

#adding the setter and getter functions for the class Client
    def getClientID(self):
        return self.clientID
    def setClientID(self, clientID):
        self.clientID = clientID

    def getClientName(self):
        return self.clientName
    def setClientName(self, clientName):
        self.clientName = clientName

    def getClientAddress(self):
        return self.clientAddress
    def setClientAddress(self, clientAddress):
        self.clientAddress = clientAddress

    def getClientContactDetails(self):
        return self.clientContactDetails
    def setClientContactDetails(self, clientContactDetails):
        self.clientContactDetails = clientContactDetails

    def getClientBudget(self):
        return self.clientBudget
    def setClientBudget(self, clientBudget):
        self.clientBudget = clientBudget

