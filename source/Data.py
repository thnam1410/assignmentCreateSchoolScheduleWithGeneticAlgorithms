from Room import Room
from Course import Course
from Shift import Shift
from Instructor import Instructor
from Student import Student
class Data:
    _rooms = [ ["A105",40] , ["B405",20] , ["C401",20] , ["A201",30] , ["C111",40]  ]
    _classTime = [ ["Ca1","06:50 - 09:15"], 
                ["Ca2",   "09:25 - 11:50"],
                ["Ca3",   "12:30 - 14:55"],
                ["Ca4",   "15:05 - 17:30"] ]
    _instructor = [["I1","Nguyen Van A"],
                    ["I2","Nguyen Thi B"],
                    ["I3","Pham Van D"],
                    ["I4","Truong Thao C"],
                    ["I5","D Van C"],
                    ["I6","E Thi F"],
                    ["I7",""],
                    ["I8",""],
                    ["I9",""],
                    ]
    _day =["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]
    def __init__(self):
        self.rooms = []
        self.classTime =[]
        self.instructor=[]
        self.day= self._day
        for i in range(len(self._rooms)):
            self.rooms.append(Room(self._rooms[i][0],self._rooms[i][1]))
        for i in range(len(self._classTime)):
            self.classTime.append(Shift(self._classTime[i][0],self._classTime[i][1]))
        for i in range(len(self._instructor)):
            self.instructor.append(Instructor(self._instructor[i][0],self._instructor[i][1]))

        course1 = Course("C1"," Artificial Intelligent", 30 , [self.instructor[1],self.instructor[2]])
        course2 = Course("C2"," Machine Learning", 20 , [self.instructor[0],self.instructor[3]])
        course3 = Course("C3"," Deep Learning", 30 , [self.instructor[5]])
        course4 = Course("C4"," Python Basic", 40 , [self.instructor[4],self.instructor[1]])
        course5 = Course("C5"," Web Application", 40 , [self.instructor[2],self.instructor[0]])
        course6 = Course("C6"," Java 2", 30 , [self.instructor[5],self.instructor[3]])
        course7 = Course("C7"," Java 1", 30 , [self.instructor[8],self.instructor[7]])
        course8 = Course("C8"," C++ Programming", 30 , [self.instructor[2],self.instructor[7]])
        course9 = Course("C9"," C Programming Basic", 30 , [self.instructor[4],self.instructor[5]])
        course10 = Course("C10"," Python Advance", 30 , [self.instructor[6],self.instructor[7]])
        course11 = Course("C11"," Clean Code", 30 , [self.instructor[4],self.instructor[8]])
        course12 = Course("C12"," XLDLL", 30 , [self.instructor[5],self.instructor[3]])
        course13 = Course("C13"," Data Mining", 30 , [self.instructor[2],self.instructor[8]])
        course14 = Course("C14"," ABC", 30 , [self.instructor[1],self.instructor[4]])
        course15 = Course("C15"," XYZ", 30 , [self.instructor[7],self.instructor[3]])
        course16 = Course("C16"," CCC", 30 , [self.instructor[5],self.instructor[3]])

        self.courses = [course1,course2,course3,course4,course5,course6,course7,
                        course8,course9,course10,course11,course12,course13,course14,course15,course16]