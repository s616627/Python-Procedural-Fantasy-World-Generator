
#civilizations and locations

#abstract location class
class Location:
    def __init__(self,name,color,char,buildings):

        #string
        self.name = name
        self.color = color

        #one character string
        self.char = char

        #buildings array
        self.buildings = buildings


class Town(Location):
    def __init__(self,name,color,char,buildings,culture,race):
        super().__init__(name,color,char,buildings)
        self.culture = culture
        self.race = race

    def print_name(self):
        print(self.name)



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

