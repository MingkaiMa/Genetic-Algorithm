from random import random, randint
from Population import Population
from Tour import Tour
from copy import deepcopy
import sys
import matplotlib.pyplot as plt

class GeneticAlgorithm():
    def __init__(self, population, pro_cross, pro_mutation, tournament_size, max_gen, elitism):
        self.population = population
        self.pro_cross = pro_cross
        self.pro_mutation = pro_mutation
        self.max_gen = max_gen
        self.tournament_size = tournament_size
        self.elitism = elitism
        self.y = []
        self.time_mutation = 0



    def check_pop(self):
        tour1 = self.population.getTour(0)
        for city in tour1.tour:
            print(city.get_x(), city.get_y())

        tour1.get_one_tour_total_distance()
        print("********")



    ##inversion mutation

    def mutation(self):
        for i in range(self.population.getPopSize()):
            if self.pro_mutation > random():
                print('mutate: ', i)
                m_tour = self.population.getTour(i)

                swap_index1 = 0
                swap_index2 = 0

                while swap_index1 == swap_index2:
                    swap_index1 = randint(0, m_tour.getTourSize() - 1)
                    swap_index2 = randint(0, m_tour.getTourSize() - 1)

                m_tour.tour[swap_index1], m_tour.tour[swap_index2] = m_tour.tour[swap_index2], m_tour.tour[swap_index1]



    ##reverse sequence mutation(RSM)

    def RSM(self):
        for i in range(1, self.population.getPopSize()):
            if self.pro_mutation > random():
                m_tour = self.population.getTour(i)
                print('mutate here:')
                print('previous: ')
                print(m_tour.tour)
                self.time_mutation += 1

                swap_index1 = 0
                swap_index2 = 0

                while swap_index1 == swap_index2:
                    swap_index1 = randint(0, m_tour.getTourSize() - 1)
                    swap_index2 = randint(0, m_tour.getTourSize() - 1)


                swap_index1 = min(swap_index1, swap_index2)
                swap_index2 = max(swap_index1, swap_index2)

                print('index1: ', swap_index1, 'index2:', swap_index2)
                R = []
                R.extend(m_tour.tour[: swap_index1])
                R.extend(m_tour.tour[swap_index1: swap_index2 + 1][::-1])
                R.extend(m_tour.tour[swap_index2 + 1:])

                m_tour.tour = deepcopy(R)

                print('after: ')
                print(m_tour.tour)





    def mutation_roulette(self):
        for i in range(1, self.population.getPopSize()):
            if self.pro_mutation > random():
                print('mutate: ', i)
                m_tour = self.population.getTour(i)
                self.time_mutation += 1
                swap_index1 = 0
                swap_index2 = 0

                while swap_index1 == swap_index2:
                    swap_index1 = randint(0, m_tour.getTourSize() - 1)
                    swap_index2 = randint(0, m_tour.getTourSize() - 1)

                m_tour.tour[swap_index1], m_tour.tour[swap_index2] = m_tour.tour[swap_index2], m_tour.tour[swap_index1]


    def list_contains(self, lst, t_city):
        for city in lst:
            if city:
                if city.get_x() == t_city.get_x() and city.get_y() == t_city.get_y():
                    return True

        return False




    def cross(self, tourParent1, tourParent2):

        tour_size = tourParent1.getTourSize()


        parent1 = deepcopy(tourParent1.getTour())
        parent2 = deepcopy(tourParent2.getTour())
        child = [None] * tour_size

        index1 = 0
        index2 = 0
        while index1 == index2:

            index1 = randint(0, tour_size - 1)
            index2 = randint(0, tour_size - 1)

        start_index = min(index1, index2)
        end_index = max(index1, index2)

        for i in range(start_index, end_index + 1):
            child[i] = parent1[i]



        for i in range(tour_size):
            if not self.list_contains(child, parent2[i]):
                for j in range(tour_size):
                    if not child[j]:
                        child[j] = parent2[i]
                        break


        if None in child:
            print(child)
            print('fuck')
            sys.exit()

        Child = Tour()
        Child.set_by_list(child)



        return Child






    def TournamentSelect(self):

        tournament_pop = Population(self.tournament_size)

        for i in range(self.tournament_size):
            random_index = randint(0, self.population.getPopSize() - 1)
            tournament_pop.addTour(self.population.getTour(random_index))

        best_case = tournament_pop.getBestFitness()
        return best_case




    def roulette_wheel_selection(self):

        sum_ = 0
        #print('ddd')
        for i in range(1, self.population.getPopSize()):
            #print('$$', self.population.getTour(i).get_fitness())
            sum_ += self.population.getTour(i).get_fitness()

        #print(sum_)
        for i in range(1, self.population.getPopSize()):
            r = random() * sum_
            for j in range(self.population.getPopSize()):
                r = r - self.population.getTour(j).get_fitness()
                if r <= 0:
                    self.population.setTour(i, self.population.getTour(j))
                    break




    def evolution_roulette(self):


        elitismOffset = 0
        if self.elitism:

            self.population.setTour(0, self.population.getBestFitness())
            elitismOffset = 1

        best_case = self.population.getTour(0)
        print('best case is: ')
        self.y.append(best_case.get_one_tour_total_distance())
        print(self.population.getBestFitness().get_fitness(), "___")
        print(best_case.get_one_tour_total_distance())
        print(best_case.get_fitness())

        self.roulette_wheel_selection()


        print(elitismOffset, 'LLL')
        for i in range(elitismOffset, self.population.getPopSize()):


            if self.pro_cross > random():

                parent_index1 = 0
                parent_index2 = 0
                while parent_index1 == parent_index2:
                    parent_index1 = randint(0, self.population.getPopSize() - 1)
                    parent_index2 = randint(0, self.population.getPopSize() - 1)

                parent1 = self.population.getTour(parent_index1)
                parent2 = self.population.getTour(parent_index2)

                child = self.cross(parent1, parent2)

                self.population.setTour(i, child)

        print(self.population.getBestFitness().get_fitness(), "___++")
        print(best_case.get_fitness())


        #for i in range(elitismOffset, self.population.getPopSize()):
        #self.mutation_roulette()
        self.RSM()


        print(self.population.getBestFitness().get_fitness(), "___--")
        print(best_case.get_fitness())








    def evolution(self):

        elitismOffset = 0
        if self.elitism:
            self.population.setTour(0, self.population.getBestFitness())
            elitismOffset = 1

        print('best case is:')
        best_case = self.population.getTour(0)
        print(best_case.get_one_tour_total_distance())
        self.y.append(best_case.get_one_tour_total_distance())

        #for city in best_case.tour:
         #   print(city)


        for i in range(elitismOffset, self.population.getPopSize()):

            parent1 = self.TournamentSelect()
            parent2 = self.TournamentSelect()


            child = self.cross(parent1, parent2)
            self.population.setTour(i, child)

        #for i in range(elitismOffset, self.population.getPopSize()):
            #self.mutation()

        self.mutation_roulette()



    def run_test(self):
        x = range(200)
        time = 0
        for i in x:
            print(i)
            time += 1

            self.evolution_roulette()
            #self.evolution()

        print("mutation time: ", self.time_mutation)
        print(len(self.y))
        print(time)
        plt.figure(1)
        plt.plot(x, self.y)
        plt.ylabel('y value')
        plt.xlabel('x value')
        plt.show()




    def get_best_case(self):
        best_case = self.population.getTour(0)
        for city in best_case.tour:
            print(city)









