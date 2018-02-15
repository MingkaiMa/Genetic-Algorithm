from Tour import Tour
from copy import deepcopy
import random

class Population():
    def __init__(self, pop_size, ):
        self.pop_size = pop_size
        self.pop = []




    def initia_pop(self, tourmanager):
        for i in range(self.pop_size):
            tour = Tour()
            tour.generate_one_tour(tourmanager)
            self.pop.append(tour)


    def addTour(self, tour):
        self.pop.append(tour)

    def getTour(self, index):
        return self.pop[index]

    def setTour(self, index, tour):
        self.pop[index] = tour


    def getBestFitness(self):
        best_fitness = deepcopy(self.pop[0])

        for i in range(self.pop_size):
            if best_fitness.get_fitness() < self.pop[i].get_fitness():
                best_fitness = deepcopy(self.pop[i])


        return best_fitness



    def getPopSize(self):
        return len(self.pop)



