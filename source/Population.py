from Schedule import Schedule
from CalculateDNA import CalculateDNA
from random import choices
from Data import Data
class Population:
    def __init__(self,populationSize,mutationRate):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.population = self.createPopulation(populationSize)
        self.bestFit = None
        self.bestFitPosition =0
        self.globalScore = 0
    def createPopulation(self,populationSize):
        p=[]
        for i in range(0,populationSize):
            p.append(Schedule().initialize())
        return p

    def overCross(self):
        a=[]
        b=[]
        for dna in self.population:
            a.append(dna)
            b.append(CalculateDNA().calculateFitnessScore(dna))
            
        for i in range(len(self.population)):
            parentA = choices(a,b)[0]
            parentB = choices(a,b)[0]

            self.population[i] = CalculateDNA().cross(parentA,parentB)  
            
            newDNA = CalculateDNA().mutation(self.mutationRate,self.population[i])
            self.population[i] = newDNA
    
    def findBestFit(self):
        score = 0
        position = 0
        for i,dna in enumerate(self.population):
            temp = CalculateDNA().calculateFitnessScore(dna)
            if temp>score:
                score = temp
                position = i
        self.globalScore = score
        self.bestFitPosition = position

    def isFinish(self):
        if(self.globalScore == 100):
            return True
        else: return False


    def display(self):   
        data = Data()
        for day in data._day:
            print("------------"+day+"------------")
            for _class in self.population[self.bestFitPosition].classes:
                if _class.getClassTime().getTime() == data._classTime[0][1] and _class.getDay() == day:
                    print(str(_class.getClassTime().getTime())+" | "+str(_class.getRoom().getNumber()) + " | " + str(_class.getInstructor().getId())+" | "+str(_class.getCourse().getName()) ) 
            for _class in self.population[self.bestFitPosition].classes:
                if _class.getClassTime().getTime() == data._classTime[1][1] and _class.getDay() == day:
                    print(str(_class.getClassTime().getTime())+" | "+str(_class.getRoom().getNumber()) + " | " + str(_class.getInstructor().getId())+" | "+str(_class.getCourse().getName()) )          
            for _class in self.population[self.bestFitPosition].classes:   
                if _class.getClassTime().getTime() == data._classTime[2][1] and _class.getDay() == day:
                    print(str(_class.getClassTime().getTime())+" | "+str(_class.getRoom().getNumber()) + " | " + str(_class.getInstructor().getId())+" | "+str(_class.getCourse().getName()) )
            for _class in self.population[self.bestFitPosition].classes:
                if _class.getClassTime().getTime() == data._classTime[3][1] and _class.getDay() == day:
                    print(str(_class.getClassTime().getTime())+" | "+str(_class.getRoom().getNumber()) + " | " + str(_class.getInstructor().getId())+" | "+str(_class.getCourse().getName()) )        

        
# if __name__ == "__main__":
#     a=Population(5,0.01)
#     a.printPopulation()
#     a.overCross()
#     a.printPopulation()
    
    """for j ,item in enumerate(parentA.classes):
                print(str(parentA.classes[j].getId())
                        +"||"+str(parentA.classes[j].getRoom().getNumber())
                        +"||"+str(parentA.classes[j].getClassTime().getTime())
                        +"||"+str(parentA.classes[j].getInstructor()[0])   )
            print("---")
            for j ,item in enumerate(parentB.classes):
                print(str(parentB.classes[j].getId())
                        +"||"+str(parentB.classes[j].getRoom().getNumber())
                        +"||"+str(parentB.classes[j].getClassTime().getTime())
                        +"||"+str(parentB.classes[j].getInstructor()[0])   )
            print("---")
            for j ,item in enumerate(self.population[i].classes):
                print(str(self.population[i].classes[j].getId())
                        +"||"+str(self.population[i].classes[j].getRoom().getNumber())
                        +"||"+str(self.population[i].classes[j].getClassTime().getTime())
                        +"||"+str(self.population[i].classes[j].getInstructor()[0])   )
            exit()""" #check parent