class Class:
    def __init__(self, id, course):
        self.id = id
        self.course= course
        self.instructor = None
        self.classTime = None
        self.room = None
        self.day = None
    def getId(self): 
        return self.id
    def getCourse(self):
        return self.course
    def getInstructor(self):
        return self.instructor
    def getClassTime(self):
        return self.classTime
    def getRoom(self):
        return self.room
    def getDay(self):
        return self.day
    def setInstructor(self,instructor):
        self.instructor = instructor
    def setClassTime(self,time):
        self.classTime= time
    def setRoom(self,room):
        self.room=room
    def setDay(self,day):
        self.day = day