class Course:
    def __init__(self, id, name, maxNumberOfStudents, instructors):
        self.id = id
        self.name =name
        self.maxNumberOfStudents = maxNumberOfStudents
        self.instructors = instructors
    def getId(self): 
        return self.id
    def getName(self): 
        return self.name
    def getMaxNumberOfStudents(self): 
        return self.maxNumberOfStudents
    def getInstructors(self): 
        return self.instructors

        