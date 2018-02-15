from City import City
from Tour import Tour
from TourManager import TourManager
from Population import Population
from GA import GeneticAlgorithm
from itertools import permutations


if __name__ == '__main__':
    tourManager = TourManager()

    city1 = City(60, 200)
    tourManager.add_city(city1)

    city2 = City(180, 200)
    tourManager.add_city(city2)

    city3 = City(80, 180)
    tourManager.add_city(city3)

    city4 = City(140, 180)
    tourManager.add_city(city4)

    city5 = City(20, 160)
    tourManager.add_city(city5)

    city6 = City(100, 160)
    tourManager.add_city(city6)

    city7 = City(200, 160)
    tourManager.add_city(city7)

    city8 = City(140, 140)
    tourManager.add_city(city8)

    city9 = City(40, 120)
    tourManager.add_city(city9)

    city10 = City(100, 120)
    tourManager.add_city(city10)

    city11 = City(180, 100)
    tourManager.add_city(city11)

    city12 = City(60, 80)
    tourManager.add_city(city12)

    #distance = 1000000
    #best_case = None

    #time = 0
    #for i in permutations(tourManager.get_city_list(), 10):
    #    time += 1
    #    L = list(i)
    #    tour = Tour()
    #    tour.set_by_list(L)
    #    current_distance = tour.get_one_tour_total_distance()
    #    if distance > current_distance:
    #        distance = current_distance
    #        best_case = tour

    #print('**')
    #print(distance)
    #print(time)










##

##

##
##    city13 = City(120, 80)
##    tourManager.add_city(city13)
##
##    city14 = City(180, 60)
##    tourManager.add_city(city14)
##
##    city15 = City(20, 40)
##    tourManager.add_city(city15)
##
##    city16 = City(100, 40)
##    tourManager.add_city(city16)
##
##    city17 = City(200, 40)
##    tourManager.add_city(city17)
##
##    city18 = City(20, 20)
##    tourManager.add_city(city18)
##
##    city19 = City(60, 20)
##    tourManager.add_city(city19)
##
##    city20 = City(160, 20)
##    tourManager.add_city(city20)



    pop = Population(100)
    pop.initia_pop(tourManager)

    GA = GeneticAlgorithm(pop, 0.9999, 0.015, 5, 100, True)


    #for i in range(100):
    #    GA.evolution()


    #GA.roulette_wheel_selection()

    GA.run_test()

    #GA.run_test()

    #GA.get_best_case()

    #GA.check_pop();








