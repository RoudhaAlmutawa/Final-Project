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
