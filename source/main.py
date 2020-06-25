from Population import Population

def main():
    populationSize = 50
    mutationRate = 5

    population = Population(populationSize,mutationRate)

    while True:   
        population.overCross()
        population.findBestFit()

        if population.isFinish:
            population.display()
            break
        

if __name__ == "__main__":
    main()
