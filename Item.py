class Item:
    def __init__(self,price,weight,name,attributes,description):

        #int
        self.price = price
        self.weight = weight

        #string
        self.name = name

        # string list
        self.attributes = attributes
        self.description = description

    def printName(self):
        print(self.name)


class Weapon(Item):
    def __init__(self,price,weight, atkMltp, defMltp, name,attributes,handleAttributes,description):

        super().__init__(price,weight,name,attributes,description)

        #int
        self.atkMltp = atkMltp
        self.defMltp = defMltp

        # string list
        self.handleAttributes = handleAttributes

    def printName(self):
        super().printName()

class Book(Item):
    def __init__(self,price,weight,name,attributes,coverAttributes,writing,description):

        super().__init__(price,weight,name,attributes,description)

        #int

        #string

        # string list
        self.coverAttributes = coverAttributes
        self.writing = writing

    def printName(self):
        super().printName()

class Food(Item):
    def __init__(self,price,fullness,weight,name,attributes,description):

        super().__init__(price, weight, name, attributes, description)

        #int
        self.fullness = fullness

        #string

        # string list

    def printName(self):
        super().printName()


class Potion(Item):
    def __init__(self, price, fullness, weight, name, attributes, effects, description):
        super().__init__(price, weight, name, attributes, description)

        # int
        self.fullness = fullness

        # string

        # string list
        self.effects = effects

    def printName(self):
        super().printName()

