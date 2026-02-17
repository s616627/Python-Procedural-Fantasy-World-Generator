#structure for procedurally creating races
import stringListFunctions
import Item
# structure for creatures

class Species:

    def __init__(self, name,f_name,plural_name,adjetive_name, attack, defense, speed, size, magicAttack, magicDefense, maxHP, sapient, bodyParts, attributes):

        #string
        self.name = name
        self.f_name = f_name
        self.plural_name = plural_name
        self.adjetive_name = adjetive_name

        #int
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.size = size
        self.magicAttack = magicAttack
        self.magicDefense = magicDefense
        self.maxHP = maxHP

        #list of strings
        self.attributes = attributes

        #bool
        self.sapient = sapient

        #list of body parts
        self.bodyParts = bodyParts

    def addTrait(self,trait):
        if trait not in self.attributes:
            self.attributes.append(trait)
            self.name = trait + " " + self.name

class Creature(Species):

    def __init__(self, name,f_name,plural_name,adjetive_name, attack, defense, speed, size, magicAttack, magicDefense, maxHP, sapient, bodyParts, personality, attributes):
        super().__init__(name,f_name,plural_name,adjetive_name, attack, defense, speed, size, magicAttack, magicDefense, maxHP, sapient, bodyParts, attributes)
        #list of strings
        self.personality: list = []

class Being:
    def __init__(self,species,being_name,level,inventory):

        #Species
        self.species = species

        #string
        self.being_name = being_name

        #int
        self.level = level

        #list
        self.inventory = inventory


class bodyPart:
    def __init__(self, name, armor, nextPart, attributes):

        #string
        self.name = name

        #armor Item
        self.armor = armor

        #connected body part(s)
        self.nextPart = nextPart

        #list of strings
        self.attributes = attributes






