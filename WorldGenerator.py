import random
import numpy as np

import  RacesAndCreatures
import stringListFunctions
from RacesAndCreatures import Species
from stringListFunctions import readFromFile, readFromFileAdvanced
import Civ
import markovNameGenerator
import Gods


class World:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        shape = (width,height)

        self.elevation_map = []
        self.temperature_map = []
        self.humidity_map = []
        self.biome_map = []

        #2d bool array for what tiles have rivers


        self.rivers = np.full(shape,False)

        #this is used to divide world into regions based on biomes and naming them after

        self.region_names = [[0 for _ in range(width)] for _ in range(height)]

        self.city_names_list = []

        self.region_dict = {

            'Plains':'OoO',
            'Forest':'###',
            'Taiga':'‡‡‡',
            'Desert':'≈≈≈',
            'Sea':' ~ ',
            'Artic Sea':' ~ ',
            'Mountains':'A^A',
            'Artic Mountains':'^A^',
            'Artic':' - ',
            'Rainforest':'TTT',
            'Savannah':'Y*Y',
            'River':'A)A'
        }

        self.fantasy_races = self.createRaces()
        self.gods = self.createGods()

        nothing = Civ.Location("---","BLACK","..",[])

        self.location_map = [[nothing for x in range(width)] for y in range(height)]

        elevation_array = []
        temperature_array = []
        humidity_array = []
        biome_array = []

        for i in range(height):

            for j in range(width):
                elevation_array.append(random.randint(0,10))
                humidity_array.append(random.randint(0,10))
                biome_array.append("???")

                if i == 0 or i == height - 1:
                    temperature_array.append(-10)
                elif i == round(height/2):
                    temperature_array.append(10)
                else:
                    temperature_array.append(random.randint(0, 10))

            self.elevation_map.append(elevation_array)
            elevation_array = []
            self.temperature_map.append(temperature_array)
            temperature_array=[]
            self.humidity_map.append(humidity_array)
            humidity_array = []
            self.biome_map.append(biome_array)
            biome_array = []

        for l in range(5):
            self.smoothNumberArray(self.elevation_map)

        for m in range(5):
            self.smoothNumberArray(self.temperature_map)
            self.smoothNumberArray(self.humidity_map)

        self.setBiomeMap()

        for z in range(100):
            self.createRiverFlow()

        self.settleRaces()

        self.createGods()

        self.assign_regions()


    def printElevation(self):
        self.printNumberArray(self.elevation_map)

    def printTemperature(self):
        self.printNumberArray(self.temperature_map)

    def printHumidity(self):
        self.printNumberArray(self.humidity_map)

    def printBiomes(self):
        self.printNumberArray(self.biome_map)

    def printRegions(self):
        self.printNumberArray(self.region_names)

    def printLocations(self):
        for row in self.location_map:
            for x in row:
                print(x.name, end=",")
            print("")




    def smoothNumberArray(self,map):
        for y in range(self.height):
            for x in range(self.width):

                if y is not self.height-1:

                    avg_elev = round((map[y][x] + map[y+1][x])/2)
                    map[y][x] = avg_elev
                    map[y+1][x] = avg_elev

        for y_coord in range(self.height):
            for x_coord in range(self.width):

                if x_coord is not self.width-1:
                    avg_elev = round((map[y_coord][x_coord] + map[y_coord][x_coord+1])/2)
                    map[y_coord][x_coord] = avg_elev
                    map[y_coord][x_coord+1] = avg_elev
                else:
                    avg_elev = round((map[y_coord][self.width-1] + map[y_coord][0]) / 2)
                    map[y_coord][self.width-1] = avg_elev
                    map[y_coord][0] = avg_elev


    def printNumberArray(self,map):
        for row in map:
            for x in row:
                print(x,end=",")
            print("")

    def printFantasyRaces(self):
        for x in range(len(self.fantasy_races)):
            print(self.fantasy_races[x].plural_name)

    def printGods(self):
        for x in range(len(self.gods)):
            print(f"{self.gods[x].name} : Rules over the domain of ")

            for y in range(len(self.gods[x].god_spheres)):
                print(f"{y+1}. {self.gods[x].god_spheres[y][0]}")



    def printPoliticalMap(self):
        for y in range(self.height):
            for x in range(self.width):

                if self.location_map[y][x].char == "C.":
                    print("C.")
                else:
                    print(". ",end="")
            print("")

    def setBiomeMap(self):

        #init(autoreset=True)

        elevation = -100
        temperature = -100
        humidity = -100

        for y in range(self.height):
            for x in range(self.width):

                elevation = self.elevation_map[y][x]
                temperature = self.temperature_map[y][x]
                humidity = self.humidity_map[y][x]

                #elevation
                # |
                # --> temperature
                #     |
                #     --> humidity

                match elevation:
                    case elevation if (elevation<5):
                        match temperature:
                            case temperature if (temperature<3):
                                self.biome_map[y][x] = "Artic Sea"
                            case _:
                                self.biome_map[y][x] = "Sea"
                    case elevation if (elevation>7):
                        match temperature:
                            case temperature if (temperature < 3):
                                self.biome_map[y][x] = "Artic Mountains"
                            case temperature if (temperature > 2):
                                match humidity:
                                    case humidity if (humidity > 7):
                                        self.biome_map[y][x] = "River"
                                    case _:
                                        self.biome_map[y][x] = "Mountains"
                    case _:
                        match temperature:
                            case temperature if (temperature < 2):
                                self.biome_map[y][x] = "Artic"
                            case temperature if (temperature<4):
                                self.biome_map[y][x] = "Taiga"
                            case temperature if (temperature > 5):
                                match humidity:
                                    case humidity if (humidity>5):
                                        self.biome_map[y][x] = "Rainforest"
                                    case humidity if (humidity<5):
                                        self.biome_map[y][x] = "Desert"
                                    case _:
                                        self.biome_map[y][x] = "Savannah"
                            case _:
                                match humidity:
                                    case humidity if (humidity>4):
                                        self.biome_map[y][x] = "Forest"
                                    case _:
                                        self.biome_map[y][x] = "Plains"






    def createRiverFlow(self):
        for x in range (self.width):
            for y in range (self.height):
                elevation = self.elevation_map[y][x]

                if (x != self.width - 1):
                    if (self.elevation_map[y][x + 1] < elevation):
                        if(self.biome_map[y][x+1] != "River"):
                            self.rivers[y][x + 1] = True

                if (y != self.height - 1):
                    if (self.elevation_map[y + 1][x] < elevation):
                        self.rivers[y+1][x] = True

                if (x != self.width - 1 and y != self.height - 1):
                    if (self.elevation_map[y + 1][x + 1] < elevation):
                        self.rivers[y+1][x + 1] = True

                if (x != 0):
                    if (self.elevation_map[y][x - 1] < elevation):
                        self.rivers[y][x - 1] = True

                if (y != 0):
                    if (self.elevation_map[y - 1][x] < elevation):
                        self.rivers[y-1][x] = True

                if (y != 0 and x != 0):
                    if (self.elevation_map[y - 1][x - 1] < elevation):
                        self.rivers[y - 1][x - 1] = True

                if (x != 0 and y != self.height - 1):
                    if (self.elevation_map[y + 1][x - 1] < elevation):
                        self.rivers[y+1][x - 1] = True

                if (x != self.width - 1 and y != 0):
                    if (self.elevation_map[y - 1][x + 1] < elevation):
                        self.rivers[y-1][x + 1] = True

                if (x == self.width - 1):
                    if (self.elevation_map[y][0] < elevation):
                        self.rivers[y][0] = True

                        if (y!=0):
                            if (self.elevation_map[y-1][0] < elevation):
                                self.rivers[y-1][0] = True

                        if (y!=self.height-1):
                            if (self.elevation_map[y+1][0] < elevation):
                                self.rivers[y+1][0] = True

                if (x == 0):
                    if (self.elevation_map[y][self.width-1] < elevation):
                        self.rivers[y][self.width-1] = True

                        if (y != 0):
                            if (self.elevation_map[y - 1][self.width-1] < elevation):
                                self.rivers[y - 1][self.width-1] = True

                        if (y != self.height - 1):
                            if (self.elevation_map[y + 1][self.width-1] < elevation):
                                self.rivers[y + 1][self.width-1] = True

    def createRaces(self):
        races = readFromFile("CreaturesAndRaces/fantasyRaces.txt")
        race_number = round((self.width*self.height)/200)
        if race_number < 4:
            race_number = 4
        elif race_number>14:
            race_number = 14
        world_races = random.sample(races, race_number)

        check_for_header = True
        counter = 0
        while check_for_header and counter<race_number:
            if world_races[counter].split(",")[0] == "#Male":
                world_races = random.sample(races, race_number)
                counter = 0
            else:
                counter = counter+1

        check_for_header = False

        final_world_races = []

        physical_traits = readFromFileAdvanced("charicteristicFiles/physicalTraits.txt")
        culture_traits = readFromFileAdvanced("charicteristicFiles/cultureTraits.txt")

        for x in range(race_number):
            races_split = world_races[x].split(",")
            attributes = races_split[11:]
            new_race = Species(races_split[0], races_split[1], races_split[2], races_split[3], races_split[4], races_split[5],
                        races_split[6], races_split[7], races_split[8], races_split[9], races_split[10], True, [],
                        attributes)

            random_trait_list = physical_traits[random.randint(0, len(physical_traits)-1)]
            random_culture_list = culture_traits[random.randint(0,len(culture_traits)-1)]

            random_trait:str = random_trait_list[random.randint(0, len(random_trait_list)-1)]
            random_culture:str = random_culture_list[random.randint(0, len(random_culture_list)-1)]

            #this is so a elf cant be short and tall
            # |
            # V
            #random_trait_list.remove(random_trait)
            #random_culture_list.remove(random_culture)

            if random_trait not in new_race.attributes:
                new_race.attributes.append(random_trait)
                new_race.plural_name = random_trait + " " + new_race.plural_name

            if random_culture not in new_race.attributes:
                new_race.attributes.append(random_culture)
                new_race.plural_name = random_culture + " " + new_race.plural_name

            final_world_races.append(new_race)

        return final_world_races


    def settleRaces(self):

        roman_city_names = readFromFile("nameFiles/romanCities.txt")
        hindu_city_names = readFromFile("nameFiles/hinduCities.txt")
        city_names = roman_city_names + hindu_city_names
        city_name_generator = markovNameGenerator.MarkovName(city_names, 3)

        colors = ["RED","GREEN","YELLOW","BLUE","MAGENTA","CYAN","WHITE",
               "GREY","PINK","LIGHTGREEN","LIGHTBLUE","PURPLE","TURQUOISE","ORANGE","BROWN"]

        race_number = len(self.fantasy_races)



        civ_colors = random.sample(colors,race_number)

        color_counter = 0

        settleable_places = []

        for i in range(self.height):
            for j in range(self.width):
                if self.biome_map[i][j] != "Sea" and self.biome_map[i][j] != "Artic Sea":
                    settleable_places.append([i,j])

        for race in self.fantasy_races:
            
            random_coord = settleable_places[random.randint(0,len(settleable_places)-1)]


            x = random_coord[1]
            y = random_coord[0]

            while self.location_map[y][x].name != "---":

                random_coord = settleable_places[random.randint(0, len(settleable_places) - 1)]

                x = random_coord[1]
                y = random_coord[0]


            city_name = city_name_generator.New()
            new_city =  Civ.Town(city_name,colors[color_counter],"[C]",[],[],race)
            self.location_map[y][x] = new_city

            self.city_names_list.append(new_city.name)


            if y != 0 :
                self.location_map[y-1][x] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y-1][x]], [], [], race)
                if x != 0:
                    self.location_map[y-1][x - 1] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y-1][x-1]], [], [], race)
                else:
                    self.location_map[y - 1][self.width - 1] = Civ.Town(city_name + " Outskirts", colors[color_counter],self.region_dict[self.biome_map[y - 1][x - 1]], [], [],race)

                if x != self.width-1:
                    self.location_map[y-1][x + 1] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y-1][x+1]], [], [], race)
                else:
                    self.location_map[y - 1][0] = Civ.Town(city_name + " Outskirts", colors[color_counter],self.region_dict[self.biome_map[y - 1][x - 1]], [], [],race)

            if y != self.height-1 :
                self.location_map[y+1][x] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y+1][x]], [], [], race)
                if x != 0:
                    self.location_map[y+1][x - 1] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y+1][x-1]], [], [], race)
                else:
                    self.location_map[y+1][self.width - 1] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y+1][self.width-1]], [], [], race)

                if x != self.width-1:
                    self.location_map[y+1][x + 1] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y+1][x+1]], [], [], race)
                else:
                    self.location_map[y + 1][0] = Civ.Town(city_name + " Outskirts", colors[color_counter],self.region_dict[self.biome_map[y + 1][0]], [],[], race)

            if x != 0 :
                self.location_map[y][x-1] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y][x-1]], [], [], race)
            else:
                self.location_map[y][self.width - 1] = Civ.Town(city_name + " Outskirts", colors[color_counter],self.region_dict[self.biome_map[y - 1][x - 1]], [], [],race)

            if x != self.width-1 :
                self.location_map[y][x+1] = Civ.Town(city_name + " Outskirts", colors[color_counter], self.region_dict[self.biome_map[y][x+1]], [], [], race)
            else:
                self.location_map[y][0] = Civ.Town(city_name + " Outskirts", colors[color_counter],self.region_dict[self.biome_map[y - 1][x - 1]], [],[], race)

            color_counter = color_counter+1

    def createGods(self):
        cultureTraits = readFromFileAdvanced("charicteristicFiles/cultureTraits.txt")
        physicalTraits = readFromFileAdvanced("charicteristicFiles/physicalTraits.txt")
        godSpheres = readFromFileAdvanced("charicteristicFiles/godspheres.txt")
        personalityTraitsGods = readFromFileAdvanced("charicteristicFiles/personalityTraitsGods.txt")

        romangods = readFromFile("nameFiles/romanGods.txt")
        hindugods = readFromFile("nameFiles/hinduGods.txt")

        romangoddesses = readFromFile("nameFiles/romanGoddesses.txt")
        hindugoddesses = readFromFile("nameFiles/hinduGoddess.txt")

        godnames = romangods + hindugods

        godGenerator = markovNameGenerator.MarkovName(godnames, 3)

        goddessGenerator = markovNameGenerator.MarkovName(godnames, 3)

        god_number = len(self.fantasy_races)*2
        if god_number < 4:
            god_number = 4

        gods = []

        for x in range(int(god_number/2)):
            gods.append(Gods.Deity(godGenerator.New(10), godSpheres, personalityTraitsGods, physicalTraits, []))

        for y in range(int(god_number/2)):
            gods.append(Gods.Deity(goddessGenerator.New(10), godSpheres, personalityTraitsGods, physicalTraits, []))


        return gods


    def assign_regions(self) -> None:

        region_count = 1


        for y in range(self.height):
            for x in range(self.width):
                current_biome = self.biome_map[y][x]



                if x != self.width-1:
                    if self.biome_map[y][x+1] is current_biome:
                        self.region_names[y][x] = self.region_names[y][x+1]

                if y != self.height-1:
                    if self.biome_map[y+1][x] is current_biome and self.region_names[y][x] != 0:
                        self.region_names[y+1][x] = self.region_names[y][x]


                if self.region_names[y][x] == 0:

                    if x != 0:
                        last_biome = self.biome_map[y][x-1]
                    else:
                        last_biome = ""

                    if last_biome is current_biome:
                        self.region_names[y][x] = region_count

                    else:
                        region_count = region_count+1
                        self.region_names[y][x] = region_count


                if y>0:
                    if self.biome_map[y-1][x] is current_biome and self.region_names[y][x] != 0:
                        self.region_names[y-1][x] = self.region_names[y][x]

                if y != self.height-1:
                    if self.biome_map[y+1][x] is current_biome and self.region_names[y][x] != 0:
                        self.region_names[y+1][x] = self.region_names[y][x]



                










