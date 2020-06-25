from Data import Data
from Class import Class
import random as rd
class Schedule:
    def __init__(self):
        self.classes = []
        self.classNumber = 0
    def initialize(self):
        data = Data()
        courses = data.courses
        for i in range(len(data.courses)):
            newClass = Class(self.classNumber,courses[i])
            self.classNumber+=1
            newClass.setInstructor(courses[i].getInstructors()[rd.randrange(0,len(courses[i].getInstructors()))])
            newClass.setRoom(data.rooms[rd.randrange(0,len(data.rooms))])
            newClass.setClassTime(data.classTime[rd.randrange(0,len(data.classTime))])
            newClass.setDay(data.day[rd.randrange(0,len(data.day))])
            self.classes.append(newClass)
        return self
    def getClasses(self):
        return self.classes



