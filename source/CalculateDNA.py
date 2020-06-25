from random import random,randint,choice
from Data import Data
class CalculateDNA:
    def __init__(self):
        self.fitnessScore = 0

    def calculateFitnessScore(self,DNA):
        score = 100
        for i in range(len(DNA.classes)-1):
            
            for j in range(i+1,len(DNA.classes)):
                
                if DNA.classes[i].getDay() == DNA.classes[j].getDay():
                    
                    if DNA.classes[i].getClassTime().getTime() == DNA.classes[j].getClassTime().getTime():
                        
                        if (DNA.classes[i].getInstructor().getId() == DNA.classes[j].getInstructor().getId()) or (DNA.classes[i].getRoom().getNumber() == DNA.classes[j].getRoom().getNumber()) :
                            score-=1
                           
        return score

    def cross(self,DNA_A,DNA_B):
        rd = randint(0,len(DNA_A.classes)-1) #8
        DNA_C = DNA_A
        
        for i in range(len(DNA_A.classes)): #0--16
            if i <= rd:
                DNA_C.classes[i] = DNA_A.classes[i]
            else:
                DNA_C.classes[i] = DNA_B.classes[i]
        return DNA_C
    
    def mutation(self,mutationRate,DNA):
        data = Data()
        rd = randint(0,len(DNA.classes)-1)#6
        
        
        for i in range(len(DNA.classes)):
            a=randint(0,10)
            if a < mutationRate and i == rd:
                
                DNA.classes[rd].setRoom(data.rooms[randint(0,len(data.rooms)-1)])
                
                DNA.classes[rd].setClassTime(data.classTime[randint(0,len(data.classTime)-1)])
                DNA.classes[rd].setInstructor(data.instructor[randint(0,len(data.instructor)-1)])
                DNA.classes[rd].setDay(data.day[randint(0,len(data.day)-1)])
        return DNA
                
    
    