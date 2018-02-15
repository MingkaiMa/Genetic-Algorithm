from City import City
from random import shuffle
import math
from copy import deepcopy

class Tour():
    def __init__(self):
        self.tour = []

    def generate_one_tour(self, tourManager):
        self.tour = deepcopy(tourManager.get_city_list())
        shuffle(self.tour)

    def get_distance_bet_two_city(self, city1, city2):
        return math.sqrt((city1.get_x() - city2.get_x()) ** 2 + (city1.get_y() - city2.get_y()) ** 2)


    def set_personal_tour(self, value, size):
        self.tour = [value] * size


    def set_by_index(self, index, value):
        self.tour[index] = value


    def set_by_list(self, lst):
        self.tour = deepcopy(lst)


    def getTour(self):
        return self.tour


    def containsCity(self, City):
        for city in self.tour:
            if city:
                if city.get_x() == City.get_x() and city.get_y() == City.get_y():
                    return True

        return False



    def get_fitness(self):
        return 1 / self.get_one_tour_total_distance()


    def getTourSize(self):
        return len(self.tour)


    def get_one_tour_total_distance(self):

        total_distance = 0

        for i in range(len(self.tour)):
            #print(i)
            if i == len(self.tour) - 1:
                temp_distance = self.get_distance_bet_two_city(self.tour[i], self.tour[0])
                #print("8", self.tour[i].get_x(), self.tour[i].get_y(), self.tour[0].get_x(), self.tour[0].get_y())
                total_distance += temp_distance
                break

            temp_distance = self.get_distance_bet_two_city(self.tour[i], self.tour[i + 1])

            #print(self.tour[i].get_x(),self.tour[i].get_y() , self.tour[i + 1].get_x(),self.tour[i + 1].get_y())
            total_distance += temp_distance

        print('&&', total_distance)
        return total_distance







