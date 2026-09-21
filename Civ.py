
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
    def __init__(self,name,color,symbol,buildings,x_coord,y_coord,culture,race,civ,pop):
        super().__init__(name,color,symbol,buildings,x_coord,y_coord)

        #other
        self.culture = culture
        self.race = race
        self.civ = civ

        # string
        self.symbol = symbol

        #int
        self.pop = pop
        self.x_coord = x_coord
        self.y_coord = y_coord

        if (pop == 1):
            self.caste_pops = {"Peasants": 1}
            self.caste_race = {"Peasants": race}
        else:
            self.caste_pops = {"Nobles": 1, "Peasants": (pop - 1)}
            self.caste_race = {"Nobles": race, "Peasants": race}




    def pop_change(self,new_pop=1):
        self.pop += new_pop

    def return_pop(self):
        pop_sum = 0
        for pop in self.caste_pops.values():
            pop_sum = pop_sum + pop

        return pop_sum

    def add_caste(self, caste_name, new_caste_race, new_caste_pop = 1):
        self.caste_pops[caste_name] = new_caste_pop + self.caste_pops[caste_name]
        self.caste_race[caste_name] = new_caste_race


    def remove_caste(self, caste_name, new_caste_pop = 1):

        new_caste_population = new_caste_pop

        if self.caste_pops[caste_name] < new_caste_population:
            new_caste_population = self.caste_pops[caste_name]

        if self.caste_pops[caste_name] != 0:
            self.caste_pops[caste_name] =  self.caste_pops[caste_name] - new_caste_population

    def change_caste(self, new_caste, new_caste_race, old_caste, new_caste_pop = 1):

        new_caste_population = new_caste_pop

        if self.caste_pops[old_caste] < new_caste_population:
            new_caste_population = self.caste_pops[old_caste]

        if self.caste_pops[old_caste] != 0:
            self.add_caste(new_caste,new_caste_race,new_caste_population)
            self.caste_pops[old_caste] = self.caste_pops[old_caste] - new_caste_population



    def destroy(self):
        self.name = self.name + " Ruins"
        self.pop = 0
        self.caste_pops = {}
        self.caste_race = {}
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

