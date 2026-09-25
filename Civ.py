
#civilizations and locations

#abstract location class
class Location:
    def __init__(self,name,color,symbol,buildings,x_coord,y_coord):

        #strings
        self.name = name
        self.color = color
        #string for sprite
        self.symbol = symbol

        #buildings array
        self.buildings = buildings

        #int
        self.x_coord = x_coord
        self.y_coord = y_coord

    def print_name(self):
        print(self.name)

    def name_change(new_name):
        name = new_name


    def destroy(self):
        self.name = self.name + " Ruins"
        self.symbol = "Ruins"

class Town(Location):
    def __init__(self,name,color,symbol,buildings,x_coord,y_coord,culture,race,civ,population):
        super().__init__(name,color,symbol,buildings,x_coord,y_coord)

        #other
        self.culture = culture
        self.race = race
        self.civ = civ

        # string
        self.symbol = symbol

        #int
        self.x_coord = x_coord
        self.y_coord = y_coord

        #pop array
        self.pops = []

        if population == 1:
            self.pops.append(Pop(self.race,"Peasant","Peasant"))
        else:
            self.pops.append(Pop(self.race,"Nobles","Nobles"))

            for i in range(population-1):
                self.pops.append(Pop(self.race,"Peasant","Peasant"))


    def return_population(self):
        return len(self.pops)

    def add_pops(self, race, name, category,amount=1):
        for i in range(amount):
            self.pops.append(Pop(race, name, category))


    def remove_pop(self, name, amount=1):

        for i in range(amount):
            for j in range(len(self.pops)):
                self.pops.pop()
                break

    def change_caste(self, old_pop_name, new_pop, amount = 1):

        for i in range(amount):
            for j in range(len(self.pops)):

                if self.pops[j].name == old_pop_name:
                    self.pops[j] = new_pop

                break



    def destroy(self):
        self.name = self.name + " Ruins"
        self.pops = []
        self.symbol = "City Ruins"
        self.buildings = []

class Civ:

    def __init__(self,gold,income,costs,races,towns,color,culture):

        #int
        self.gold = gold
        self.income = income
        self.costs = costs

        #list of all races in the civ
        self.races = races

        #list of all towns in civ
        self.towns = towns

        #color for colorama
        self.color = color

        #culture
        self.culture = culture

class Pop:
    def __init__(self, race, name, category):

        #Race
        self.race = race

        #string
        self.name = name
        self.category = category