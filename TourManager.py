from Tour import Tour

class TourManager():
    def __init__(self):
        self.city_list = []

    def add_city(self, city):
        self.city_list.append(city)

    def tour_size(self):
        return len(self.city_list)

    def get_city(self, index):
        return self.city_list[index]

    def get_city_list(self):
        return self.city_list