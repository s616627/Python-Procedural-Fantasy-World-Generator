import stringListFunctions
import random

class Deity:
    def __init__(self,name,spheres,personalities,attributes,forms):

        #string
        self.name = name

        # string list

        self.god_spheres = random.sample(spheres,3)
        for sphere in self.god_spheres:
            spheres.remove(sphere)

        self.god_personality = random.sample(personalities,3)
        self.god_attributes = random.sample(attributes,3)

        # forms and god_forms are a list of creatures
        #god_forms = random.sample(forms,2)

    def printName(self):
        print(self.name)

    def printSpheres(self):

        print("Lord of ", end = "")
        for sphere in self.god_spheres:
            if sphere == self.god_spheres[-1]:
                print("and",sphere)
            else:
                print(sphere,end=', ')

    def printPersonality(self):
        for personality in self.god_personality:
            if personality == self.god_personality[-1]:
                print("and", personality)
            else:
                print(personality, end=', ')
